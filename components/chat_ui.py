import streamlit as st
from skills.loader import load_system_prompt
from utils.session import (
    get_historico,
    append_mensagem,
    build_context_prefix,
    save_portable_context,
    marcar_concluida,
    avancar_skill,
)
from utils.llm_provider import get_provider, AuthenticationError as LLMAuthError
from components.file_download import render_download_buttons
from config import PIPELINE, PIPELINE_IDS

_MARCADOR_CONTEXTO = "=== BLOCO DE CONTEXTO PORTÁTIL ==="
_MARCADOR_FIM = "=== FIM DO BLOCO ==="


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


def render_chat(skill_index: int):
    skill = PIPELINE[skill_index]
    skill_id = skill["id"]

    st.subheader(skill["titulo"])
    st.caption(skill["descricao"])

    # Exibe histórico
    historico = get_historico(skill_id)
    for msg in historico:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Entrada do usuário
    user_input = st.chat_input("Digite sua mensagem...")

    if user_input:
        append_mensagem(skill_id, "user", user_input)
        with st.chat_message("user"):
            st.markdown(user_input)

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

            with st.chat_message("assistant"):
                resposta_completa = ""
                placeholder = st.empty()

                for texto in provider.stream_response(system, get_historico(skill_id), model, api_key):
                    resposta_completa += texto
                    placeholder.markdown(resposta_completa + "▌")

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
        if skill_index < len(PIPELINE) - 1:
            if st.button("Próxima etapa →", type="primary", use_container_width=True):
                marcar_concluida(skill_id)
                avancar_skill()
                st.rerun()
        else:
            if st.button("Concluir pipeline ✓", type="primary", use_container_width=True):
                marcar_concluida(skill_id)
                st.success("Pipeline concluído! Todos os capítulos foram gerados.")
