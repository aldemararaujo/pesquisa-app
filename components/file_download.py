import streamlit as st
from datetime import date
from generators.docx_generator import markdown_para_docx
from generators.pdf_generator import docx_para_pdf


def render_download_buttons(skill_id: str, texto_md: str):
    if not texto_md:
        return

    data_hoje = date.today().strftime("%Y%m%d")
    nome_base = f"{skill_id}_{data_hoje}"

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
        docx_bytes = markdown_para_docx(texto_md, titulo=skill_id)
        st.download_button(
            label="Baixar .docx",
            data=docx_bytes,
            file_name=f"{nome_base}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
        )

    with col3:
        pdf_bytes = docx_para_pdf(docx_bytes)
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
