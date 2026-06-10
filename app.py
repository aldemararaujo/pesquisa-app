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
        padding-top: 0 !important;
    }

    /* Permite sticky + gap moderado entre elementos da sidebar */
    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        overflow: visible !important;
        gap: 0.3rem !important;
    }

    /* Padding leve nos wrappers de elemento */
    section[data-testid="stSidebar"] [data-testid="element-container"] {
        padding-top: 0.05rem !important;
        padding-bottom: 0.05rem !important;
        margin-bottom: 0 !important;
    }

    /* Botões da sidebar com altura equilibrada */
    section[data-testid="stSidebar"] .stButton > button {
        padding-top: 0.3rem !important;
        padding-bottom: 0.3rem !important;
        min-height: 2.1rem !important;
        line-height: 1.3 !important;
    }

    /* Parágrafos gerados por st.markdown na sidebar */
    section[data-testid="stSidebar"] .stMarkdown p {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
        line-height: 1.5 !important;
    }

    /* Separadores --- com respiro moderado */
    section[data-testid="stSidebar"] hr {
        margin-top: 0.4rem !important;
        margin-bottom: 0.4rem !important;
    }

    /* Espaçamento leve nos progress bars */
    section[data-testid="stSidebar"] .stProgress {
        margin-top: 0.2rem !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }

    /* Cabeçalho fixo no topo da sidebar */
    section[data-testid="stSidebar"] [data-testid="element-container"]:has(.sidebar-header) {
        position: sticky !important;
        top: 0 !important;
        z-index: 100 !important;
        background-color: #F0F2F6 !important;
        padding-bottom: 0 !important;
    }

    /* Tipografia — três linhas */
    .sidebar-header {
        text-align: center;
        padding: 0.75rem 0.5rem 0.75rem 0.5rem;
        border-bottom: 1px solid rgba(31, 73, 125, 0.18);
        position: relative;
    }
    .sh-icon {
        font-size: 2rem;
        line-height: 1.3;
        display: block;
    }
    .sh-brand {
        font-size: 1.65rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        color: #1F497D;
        font-family: Georgia, 'Times New Roman', serif;
        line-height: 1.2;
        display: block;
    }
    .sh-tagline {
        font-size: 0.78rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        opacity: 0.8;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 700;
        margin-top: 0.15rem;
        display: block;
    }

    .sh-version {
        font-size: 0.7rem;
        letter-spacing: 0.1em;
        opacity: 0.65;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 400;
        margin-top: 0.2rem;
        display: block;
    }

    div[data-testid="stVerticalBlock"] > div {
        gap: 0.25rem !important;
    }

    /* Esconde o span âncora do botão de upload */
    [data-testid="element-container"]:has(#_ul_anchor_) {
        height: 0 !important;
        overflow: hidden !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Posiciona o botão toggle dentro do campo de chat (sidebar expandida ≈ 21rem) */
    [data-testid="element-container"]:has(#_ul_anchor_) + [data-testid="element-container"] {
        position: fixed !important;
        bottom: 10px !important;
        left: calc(21rem + 12px) !important;
        z-index: 999 !important;
        width: 36px !important;
        height: 36px !important;
        padding: 0 !important;
    }
    [data-testid="element-container"]:has(#_ul_anchor_) + [data-testid="element-container"] button {
        border-radius: 50% !important;
        width: 36px !important;
        height: 36px !important;
        min-height: 0 !important;
        padding: 0 !important;
        font-size: 1rem !important;
        line-height: 1 !important;
    }

    /* ===== Contador de tokens ===== */
    .token-counter {
        background: rgba(31, 73, 125, 0.07);
        border: 1px solid rgba(31, 73, 125, 0.18);
        border-radius: 8px;
        padding: 0.5rem 0.75rem 0.4rem;
        text-align: center;
        margin: 0.2rem 0;
    }
    .tc-label {
        font-size: 0.62rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        opacity: 0.6;
        font-weight: 600;
        margin-bottom: 0.15rem;
    }
    .tc-numbers { line-height: 1.1; }
    .tc-used {
        font-size: 1.55rem;
        font-weight: 800;
        color: #1F497D;
        font-family: Georgia, serif;
    }
    .tc-sep {
        font-size: 1rem;
        opacity: 0.45;
        margin: 0 0.1rem;
    }
    .tc-total {
        font-size: 0.85rem;
        opacity: 0.55;
        font-weight: 500;
    }
    .tc-unit {
        font-size: 0.62rem;
        opacity: 0.55;
        margin-top: 0.1rem;
        letter-spacing: 0.05em;
    }
    .tc-medio .tc-used { color: #b86e00; }
    .tc-alto  .tc-used { color: #b91c1c; }
    .tc-medio { border-color: rgba(184,110,0,0.35) !important; background: rgba(184,110,0,0.06) !important; }
    .tc-alto  { border-color: rgba(185,28,28,0.35)  !important; background: rgba(185,28,28,0.06)  !important; }

    /* ===== Progresso do pipeline ===== */
    .etapas-counter {
        background: rgba(31, 73, 125, 0.07);
        border: 1px solid rgba(31, 73, 125, 0.18);
        border-radius: 8px;
        padding: 0.5rem 0.75rem 0.4rem;
        text-align: center;
        margin: 0.2rem 0;
    }
    .ep-label {
        font-size: 0.62rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        opacity: 0.6;
        font-weight: 600;
        margin-bottom: 0.15rem;
    }
    .ep-numbers { line-height: 1.1; }
    .ep-done {
        font-size: 1.55rem;
        font-weight: 800;
        color: #1F497D;
        font-family: Georgia, serif;
    }
    .ep-sep {
        font-size: 1rem;
        opacity: 0.45;
        margin: 0 0.1rem;
    }
    .ep-total {
        font-size: 0.85rem;
        opacity: 0.55;
        font-weight: 500;
    }
    .ep-unit {
        font-size: 0.62rem;
        opacity: 0.55;
        margin-top: 0.1rem;
        letter-spacing: 0.05em;
    }
    .ep-medio    .ep-done  { color: #b86e00; }
    .ep-completo .ep-done  { color: #15803d; }
    .ep-medio    { border-color: rgba(184,110,0,0.35) !important; background: rgba(184,110,0,0.06) !important; }
    .ep-completo { border-color: rgba(21,128,61,0.35)  !important; background: rgba(21,128,61,0.06)  !important; }

    /* Botão nativo de recolher sidebar — sempre visível */
    [data-testid="stSidebarCollapseButton"] {
        opacity: 1 !important;
        visibility: visible !important;
    }
    [data-testid="stSidebarCollapseButton"] button {
        opacity: 1 !important;
        visibility: visible !important;
    }

    /* Abre espaço no textarea para o botão não sobrepor o texto */
    [data-testid="stChatInputContainer"] textarea {
        padding-left: 3rem !important;
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


def _detectar_provedor(chave: str):
    """Retorna (provider_id, ambiguo). ambiguo=True quando sk- pode ser OpenAI ou DeepSeek."""
    if not chave:
        return None, False
    if chave.startswith("sk-ant-"):
        return "anthropic", False
    if chave.startswith("AIza"):
        return "gemini", False
    if chave.startswith("sk-"):
        return "openai", True
    return None, False


@st.dialog("Configuração", width="large")
def _dialog_configuracao():
    provider_id = st.session_state.get("selected_provider", DEFAULT_PROVIDER)

    # Sincroniza api_key do widget do render anterior
    _wk = f"_api_key_{provider_id}"
    if _wk in st.session_state:
        st.session_state.api_key = st.session_state[_wk]
    api_key = st.session_state.get("api_key", "")

    # Auto-detecção do provedor pela chave
    detected, ambiguous = _detectar_provedor(api_key)
    if detected and detected != provider_id:
        st.session_state[f"_api_key_{detected}"] = api_key
        st.session_state["selected_provider"] = detected
        st.session_state["selected_model"] = PROVIDERS[detected]["default_model"]
        provider_id = detected

    prov = PROVIDERS[provider_id]

    # 1. Nome do provedor em destaque
    if detected:
        st.markdown(
            f"<h2 style='margin-bottom:0.1rem'>{prov['label']}</h2>",
            unsafe_allow_html=True,
        )
        if ambiguous:
            ambi = st.radio(
                "Confirme o provedor:",
                options=["openai", "deepseek"],
                format_func=lambda x: PROVIDERS[x]["label"],
                index=0 if provider_id == "openai" else 1,
                horizontal=True,
                key="_ambi_provider",
            )
            if ambi != provider_id:
                st.session_state["selected_provider"] = ambi
                st.session_state["selected_model"] = PROVIDERS[ambi]["default_model"]
                provider_id = ambi
                prov = PROVIDERS[provider_id]
    else:
        provider_ids = list(PROVIDERS.keys())
        current_idx = provider_ids.index(provider_id) if provider_id in provider_ids else 0
        st.selectbox(
            "Provedor de IA",
            options=provider_ids,
            format_func=lambda x: PROVIDERS[x]["label"],
            index=current_idx,
            key="_provider_select",
            on_change=_on_provider_change,
        )
        provider_id = st.session_state.get("selected_provider", DEFAULT_PROVIDER)
        prov = PROVIDERS[provider_id]

    # 2. Chave de API
    if api_key:
        st.success("API configurada", icon="✅")
    else:
        st.warning("Insira a chave de API", icon="⚠️")

    st.text_input(
        prov["key_label"],
        type="password",
        value=api_key,
        placeholder=prov["key_placeholder"],
        key=f"_api_key_{provider_id}",
        help="Sua chave permanece apenas nesta sessão e não é armazenada.",
    )
    st.session_state.api_key = st.session_state.get(f"_api_key_{provider_id}", "")


# Painel lateral
with st.sidebar:
    st.markdown("""
<div class="sidebar-header">
    <div class="sh-icon">📋</div>
    <div class="sh-brand">FiatLux</div>
    <div class="sh-tagline">Projeto de Pesquisa</div>
    <div class="sh-version">v1.1.0 &middot; jun 2026</div>
</div>
""", unsafe_allow_html=True)

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
st.markdown(f"<script>document.title='{_tab_title}'</script>", unsafe_allow_html=True)

skill_atual = st.session_state.skill_atual
render_chat(skill_atual)
