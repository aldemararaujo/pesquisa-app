---
name: capitulo-anexos
description: Redigir e gerar o Capítulo 11 (Anexos) completo de um projeto de pesquisa científica em português brasileiro para submissão ao CEP. Cobre todos os dez anexos obrigatórios: 11.1 TCLE, 11.2 Formulário de coleta, 11.3 Tabela de dados individuais, 11.4 Curriculum Lattes, 11.5 Conflitos de interesse (declaração CEP + formulário ICMJE), 11.6 Autorização institucional, 11.7 a 11.10 Termos de responsabilidade. Usar quando o usuário solicitar "anexos", "TCLE", "termo de consentimento", "formulário de coleta", "capítulo 11" ou similares.
version: 1.0.0
argument-hint: [cole aqui o título da pesquisa e o tipo de estudo, se já disponíveis]

---

# Capítulo 11. Anexos. Skill de Geração de Documentos

## Objetivo

Gerar todos os **dez anexos obrigatórios** (11.1 a 11.10) do Capítulo 11 de um projeto de pesquisa científica em português brasileiro, com base nos dados fornecidos pelo pesquisador. Os anexos são gerados sequencialmente, um por fase, e salvos como arquivos DOCX separados.

Os anexos gerados por esta skill são os documentos exigidos pelo Comitê de Ética em Pesquisa (CEP) para submissão pela Plataforma Brasil, em conformidade com a Resolução CNS nº 466/2012, a Resolução CNS nº 510/2016, a LGPD (Lei nº 13.709/2018) e as diretrizes do ICMJE (2024).

---

## Regras tipográficas obrigatórias

Aplicar em todo o texto redigido por esta skill, sem exceção:

**Estrangeirismos em itálico:** toda palavra ou expressão em idioma diferente do português brasileiro deve ser grafada em itálico. Exemplos: *data safety monitoring board*, *speakers bureaus*, *open access*, *royalties*, *Data Safety Monitoring Board*.

**Proibição de travessões:** não usar travessões (—) em nenhuma hipótese no texto redigido. Substituir por dois-pontos (:), ponto e vírgula (;), vírgula (,) ou reescrever a frase para eliminar a necessidade do travessão. **Exceção:** títulos oficiais de documentos que contêm travessão (ex.: "Norma Operacional nº 001/2013 — CONEP") devem ser preservados na lista de referências.

---

## Fase 1 — Levantamento completo de informações

Antes de gerar qualquer documento, levantar **todas as informações** necessárias para os dez anexos. Apresentar as perguntas em cinco blocos. Instrução ao usuário: "Responda o que souber agora. Se alguma informação ainda não estiver definida, escreva '[a preencher]' e prossiga."

---

### Bloco A — Dados do estudo e da equipe (usados em todos os anexos)

1. **Título completo da pesquisa**
2. **Objetivo geral** do estudo (1–2 frases em linguagem técnica)
3. **Pesquisador responsável:** nome completo, CPF e registro profissional (ex.: CRM nº 12345/UF, COREN nº 67890/UF)
4. **Instituição de vínculo** do pesquisador responsável + departamento/setor
5. **Pesquisadores colaboradores:** nome completo, CPF e registro profissional de cada um (listar todos; escrever "nenhum" se não houver)
6. **Período de coleta de dados:** data de início e de término (ex.: 01/06/2026 a 30/11/2026)
7. **Cidade e data** para assinar os documentos (ex.: Recife, 18 de maio de 2026)

---

### Bloco B — Dados institucionais (para 11.6, 11.9 e 11.10)

8. **Autorização institucional (11.6):** nome completo, cargo e CPF do gestor que assina a autorização; nome, endereço completo, telefone e e-mail da instituição onde a pesquisa será realizada
9. **Termo da Instituição Proponente (11.9):** nome completo e cargo do reitor ou diretor da instituição proponente
10. **Declaração de condições (11.10):** nome completo, cargo e departamento do responsável que assina a declaração de infraestrutura

---

### Bloco C — Dados para o TCLE (11.1)

