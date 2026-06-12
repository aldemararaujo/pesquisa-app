import streamlit as st
from datetime import date
from generators.docx_generator import markdown_para_docx
from generators.pdf_generator import docx_para_pdf
from components.welcome_ui import rodape_aceite


def render_download_buttons(skill_id: str, texto_md: str):
    if not texto_md:
        return

    if skill_id == "compilacao-final":
        texto_md = texto_md + rodape_aceite()

    data_hoje = date.today().strftime("%Y%m%d")
    nome_base = f"{skill_id}_{data_hoje}"
    cache_key = f"_dl_{skill_id}_{abs(hash(texto_md)) % 10**9}"

    if cache_key not in st.session_state:
        barra = st.progress(0, text="Preparando conteúdo...")
        barra.progress(25, text="Gerando documento Word...")
        docx_bytes = markdown_para_docx(texto_md, titulo=skill_id)
        barra.progress(70, text="Gerando PDF...")
        pdf_bytes = docx_para_pdf(docx_bytes)
        barra.progress(100, text="✅ Arquivos prontos para download!")
        barra.empty()
        st.session_state[cache_key] = (docx_bytes, pdf_bytes)
    else:
        docx_bytes, pdf_bytes = st.session_state[cache_key]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            label="Baixar .md",
            data=texto_md.encode("utf-8"),
            file_name=f"{nome_base}.md",
            mime="text/markdown",
            use_container_width=True,
        )

    with col2:
        st.download_button(
            label="Baixar .docx",
            data=docx_bytes,
            file_name=f"{nome_base}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
        )

    with col3:
        if pdf_bytes:
            st.download_button(
                label="Baixar .pdf",
                data=pdf_bytes,
                file_name=f"{nome_base}.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        else:
            st.caption("PDF indisponível")
