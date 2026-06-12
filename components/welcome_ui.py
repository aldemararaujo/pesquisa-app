import streamlit as st
from datetime import datetime

from components.footer import render_footer
from components.config_ui import render_config_form, api_conectada
from config import APP_VERSION

_MESES = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",
]


def _data_extensa(dt: datetime) -> str:
    return f"{dt.day} de {_MESES[dt.month - 1]} de {dt.year}, às {dt.hour:02d}h{dt.minute:02d}min{dt.second:02d}s"


def rodape_aceite() -> str:
    """Bloco de rastreabilidade anexado aos relatórios finais."""
    aceite = st.session_state.get("termo_aceite_em")
    if not aceite:
        return ""
    return (
        "\n\n---\n\n"
        "**Registro de rastreabilidade — FiatLux**\n\n"
        f"Termo de uso aceito pelo usuário em {_data_extensa(aceite)}.\n\n"
        "Conteúdo gerado com apoio de inteligência artificial; "
        "as informações devem ser confirmadas em outras fontes."
    )


def _conectar(chave: str):
    """Executa o teste de conexão e registra a validação na sessão."""
    from utils.llm_provider import testar_conexao, AuthenticationError
    provider_id = st.session_state.get("selected_provider")
    model = st.session_state.get("selected_model")
    try:
        with st.spinner("Testando a conexão com o provedor..."):
            testar_conexao(provider_id, model, chave)
        st.session_state.api_validada = (provider_id, model, chave)
        st.rerun()
    except AuthenticationError:
        st.error("Chave inválida ou não autorizada pelo provedor. Confira e tente novamente.", icon="❌")
    except Exception as e:
        st.error(f"Falha na conexão: {e}", icon="❌")


_TERMO = """
1. **Estado da ferramenta** — Aceito utilizar a ferramenta no estado em que se
encontra, sem garantias de qualquer natureza quanto a disponibilidade,
desempenho ou resultados.

2. **Limites da inteligência artificial** — Estou ciente de que a inteligência
artificial pode cometer erros, inclusive em julgamentos metodológicos e em
cálculos, e que nenhuma resposta dispensa avaliação crítica.

3. **Verificação em outras fontes** — Comprometo-me a confirmar as informações
produzidas pela ferramenta em outras fontes antes de utilizá-las em trabalhos
acadêmicos, decisões ou publicações.
"""


