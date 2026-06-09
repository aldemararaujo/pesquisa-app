---
name: etapas-e-cronograma
description: Redigir a seção 3 (Etapas e Cronograma), o Capítulo 4 (Relação de Materiais Necessários) e o Capítulo 5 (Orçamento: 5.1 Quadro de recursos, fontes e destinação; 5.2 Previsão de ressarcimento de gastos aos sujeitos da pesquisa) de um projeto de pesquisa científica em português brasileiro. Usar quando o usuário solicitar "etapas da pesquisa", "cronograma", "seção de etapas", "materiais necessários", "orçamento", "quadro de recursos", "ressarcimento", "seção 3", "capítulo 4" ou "capítulo 5" do projeto. A skill coleta todas as informações de uma só vez, redige 3.1 com linguagem acadêmica formal no futuro do indicativo, gera a tabela de Gantt (3.2), lista os materiais em tabela por categoria (Cap. 4) e produz o quadro de recursos com fontes e destinação mais o texto de ressarcimento (Cap. 5).
version: 2.0.1
argument-hint: [duração-em-meses] [período-de-início]

---

# Etapas e Cronograma, Materiais e Orçamento — Skill de Redação Acadêmica

## Objetivo

Produzir três seções completas de um projeto de pesquisa científica em português brasileiro formal:

- **3. Etapas e Cronograma**
  - 3.1 Etapas da pesquisa — lista numerada com breve descrição de cada etapa
  - 3.2 Cronograma — tabela de Gantt distribuindo as etapas ao longo do período de execução
- **4. Relação de Materiais Necessários** — tabela por categoria com todos os materiais e equipamentos previstos
- **5. Orçamento**
  - 5.1 Quadro de recursos, fontes e destinação — tabela com itens, valores, fonte de financiamento e destinação
  - 5.2 Previsão de ressarcimento de gastos aos sujeitos da pesquisa — texto fundamentado na CNS 466/12

Todo o texto redigido deve estar no **futuro do indicativo** ("será realizada", "serão coletados") por se tratar de um projeto ainda a ser executado.

---

## Regras tipográficas obrigatórias

Aplicar em todo o texto redigido por esta skill, sem exceção:

**Estrangeirismos em itálico:** toda palavra ou expressão em idioma diferente do português brasileiro deve ser grafada em itálico (ex.: *software*, *data sharing*, *open access*).

**Proibição de travessões:** não usar travessões (—) em nenhuma hipótese no texto redigido. Substituir por dois-pontos (:), ponto e vírgula (;) ou vírgula (,). Exceção: títulos oficiais de documentos que já contêm travessão devem ser preservados na lista de referências.

---

## Fase 1 — Levantamento completo das informações

Solicitar **todas** as informações abaixo em um único bloco, para que o usuário responda de uma só vez. Se o usuário já tiver fornecido alguma delas no prompt inicial, aproveitar e não repetir as perguntas correspondentes.

**Bloco A — Seção 3 (Etapas e Cronograma)**

1. **Duração total da pesquisa** em meses (ex.: 6, 12, 18, 24)
2. **Período de início** (ex.: Janeiro/2025, Março/2026, 1º semestre/2025)
3. **Unidade de tempo do cronograma**: mensal ou bimestral
   - Sugerir **mensal** se duração ≤ 12 meses
   - Sugerir **bimestral** se duração > 12 meses
4. **Haverá relatório parcial?** (sim/não — se sim, em qual mês aproximado)

**Bloco B — Capítulos 4 e 5 (Materiais e Orçamento)**

