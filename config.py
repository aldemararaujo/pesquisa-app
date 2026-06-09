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

CONTEXT_LIMITS = {
    "anthropic": 200_000,
    "openai": 128_000,
    "gemini": 1_000_000,
    "deepseek": 64_000,
}

PIPELINE = [
    {
        "id": "research-topic-mapper",
        "titulo": "Mapeamento do Tema",
        "descricao": "Defina e delimite o tema de pesquisa: área, subárea, recorte populacional e viabilidade. Resultado: tema claro e pronto para avançar.",
        "fase": "Pré-redação",
    },
    {
        "id": "pico-research-question",
        "titulo": "Pergunta de Pesquisa",
        "descricao": "Transforme o tema em pergunta estruturada no formato PICO, definindo população, intervenção, comparação e desfecho do estudo.",
        "fase": "Pré-redação",
    },
    {
        "id": "plano-intencao",
        "titulo": "Plano de Intenção",
        "descricao": "Consolide a ideia em um resumo executivo validado, com avaliação de viabilidade e checklist para submissão ao CEP.",
        "fase": "Pré-redação",
    },
    {
        "id": "fundamentacao-teorica",
        "titulo": "Fundamentação Teórica",
        "descricao": "Construa o referencial teórico com conceitos-chave, revisão da literatura e a lacuna do conhecimento que justifica a pesquisa.",
        "fase": "Capítulos",
    },
    {
        "id": "introducao-pesquisa",
        "titulo": "Capítulo 1 — Introdução",
        "descricao": "Redija a introdução com contexto, relevância, hipótese e objetivo geral do estudo. Base argumentativa para todo o projeto.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-metodos",
        "titulo": "Capítulo 2 — Métodos",
        "descricao": "Descreva o delineamento, critérios de inclusão e exclusão, cálculo amostral, instrumentos de coleta e análise estatística.",
        "fase": "Capítulos",
    },
    {
        "id": "etapas-e-cronograma",
        "titulo": "Capítulos 3, 4 e 5",
        "descricao": "Detalhe as etapas operacionais, cronograma em Gantt, recursos materiais e orçamento completo com fontes de financiamento.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-monitorizacao",
        "titulo": "Capítulo 6 — Monitorização",
        "descricao": "Estabeleça medidas de proteção aos participantes, monitorização dos dados, confidencialidade e critérios de suspensão do estudo.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-riscos-beneficios",
        "titulo": "Capítulo 7 — Riscos e Benefícios",
        "descricao": "Elabore a matriz de riscos, analise os benefícios esperados e demonstre que a relação risco-benefício é eticamente aceitável.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-propriedade-responsabilidades",
        "titulo": "Capítulos 8, 9 e 10",
        "descricao": "Defina direitos de propriedade intelectual, plano de divulgação e responsabilidades do pesquisador, instituição e patrocinador.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-anexos",
        "titulo": "Capítulo 11 — Anexos",
        "descricao": "Elabore TCLE, formulário de coleta, declarações de conflito de interesse, autorizações institucionais e termos de responsabilidade.",
        "fase": "Capítulos",
    },
    {
        "id": "referencias-bibliograficas",
        "titulo": "Referências Bibliográficas",
        "descricao": "Consolide todas as referências citadas, elimine duplicatas e formate na norma Vancouver com verificação de completude.",
        "fase": "Finalização",
    },
    {
        "id": "elementos-pre-textuais",
        "titulo": "Elementos Pré-textuais",
        "descricao": "Gere capa, folha de informações gerais no formato CEP, sumário completo e lista de abreviaturas do projeto de pesquisa.",
        "fase": "Finalização",
    },
    {
        "id": "compilacao-final",
        "titulo": "Compilação Final",
        "descricao": "Verifique a coerência entre todos os capítulos e compile o documento completo em Markdown, Word e PDF pronto para o CEP.",
        "fase": "Finalização",
    },
]

PIPELINE_IDS = [s["id"] for s in PIPELINE]
