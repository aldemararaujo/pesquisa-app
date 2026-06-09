import streamlit as st
from utils.session import init_session
from components.pipeline_nav import render_pipeline_nav
from components.chat_ui import render_chat
from config import PIPELINE

st.set_page_config(
    page_title="Projeto de Pesquisa — Redação com IA",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()

# Painel lateral — API key e navegação
with st.sidebar:
    st.markdown("### Chave de API")
    api_key_input = st.text_input(
        "Anthropic API Key",
        type="password",
        value=st.session_state.get("api_key", ""),
        placeholder="sk-ant-...",
        help="Sua chave permanece apenas nesta sessão e não é armazenada.",
    )
    if api_key_input:
        st.session_state.api_key = api_key_input

    st.markdown("---")
    render_pipeline_nav()

# Cabeçalho principal (só na tela inicial)
if not st.session_state.skills_concluidas and st.session_state.skill_atual == 0:
    st.title("Projeto de Pesquisa — Redação com IA")
    st.markdown(
        """
        Esta ferramenta guia você pelo processo completo de redação de um projeto de pesquisa
        científica em português brasileiro, da definição do tema até a compilação final para
        submissão ao CEP.

        **Como usar:**
        1. Insira sua chave de API Anthropic no painel lateral
        2. Siga as etapas do pipeline na ordem indicada
        3. Ao final de cada etapa, baixe os arquivos gerados e avance para a próxima

        ---
        """
    )

skill_atual = st.session_state.skill_atual
render_chat(skill_atual)
