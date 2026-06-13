import streamlit as st
from utils.session import init_session
from components.pipeline_nav import render_pipeline_nav
from components.chat_ui import render_chat
from components.council_ui import render_council
from components.welcome_ui import render_welcome
from components.footer import render_footer
from components.config_ui import render_config_form
from config import DEFAULT_PROVIDER, APP_VERSION

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

# Rola tela principal e sidebar para o topo após transições de tela
if st.session_state.pop("_rolar_topo", False):
    st.iframe("""
<script>
    function rolarTopo() {
        const doc = window.parent.document;
        const seletores = [
            '[data-testid="stAppViewContainer"]',
            '[data-testid="stMain"]',
            'section.main',
            'section[data-testid="stSidebar"] > div',
        ];
        for (const sel of seletores) {
            const el = doc.querySelector(sel);
            if (el) el.scrollTo({top: 0, behavior: "instant"});
        }
        doc.documentElement.scrollTo({top: 0, behavior: "instant"});
    }
    setTimeout(rolarTopo, 100);
    setTimeout(rolarTopo, 350);
</script>
""", height=1)

# Tela de entrada obrigatória: apresentação e termo de concordância
if not st.session_state.termo_aceito or st.session_state.mostrar_apresentacao:
    render_welcome()
    st.stop()

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

    /* Expansores de fase na sidebar */
    section[data-testid="stSidebar"] [data-testid="stExpander"] {
        border: 1px solid rgba(31, 73, 125, 0.15) !important;
        border-radius: 8px !important;
        margin-bottom: 0.3rem !important;
    }
    section[data-testid="stSidebar"] [data-testid="stExpander"] summary p {
        font-weight: 700 !important;
        font-size: 0.88rem !important;
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
</style>
""", unsafe_allow_html=True)


@st.dialog("Como usar o FiatLux", width="large")
def _dialog_como_usar():
    st.markdown("""
**1. Configure a IA**
Abra "Configuração" na barra lateral, escolha o provedor, insira sua chave de API e selecione o modelo.
Sua chave não é armazenada — fica apenas nesta sessão.

**2. Siga o pipeline em ordem**
O pipeline tem 14 etapas, do mapeamento do tema até a compilação final.
Complete cada etapa antes de avançar para a próxima.

**3. Converse com a IA**
Digite sua mensagem no campo de chat.
Para anexar arquivos `.txt`, `.md` ou `.docx` como contexto, use o clipe 📎 dentro do próprio campo de mensagem.

**4. Baixe os arquivos gerados**
Ao final de cada etapa, exporte o resultado em Markdown, Word ou PDF.

**5. Monitore o uso de contexto**
A barra na sidebar mostra quantos tokens foram consumidos na etapa atual.
O total acumulado da sessão aparece ao final da barra lateral.

**6. EMIL — Conselho de Especialistas**
Fora do pipeline, o Conselho analisa um documento pronto (projeto, relatório
final ou artigo): oito especialistas emitem pareceres, revisam uns aos outros
de forma anônima e um relator consolida tudo em um relatório com sugestões.
    """)


@st.dialog("Configuração", width="large")
def _dialog_configuracao():
    render_config_form()


# Painel lateral
with st.sidebar:
    st.markdown(f"""
<div class="sidebar-header">
    <div class="sh-icon">📋</div>
    <div class="sh-brand">FiatLux</div>
    <div class="sh-version">{APP_VERSION}</div>
</div>
""", unsafe_allow_html=True)

    if st.button("ℹ️ Como usar", use_container_width=True):
        _dialog_como_usar()

    config_label = "✅ Configuração" if st.session_state.get("api_key") else "⚠️ Configuração"
    if st.button(config_label, use_container_width=True):
        _dialog_configuracao()

    st.markdown("---")

    _conselho_ativo = st.session_state.get("modo_app") == "conselho"
    _conselho_label = "🏛️ EMIL — Conselho de Especialistas"
    if st.button(
        _conselho_label,
        use_container_width=True,
        type="primary" if _conselho_ativo else "secondary",
    ):
        if not _conselho_ativo:
            st.session_state.modo_app = "conselho"
            st.rerun()

    st.markdown("---")

    _trilha_ativa = st.session_state.get("modo_app") == "pipeline"
    if st.button(
        "🧭 SAUL — Trilha do Projeto de Pesquisa",
        use_container_width=True,
        type="primary" if _trilha_ativa else "secondary",
    ):
        if st.session_state.saul_expandido:
            st.session_state.saul_expandido = False
        else:
            st.session_state.saul_expandido = True
            st.session_state.modo_app = "pipeline"
        st.rerun()

    if st.session_state.saul_expandido:
        render_pipeline_nav()


if st.session_state.get("modo_app") == "conselho":
    render_council()
else:
    skill_atual = st.session_state.skill_atual
    render_chat(skill_atual)

render_footer()
