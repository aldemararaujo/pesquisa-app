import streamlit as st


def init_session():
    from config import PROVIDERS, DEFAULT_PROVIDER
    defaults = {
        "skill_atual": 0,
        "skills_concluidas": set(),
        "historico": {},
        "contextos_portateis": {},
        "tokens_por_skill": {},
        "etapas_prontas": {},
        "upload_counter": 0,
        "api_key": "",
        "selected_provider": DEFAULT_PROVIDER,
        "selected_model": PROVIDERS[DEFAULT_PROVIDER]["default_model"],
        "modo_app": "pipeline",
        "conselho": {},
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def add_tokens(skill_id: str, input_tokens: int, output_tokens: int):
    tokens = st.session_state.setdefault("tokens_por_skill", {})
    if skill_id not in tokens:
        tokens[skill_id] = {"input": 0, "output": 0}
    tokens[skill_id]["input"] += input_tokens
    tokens[skill_id]["output"] += output_tokens


def get_historico(skill_id: str) -> list:
    return st.session_state.historico.get(skill_id, [])


def append_mensagem(skill_id: str, role: str, content: str):
    if skill_id not in st.session_state.historico:
        st.session_state.historico[skill_id] = []
    st.session_state.historico[skill_id].append({"role": role, "content": content})


def save_portable_context(skill_id: str, context_text: str):
    st.session_state.contextos_portateis[skill_id] = context_text


def build_context_prefix(skill_ids_anteriores: list[str]) -> str:
    partes = []
    for sid in skill_ids_anteriores:
        ctx = st.session_state.contextos_portateis.get(sid)
        if ctx:
            partes.append(ctx)
    if not partes:
        return ""
    return (
        "## CONTEXTO DO PROJETO (gerado nas etapas anteriores)\n\n"
        + "\n\n---\n\n".join(partes)
        + "\n\n---\n\n"
    )


def marcar_concluida(skill_id: str):
    st.session_state.skills_concluidas.add(skill_id)


def avancar_skill():
    from config import PIPELINE
    atual = st.session_state.skill_atual
    if atual < len(PIPELINE) - 1:
        st.session_state.skill_atual = atual + 1
