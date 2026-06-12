"""Motor do Conselho de Especialistas: chamadas LLM das quatro etapas.

Cada etapa é uma chamada independente (sem histórico de chat) ao provedor
e modelo selecionados na sessão. O laço sobre as personas e a persistência
incremental ficam na camada de UI (components.council_ui).
"""

import re
import time
from typing import Callable

import streamlit as st

from config import CONTEXT_LIMITS
from utils.llm_provider import get_provider
from utils.session import add_tokens
from council.personas import (
    PERSONAS,
    PROMPT_IDENTIFICACAO,
    PROMPT_REVISAO_CRUZADA_TEMPLATE,
    PROMPT_RELATOR,
    instrucao_extra,
)

DOC_MAX_FRACAO_CONTEXTO = 0.55

# Limites de tokens por minuto são comuns nos provedores (ex.: Anthropic nível
# inicial: 30.000 tokens de entrada por minuto). Em erro 429, aguardamos a
# janela do minuto renovar e tentamos de novo antes de desistir.
_MAX_TENTATIVAS = 5
_ESPERA_RATE_LIMIT_S = 65

_ROTULOS = ["Parecerista A", "Parecerista B", "Parecerista C", "Parecerista D",
            "Parecerista E", "Parecerista F", "Parecerista G"]

TIPOS_LABEL = {
    "projeto": "Projeto de pesquisa",
    "relatorio": "Relatório final de pesquisa",
    "artigo": "Artigo científico",
}


def estimar_tokens(texto: str) -> int:
    return int(len(texto) / 3.5)


def truncar_documento(texto: str, provider_id: str) -> tuple[str, bool]:
    """Trunca o documento em fronteira de parágrafo quando excede a fração
    permitida da janela de contexto do provedor. Retorna (texto, foi_truncado)."""
    limite_tokens = int(CONTEXT_LIMITS.get(provider_id, 128_000) * DOC_MAX_FRACAO_CONTEXTO)
    if estimar_tokens(texto) <= limite_tokens:
        return texto, False

    limite_chars = int(limite_tokens * 3.5)
    corte = texto.rfind("\n\n", 0, limite_chars)
    if corte < limite_chars // 2:
        corte = limite_chars
    return texto[:corte].rstrip(), True


def eh_rate_limit(e: Exception) -> bool:
    texto = str(e).lower()
    return (
        type(e).__name__ == "RateLimitError"
        or "rate_limit" in texto
        or "rate limit" in texto
        or "429" in texto
    )


def _aguardar_rate_limit(tentativa: int):
    aviso = st.empty()
    for restante in range(_ESPERA_RATE_LIMIT_S, 0, -1):
        aviso.caption(
            f"⏳ Limite de tokens por minuto do provedor atingido "
            f"(tentativa {tentativa} de {_MAX_TENTATIVAS - 1}). "
            f"Aguardando {restante}s para continuar automaticamente..."
        )
        time.sleep(1)
    aviso.empty()


def _chamar(system: str, user_content: str,
            on_chunk: Callable[[str], None] | None = None) -> str:
    provider_id = st.session_state.get("selected_provider", "anthropic")
    model = st.session_state.get("selected_model", "claude-sonnet-4-6")
    api_key = st.session_state.get("api_key", "")

    provider = get_provider(provider_id)
    messages = [{"role": "user", "content": user_content}]

    def _on_tokens(input_t: int, output_t: int):
        add_tokens("conselho", input_t, output_t)

    for tentativa in range(1, _MAX_TENTATIVAS + 1):
        try:
            resposta = ""
            for texto in provider.stream_response(system, messages, model, api_key, on_tokens=_on_tokens):
                resposta += texto
                if on_chunk:
                    on_chunk(resposta)
            return resposta
        except Exception as e:
            if eh_rate_limit(e) and tentativa < _MAX_TENTATIVAS:
                _aguardar_rate_limit(tentativa)
                continue
            raise
    return ""


def parse_tipo_documento(identificacao: str) -> str:
    m = re.search(r"^TIPO:\s*(.+)$", identificacao, flags=re.MULTILINE | re.IGNORECASE)
    if m:
        valor = m.group(1).strip().lower()
        if "artigo" in valor:
            return "artigo"
        if "relat" in valor:
            return "relatorio"
        if "projeto" in valor:
            return "projeto"
    return "projeto"