5. **Tipo de estudo**: observacional, experimental/intervencional, qualitativo, misto ou outro (descrever brevemente) — usado para sugerir categorias de materiais pertinentes
6. **Materiais e equipamentos previstos**: listar livremente tudo que planeja usar (consumíveis, equipamentos, *softwares*, impressos, etc.); a skill organizará a lista em categorias
7. **Fonte(s) de financiamento**: recursos próprios do pesquisador, bolsa institucional (especificar agência: CNPq, CAPES, FAPESP, FAPERJ, FAPEMIG, FAPESQ, etc.), edital específico, verba de pesquisa da instituição, ou sem financiamento externo
8. **Os participantes terão gastos decorrentes da participação?** (transporte, alimentação, estacionamento, ausência remunerada do trabalho): se sim, descrever os tipos de gasto e o valor estimado por participante/sessão; se não, informar por quê (ex.: coleta online sem deslocamento, coleta no local de trabalho do participante)
9. **Haverá pagamento a serviços ou profissionais contratados?** (estatístico, transcritor de entrevistas, revisor, digitador): se sim, informar o serviço e o valor estimado em R$
10. **Mês e ano de referência do orçamento** (ex.: maio/2026) — padrão: mês e ano atuais

---

## Fase 2 — Redação de 3.1 (Etapas da pesquisa)

Redigir um parágrafo introdutório de 2 a 3 frases descrevendo que a pesquisa será conduzida em etapas sequenciais e interdependentes, conforme planejamento metodológico. Em seguida, apresentar a lista de etapas abaixo com 1 a 2 frases de descrição cada, em linguagem acadêmica formal no futuro do indicativo.

**Etapas fixas (sempre nesta ordem):**

1. **Coleta de dados** — aplicação dos instrumentos de coleta (questionários, exames, entrevistas, consulta a prontuários ou outra fonte de dados) junto à população do estudo, conforme protocolo metodológico aprovado.

2. **Armazenamento dos dados** — os dados coletados serão registrados em banco de dados estruturado (planilha eletrônica ou *software* específico), com controle de acesso restrito aos pesquisadores responsáveis, garantindo a confidencialidade e integridade das informações.

3. **Tabulação dos dados** — organização e codificação das variáveis coletadas, com revisão da consistência interna dos registros e preparação do banco de dados para análise estatística.

4. **Relatório parcial** *(incluir somente se o usuário confirmar que haverá)* — elaboração de relatório de andamento da pesquisa, apresentando os resultados preliminares obtidos até o período referido, conforme exigência institucional ou do órgão financiador.

5. **Análise dos dados** — processamento estatístico do banco de dados utilizando *software* adequado, com aplicação dos testes previamente definidos no protocolo metodológico, para verificar as hipóteses do estudo.

6. **Interpretação dos resultados** — discussão crítica dos achados obtidos na análise estatística, confrontando-os com a literatura científica vigente e avaliando as implicações clínicas, epidemiológicas ou sociais dos resultados.

7. **Relatório final** — consolidação de todos os resultados e conclusões do estudo em documento técnico-científico final, apresentado à instituição proponente e, quando pertinente, ao órgão financiador.

8. **Elaboração do artigo original** — redação do manuscrito científico destinado à submissão em periódico indexado, com estrutura conforme as normas de publicação do veículo-alvo (Introdução, Métodos, Resultados, Discussão e Conclusão).

**Instrução de formatação:** apresentar as etapas como lista numerada, cada etapa em negrito seguida de dois-pontos e a descrição. Adaptar a descrição ao tipo de estudo se o usuário tiver fornecido contexto (pergunta 5).

---

## Fase 3 — Geração de 3.2 (Cronograma)

Gerar uma tabela de Gantt simplificada em formato Markdown, seguindo as regras abaixo:

### Regras de construção da tabela

**Colunas:** períodos sequenciais a partir do mês/período de início informado pelo usuário.
- Unidade mensal: "Jan/25", "Fev/25", etc.
- Unidade bimestral: "1º Bim/25", "2º Bim/25", etc. (cada bimestre = 2 meses)

**Linhas:** as 8 etapas (ou 7, se não houver relatório parcial).

**Células:** `X` quando a etapa está ativa naquele período; célula vazia quando não está.

### Distribuição padrão das etapas ao longo do tempo

Aplicar a distribuição abaixo, proporcional à duração total (ajustar os intervalos conforme o número de meses/bimestres):

