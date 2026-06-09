import streamlit as st
from skills.loader import load_system_prompt
from utils.session import (
    get_historico,
    append_mensagem,
    build_context_prefix,
    save_portable_context,
    marcar_concluida,
    avancar_skill,
    add_tokens,
)
from utils.llm_provider import get_provider, AuthenticationError as LLMAuthError
from components.file_download import render_download_buttons
from config import PIPELINE, PIPELINE_IDS

_MARCADOR_CONTEXTO = "=== BLOCO DE CONTEXTO PORTÁTIL ==="
_MARCADOR_FIM = "=== FIM DO BLOCO ==="
_MARCADOR_CONCLUSAO = "=== ETAPA CONCLUÍDA ==="


def _extrair_contexto_portatil(texto: str) -> str | None:
    inicio = texto.find(_MARCADOR_CONTEXTO)
    if inicio == -1:
        return None
    fim = texto.find(_MARCADOR_FIM, inicio)
    if fim == -1:
        return texto[inicio:]
    return texto[inicio: fim + len(_MARCADOR_FIM)]


def _ultimo_md(skill_id: str) -> str:
    historico = get_historico(skill_id)
    for msg in reversed(historico):
        if msg["role"] == "assistant" and len(msg["content"]) > 200:
            return msg["content"]
    return ""


def _gerar_resumo_etapa(skill_id: str, titulo: str):
    historico = get_historico(skill_id)
    if not historico:
        return

    api_key = st.session_state.get("api_key", "")
    if not api_key:
        return

    provider_id = st.session_state.get("selected_provider", "anthropic")
    model = st.session_state.get("selected_model", "claude-sonnet-4-6")

    try:
        provider = get_provider(provider_id)
        system = "Você é um assistente de síntese de projetos de pesquisa científica."
        msgs = historico + [{
            "role": "user",
            "content": (
                f"Com base na conversa acima sobre a etapa '{titulo}', "
                "gere um resumo estruturado de até 300 palavras contendo:\n"
                "- Tema e objetivo do projeto\n"
                "- Decisões e definições feitas nesta etapa\n"
                "- Dados específicos relevantes (população, delineamento, método, etc.)\n\n"
                "Este resumo será usado como contexto nas próximas etapas. "
                "Seja conciso e objetivo."
            ),
        }]
        resumo = ""
        for texto in provider.stream_response(system, msgs, model, api_key):
            resumo += texto
        if resumo:
            save_portable_context(skill_id, f"[Resumo — {titulo}]\n\n{resumo}")
    except Exception:
        pass


