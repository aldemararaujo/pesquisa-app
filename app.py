import streamlit as st
from utils.session import init_session, get_historico
from components.pipeline_nav import render_pipeline_nav
from components.chat_ui import render_chat
from config import PIPELINE, PROVIDERS, DEFAULT_PROVIDER

st.set_page_config(
    page_title="FiatLux - Projeto de Pesquisa",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()

st.markdown("""
<style>
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
    }
    section[data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem !important;
    }
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.25rem !important;
    }
</style>
""", unsafe_allow_html=True)


def _on_provider_change():
    new_provider = st.session_state["_provider_select"]
    if new_provider != st.session_state.get("selected_provider"):
        st.session_state["selected_provider"] = new_provider
        st.session_state["selected_model"] = PROVIDERS[new_provider]["default_model"]
        st.session_state["api_key"] = ""


def _on_model_change():
    st.session_state["selected_model"] = st.session_state["_model_select"]


# Painel lateral
with st.sidebar:
    st.markdown("## 📋 FiatLux - Projeto de Pesquisa")
    st.markdown("---")

    # Status e chave de API
    provider_id = st.session_state.get("selected_provider", DEFAULT_PROVIDER)
    prov = PROVIDERS[provider_id]

    if st.session_state.get("api_key"):
        st.success("API configurada", icon="✅")
    else:
        st.warning("Insira a chave de API", icon="⚠️")

    st.text_input(
        prov["key_label"],
        type="password",
        value=st.session_state.get("api_key", ""),
        placeholder=prov["key_placeholder"],
        key=f"_api_key_{provider_id}",
        help="Sua chave permanece apenas nesta sessão e não é armazenada.",
    )
    st.session_state.api_key = st.session_state.get(f"_api_key_{provider_id}", "")

    with st.expander("Provedor e modelo", expanded=False):
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

    st.markdown("---")
    render_pipeline_nav()


# Cabeçalho principal — visível só antes da primeira mensagem na etapa 1
primeiro_skill_id = PIPELINE[0]["id"]
mostrar_cabecalho = (
    st.session_state.skill_atual == 0
    and not st.session_state.skills_concluidas
    and len(get_historico(primeiro_skill_id)) == 0
)

if mostrar_cabecalho:
    col_icon, col_text = st.columns([1, 6])
    with col_icon:
        st.markdown("## 📋")
    with col_text:
        st.markdown("# FiatLux")
        st.caption("Assistente de redação para projetos de pesquisa científica em português brasileiro")

    st.markdown("---")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**1. Configure a IA**")
        st.markdown("Escolha o provedor e insira a chave de API na barra lateral.")
    with c2:
        st.markdown("**2. Siga o pipeline**")
        st.markdown("Complete cada etapa em ordem — do mapeamento do tema à compilação final.")
    with c3:
        st.markdown("**3. Baixe os arquivos**")
        st.markdown("Ao final de cada etapa, exporte em Markdown, Word ou PDF.")

    st.markdown("---")

_total_tokens = sum(
    v["input"] + v["output"]
    for v in st.session_state.get("tokens_por_skill", {}).values()
)
_tab_title = (
    f"FiatLux ({_total_tokens:,} tokens)"
    if _total_tokens > 0
    else "FiatLux - Projeto de Pesquisa"
)
st.markdown(f"<script>document.title = '{_tab_title}';</script>", unsafe_allow_html=True)

skill_atual = st.session_state.skill_atual
render_chat(skill_atual)