| Etapa | Período de execução |
|---|---|
| Coleta de dados | 1º terço da pesquisa |
| Armazenamento dos dados | Simultâneo à coleta (mesmo período) |
| Tabulação dos dados | Último mês da coleta + 1 a 2 períodos após |
| Relatório parcial (se houver) | Aproximadamente na metade da pesquisa |
| Análise dos dados | Após tabulação, 2 a 3 períodos |
| Interpretação dos resultados | Simultânea ou logo após a análise |
| Relatório final | Penúltimo ou último período |
| Elaboração do artigo original | Último ou dois últimos períodos |

**Sobreposições realistas obrigatórias:**
- Coleta e armazenamento ocorrem **simultaneamente**
- Interpretação começa enquanto a análise ainda está em andamento
- Relatório final e artigo podem se sobrepor no último período

### Exemplo de saída para 12 meses, início Janeiro/2025, unidade mensal

```
| Etapa                          | Jan | Fev | Mar | Abr | Mai | Jun | Jul | Ago | Set | Out | Nov | Dez |
|--------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Coleta de dados                |  X  |  X  |  X  |  X  |     |     |     |     |     |     |     |     |
| Armazenamento dos dados        |  X  |  X  |  X  |  X  |     |     |     |     |     |     |     |     |
| Tabulação dos dados            |     |     |     |  X  |  X  |     |     |     |     |     |     |     |
| Relatório parcial              |     |     |     |     |     |  X  |     |     |     |     |     |     |
| Análise dos dados              |     |     |     |     |     |  X  |  X  |  X  |     |     |     |     |
| Interpretação dos resultados   |     |     |     |     |     |     |     |  X  |  X  |     |     |     |
| Relatório final                |     |     |     |     |     |     |     |     |     |  X  |  X  |     |
| Elaboração do artigo original  |     |     |     |     |     |     |     |     |     |     |  X  |  X  |
```

Adaptar a tabela à duração e unidade de tempo fornecidas pelo usuário. Se não houver relatório parcial, omitir aquela linha.

---

## Fase 4 — Redação do Capítulo 4 (Relação de materiais necessários)

Antes de redigir, carregar o arquivo de referência com a ferramenta **Read**:
`references/materiais-e-orcamento.md`

Consultar a Seção 1 desse arquivo para sugerir itens pertinentes ao tipo de estudo informado pelo usuário. Cruzar com a lista livre fornecida pelo usuário (pergunta 6) e organizar por categoria.

### Parágrafo introdutório

Redigir 2 a 3 frases declarando que os materiais e equipamentos listados a seguir são necessários à execução das etapas descritas na seção 3.1, em conformidade com o protocolo metodológico aprovado. Citar o tipo de estudo se o usuário o tiver informado.

### Tabela de materiais

Apresentar a tabela agrupada por categoria. Incluir apenas as categorias que tiverem pelo menos um item. Omitir categorias vazias.

**Categorias disponíveis (nesta ordem de apresentação):**
1. Materiais de consumo
2. Equipamentos
3. Recursos humanos contratados
4. Tecnologia da informação
5. Infraestrutura e serviços
6. Transporte e diárias
7. Outros

**Formato:**

| Categoria | Item | Quantidade | Unidade |
|---|---|---|---|
| Materiais de consumo | [ex.: Formulário de coleta de dados impresso] | [N] | unidade |
| Materiais de consumo | [ex.: Caneta esferográfica] | [N] | unidade |
| Equipamentos | [ex.: Balança digital antropométrica] | 1 | unidade |
| Tecnologia da informação | [ex.: Licença de *software* estatístico SPSS v.29] | 1 | licença anual |

Consultar a Seção 4 do arquivo de referência para unidades de medida padrão por tipo de item.

Após a tabela, não adicionar texto explicativo.

### Saída esperada para o Capítulo 4

```
4. RELAÇÃO DE MATERIAIS NECESSÁRIOS

[Parágrafo introdutório de 2–3 frases]

| Categoria | Item | Quantidade | Unidade |
|---|---|---|---|
[linhas da tabela]
```

