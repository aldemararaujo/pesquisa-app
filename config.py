CLAUDE_MODEL = "claude-sonnet-4-6"

PROVIDERS = {
    "anthropic": {
        "label": "Anthropic (Claude)",
        "key_label": "Chave Anthropic API",
        "key_placeholder": "sk-ant-...",
        "models": [
            "claude-opus-4-5",
            "claude-sonnet-4-6",
            "claude-sonnet-4-5",
            "claude-3-5-sonnet-20241022",
            "claude-3-5-haiku-20241022",
        ],
        "default_model": "claude-sonnet-4-6",
    },
    "openai": {
        "label": "OpenAI (ChatGPT)",
        "key_label": "Chave OpenAI API",
        "key_placeholder": "sk-...",
        "models": [
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4-turbo",
            "o1-mini",
        ],
        "default_model": "gpt-4o",
    },
    "gemini": {
        "label": "Google (Gemini)",
        "key_label": "Chave Google AI API",
        "key_placeholder": "AIza...",
        "models": [
            "gemini-2.0-flash",
            "gemini-1.5-pro",
            "gemini-1.5-flash",
        ],
        "default_model": "gemini-2.0-flash",
    },
    "deepseek": {
        "label": "DeepSeek",
        "key_label": "Chave DeepSeek API",
        "key_placeholder": "sk-...",
        "models": [
            "deepseek-chat",
            "deepseek-reasoner",
        ],
        "default_model": "deepseek-chat",
    },
}

DEFAULT_PROVIDER = "anthropic"

PIPELINE = [
    {
        "id": "research-topic-mapper",
        "titulo": "Mapeamento do Tema",
        "descricao": "Passo 1 — Mapeamento e definição do tema de pesquisa",
        "fase": "Pré-redação",
    },
    {
        "id": "pico-research-question",
        "titulo": "Pergunta de Pesquisa",
        "descricao": "Passo 2 — Transformação do tema em pergunta PICO",
        "fase": "Pré-redação",
    },
    {
        "id": "plano-intencao",
        "titulo": "Plano de Intenção",
        "descricao": "Passo 3 — Resumo estruturado do projeto",
        "fase": "Pré-redação",
    },
    {
        "id": "fundamentacao-teorica",
        "titulo": "Fundamentação Teórica",
        "descricao": "Referencial teórico — capítulo independente",
        "fase": "Capítulos",
    },
    {
        "id": "introducao-pesquisa",
        "titulo": "Capítulo 1 — Introdução",
        "descricao": "Contexto, hipótese e objetivo",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-metodos",
        "titulo": "Capítulo 2 — Métodos",
        "descricao": "Delineamento, amostra e método de coleta",
        "fase": "Capítulos",
    },
    {
        "id": "etapas-e-cronograma",
        "titulo": "Capítulos 3, 4 e 5",
        "descricao": "Etapas, cronograma, recursos e orçamento",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-monitorizacao",
        "titulo": "Capítulo 6 — Monitorização",
        "descricao": "Proteção, segurança e acompanhamento dos dados",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-riscos-beneficios",
        "titulo": "Capítulo 7 — Riscos e Benefícios",
        "descricao": "Matriz de riscos e análise ética",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-propriedade-responsabilidades",
        "titulo": "Capítulos 8, 9 e 10",
        "descricao": "Propriedade intelectual e responsabilidades",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-anexos",
        "titulo": "Capítulo 11 — Anexos",
        "descricao": "TCLE, formulários, declarações e termos",
        "fase": "Capítulos",
    },
    {
        "id": "referencias-bibliograficas",
        "titulo": "Referências Bibliográficas",
        "descricao": "Consolidação e formatação Vancouver",
        "fase": "Finalização",
    },
    {
        "id": "elementos-pre-textuais",
        "titulo": "Elementos Pré-textuais",
        "descricao": "Capa, sumário e lista de abreviaturas",
        "fase": "Finalização",
    },
    {
        "id": "compilacao-final",
        "titulo": "Compilação Final",
        "descricao": "Verificação de coerência e documento completo",
        "fase": "Finalização",
    },
]

PIPELINE_IDS = [s["id"] for s in PIPELINE]
