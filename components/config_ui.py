import streamlit as st
from config import PROVIDERS, DEFAULT_PROVIDER


def _on_provider_change():
    new_provider = st.session_state["_provider_select"]
    if new_provider != st.session_state.get("selected_provider"):
        st.session_state["selected_provider"] = new_provider
        st.session_state["selected_model"] = PROVIDERS[new_provider]["default_model"]
        st.session_state["api_key"] = ""


def _on_model_change():
    st.session_state["selected_model"] = st.session_state["_model_select"]


def _on_key_change():
    # Enter no campo da chave dispara o teste automático na tela de entrada
    st.session_state["_auto_conectar"] = True


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


def render_config_form():
    """Formulário de configuração da API: provedor, chave e modelo.

    Usado tanto no dialog da sidebar quanto na tela de entrada."""
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
        on_change=_on_key_change,
        help="Sua chave permanece apenas nesta sessão e não é armazenada.",
    )
    st.session_state.api_key = st.session_state.get(f"_api_key_{provider_id}", "")

    # 3. Modelo
    modelos = prov["models"]
    modelo_atual = st.session_state.get("selected_model", prov["default_model"])
    idx_modelo = modelos.index(modelo_atual) if modelo_atual in modelos else 0
    st.selectbox(
        "Modelo",
        options=modelos,
        index=idx_modelo,
        key="_model_select",
        on_change=_on_model_change,
        help="O modelo padrão do provedor é recomendado para a maioria dos casos.",
    )


def api_conectada() -> bool:
    """True quando o teste de conexão validou exatamente o provedor, o modelo
    e a chave atualmente selecionados."""
    validada = st.session_state.get("api_validada")
    if not validada:
        return False
    atual = (
        st.session_state.get("selected_provider"),
        st.session_state.get("selected_model"),
        st.session_state.get("api_key", ""),
    )
    return validada == atual