---

## Fase 5 — Redação do Capítulo 5 (Orçamento)

O arquivo de referência já deve estar carregado da Fase 4. Se não estiver, carregar novamente com a ferramenta **Read**:
`references/materiais-e-orcamento.md`

### Fase 5.1 — Seção 5.1: Quadro de recursos, fontes e destinação

**Parágrafo introdutório:** 2 frases situando o orçamento no contexto do estudo e mencionando a(s) fonte(s) de financiamento informadas pelo usuário.

**Tabela do quadro de recursos:**

- Usar os mesmos itens listados no Capítulo 4 como base
- Acrescentar serviços contratados (pergunta 9) que não sejam materiais físicos
- Agrupar por categoria com subtotais
- Incluir linha de TOTAL GERAL ao final
- Campos de valor desconhecidos: marcar como `[a preencher]`

**Formato:**

| Item | Qtd. | Valor unitário (R$) | Total (R$) | Fonte de financiamento | Destinação |
|---|---|---|---|---|---|
| **Materiais de consumo** | | | | | |
| [Item 1] | [N] | [valor] | [total] | [fonte] | [etapa] |
| Subtotal: Materiais de consumo | | | [subtotal] | | |
| **Equipamentos** | | | | | |
| [Item] | [N] | [valor] | [total] | [fonte] | [etapa] |
| Subtotal: Equipamentos | | | [subtotal] | | |
| **TOTAL GERAL** | | | **[total]** | | |

Se houver campos marcados como `[a preencher]`, acrescentar nota de rodapé ao final da tabela:
> (*) Valor a ser definido após cotação com fornecedor.

**Instrução de consistência:** os itens e quantidades desta tabela devem ser idênticos aos do Capítulo 4. Se o usuário informar (pergunta 9) algum serviço contratado que não aparece como material no Cap. 4 (ex.: estatístico contratado), incluí-lo somente nesta tabela, sob a categoria correspondente.

### Fase 5.2 — Seção 5.2: Previsão de ressarcimento de gastos aos sujeitos da pesquisa

Consultar a Seção 3 do arquivo de referência para o texto padrão baseado na CNS 466/12 e para identificar se o tipo de estudo (pergunta 5) é de ciências humanas/sociais (aplicar CNS 510/2016 adicionalmente).

**Condição A — Há ressarcimento previsto** (usuário confirmou na pergunta 8 que participantes terão gastos):

Redigir **dois parágrafos**:

*Parágrafo 1:* Declarar que os participantes serão ressarcidos dos gastos comprovadamente decorrentes de sua participação na pesquisa, em conformidade com o item IV.3.g da Resolução CNS nº 466/2012, que veda qualquer forma de ônus financeiro ao participante decorrente da pesquisa. Listar os tipos de ressarcimento previstos (transporte, alimentação, estacionamento, compensação de horas de trabalho perdidas) e os valores ou critérios de cálculo correspondentes. Citar: (Brasil, 2012).

*Parágrafo 2:* Descrever o mecanismo de ressarcimento: momento do pagamento (por sessão de coleta, ao final, mensalmente), forma de comprovação (apresentação de bilhete/nota fiscal ou declaração assinada), responsável pelo pagamento e fonte de custeio (identificar a rubrica correspondente no quadro 5.1). Citar: (Brasil, 2012).

**Condição B — Não há ressarcimento previsto** (usuário confirmou na pergunta 8 que não haverá gastos):

Redigir **um parágrafo único**, com a justificativa contextual pertinente ao tipo de coleta. Consultar a Seção 3 do arquivo de referência para a variante correta:
- Variante 1: coleta online (questionário eletrônico sem deslocamento)
- Variante 2: coleta no local de trabalho do participante
- Variante 3: coleta na instituição proponente, sem ausência remunerada (participante é funcionário da instituição)

Adaptar a variante ao contexto específico informado pelo usuário. Sempre fundamentar com CNS 466/12, item IV.3.g.

