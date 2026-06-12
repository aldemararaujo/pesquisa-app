"""Página do Conselho de Especialistas: upload, execução das etapas e resultados."""

import zipfile
from datetime import date
from io import BytesIO

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
from generators.docx_generator import markdown_para_docx
from generators.pdf_generator import docx_para_pdf

_MIME_DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


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


def _cache_key_documento(doc_id: str, texto_md: str) -> str:
    return f"_dl_conselho-{doc_id}_{abs(hash(texto_md)) % 10**9}"


def _arquivos_documento(doc_id: str, texto_md: str) -> tuple[bytes, bytes | None]:
    """Gera (com cache na sessão) os bytes de DOCX e PDF de um documento."""
    cache_key = _cache_key_documento(doc_id, texto_md)
    if cache_key not in st.session_state:
        docx_bytes = markdown_para_docx(texto_md, titulo=doc_id)
        pdf_bytes = docx_para_pdf(docx_bytes)
        st.session_state[cache_key] = (docx_bytes, pdf_bytes)
    return st.session_state[cache_key]


def _zip_completo(documentos: list[tuple[str, str, str]]) -> bytes:
    """Monta (com cache na sessão) um zip com todos os documentos nos 3 formatos."""
    chave = f"_dl_conselho-zip_{abs(hash(tuple(t for _, _, t in documentos))) % 10**9}"
    if chave not in st.session_state:
        buf = BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            for doc_id, _, texto in documentos:
                docx_bytes, pdf_bytes = _arquivos_documento(doc_id, texto)
                zf.writestr(f"{doc_id}.md", texto)
                zf.writestr(f"{doc_id}.docx", docx_bytes)
                if pdf_bytes:
                    zf.writestr(f"{doc_id}.pdf", pdf_bytes)
        st.session_state[chave] = buf.getvalue()
    return st.session_state[chave]


def _render_downloads(conselho: dict):
    participantes = _personas_selecionadas(conselho)
    data_hoje = date.today().strftime("%Y%m%d")

    documentos = [("relatorio-final", "📑 **Relatório final do conselho**", conselho["relatorio"])]
    for p in participantes:
        parecer = conselho["pareceres"].get(p["id"])
        if parecer:
            documentos.append((f"parecer-{p['id']}", f"Parecer: {p['nome_curto']}", parecer))

    with st.expander("📥 Downloads", expanded=True):
        # Primeira renderização: gera todos os arquivos com uma única barra
        pendentes = sum(
            1 for doc_id, _, texto in documentos
            if _cache_key_documento(doc_id, texto) not in st.session_state
        )
        if pendentes:
            barra = st.progress(0, text="Preparando arquivos...")
            for i, (doc_id, _, texto) in enumerate(documentos, start=1):
                barra.progress(i / len(documentos), text=f"Preparando arquivos: {i} de {len(documentos)}...")
                _arquivos_documento(doc_id, texto)
            barra.empty()

        for doc_id, rotulo, texto in documentos:
            docx_bytes, pdf_bytes = _arquivos_documento(doc_id, texto)
            nome_base = f"conselho-{doc_id}_{data_hoje}"
            col_nome, col_md, col_docx, col_pdf = st.columns([3, 1, 1, 1])
            with col_nome:
                st.markdown(rotulo)
            with col_md:
                st.download_button(
                    ".md", data=texto.encode("utf-8"),
                    file_name=f"{nome_base}.md", mime="text/markdown",
                    key=f"dlbtn_{doc_id}_md", use_container_width=True,
                )
            with col_docx:
                st.download_button(
                    ".docx", data=docx_bytes,
                    file_name=f"{nome_base}.docx", mime=_MIME_DOCX,
                    key=f"dlbtn_{doc_id}_docx", use_container_width=True,
                )
            with col_pdf:
                if pdf_bytes:
                    st.download_button(
                        ".pdf", data=pdf_bytes,
                        file_name=f"{nome_base}.pdf", mime="application/pdf",
                        key=f"dlbtn_{doc_id}_pdf", use_container_width=True,
                    )
                else:
                    st.caption("PDF indisponível")
            if doc_id == "relatorio-final":
                st.markdown("---")

        st.download_button(
            "⬇ Baixar tudo (.zip)",
            data=_zip_completo(documentos),
            file_name=f"conselho-completo_{data_hoje}.zip",
            mime="application/zip",
            key="dlbtn_zip",
            type="primary",
            use_container_width=True,
        )


def _render_resultados(conselho: dict):
    participantes = _personas_selecionadas(conselho)

    _render_downloads(conselho)

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

    st.markdown("---")
    st.markdown("### Relatório final do conselho")
    st.markdown(conselho["relatorio"])

    st.markdown("---")
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