def rotulos_anonimos(persona_id: str, ids_selecionados: list[str] | None = None) -> dict[str, str]:
    """Mapeia os ids das demais personas participantes para rótulos anônimos,
    em ordem determinística (ordem de PERSONAS, excluindo a própria).
    ids_selecionados restringe aos especialistas escolhidos; None inclui todos."""
    if ids_selecionados is None:
        ids_selecionados = [p["id"] for p in PERSONAS]
    outros = [
        p["id"] for p in PERSONAS
        if p["id"] in ids_selecionados and p["id"] != persona_id
    ]
    return dict(zip(outros, _ROTULOS))


def etapa_identificacao(doc: str, on_chunk=None) -> str:
    user = f"Documento a classificar:\n\n{doc}"
    return _chamar(PROMPT_IDENTIFICACAO, user, on_chunk)


def etapa_parecer(persona: dict, doc: str, identificacao: str, tipo: str,
                  on_chunk=None) -> str:
    system = persona["system_prompt"]
    extra = instrucao_extra(persona["id"], tipo)
    if extra:
        system = system + "\n\n" + extra

    user = (
        f"IDENTIFICAÇÃO DO DOCUMENTO (feita por analista documental):\n"
        f"{identificacao}\n\n"
        f"---\n\n"
        f"DOCUMENTO COMPLETO PARA ANÁLISE:\n\n{doc}"
    )
    return _chamar(system, user, on_chunk)


def etapa_revisao(persona: dict, identificacao: str,
                  pareceres: dict[str, str],
                  ids_selecionados: list[str] | None = None,
                  on_chunk=None) -> str:
    identidade = (
        f"Você é o {persona['nome']} de um conselho de avaliação de documentos "
        f"de pesquisa acadêmica."
    )
    system = PROMPT_REVISAO_CRUZADA_TEMPLATE.format(identidade_curta=identidade)

    rotulos = rotulos_anonimos(persona["id"], ids_selecionados)
    blocos_outros = []
    for outro_id, rotulo in rotulos.items():
        parecer = pareceres.get(outro_id, "")
        blocos_outros.append(f"### {rotulo}\n\n{parecer}")

    user = (
        f"IDENTIFICAÇÃO DO DOCUMENTO:\n{identificacao}\n\n"
        f"---\n\n"
        f"SEU PARECER ({persona['nome']}):\n\n{pareceres.get(persona['id'], '')}\n\n"
        f"---\n\n"
        f"PARECERES DOS DEMAIS CONSELHEIROS (anonimizados):\n\n"
        + "\n\n---\n\n".join(blocos_outros)
    )
    return _chamar(system, user, on_chunk)


def etapa_sintese(identificacao: str, tipo: str, pareceres: dict[str, str],
                  revisoes: dict[str, str], data_analise: str,
                  on_chunk=None) -> str:
    blocos_pareceres = []
    blocos_revisoes = []
    for p in PERSONAS:
        pid = p["id"]
        if pid not in pareceres:
            continue
        blocos_pareceres.append(f"### Parecer da área: {p['nome_curto']}\n\n{pareceres[pid]}")
        if revisoes.get(pid):
            blocos_revisoes.append(f"### Revisão cruzada de {p['nome_curto']}\n\n{revisoes[pid]}")

    user = (
        f"Data da análise: {data_analise}\n"
        f"Tipo do documento: {TIPOS_LABEL.get(tipo, tipo)}\n\n"
        f"IDENTIFICAÇÃO DO DOCUMENTO:\n{identificacao}\n\n"
        f"=== PARECERES DOS CONSELHEIROS ===\n\n"
        + "\n\n---\n\n".join(blocos_pareceres)
    )
    if blocos_revisoes:
        user += (
            "\n\n=== REVISÕES CRUZADAS ===\n\n"
            + "\n\n---\n\n".join(blocos_revisoes)
        )
    else:
        user += (
            "\n\nObservação: a análise contou com um único conselheiro, "
            "portanto não houve rodada de revisão cruzada."
        )
    return _chamar(PROMPT_RELATOR, user, on_chunk)