**Lista de referências (obrigatória ao final da seção 5.2):**

Incluir as referências citadas, no formato Vancouver, em ordem alfabética. Incluir obrigatoriamente:
- Brasil. Conselho Nacional de Saúde. Resolução nº 466, de 12 de dezembro de 2012. Diário Oficial da União. 2013 Jun 13;seção 1:59. Disponível em: https://conselho.saude.gov.br/resolucoes/2012/Reso466.pdf

Se o tipo de estudo for qualitativo ou de ciências humanas e sociais, incluir também:
- Brasil. Conselho Nacional de Saúde. Resolução nº 510, de 7 de abril de 2016. Diário Oficial da União. 2016 Mai 24;seção 1:44. Disponível em: https://conselho.saude.gov.br/resolucoes/2016/Reso510.pdf

### Saída esperada para o Capítulo 5

```
5. ORÇAMENTO

5.1 Quadro de recursos, fontes e destinação

[Parágrafo introdutório de 2 frases]

| Item | Qtd. | Valor unitário (R$) | Total (R$) | Fonte de financiamento | Destinação |
|---|---|---|---|---|---|
[linhas da tabela com subtotais e total geral]

[(*) Nota de rodapé se houver campos [a preencher]]

5.2 Previsão de ressarcimento de gastos aos sujeitos da pesquisa

[1 ou 2 parágrafos conforme Condição A ou B]

Referências

[Lista Vancouver]
```

---

## Fase 6 — Geração de Arquivos (automática, após o checklist)

Imediatamente após a entrega do texto completo e do checklist de qualidade, gerar os
três arquivos sem aguardar novo comando do pesquisador. [O sistema gerará o arquivo para download]
nome base: `etapas-cronograma_[AAAAMMDD]`

**Ordem de geração:**
1. Salvar o texto completo em `etapas-cronograma_[AAAAMMDD].md` com a ferramenta **Write**
2. Gerar `etapas-cronograma_[AAAAMMDD].docx` (instruções abaixo)
3. Gerar `etapas-cronograma_[AAAAMMDD].pdf` (instruções abaixo)
4. Confirmar ao pesquisador os três caminhos completos dos arquivos gerados

### DOCX

Converter o `.md` gerado no Passo 1 para DOCX com pandoc:
```
pandoc "C:\Users\aldem\etapas-cronograma_[AAAAMMDD].md" -o "C:\Users\aldem\etapas-cronograma_[AAAAMMDD].docx" --from markdown --to docx
```
Se pandoc não estiver instalado (`winget install pandoc`), manter o `.md` e informar o usuário.

### PDF

**Passo 2 — Salvar como HTML intermediário:**
Usar a ferramenta **Write** para salvar o conteúdo como arquivo `.html` com formatação completa (estilos CSS *inline*, tabela renderizada, charset UTF-8, tag `lang="pt-BR"`, margens A4 de 25mm), em `C:\Users\aldem\etapas-cronograma_[AAAAMMDD].html`.

> Atenção: tabelas com muitas colunas (especialmente a tabela 5.1) podem quebrar em PDF. Informar ao usuário que, se a tabela parecer cortada, pode usar Ctrl+P no navegador e ajustar a escala para 75%. Para edição posterior, escolha a opção DOCX.

**Passo 3 — Converter para PDF com wkhtmltopdf:**
```
& "C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe" --encoding utf-8 --page-size A4 --margin-top 25mm --margin-bottom 25mm --margin-left 25mm --margin-right 25mm "C:\Users\aldem\etapas-cronograma_[AAAAMMDD].html" "C:\Users\aldem\etapas-cronograma_[AAAAMMDD].pdf"
```
Fallback via pandoc: `pandoc "...[AAAAMMDD].md" -o "...[AAAAMMDD].pdf" --pdf-engine=wkhtmltopdf`

**Passo 4 — Se nenhum conversor funcionar:**
Manter o `.html` e informar:
> "PDF não gerado automaticamente. Abra o arquivo HTML no navegador e use Ctrl+P → 'Salvar como PDF'."