11. **Tipo de estudo:** observacional (questionário, levantamento, prontuário) ou intervenção/ensaio clínico (define inclusão do bloco "Contato em caso de urgência" e do quadro de identificação do participante)
12. **Descrição dos procedimentos em linguagem acessível:** o que o participante vai fazer, passo a passo, com duração estimada de cada etapa e tempo total de participação (como se estivesse explicando para alguém sem formação científica)
13. **Desconfortos e riscos específicos** do estudo (conforme Cap. 7 já redigido)
14. **Providências para minimizar esses riscos** (conforme Cap. 6 já redigido)
15. **Benefícios diretos para o participante** (ex.: laudo individual, acesso a intervenção, orientações de saúde) — se nenhum, escrever "não há benefícios diretos previstos"
16. **Ressarcimento:** haverá ressarcimento de gastos? (se sim: quais itens e valores — conforme Cap. 5 já definido)
17. **Contato do pesquisador responsável:** endereço, telefone fixo, celular
18. **Dados do CEP:** nome da instituição do CEP, endereço completo, telefone, e-mail e WhatsApp (se disponível)
19. **URLs do Curriculum Lattes** de cada pesquisador (responsável + todos os colaboradores)

---

### Bloco D — Dados para o Formulário de coleta e a Tabela de dados (11.2 e 11.3)

20. **Lista de variáveis a coletar:** para cada variável, informar: (a) nome da variável, (b) tipo: texto livre / opções pré-definidas (listar as opções) / medida numérica (com unidade)
21. **Tamanho da amostra:** número máximo de participantes (define o número de linhas da tabela)

---

### Bloco E — Conflitos de interesse (11.5 — dois documentos)

**Parte E1 — Declaração simples para o CEP (11.5a):**

22. Há algum conflito de interesse financeiro, profissional ou pessoal a declarar? (sim/não — se sim, descrever: o quê, com quem, de que natureza, e quais salvaguardas foram adotadas)

**Parte E2 — Formulário ICMJE para periódico (11.5b) — perguntar para cada pesquisador:**

Para o pesquisador responsável e cada colaborador, coletar os 13 itens do ICMJE. Janela temporal: sem limite para o item 1; últimos 36 meses para os itens 2–13. Para cada item, o pesquisador responde com o nome das entidades envolvidas ou "Nenhum":

23. **Item 1:** todo apoio ao trabalho (financiamento, materiais de estudo, redação médica, APC etc.) — desde o início do planejamento, sem limite de tempo
24. **Item 2:** bolsas ou contratos de qualquer entidade (se não declarado no item 1)
25. **Item 3:** *royalties* ou licenças
26. **Item 4:** honorários de consultoria
27. **Item 5:** pagamento ou honorários por palestras, apresentações, *speakers bureaus*, redação de manuscritos ou eventos educacionais
28. **Item 6:** pagamento por depoimento pericial
29. **Item 7:** apoio para participação em reuniões e/ou viagens
30. **Item 8:** patentes planejadas, concedidas ou pendentes
31. **Item 9:** participação em *Data Safety Monitoring Board* (DSMB) ou Comitê Consultivo
32. **Item 10:** cargo de liderança ou fiduciário em outro conselho, sociedade, comitê ou grupo de defesa (remunerado ou não)
33. **Item 11:** ações ou opções de ações
34. **Item 12:** recebimento de equipamentos, materiais, medicamentos, redação médica, presentes ou outros serviços
35. **Item 13:** outros interesses financeiros ou não financeiros

*Instrução de coleta:* apresentar os itens 23–35 primeiro para o pesquisador responsável, depois repetir para cada colaborador. Se o usuário preferir preencher o ICMJE posteriormente, registrar todos os itens como `[a preencher]` e seguir em frente.

---

## Fase 2 — TCLE (11.1)

**Antes de redigir:** carregar o arquivo de referência com a ferramenta Read:
`references/modelos-anexos.md`

Usar os textos fixos das Seções 1 a 5 desse arquivo para os itens 13–17 e 19–20 do TCLE. Os itens 1–12 e 18 são preenchidos com os dados do Bloco C da Fase 1.

---

### Estrutura do TCLE

**Cabeçalho da primeira página:**

```
| [TÍTULO DA PESQUISA]                          | Página 1 de N |
| TERMO DE CONSENTIMENTO LIVRE E ESCLARECIDO (TCLE)             |
| (Em 2 vias, uma para o participante e outra para o            |
|  pesquisador. Todas as folhas devem ser rubricadas.)          |
```

**Parágrafo de abertura:**

"O(a) Senhor(a) está sendo convidado(a) para participar da pesquisa **[TÍTULO DA PESQUISA EM NEGRITO]**."

