APP_VERSION = "v1.3.0 · 12 jun 2026"

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
        "descricao": "Explore e delimite o tema de pesquisa identificando área, subárea, recorte populacional e contexto institucional. A IA orienta o levantamento de lacunas na literatura, a análise de viabilidade e a definição de um tema específico, original e exequível no prazo disponível.",
        "fase": "Pré-redação",
    },
    {
        "id": "pico-research-question",
        "titulo": "Pergunta de Pesquisa",
        "descricao": "Transforme o tema delimitado em uma pergunta científica estruturada no formato PICO: Paciente, Intervenção, Comparação e Desfecho. A pergunta resultante guia todo o delineamento metodológico e é o critério central para a revisão da literatura e a seleção dos estudos.",
        "fase": "Pré-redação",
    },
    {
        "id": "plano-intencao",
        "titulo": "Plano de Intenção",
        "descricao": "Consolide a ideia em um resumo executivo estruturado com título, objetivo, hipótese e contexto. Em três fases: coleta de dados, geração do Plano com PDF e Avaliação de Viabilidade com veredicto em três níveis e plano de ação para os itens críticos identificados.",
        "fase": "Pré-redação",
    },
    {
        "id": "fundamentacao-teorica",
        "titulo": "Fundamentação Teórica",
        "descricao": "Construa o referencial teórico identificando conceitos-chave, revisando a literatura disponível e apontando a lacuna do conhecimento que justifica a pesquisa. Gera texto acadêmico formal em português brasileiro com citações Vancouver integradas ao longo do capítulo.",
        "fase": "Capítulos",
    },
    {
        "id": "introducao-pesquisa",
        "titulo": "Capítulo 1 — Introdução",
        "descricao": "Redija o Capítulo 1 com contexto epidemiológico ou clínico, justificativa da relevância, hipótese central e objetivo geral do estudo. Estabelece a base argumentativa que orienta todos os demais capítulos e fundamenta a necessidade da pesquisa perante o CEP.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-metodos",
        "titulo": "Capítulo 2 — Métodos",
        "descricao": "Descreva o Capítulo 2 com delineamento do estudo, critérios de inclusão e exclusão, cálculo amostral, instrumentos de coleta e análise estatística. Adapta-se ao tipo de estudo seguindo as diretrizes CONSORT, STROBE ou PRISMA e a Resolução CNS 466/2012.",
        "fase": "Capítulos",
    },
    {
        "id": "etapas-e-cronograma",
        "titulo": "Capítulos 3, 4 e 5",
        "descricao": "Detalhe os Capítulos 3, 4 e 5: etapas operacionais da pesquisa, cronograma em diagrama de Gantt, lista de recursos materiais por categoria e orçamento itemizado com valor unitário, total, fonte e destinação. Segue a base legal da CNS 466/2012 e 510/2016.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-monitorizacao",
        "titulo": "Capítulo 6 — Monitorização",
        "descricao": "Elabore o Capítulo 6 com medidas de proteção aos participantes, sistema de monitorização de dados, plano de confidencialidade conforme a LGPD e critérios de suspensão do estudo. Inclui referências à tabela CTCAE v5.0 e às regras de parada pré-estabelecidas.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-riscos-beneficios",
        "titulo": "Capítulo 7 — Riscos e Benefícios",
        "descricao": "Elabore o Capítulo 7 com a Matriz de Riscos (probabilidade e severidade), narrativo de análise, avaliação dos benefícios esperados e a relação risco-benefício exigida pelo CEP. Fundamentado na Declaração de Helsinque e na Resolução CNS 466/2012.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-propriedade-responsabilidades",
        "titulo": "Capítulos 8, 9 e 10",
        "descricao": "Redija os Capítulos 8, 9 e 10: direitos de propriedade intelectual (Lei 9.610/98), plano de divulgação com princípios FAIR, responsabilidades do pesquisador, instituição e patrocinador (ICMJE 2023) e declaração de autonomia ou salvaguardas para grupos vulneráveis.",
        "fase": "Capítulos",
    },
    {
        "id": "capitulo-anexos",
        "titulo": "Capítulo 11 — Anexos",
        "descricao": "Produza os 10 anexos do Capítulo 11: TCLE com 20 itens obrigatórios (CNS 466/12), formulário de coleta de dados, tabela de dados individuais, currículos Lattes, declarações ICMJE de conflito de interesse, autorização institucional e quatro termos de responsabilidade.",
        "fase": "Capítulos",
    },
    {
        "id": "referencias-bibliograficas",
        "titulo": "Referências Bibliográficas",
        "descricao": "Consolide todas as referências citadas no projeto, elimine duplicatas por DOI, PMID ou similaridade de título e formate na norma Vancouver com ordenação alfabética. Campos ausentes são sinalizados e um relatório de duplicatas é gerado ao usuário ao final.",
        "fase": "Finalização",
    },
    {
        "id": "elementos-pre-textuais",
        "titulo": "Elementos Pré-textuais",
        "descricao": "Gere a capa com titulação e contatos da equipe, a folha de Informações Gerais no formato Plataforma Brasil (alíneas a–l), o sumário completo com todos os capítulos e subseções, e a lista de abreviaturas em duas colunas ordenadas alfabeticamente.",
        "fase": "Finalização",
    },
    {
        "id": "compilacao-final",
        "titulo": "Compilação Final",
        "descricao": "Verifique a coerência do projeto em três dimensões (conteúdo, forma e estilo), gere relatório com pendências críticas e sugestões e compile o documento final em quatro formatos: Markdown, Word, PDF e relatório de coerência datado. Encerra o pipeline completo.",
        "fase": "Finalização",
    },
]

PIPELINE_IDS = [s["id"] for s in PIPELINE]
