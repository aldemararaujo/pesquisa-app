import streamlit as st


def render_footer():
    """Rodapé institucional exibido em todas as páginas."""
    st.markdown("""
<style>
    .app-footer {
        text-align: center;
        font-size: 0.74rem;
        line-height: 1.6;
        color: #1F497D;
        opacity: 0.75;
        padding-top: 0.6rem;
    }
    .app-footer .af-copy { font-weight: 700; }
    div.st-key-footer_termo_btn,
    div.st-key-footer_termo_btn > div,
    div.st-key-footer_termo_btn [data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }
    div.st-key-footer_termo_btn button {
        font-size: 0.74rem !important;
        color: #1F497D !important;
        opacity: 0.85;
        text-decoration: underline;
        padding: 0 !important;
        min-height: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
<div class="app-footer">
    <span class="af-copy">Copyright © 2026 Aldemar Araujo Castro</span><br>
    Disciplina de Pesquisa em Ciências da Saúde da Universidade Estadual
    de Ciências da Saúde de Alagoas (UNCISAL)<br>
    Maceió · Alagoas · Brasil
</div>
""", unsafe_allow_html=True)

    if st.button("Apresentação e termo de uso", key="footer_termo_btn", type="tertiary"):
        st.session_state.mostrar_apresentacao = True
        st.session_state._rolar_topo = True
        st.rerun()