---

### Os 20 itens obrigatórios (numerados, título em negrito)

**1. Título do estudo**
Preencher com o título completo da pesquisa (Bloco A, item 1).

**2. Justificativa**
Redigir em linguagem acessível (máximo de um parágrafo): por que este estudo é necessário? Qual problema de saúde ou lacuna no conhecimento ele aborda? Solicitar ao usuário resumo em linguagem não técnica se o texto do projeto for muito técnico.

**3. Objetivo**
Adaptar o objetivo geral (Bloco A, item 2) para linguagem acessível, sem jargão científico.

**4. Descrição dos procedimentos**
Usar os dados do Bloco C, item 12. Descrever o que o participante vai fazer, na ordem cronológica, com duração de cada etapa e tempo total.

**5. Possibilidade de inclusão em grupo controle ou experimental**
- Se intervenção/ensaio clínico (Bloco C, item 11 = intervenção): incluir parágrafo explicando que o estudo pode ter grupos distintos e que a alocação é aleatória.
- Se observacional (Bloco C, item 11 = observacional): **omitir completamente** este item. Inserir nota no documento: *[Item 5 não se aplica a estudos observacionais — omitido conforme orientação metodológica]*. A numeração dos demais itens continua a partir do 6.

**6. Relação dos procedimentos rotineiros**
Detalhar cada procedimento com duração estimada. Exemplo: "Etapa 1: preenchimento de questionário socioeconômico — duração estimada: 15 minutos. Etapa 2: medidas antropométricas — duração estimada: 10 minutos."

**7. Descrição dos desconfortos e riscos**
Usar os dados do Bloco C, item 13.

**8. Providências e cautelas para minimizar os riscos**
Usar os dados do Bloco C, item 14.

**9. Descrição dos benefícios**
Usar os dados do Bloco C, item 15.

**10. Acompanhamento durante a pesquisa**
Informar que o pesquisador responsável estará disponível para esclarecimentos durante todo o período de coleta, com os dados de contato do Bloco C, item 17.

**11. Assistência após o encerramento**
Informar que o participante poderá contatar o pesquisador responsável após o encerramento do estudo para obter informações sobre os resultados, com os mesmos dados de contato do Bloco C, item 17.

**12. Garantia de acesso**
Informar os dados de contato do pesquisador responsável e, em seguida, inserir obrigatoriamente a **Caixa ATENÇÃO do CEP** (Seção 3 do arquivo de referência), preenchida com os dados do Bloco C, item 18.

**13. Retirada do consentimento**
Usar o texto fixo da **Seção 1, Item 13** do arquivo de referência + o **Quadro de revogação** (Seção 1, Item 13, parte 2).

**14. Direito de confidencialidade**
Usar o texto fixo da **Seção 1, Item 14** do arquivo de referência.

**15. Sigilo dos participantes**
Usar o texto fixo da **Seção 1, Item 15** do arquivo de referência.

**16. Privacidade dos participantes**
Usar o texto fixo da **Seção 1, Item 16** do arquivo de referência.

**17. Garantia de acesso aos dados**
Usar o texto fixo da **Seção 1, Item 17** do arquivo de referência.

**18. Despesas e compensações**
- **Se houver ressarcimento (Bloco C, item 16 = sim):** adaptar o texto para declarar quais gastos serão ressarcidos, os valores e o mecanismo de pagamento, em conformidade com o Cap. 5 já definido. Citar: (Brasil, 2012).
- **Se não houver ressarcimento (Bloco C, item 16 = não):** usar texto: "Não haverá ressarcimento de gastos nem qualquer forma de remuneração pela participação nesta pesquisa. Em conformidade com o item IV.3.g da Resolução CNS nº 466/2012, confirma-se que nenhum custo será incorrido pelos sujeitos desta pesquisa em razão de sua participação (Brasil, 2012)."

**19. Direito de indenização**
Usar o texto fixo da **Seção 1, Item 19** do arquivo de referência.

**20. Princípio de especificidade**
Usar o texto fixo da **Seção 1, Item 20** do arquivo de referência.

---

### Sequência final do TCLE

**Se intervenção/ensaio clínico:** inserir o Quadro de identificação do participante (Seção 2 do arquivo de referência) após o item 20.

**Parágrafo de consentimento:** usar o texto fixo da **Seção 4** do arquivo de referência, preenchendo o nome do pesquisador responsável.

