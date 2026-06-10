import streamlit as st
from config import PIPELINE, CONTEXT_LIMITS


def render_pipeline_nav():
    st.sidebar.markdown(
        '<p style="font-weight:700;font-size:0.85rem;letter-spacing:0.05em;'
        'margin:0;padding:0.5rem 0 0.2rem;line-height:1.5">'
        'TRILHA DA PESQUISA</p>',
        unsafe_allow_html=True,
    )

    fases_vistas = []
    for i, skill in enumerate(PIPELINE):
        fase = skill["fase"]
        if fase not in fases_vistas:
            if fases_vistas:
                st.sidebar.markdown("---")
            fases_vistas.append(fase)
            st.sidebar.markdown(
                f'<p style="font-weight:700;font-size:0.9rem;'
                f'margin:0;padding:0.6rem 0 0.25rem;line-height:1.5">'
                f'{fase}</p>',
                unsafe_allow_html=True,
            )

        atual = st.session_state.skill_atual
        concluidas = st.session_state.skills_concluidas

        if skill["id"] in concluidas:
            icone = "✅"
        elif i == atual:
            icone = "▶"
        else:
            icone = "○"

        label = f"{icone} {skill['titulo']}"

        if i == atual:
            if st.sidebar.button(label, key=f"nav_{i}", use_container_width=True, type="primary"):
                pass
        else:
            if st.sidebar.button(label, key=f"nav_{i}", use_container_width=True):
                st.session_state.skill_atual = i
                st.rerun()

    st.sidebar.markdown("---")

    # Indicador de uso de contexto da etapa atual

    skill_id_atual = PIPELINE[st.session_state.skill_atual]["id"]
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
    concluidas_n = len(st.session_state.skills_concluidas)
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
