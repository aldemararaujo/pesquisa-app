import streamlit as st
from config import PIPELINE


def render_pipeline_nav():
    st.sidebar.title("Pipeline de Pesquisa")
    st.sidebar.markdown("---")

    fases_vistas = []
    for i, skill in enumerate(PIPELINE):
        fase = skill["fase"]
        if fase not in fases_vistas:
            fases_vistas.append(fase)
            st.sidebar.markdown(f"**{fase}**")

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
            st.sidebar.markdown(f"**{label}**")
        elif skill["id"] in concluidas:
            if st.sidebar.button(label, key=f"nav_{i}", use_container_width=True):
                st.session_state.skill_atual = i
                st.rerun()
        else:
            st.sidebar.markdown(f"<span style='color:#999'>{label}</span>", unsafe_allow_html=True)

    st.sidebar.markdown("---")
    progresso = len(st.session_state.skills_concluidas) / len(PIPELINE)
    st.sidebar.progress(progresso, text=f"{len(st.session_state.skills_concluidas)}/{len(PIPELINE)} etapas concluídas")