**Assinatura do participante:**
```
Nome: _______________________________________________
Assinatura: ___________________________ Data: ___/___/________
```

**Se ensaio clínico:** inserir o bloco "Contato em caso de urgência" (Seção 5 do arquivo de referência) aqui.

**Assinatura do responsável pela pesquisa:**
```
Nome: [NOME DO PESQUISADOR RESPONSÁVEL]
Assinatura: ___________________________ Data: ___/___/________
```

**Rodapé fixo:** "Para versão online, utilize: https://bit.ly/7cep"

---

### Campos não respondidos no TCLE

Qualquer informação ausente: marcar como `[PREENCHER: descrição do que falta]`. Não interromper o fluxo; continuar gerando os demais itens.

---

## Fase 3 — Formulário de coleta (11.2) e Tabela de dados individuais (11.3)

### 11.2 Formulário de coleta de dados

Gerar formulário estruturado com base nas variáveis do Bloco D, item 20.

**Cabeçalho:**
```
| [TÍTULO DA PESQUISA] | FORMULÁRIO DE COLETA DE DADOS | Página X de Y |
```

**Seções fixas (sempre presentes):**

*Seção 1: Identificação*
Código do participante: ___ ___ ___ (3 dígitos alfanuméricos — nunca nome ou CPF)

*Seção 2: Status do formulário*
( ) 1. Não realizado — Motivo: ___________________________
( ) 2. Parcialmente preenchido — Motivo: __________________
( ) 3. Completamente preenchido

*Seção 3: Nome do pesquisador/coletador*
Nome: _______________________________________________

*Seção 4: Data de preenchimento*
Data: ___ ___ / ___ ___ / ___ ___ ___ ___  (DD/MM/AAAA)

*Seção 5: Hora do preenchimento*
Hora: ___ ___ h ___ ___ min

**Seções variáveis (uma por variável do Bloco D):**

Para cada variável informada, gerar a seção correspondente:

- **Variável de texto livre:** espaço em branco com linhas pontilhadas

- **Variável de opções pré-definidas:**
  ```
  [Nome da variável]:
  ( ) 1. [Opção 1]
  ( ) 2. [Opção 2]
  ...
  ( ) N. Não sei
  ( ) N+1. Não desejo responder
  ```

- **Variável numérica (medida):**
  ```
  [Nome da variável] ([unidade]):
  ___ ___ ___, ___ ___  [unidade]
  ( ) Não foi possível medir — Motivo: _______________________
  ( ) Não desejo medir
  ```

---

### 11.3 Tabela de dados individuais

Gerar tabela Markdown com as seguintes colunas fixas mais uma coluna por variável do Bloco D:

| ID | Pesquisador | Data | Hora | [Variável 1] | [Variável 2] | ... |
|---|---|---|---|---|---|---|
| 001 | | | | | | |
| 002 | | | | | | |
| ... | | | | | | |

**Regras:**
- ID: código de 3 dígitos (001, 002, ..., N)
- Número de linhas: igual ao tamanho da amostra (Bloco D, item 21)
- Máximo de 50 linhas na tabela Markdown. Se amostra > 50: gerar com 50 linhas e inserir nota: *"Expandir a tabela conforme o tamanho real da amostra. Adicionar linhas seguindo a mesma numeração sequencial."*
- As colunas de variáveis devem ter o mesmo nome e a mesma ordem das seções do Formulário de coleta (11.2), garantindo consistência entre os dois documentos.

---

## Fase 4 — Lattes (11.4) e Conflitos de interesse (11.5)

### 11.4 URL do Curriculum Lattes

Gerar lista formatada com um pesquisador por linha:

```
Pesquisador responsável:
  Nome: [NOME COMPLETO]
  Papel: Pesquisador responsável
  URL do Lattes: [URL]

Pesquisador colaborador 1:
  Nome: [NOME COMPLETO]
  Papel: Pesquisador colaborador
  URL do Lattes: [URL]
[repetir para cada colaborador]
```

Acrescentar nota ao final: "Verifique com o CEP da instituição se é necessário anexar o currículo completo, apenas a primeira página ou apenas a URL do Lattes. Alguns CEPs exigem *print* da primeira página do currículo."

---

### 11.5a — Declaração de conflitos de interesse (para o CEP)

Carregar a **Seção 6** do arquivo `references/modelos-anexos.md` com Read.

