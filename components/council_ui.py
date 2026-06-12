"""Página do Conselho de Especialistas: upload, execução das etapas e resultados."""

from datetime import date

import streamlit as st

from council.personas import PERSONAS, PERSONA_IDS
from council.engine import (
    etapa_identificacao,
    etapa_parecer,
    etapa_revisao,
    etapa_sintese,
    parse_tipo_documento,
    truncar_documento,
    TIPOS_LABEL,
)
from council.engine import eh_rate_limit
from utils.doc_extract import extrair_texto
from utils.llm_provider import AuthenticationError as LLMAuthError
from components.file_download import render_download_buttons

_RELATORIO_ID = "conselho-relatorio"


def _personas_selecionadas(conselho: dict) -> list[dict]:
    """Personas participantes da análise, na ordem de PERSONAS. Análises
    antigas na sessão (sem a chave) consideram todos os especialistas."""
    ids = conselho.get("selecionados") or PERSONA_IDS
    return [p for p in PERSONAS if p["id"] in ids]


def render_council():
    st.subheader("🏛️ Conselho de Especialistas")
    st.caption(
        "Envie um projeto de pesquisa, relatório final ou artigo científico. "
        "Oito especialistas emitem pareceres independentes, revisam os pareceres "
        "uns dos outros de forma anônima e um relator consolida tudo em um "
        "relatório detalhado com sugestões de aprimoramento."
    )

    conselho = st.session_state.setdefault("conselho", {})

    if not conselho.get("doc_texto"):
        _render_upload(conselho)
        return

    _render_info_documento(conselho)

    if conselho.get("erro"):
        st.error(f"A análise foi interrompida: {conselho['erro']}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("▶ Continuar análise", type="primary", use_container_width=True):
                conselho["erro"] = None
                conselho["executando"] = True
                st.rerun()
        with col2:
            if st.button("Reiniciar análise", use_container_width=True):
                _limpar_conselho()
                st.rerun()
        _render_resultados_parciais(conselho)
        return

    if conselho.get("executando"):
        _executar_analise(conselho)
        return

    if conselho.get("relatorio"):
        _render_resultados(conselho)
        return

    # Documento carregado mas análise ainda não iniciada (estado raro de fallback)
    if st.button("▶ Iniciar análise", type="primary"):
        conselho["executando"] = True
        st.rerun()


def _render_upload(conselho: dict):
    st.markdown("#### Especialistas do conselho")
    st.caption(
        "Escolha quais especialistas participam da análise. "
        "Por padrão, todos participam."
    )
    colunas = st.columns(4)
    selecionados = []
    for i, persona in enumerate(PERSONAS):
        with colunas[i % 4]:
            marcado = st.checkbox(
                persona["nome_curto"],
                value=True,
                key=f"_sel_{persona['id']}",
            )
            if marcado:
                selecionados.append(persona["id"])

    if not selecionados:
        st.warning("Selecione ao menos um especialista para a análise.")

    uploaded_file = st.file_uploader(
        "Documento para análise (.pdf  .docx  .md  .txt)",
        type=["pdf", "docx", "md", "txt"],
        key="conselho_upload",
    )

    api_key = st.session_state.get("api_key", "")
    if not api_key:
        st.warning("Configure sua chave de API no painel lateral antes de iniciar.")

    iniciar = st.button(
        "▶ Iniciar análise",
        type="primary",
        disabled=not (uploaded_file and api_key and selecionados),
        use_container_width=True,
    )

    if iniciar and uploaded_file:
        with st.spinner("Extraindo texto do documento..."):
            texto, aviso = extrair_texto(uploaded_file)

        if not texto.strip():
            st.error(aviso or "Não foi possível extrair texto do documento.")
            return

        provider_id = st.session_state.get("selected_provider", "anthropic")
        texto, truncado = truncar_documento(texto, provider_id)

        conselho.update({
            "doc_nome": uploaded_file.name,
            "doc_texto": texto,
            "doc_truncado": truncado,
            "aviso_extracao": aviso,
            "selecionados": selecionados,
            "identificacao": None,
            "tipo_documento": None,
            "pareceres": {},
            "revisoes": {},
            "relatorio": None,
            "executando": True,
            "erro": None,
        })
        st.rerun()


def _render_info_documento(conselho: dict):
    tipo = conselho.get("tipo_documento")
    tipo_label = TIPOS_LABEL.get(tipo, "ainda não identificado")
    n_areas = len(_personas_selecionadas(conselho))
    plural = "especialistas" if n_areas > 1 else "especialista"
    st.info(
        f"📄 **{conselho.get('doc_nome', '')}** · Tipo: {tipo_label} · "
        f"Conselho com {n_areas} {plural}"
    )

    if conselho.get("aviso_extracao"):
        st.warning(conselho["aviso_extracao"])
    if conselho.get("doc_truncado"):
        st.warning(
            "O documento excede a janela de contexto do provedor selecionado e "
            "foi truncado: apenas a parte inicial será analisada. Considere usar "
            "um provedor com janela maior (Gemini ou Anthropic)."
        )


def _executar_analise(conselho: dict):
    pareceres = conselho.setdefault("pareceres", {})
    revisoes = conselho.setdefault("revisoes", {})
    doc = conselho["doc_texto"]
    participantes = _personas_selecionadas(conselho)
    ids_participantes = [p["id"] for p in participantes]
    n = len(participantes)

    try:
        # Etapa 0: identificação
        with st.status("Etapa 1 de 4 · Identificando o documento...", expanded=True) as status:
            if not conselho.get("identificacao"):
                placeholder = st.empty()
                resultado = etapa_identificacao(doc, on_chunk=lambda t: placeholder.markdown(t + "▌"))
                placeholder.empty()
                conselho["identificacao"] = resultado
                conselho["tipo_documento"] = parse_tipo_documento(resultado)
            tipo_label = TIPOS_LABEL.get(conselho["tipo_documento"], "")
            status.update(label=f"Etapa 1 de 4 · Documento identificado: {tipo_label} ✓", state="complete", expanded=False)

        identificacao = conselho["identificacao"]
        tipo = conselho["tipo_documento"]

        # Etapa 1: pareceres
        with st.status("Etapa 2 de 4 · Pareceres dos especialistas...", expanded=True) as status:
            progresso = st.empty()
            placeholder = st.empty()
            for i, persona in enumerate(participantes, start=1):
                if pareceres.get(persona["id"]):
                    continue
                progresso.markdown(f"**Parecer {i} de {n}: {persona['nome_curto']}**")
                resultado = etapa_parecer(
                    persona, doc, identificacao, tipo,
                    on_chunk=lambda t: placeholder.markdown(t + "▌"),
                )
                pareceres[persona["id"]] = resultado
                placeholder.empty()
            progresso.empty()
            status.update(label="Etapa 2 de 4 · Pareceres concluídos ✓", state="complete", expanded=False)

        # Etapa 2: revisão cruzada (dispensada quando há um único especialista)
        if n < 2:
            with st.status(
                "Etapa 3 de 4 · Revisão cruzada dispensada: apenas um especialista",
                expanded=False,
            ) as status:
                status.update(state="complete")
        else:
            with st.status("Etapa 3 de 4 · Revisão cruzada anônima...", expanded=True) as status:
                progresso = st.empty()
                placeholder = st.empty()
                for i, persona in enumerate(participantes, start=1):
                    if revisoes.get(persona["id"]):
                        continue
                    progresso.markdown(f"**Revisão {i} de {n}: {persona['nome_curto']}**")
                    resultado = etapa_revisao(
                        persona, identificacao, pareceres,
                        ids_selecionados=ids_participantes,
                        on_chunk=lambda t: placeholder.markdown(t + "▌"),
                    )
                    revisoes[persona["id"]] = resultado
                    placeholder.empty()
                progresso.empty()
                status.update(label="Etapa 3 de 4 · Revisão cruzada concluída ✓", state="complete", expanded=False)

        # Etapa 3: síntese do relator
        with st.status("Etapa 4 de 4 · Síntese do relator...", expanded=True) as status:
            if not conselho.get("relatorio"):
                placeholder = st.empty()
                data_analise = date.today().strftime("%d de %B de %Y")
                resultado = etapa_sintese(
                    identificacao, tipo, pareceres, revisoes, data_analise,
                    on_chunk=lambda t: placeholder.markdown(t + "▌"),
                )
                placeholder.empty()
                conselho["relatorio"] = resultado
            status.update(label="Etapa 4 de 4 · Relatório consolidado ✓", state="complete", expanded=False)

        conselho["executando"] = False
        st.rerun()

    except LLMAuthError:
        conselho["executando"] = False
        conselho["erro"] = "chave de API inválida. Verifique a configuração no painel lateral."
        st.rerun()
    except Exception as e:
        conselho["executando"] = False
        if eh_rate_limit(e):
            conselho["erro"] = (
                "o limite de tokens por minuto da sua conta no provedor foi "
                "atingido repetidamente, mesmo após esperas automáticas. "
                "Aguarde alguns minutos e clique em Continuar análise: o "
                "progresso já feito está preservado. Se o erro persistir, o "
                "documento pode ser grande demais para o limite do seu plano: "
                "use um provedor com limite maior ou aumente o nível da conta."
            )
        else:
            conselho["erro"] = f"{e}"
        st.rerun()


def _render_resultados(conselho: dict):
    participantes = _personas_selecionadas(conselho)
    st.markdown("### Pareceres dos especialistas")
    abas = st.tabs([p["nome_curto"] for p in participantes])
    for aba, persona in zip(abas, participantes):
        with aba:
            parecer = conselho["pareceres"].get(persona["id"])
            st.markdown(parecer or "_Parecer não disponível._")
            revisao = conselho["revisoes"].get(persona["id"])
            if revisao:
                with st.expander("Revisão cruzada deste especialista"):
                    st.markdown(revisao)
            if parecer:
                st.caption("Baixar este parecer:")
                render_download_buttons(f"conselho-{persona['id']}", parecer)

    st.markdown("---")
    st.markdown("### Relatório final do conselho")
    st.markdown(conselho["relatorio"])

    st.markdown("---")
    render_download_buttons(_RELATORIO_ID, conselho["relatorio"])

    if st.button("Reiniciar análise", use_container_width=True):
        _limpar_conselho()
        st.rerun()


def _render_resultados_parciais(conselho: dict):
    pareceres = conselho.get("pareceres", {})
    if not conselho.get("identificacao") and not pareceres:
        return
    st.markdown("---")
    st.markdown("#### Resultados parciais já obtidos")
    if conselho.get("identificacao"):
        with st.expander("Identificação do documento"):
            st.markdown(conselho["identificacao"])
    for persona in _personas_selecionadas(conselho):
        parecer = pareceres.get(persona["id"])
        if parecer:
            with st.expander(f"Parecer: {persona['nome_curto']}"):
                st.markdown(parecer)


def _limpar_conselho():
    st.session_state.conselho = {}
    for key in list(st.session_state.keys()):
        if key.startswith("_dl_conselho-"):
            del st.session_state[key]