def render_chat(skill_index: int):
    skill = PIPELINE[skill_index]
    skill_id = skill["id"]

    st.subheader(skill["titulo"])
    st.caption(skill["descricao"])

    # Indicador de status da etapa
    etapa_pronta = st.session_state.get("etapas_prontas", {}).get(skill_id, False)
    if etapa_pronta:
        st.success("✅ Etapa concluída — clique em **Próxima etapa →** para avançar.")
    elif get_historico(skill_id):
        st.info("💬 Etapa em andamento — continue a conversa com a IA.")

    # Exibe histórico
    historico = get_historico(skill_id)
    for msg in historico:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Botão "+" para alternar visibilidade do uploader
    upload_key = f"upload_{skill_id}_{st.session_state.get('upload_counter', 0)}"
    _vis_key = f"_upload_vis_{skill_id}"
    _upload_vis = st.session_state.get(_vis_key, False)
    col_plus, _ = st.columns([1, 16])
    with col_plus:
        if st.button("✕" if _upload_vis else "＋", key=f"_toggle_up_{skill_id}", help="Anexar arquivo ao contexto"):
            st.session_state[_vis_key] = not _upload_vis

    uploaded_file = None
    if st.session_state.get(_vis_key, False):
        uploaded_file = st.file_uploader(
            "Formatos aceitos: .txt  .md  .docx",
            type=["txt", "md", "docx"],
            key=upload_key,
            label_visibility="collapsed",
        )

    # Entrada do usuário
    user_input = st.chat_input("Digite sua mensagem...")

    if user_input or uploaded_file:
        # Extrai conteúdo do arquivo se houver
        file_content = ""
        file_name = ""
        if uploaded_file:
            file_name = uploaded_file.name
            if file_name.endswith(".docx"):
                from io import BytesIO
                from docx import Document as DocxDocument
                doc = DocxDocument(BytesIO(uploaded_file.read()))
                file_content = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
            else:
                file_content = uploaded_file.read().decode("utf-8", errors="replace")
            st.session_state.upload_counter = st.session_state.get("upload_counter", 0) + 1

        # Monta mensagem para o LLM (arquivo + texto do usuário)
        partes = []
        if file_content:
            partes.append(f"[Arquivo: {file_name}]\n\n{file_content}")
        if user_input:
            partes.append(user_input)
        mensagem_llm = "\n\n---\n\n".join(partes)

        # Texto exibido na bolha do chat
        if user_input and file_name:
            display_text = f"{user_input}\n\n*Arquivo anexado: {file_name}*"
        elif file_name:
            display_text = f"*Arquivo anexado: {file_name}*"
        else:
            display_text = user_input

        append_mensagem(skill_id, "user", mensagem_llm)
        with st.chat_message("user"):
            st.markdown(display_text)

        api_key = st.session_state.get("api_key", "")
        if not api_key:
            st.error("Insira sua chave de API no painel lateral.")
            return

        provider_id = st.session_state.get("selected_provider", "anthropic")
        model = st.session_state.get("selected_model", "claude-sonnet-4-6")

        try:
            provider = get_provider(provider_id)

            # Monta system prompt com contexto das etapas anteriores
            skill_prompt = load_system_prompt(skill_id)
            ids_anteriores = PIPELINE_IDS[:skill_index]
            contexto_prefix = build_context_prefix(ids_anteriores)
            system = contexto_prefix + skill_prompt if contexto_prefix else skill_prompt

            def _on_tokens(input_t: int, output_t: int):
                add_tokens(skill_id, input_t, output_t)

            with st.chat_message("assistant"):
                resposta_completa = ""
                placeholder = st.empty()

                for texto in provider.stream_response(system, get_historico(skill_id), model, api_key, on_tokens=_on_tokens):
                    resposta_completa += texto
                    placeholder.markdown(resposta_completa + "▌")

                # Detecta e remove marcador de conclusão antes de exibir e salvar
                if _MARCADOR_CONCLUSAO in resposta_completa:
                    st.session_state.setdefault("etapas_prontas", {})[skill_id] = True
                    resposta_completa = resposta_completa.replace(_MARCADOR_CONCLUSAO, "").rstrip()

                placeholder.markdown(resposta_completa)

            append_mensagem(skill_id, "assistant", resposta_completa)

            # Salva contexto portátil se presente na resposta
            ctx = _extrair_contexto_portatil(resposta_completa)
            if ctx:
                save_portable_context(skill_id, ctx)

        except LLMAuthError:
            st.error("Chave de API inválida. Verifique e tente novamente.")
        except Exception as e:
            st.error(f"Erro ao chamar a API: {e}")

    # Botões de controle ao final do chat
    st.markdown("---")
    col_dl, col_av = st.columns([3, 1])

    with col_dl:
        ultimo_md = _ultimo_md(skill_id)
        if ultimo_md:
            render_download_buttons(skill_id, ultimo_md)

    with col_av:
        etapa_pronta = st.session_state.get("etapas_prontas", {}).get(skill_id, False)

        if skill_index < len(PIPELINE) - 1:
            if etapa_pronta:
                if st.button("Próxima etapa →", type="primary", use_container_width=True):
                    with st.spinner("Salvando contexto da etapa..."):
                        _gerar_resumo_etapa(skill_id, skill["titulo"])
                    marcar_concluida(skill_id)
                    avancar_skill()
                    st.rerun()
            else:
                if st.button("Próxima etapa →", type="secondary", use_container_width=True):
                    st.warning(
                        "⚠️ Esta etapa ainda não foi concluída. "
                        "Continue a conversa — a IA sinalizará quando todos os "
                        "entregáveis estiverem prontos."
                    )
        else:
            if etapa_pronta:
                if st.button("Concluir pipeline ✓", type="primary", use_container_width=True):
                    with st.spinner("Salvando contexto da etapa..."):
                        _gerar_resumo_etapa(skill_id, skill["titulo"])
                    marcar_concluida(skill_id)
                    st.success("Pipeline concluído! Todos os capítulos foram gerados.")
            else:
                if st.button("Concluir pipeline ✓", type="secondary", use_container_width=True):
                    st.warning(
                        "⚠️ Esta etapa ainda não foi concluída. "
                        "Continue a conversa — a IA sinalizará quando todos os "
                        "entregáveis estiverem prontos."
                    )