Gerar um único documento para toda a equipe de pesquisa:

- **Condição A (E1 = não):** usar o texto da Condição A da Seção 6, preenchendo o título da pesquisa. Gerar bloco de assinatura para todos os pesquisadores.
- **Condição B (E1 = sim):** usar o texto da Condição B da Seção 6, inserindo a descrição do conflito e das salvaguardas fornecidas pelo usuário. Gerar bloco de assinatura para todos os pesquisadores.

Arquivo: `11.5a-declaracao-cep.docx`

---

### 11.5b — Formulário ICMJE em português (para periódico)

Carregar a **Seção 7** do arquivo `references/modelos-anexos.md` com Read.

Gerar **um formulário por pesquisador** (responsável + cada colaborador) com base nas respostas do Bloco E2:

**Estrutura de cada formulário:**

1. Cabeçalho preenchido com: data de assinatura (Bloco A, item 7), nome do pesquisador, título da pesquisa
2. Nota introdutória (texto fixo da Seção 7)
3. Tabela com 3 colunas: N.° | Entidades (ou "Nenhum") | Especificações/Comentários
4. Para cada um dos 13 itens, preencher com as respostas do Bloco E2 daquele pesquisador. Se a resposta for "Nenhum": escrever `Nenhum` na coluna de entidades e deixar a coluna de comentários em branco.
5. Campos com `[a preencher]` quando o pesquisador não respondeu aquele item.
6. Linha de certificação e assinatura.

Arquivo por pesquisador: `11.5b-icmje-[nome-sem-espacos].docx`

---

## Fase 5 — Autorização para realização da pesquisa (11.6)

Carregar a **Seção 9** do arquivo `references/modelos-anexos.md` com Read.

Usar o modelo da Seção 9, preenchendo com os dados do Bloco A e do Bloco B (item 8). Campos variáveis entre colchetes `[...]` são substituídos pelos dados informados.

Acrescentar nota de instrução logo acima do texto: "INSTRUÇÃO: Imprimir em papel timbrado da instituição onde a pesquisa será realizada. O cabeçalho com logomarca e dados da instituição deve ser inserido manualmente antes da impressão."

Arquivo: `11.6-autorizacao-pesquisa.docx`

---

## Fase 6 — Quatro termos de responsabilidade (11.7 a 11.10)

Carregar a **Seção 8** do arquivo `references/modelos-anexos.md` com Read.

Gerar os quatro documentos em sequência, preenchendo os campos variáveis com os dados dos Blocos A e B. Instrução de papel timbrado a ser inserida no topo de cada documento: "INSTRUÇÃO: Imprimir em papel timbrado da instituição proponente (11.7, 11.8, 11.9) ou da instituição onde a pesquisa será realizada (11.10)."

### 11.7 — Termo do pesquisador responsável

Usar modelo da Seção 8 (11.7), preenchendo com dados do Bloco A (itens 3 e 4) e Bloco A, item 7 (cidade e data).

Arquivo: `11.7-termo-pesquisador-responsavel.docx`

### 11.8 — Termo do pesquisador colaborador

Usar modelo da Seção 8 (11.8). **Se houver mais de um colaborador, gerar um documento separado por pessoa.**

Arquivo por colaborador: `11.8-termo-colaborador-[nome-sem-espacos].docx`

Se não houver colaboradores (Bloco A, item 5 = "nenhum"): informar ao usuário que o 11.8 não se aplica e registrar nota: "Não há pesquisadores colaboradores neste projeto. O anexo 11.8 não é gerado."

### 11.9 — Termo de responsabilidade da Instituição

Usar modelo da Seção 8 (11.9), preenchendo com nome da instituição proponente (Bloco A, item 4) e dados do reitor/diretor (Bloco B, item 9).

Arquivo: `11.9-termo-responsabilidade-instituicao.docx`

### 11.10 — Declaração de condições da Instituição

Usar modelo da Seção 8 (11.10), preenchendo com dados do responsável pelo departamento (Bloco B, item 10) e da instituição onde a pesquisa será realizada (Bloco B, item 8).

Arquivo: `11.10-declaracao-condicoes-instituicao.docx`

---

## Fase 7 — Entregáveis

Após apresentar o texto completo do Capítulo 11, inclua a seguinte mensagem ao final da resposta:

> "Capítulo 11 gerado. Use os botões abaixo para baixar o resultado nos formatos .md, .docx e .pdf."