Após PDF gerado com sucesso, remover o `.html` temporário. O `.md` é parte da entrega — não remover.

---

## Saída final esperada

Entregar o texto completo pronto para copiar e colar no projeto, com a seguinte estrutura:

```
3. ETAPAS E CRONOGRAMA

3.1 Etapas da pesquisa

[Parágrafo introdutório de 2–3 frases]

1. Coleta de dados: [descrição]
2. Armazenamento dos dados: [descrição]
3. Tabulação dos dados: [descrição]
[4. Relatório parcial: [descrição] — somente se confirmado]
[4 ou 5]. Análise dos dados: [descrição]
[5 ou 6]. Interpretação dos resultados: [descrição]
[6 ou 7]. Relatório final: [descrição]
[7 ou 8]. Elaboração do artigo original: [descrição]

3.2 Cronograma

[Tabela de Gantt em Markdown]

4. RELAÇÃO DE MATERIAIS NECESSÁRIOS

[Parágrafo introdutório de 2–3 frases]

| Categoria | Item | Quantidade | Unidade |
|---|---|---|---|
[linhas da tabela]

5. ORÇAMENTO

5.1 Quadro de recursos, fontes e destinação

[Parágrafo introdutório de 2 frases]

| Item | Qtd. | Valor unitário (R$) | Total (R$) | Fonte de financiamento | Destinação |
|---|---|---|---|---|---|
[linhas da tabela]

5.2 Previsão de ressarcimento de gastos aos sujeitos da pesquisa

[1 ou 2 parágrafos]

Referências

[Lista Vancouver]
```

Não adicionar texto após as referências. Não incluir comentários ou notas de rodapé além dos previstos explicitamente nestas instruções.

**Próxima etapa:** solicite a skill `/capitulo-monitorizacao` para redigir o Capítulo 6 — Monitorização dos dados e proteção dos participantes.

---

## Checklist de qualidade: revisão antes de entregar o texto

**Seção 3.1 e 3.2:**
- [ ] 8 etapas padrão presentes (ou 7 sem relatório parcial)
- [ ] Tabela de Gantt com sobreposições realistas obrigatórias (coleta + armazenamento simultâneos; interpretação sobreposta à análise)
- [ ] Futuro do indicativo em todos os verbos das descrições

**Capítulo 4:**
- [ ] Parágrafo introdutório presente
- [ ] Tabela com categorias pertinentes ao tipo de estudo informado
- [ ] Nenhuma categoria vazia incluída
- [ ] Itens do Cap. 4 são os mesmos do Cap. 5 (consistência cruzada verificada)
- [ ] Unidades de medida padrão aplicadas

**Capítulo 5.1:**
- [ ] Todos os itens do Cap. 4 presentes na tabela (mais serviços contratados, se houver)
- [ ] Subtotais por categoria presentes e corretos
- [ ] TOTAL GERAL calculado (ou marcado como [a preencher] se valores ausentes)
- [ ] Fonte de financiamento preenchida em cada linha
- [ ] Destinação (etapa/objetivo) preenchida em cada linha
- [ ] Nota de rodapé incluída se houver campos [a preencher]

**Capítulo 5.2:**
- [ ] Condição A ou B aplicada conforme contexto do estudo
- [ ] Base legal CNS 466/12, item IV.3.g, citada
- [ ] Justificativa contextual presente (não apenas a citação da norma)
- [ ] Se Condição A: mecanismo de pagamento descrito (momento, forma, responsável, rubrica)
- [ ] Se estudo qualitativo/humanas: CNS 510/2016 também citada
- [ ] Lista de referências Vancouver ao final da seção

**Requisitos gerais:**
- [ ] Texto em português brasileiro formal, futuro do indicativo
- [ ] Sem travessões (—) no texto redigido
- [ ] Estrangeirismos em itálico
- [ ] Consistência entre Cap. 4 e 5.1 (mesmos itens, mesmas quantidades)
