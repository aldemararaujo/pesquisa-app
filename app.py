import streamlit as st
from utils.session import init_session
from components.pipeline_nav import render_pipeline_nav
from components.chat_ui import render_chat
from config import PROVIDERS, DEFAULT_PROVIDER

st.set_page_config(
    page_title="FiatLux - Projeto de Pesquisa",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()

# Mantém api_key sincronizada com o widget do dialog (persiste mesmo com dialog fechado)
_prov_id = st.session_state.get("selected_provider", DEFAULT_PROVIDER)
if f"_api_key_{_prov_id}" in st.session_state:
    st.session_state.api_key = st.session_state[f"_api_key_{_prov_id}"]

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


@st.dialog("Como usar o FiatLux", width="large")
def _dialog_como_usar():
    st.markdown("""
**1. Configure a IA**
Abra "Configuração" na barra lateral, escolha o provedor e insira sua chave de API.
Sua chave não é armazenada — fica apenas nesta sessão.

**2. Siga o pipeline em ordem**
O pipeline tem 14 etapas, do mapeamento do tema até a compilação final.
Complete cada etapa antes de avançar para a próxima.

**3. Converse com a IA**
Digite sua mensagem no campo de chat.
Você também pode anexar arquivos `.txt`, `.md` ou `.docx` como contexto.

**4. Baixe os arquivos gerados**
Ao final de cada etapa, exporte o resultado em Markdown, Word ou PDF.

**5. Monitore o uso de contexto**
A barra na sidebar mostra quantos tokens foram consumidos na etapa atual.
A aba do navegador exibe o total acumulado de tokens da sessão.
    """)


def _on_provider_change():
    new_provider = st.session_state["_provider_select"]
    if new_provider != st.session_state.get("selected_provider"):
        st.session_state["selected_provider"] = new_provider
        st.session_state["selected_model"] = PROVIDERS[new_provider]["default_model"]
        st.session_state["api_key"] = ""


def _on_model_change():
    st.session_state["selected_model"] = st.session_state["_model_select"]


@st.dialog("Configuração", width="large")
def _dialog_configuracao():
    provider_id = st.session_state.get("selected_provider", DEFAULT_PROVIDER)
    prov = PROVIDERS[provider_id]

    if st.session_state.get("api_key"):
        st.success("API configurada", icon="✅")
    else:
        st.warning("Insira a chave de API abaixo", icon="⚠️")

    st.text_input(
        prov["key_label"],
        type="password",
        value=st.session_state.get("api_key", ""),
        placeholder=prov["key_placeholder"],
        key=f"_api_key_{provider_id}",
        help="Sua chave permanece apenas nesta sessão e não é armazenada.",
    )
    st.session_state.api_key = st.session_state.get(f"_api_key_{provider_id}", "")

    st.divider()

    provider_ids = list(PROVIDERS.keys())
    current_provider_idx = provider_ids.index(provider_id) if provider_id in provider_ids else 0
    st.selectbox(
        "Provedor de IA",
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


# Painel lateral
with st.sidebar:
    st.markdown("## 📋 FiatLux - Projeto de Pesquisa")

    if st.button("ℹ️ Como usar", use_container_width=True):
        _dialog_como_usar()

    config_label = "✅ Configuração" if st.session_state.get("api_key") else "⚠️ Configuração"
    if st.button(config_label, use_container_width=True):
        _dialog_configuracao()

    st.markdown("---")
    render_pipeline_nav()


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
