import streamlit as st
from config import PIPELINE, CONTEXT_LIMITS

_FASE_ICONES = {
    "Pré-redação": "🧭",
    "Capítulos": "📖",
    "Finalização": "📦",
}


def render_pipeline_nav():
    atual = st.session_state.skill_atual
    concluidas = st.session_state.skills_concluidas
    fase_atual = PIPELINE[atual]["fase"]

    # Agrupa etapas por fase, preservando a ordem do pipeline
    fases = []
    for skill in PIPELINE:
        if skill["fase"] not in fases:
            fases.append(skill["fase"])

    for fase in fases:
        indices = [i for i, s in enumerate(PIPELINE) if s["fase"] == fase]
        feitas = sum(1 for i in indices if PIPELINE[i]["id"] in concluidas)
        icone_fase = _FASE_ICONES.get(fase, "📁")
        rotulo = f"{icone_fase} {fase} · {feitas}/{len(indices)}"

        with st.sidebar.expander(rotulo, expanded=(fase == fase_atual)):
            for i in indices:
                skill = PIPELINE[i]

                if skill["id"] in concluidas:
                    icone = "✅"
                elif i == atual:
                    icone = "▶"
                else:
                    icone = "○"

                label = f"{icone} {skill['titulo']}"

                if i == atual:
                    if st.button(label, key=f"nav_{i}", use_container_width=True, type="primary"):
                        if st.session_state.get("modo_app") != "pipeline":
                            st.session_state.modo_app = "pipeline"
                            st.session_state._rolar_topo = True
                            st.rerun()
                else:
                    if st.button(label, key=f"nav_{i}", use_container_width=True):
                        st.session_state.skill_atual = i
                        st.session_state.modo_app = "pipeline"
                        st.session_state._rolar_topo = True
                        st.rerun()

    st.sidebar.markdown("---")

    # Indicador de uso de contexto da etapa atual
    skill_id_atual = PIPELINE[atual]["id"]
    tokens = st.session_state.get("tokens_por_skill", {}).get(skill_id_atual, {"input": 0, "output": 0})
    total_tokens = tokens["input"] + tokens["output"]
    provider_id = st.session_state.get("selected_provider", "anthropic")
    limite = CONTEXT_LIMITS.get(provider_id, 128_000)
    pct_ctx = min(total_tokens / limite, 1.0)
    if pct_ctx >= 0.8:
        cor_class = "tc-alto"
    elif pct_ctx >= 0.5:
        cor_class = "tc-medio"
    else:
        cor_class = "tc-baixo"

    st.sidebar.markdown(f"""
<div class="token-counter {cor_class}">
    <div class="tc-label">Contexto da etapa</div>
    <div class="tc-numbers">
        <span class="tc-used">{total_tokens:,}</span>
        <span class="tc-sep"> / </span>
        <span class="tc-total">{limite:,}</span>
    </div>
    <div class="tc-unit">tokens &nbsp;&middot;&nbsp; {pct_ctx*100:.1f}%</div>
</div>
""", unsafe_allow_html=True)
    st.sidebar.progress(pct_ctx)

    st.sidebar.markdown("---")
    concluidas_n = len(concluidas)
    total_n = len(PIPELINE)
    progresso = concluidas_n / total_n

    if concluidas_n == total_n:
        ep_class = "ep-completo"
    elif progresso >= 0.5:
        ep_class = "ep-medio"
    else:
        ep_class = "ep-inicio"

    st.sidebar.markdown(f"""
<div class="etapas-counter {ep_class}">
    <div class="ep-label">Progresso do pipeline</div>
    <div class="ep-numbers">
        <span class="ep-done">{concluidas_n}</span>
        <span class="ep-sep"> / </span>
        <span class="ep-total">{total_n}</span>
    </div>
    <div class="ep-unit">etapas concluídas &nbsp;&middot;&nbsp; {progresso*100:.0f}%</div>
</div>
""", unsafe_allow_html=True)
    st.sidebar.progress(progresso)

    # Total acumulado da sessão (substitui o título dinâmico da aba, que não funcionava)
    _sessao = sum(
        v["input"] + v["output"]
        for v in st.session_state.get("tokens_por_skill", {}).values()
    )
    if _sessao > 0:
        st.sidebar.caption(f"Total da sessão: {_sessao:,} tokens")
