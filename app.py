import streamlit as st
from utils.session import init_session
from components.pipeline_nav import render_pipeline_nav
from components.chat_ui import render_chat
from config import PIPELINE, PROVIDERS, DEFAULT_PROVIDER

st.set_page_config(
    page_title="FiatLux - Projeto de Pesquisa",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()

def _on_provider_change():
    new_provider = st.session_state["_provider_select"]
    if new_provider != st.session_state.get("selected_provider"):
        st.session_state["selected_provider"] = new_provider
        st.session_state["selected_model"] = PROVIDERS[new_provider]["default_model"]
        st.session_state["api_key"] = ""


def _on_model_change():
    st.session_state["selected_model"] = st.session_state["_model_select"]


# Painel lateral — provedor, modelo, API key e navegação
with st.sidebar:
    st.markdown("### Provedor de IA")

    provider_ids = list(PROVIDERS.keys())
    current_provider = st.session_state.get("selected_provider", DEFAULT_PROVIDER)
    current_provider_idx = provider_ids.index(current_provider) if current_provider in provider_ids else 0

    st.selectbox(
        "Provedor",
        options=provider_ids,
        format_func=lambda x: PROVIDERS[x]["label"],
        index=current_provider_idx,
        key="_provider_select",
        on_change=_on_provider_change,
    )

    prov = PROVIDERS[st.session_state.get("selected_provider", DEFAULT_PROVIDER)]
    model_options = prov["models"]
    current_model = st.session_state.get("selected_model", prov["default_model"])
    if current_model not in model_options:
        current_model = prov["default_model"]

    st.selectbox(
        "Modelo",
        options=model_options,
        index=model_options.index(current_model),
        key="_model_select",
        on_change=_on_model_change,
    )

    st.markdown("### Chave de API")
    provider_id = st.session_state.get("selected_provider", DEFAULT_PROVIDER)
    api_key_input = st.text_input(
        prov["key_label"],
        type="password",
        value=st.session_state.get("api_key", ""),
        placeholder=prov["key_placeholder"],
        key=f"_api_key_{provider_id}",
        help="Sua chave permanece apenas nesta sessão e não é armazenada.",
    )
    st.session_state.api_key = st.session_state.get(f"_api_key_{provider_id}", "")

    st.markdown("---")
    render_pipeline_nav()

# Cabeçalho principal (só na tela inicial)
if not st.session_state.skills_concluidas and st.session_state.skill_atual == 0:
    st.title("FiatLux - Projeto de Pesquisa")
    st.markdown(
        """
        Esta ferramenta guia você pelo processo completo de redação de um projeto de pesquisa
        científica em português brasileiro, da definição do tema até a compilação final para
        submissão ao CEP.

        **Como usar:**
        1. Escolha o provedor de IA e insira sua chave de API no painel lateral
        2. Siga as etapas do pipeline na ordem indicada
        3. Ao final de cada etapa, baixe os arquivos gerados e avance para a próxima

        ---
        """
    )

skill_atual = st.session_state.skill_atual
render_chat(skill_atual)