def render_welcome():
    st.markdown("""
<style>
    .welcome-header {
        text-align: center;
        padding: 1rem 0 0.5rem;
    }
    .wh-icon { font-size: 2.6rem; line-height: 1.2; display: block; }
    .wh-brand {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        color: #1F497D;
        font-family: Georgia, 'Times New Roman', serif;
        line-height: 1.2;
        display: block;
    }
    .wh-version {
        font-size: 0.78rem;
        letter-spacing: 0.1em;
        opacity: 0.65;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 400;
        margin-top: 0.25rem;
        display: block;
    }
    .welcome-card {
        background: rgba(31, 73, 125, 0.05);
        border: 1px solid rgba(31, 73, 125, 0.18);
        border-radius: 10px;
        padding: 1rem 1.2rem;
        height: 100%;
    }
    .wc-titulo {
        font-weight: 800;
        color: #1F497D;
        font-size: 1.05rem;
        margin-bottom: 0.4rem;
    }

    /* Seção da API: azul institucional suave (área de configuração) */
    div.st-key-secao_api {
        background: rgba(31, 73, 125, 0.06);
        border: 1px solid rgba(31, 73, 125, 0.20);
        border-radius: 12px;
        padding: 1rem 1.4rem 1.2rem;
        margin-top: 1rem;
    }
    div.st-key-secao_api [data-testid="stVerticalBlockBorderWrapper"] {
        background: #FFFFFF;
        border-radius: 10px;
    }

    /* Seção do termo: âmbar suave (atenção e leitura cuidadosa) */
    div.st-key-secao_termo {
        background: rgba(184, 110, 0, 0.06);
        border: 1px solid rgba(184, 110, 0, 0.28);
        border-radius: 12px;
        padding: 1rem 1.4rem 1.2rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="welcome-header">
    <span class="wh-icon">📋</span>
    <span class="wh-brand">FiatLux</span>
    <span class="wh-version">{APP_VERSION}</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("## Como funciona")
    st.markdown(
        "O FiatLux reúne duas ferramentas complementares de apoio à pesquisa científica."
    )

    col_emil, col_saul = st.columns(2)
    with col_emil:
        st.markdown("""
<div class="welcome-card">
    <div class="wc-titulo">🏛️ EMIL — Conselho de Especialistas</div>
    <p>Analisa um documento pronto: projeto de pesquisa, relatório final ou artigo.
    Oito especialistas emitem pareceres independentes, revisam uns aos outros de
    forma anônima e um relator consolida tudo em um relatório final com sugestões
    de aprimoramento.</p>
</div>
""", unsafe_allow_html=True)
    with col_saul:
        st.markdown("""
<div class="welcome-card">
    <div class="wc-titulo">🧭 SAUL — Trilha do Projeto de Pesquisa</div>
    <p>Conduz a construção de um projeto de pesquisa em 14 etapas guiadas, do
    mapeamento do tema à compilação final do documento. Cada etapa gera arquivos
    para download em Markdown, Word e PDF.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("## Por que eles existem")
    st.markdown("""
A redação científica exige duas formas de apoio que nem sempre estão ao alcance
de quem pesquisa: uma orientação metodológica estruturada, que conduza o
trabalho passo a passo, e uma banca crítica, que examine o texto pronto com
rigor e aponte caminhos de melhoria.

EMIL e SAUL reproduzem esses dois apoios. SAUL faz o papel do orientador que
acompanha cada etapa da construção do projeto; EMIL faz o papel da banca que
critica o resultado e devolve pareceres fundamentados. Nenhum dos dois
substitui orientadores reais, comitês de ética ou a revisão humana — eles
existem para ampliar o acesso a esses cuidados, não para dispensá-los.
""")

    ja_aceito = st.session_state.get("termo_aceito", False)

    if not ja_aceito:
        with st.container(key="secao_api"):
            st.markdown("## Configure sua chave de API")
            st.markdown("""
O FiatLux funciona com a **sua própria chave de API** de um provedor de
inteligência artificial — Anthropic, OpenAI, Google Gemini ou DeepSeek.
A chave permanece apenas nesta sessão e **não é armazenada**.

**Como fazer:**

1. Obtenha a chave no site do provedor:
[console.anthropic.com](https://console.anthropic.com) (Anthropic),
[platform.openai.com](https://platform.openai.com) (OpenAI),
[aistudio.google.com](https://aistudio.google.com) (Google Gemini) ou
[platform.deepseek.com](https://platform.deepseek.com) (DeepSeek).
2. Cole a chave no campo destacado abaixo — o provedor é detectado
automaticamente.
3. Clique em **Conectar** para validar a chave.
""")
            with st.container(border=True):
                render_config_form()
                auto = st.session_state.pop("_auto_conectar", False)

                if api_conectada():
                    st.success("Conectado — API validada e pronta para uso.", icon="🔌")
                else:
                    chave = st.session_state.get("api_key", "")
                    clicou = st.button("🔌 Conectar", type="primary", use_container_width=True)
                    if clicou and not chave:
                        st.warning("Insira a chave de API antes de conectar.", icon="⚠️")
                    elif clicou or (auto and chave):
                        _conectar(chave)

    with st.container(key="secao_termo"):
        st.markdown("### Termo de concordância")
        st.markdown(_TERMO)

        if ja_aceito:
            aceite = st.session_state.get("termo_aceite_em")
            if aceite:
                st.success(f"Termo aceito em {_data_extensa(aceite)}.", icon="✅")
            if st.button("← Voltar à ferramenta", type="primary"):
                st.session_state.mostrar_apresentacao = False
                st.rerun()
        else:
            concorda = st.checkbox("Li e concordo com o termo de uso acima.", key="_termo_checkbox")
            if st.button("Começar", type="primary"):
                if not api_conectada():
                    st.warning("Conecte a API antes de iniciar.", icon="⚠️")
                elif not concorda:
                    st.warning("É necessário marcar a caixa de concordância para iniciar.", icon="⚠️")
                else:
                    st.session_state.termo_aceito = True
                    st.session_state.termo_aceite_em = datetime.now()
                    st.session_state.mostrar_apresentacao = False
                    st.rerun()

    render_footer()