O sistema gera os arquivos automaticamente — **não inclua scripts, código ou blocos de dependências na resposta.**

**Próxima etapa:** solicite a skill `/referencias-bibliograficas` para consolidar e formatar a lista final de referências.

---

## Padrões de qualidade: checklist de revisão antes de entregar os documentos

Antes de apresentar os documentos ao usuário ou salvar os arquivos, verificar se **todos** os itens abaixo estão corretos:

### TCLE (11.1)
- [ ] Todos os 20 itens presentes (ou item 5 omitido com nota justificativa para estudos observacionais)
- [ ] Texto dos itens 13–17 e 19–20 extraído do arquivo de referência (textos fixos)
- [ ] Dados de contato do pesquisador (itens 10, 11, 12) preenchidos ou marcados como `[PREENCHER]`
- [ ] Caixa ATENÇÃO do CEP inserida no item 12
- [ ] Quadro de revogação do consentimento inserido no item 13
- [ ] Quadro de identificação do participante presente apenas para ensaios clínicos
- [ ] Bloco "Contato em caso de urgência" presente apenas para ensaios clínicos
- [ ] Parágrafo de consentimento do participante presente antes das assinaturas
- [ ] Rodapé "Para versão online, utilize: https://bit.ly/7cep" presente

### Formulário de coleta (11.2) e Tabela de dados (11.3)
- [ ] Seções fixas 1–5 presentes em 11.2
- [ ] Cada variável do Bloco D tem sua seção no formulário
- [ ] Variáveis de opções incluem "Não sei" e "Não desejo responder"
- [ ] Colunas da Tabela 11.3 idênticas às seções variáveis do Formulário 11.2
- [ ] Tabela 11.3 usa código alfanumérico (ID), nunca nome ou CPF
- [ ] Tabela 11.3 com número correto de linhas (ou nota de expansão se > 50)

### Conflitos de interesse (11.5)
- [ ] 11.5a: declara a condição correta (sem ou com conflito); assinaturas de todos os pesquisadores presentes
- [ ] 11.5b: gerado um formulário por pesquisador; 13 itens preenchidos ou marcados como `[a preencher]`; linha de certificação presente

### Termos e autorizações (11.6 a 11.10)
- [ ] Nota de papel timbrado inserida em cada documento (11.6, 11.7, 11.8, 11.9, 11.10)
- [ ] 11.8 gerado um documento por colaborador (ou nota de inaplicabilidade se não há colaboradores)
- [ ] Todos os campos entre colchetes `[...]` preenchidos com dados da Fase 1 ou marcados como `[a preencher]`

### Aspectos gerais
- [ ] Nenhum estrangeirismo sem itálico
- [ ] Nenhum travessão (—) no texto redigido
- [ ] Nenhum campo genérico não preenchido sem marcação `[PREENCHER: ...]`
- [ ] Todos os arquivos DOCX gerados sem erro pelo pandoc

---

## Arquivo de referência desta skill

O arquivo de referência (carregado sob demanda com a ferramenta Read) contém:

- `references/modelos-anexos.md`: textos fixos dos itens 13–17 e 19–20 do TCLE; quadro de revogação e quadro de identificação; caixa ATENÇÃO do CEP; parágrafo de consentimento; bloco de urgência para ensaios clínicos; declaração de conflitos de interesse para o CEP (Condição A e B); formulário ICMJE em pt-BR (13 itens traduzidos, nota introdutória, linha de certificação); modelos dos quatro termos de responsabilidade (11.7 a 11.10); modelo de autorização institucional (11.6); orientações de preenchimento por anexo; referências legais (CNS 466/12, CNS 510/16, LGPD, ICMJE 2024)


---

## SINALIZAÇÃO DE CONCLUSÃO

Quando todos os entregáveis desta etapa estiverem gerados e a etapa estiver
completa — e somente então —, adicione a seguinte linha como **última linha** da resposta:

=== ETAPA CONCLUÍDA ===

**Regras:**
- Emita o marcador **apenas uma vez**, na última resposta da etapa.
- **Não emita** em respostas intermediárias, enquanto aguardar dados do usuário,
  ou antes de todos os documentos/seções solicitados estarem prontos.
- Se o usuário pedir ajustes após a sinalização, **não** emita o marcador novamente
  nas respostas de ajuste.
