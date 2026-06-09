---
name: elementos-pre-textuais
description: Gerar os elementos pré-textuais de um projeto de pesquisa científica em português brasileiro: capa (folha de rosto), página de Informações Gerais (formato CEP/Plataforma Brasil), sumário e lista de abreviaturas/siglas/símbolos/sinais. Reúne dados já elaborados nos capítulos anteriores do projeto, minimizando reentrada de informações. Usar quando o usuário solicitar "capa", "folha de rosto", "informações gerais", "sumário", "lista de abreviaturas" ou similares.
version: 1.0.0
argument-hint: [cole aqui o título da pesquisa e o nome do pesquisador responsável, se já disponíveis]

---

# Elementos Pré-textuais. Skill de Geração de Documentos

## Objetivo

Gerar os quatro elementos pré-textuais do projeto de pesquisa em um único arquivo DOCX, na ordem correta para montagem do documento final:

1. **Capa** (folha de rosto)
2. **Informações Gerais** (formato exigido pelo CEP / Plataforma Brasil)
3. **Sumário** (com numeração de página a preencher após montagem)
4. **Lista de Abreviaturas, Siglas, Símbolos e Sinais** (ordem alfabética)

Esta skill é executada **após** os capítulos 1 a 11 e as referências bibliográficas já terem sido redigidos pelos demais skills do plugin. Os dados são reaproveitados dos capítulos anteriores: o usuário copia as informações já elaboradas, evitando re-elaboração.

---

## Regras tipográficas obrigatórias

**Estrangeirismos em itálico:** toda palavra ou expressão em idioma diferente do português brasileiro deve ser grafada em itálico. Exemplos: *e-mail* (manter sem itálico quando for parte de endereço de e-mail), *lattes*, *online*.

**Proibição de travessões:** não usar travessões (—) em nenhuma hipótese no texto redigido. Substituir por dois-pontos (:), ponto e vírgula (;) ou vírgula. **Exceção:** nomes de locais e instituições que contenham travessão na grafia oficial devem ser mantidos (ex.: "Maceió – Alagoas" no endereço, que usa o sinal tipográfico de travessão como separador geográfico convencional).

---

## Fase 1 — Levantamento completo de informações

Apresentar as perguntas em dois blocos. Instruir o usuário: "Copie as informações dos capítulos já redigidos quando disponíveis. Se algum dado ainda não estiver definido, escreva '[a preencher]' e prossiga."

---

### Bloco A — Dados reaproveitados dos capítulos anteriores

*(Copiar dos outputs dos skills já executados)*

**1. Título completo da pesquisa**

**2. Objetivo geral** (1–2 frases em linguagem técnica — copiar do Cap. 1 ou do `plano-intencao`)

**3. Pesquisador responsável** — informar todos os campos a seguir:
- Nome completo
- E-mail profissional
- Cargo/função (ex.: Professor Assistente, Médico Residente, Mestrando)
- Titulação (ex.: Especialista, Mestre, Doutor)
- Instituição de vínculo: nome completo + sigla
- Cidade e UF
- Telefone (incluir código do país se necessário, ex.: +55 82 9982-6032)
- URL do Curriculum Lattes

**4. Pesquisadores colaboradores** (se houver): os mesmos dados do item 3 para cada colaborador, um por linha. Escrever "Nenhum" se não houver.

**5. Instituição onde será realizada a pesquisa** — informar todos os campos:
- Nome completo da instituição
- Sigla
- Logradouro completo (rua, número, complemento/andar/sala)
- CEP (formato: NNNNN-NNN)
- Cidade, UF e País
- Telefone (com código internacional se necessário)
- URL do site institucional

**6. Período de coleta de dados:**
- Data de início (dd/mm/aaaa)
- Data de término (dd/mm/aaaa)

**7. Custo total estimado** da pesquisa (conforme Cap. 5, seção 5.1): informar valor em reais com duas casas decimais (ex.: R$ 288,00). Escrever "Recursos próprios sem custo adicional" se não houver custo.

**8. Fonte de financiamento** (conforme Cap. 5): ex.: "Recursos próprios", "CNPq — Edital Universal nº 01/2026", "Nenhuma". Usar "Nenhuma" se não houver financiamento externo.

**9. Conflito de interesse:** informar a URL onde o formulário ICMJE preenchido está hospedado (ex.: http://bit.ly/aldemarci para o pesquisador responsável, e URLs separadas para cada colaborador, se houver). Se não houver URL (formulário não publicado online), escrever "Sem conflito de interesse declarado" ou "Declarado no Capítulo 11, Anexo 11.5."

---

### Bloco B — Dados novos (não coletados por nenhum outro skill)

**10. Orientador** (se houver): informar os mesmos campos do item 3 (nome, e-mail, cargo, titulação, instituição com sigla, cidade, UF, telefone, URL Lattes). Escrever "Não se aplica" se não houver orientador.

**11. Lista de abreviaturas, siglas, símbolos e sinais** utilizados no projeto: informar no formato `SIGLA = Significado por extenso`, uma por linha. Exemplo:
```
CEP = Comitê de Ética em Pesquisa
CNS = Conselho Nacional de Saúde
DM2 = Diabetes mellitus tipo 2
HbA1c = Hemoglobina glicada A1c
SF-36 = Short Form 36 Health Survey
```
Escrever "Nenhuma" se não houver abreviaturas.

**12. Data da versão do documento:** padrão automático = data e hora atuais no formato dd/mm/aaaa hh:mm. O usuário pode informar outra data se desejar (ex.: data da última revisão manual).

---

## Fase 2 — Capa (Folha de Rosto)

Gerar a capa centralizada com a seguinte estrutura:

```
INSTRUÇÃO: Inserir logomarca da instituição no espaço indicado antes da impressão.

[ESPAÇO PARA LOGOMARCA DA INSTITUIÇÃO]

[NOME COMPLETO DA INSTITUIÇÃO]
[SIGLA] | [DEPARTAMENTO/SETOR]

─────────────────────────────────────────────

PROJETO DE PESQUISA

─────────────────────────────────────────────

[TÍTULO DA PESQUISA EM MAIÚSCULAS]

─────────────────────────────────────────────

Pesquisador responsável: [Nome completo], [Titulação]
[E-mail] | Telefone: [Telefone]

[Se houver orientador — incluir a linha abaixo:]
Orientador: [Nome completo], [Titulação]
[E-mail] | Telefone: [Telefone]

[Se houver colaboradores — incluir:]
Pesquisador colaborador: [Nome], [Titulação]

─────────────────────────────────────────────

[Cidade], [Ano]
```

---

## Fase 3 — Página de Informações Gerais

Gerar exatamente no formato a seguir, com os campos preenchidos. As letras das alíneas devem ser **estritamente sequenciais** (a, b, c, d, e, f, g, h, i, j, k, l), sem repetição. Se a alínea f) (Orientador) for omitida por não se aplicar, as letras subsequentes avançam automaticamente (g → f, h → g, etc.).

---

**1. Informações Gerais**

**a) Local onde será efetuado o estudo:**
[Nome completo da instituição], [Cidade], [UF].

**b) Endereço:**
[Logradouro completo — rua, número, complemento].
[CEP]     [Cidade] – [Estado], [País].
Telefone: [Telefone com código internacional].
URL: [URL do site]

**c) Pesquisador principal:**
[Nome completo] <[e-mail]>; [Cargo], [Titulação], da [Instituição com sigla], [Cidade], [UF], telefone: [telefone]. Lattes: [URL Lattes].

**d) Conflito de interesse:**
[Se houver URL:] Formulário ICMJE disponível em: [URL]. [Acrescentar URLs dos colaboradores, se houver, cada um com seu nome.]
[Se não houver URL:] Sem conflito de interesse declarado. / Declarado no Capítulo 11, Anexo 11.5.

**e) Fonte de financiamento:**
[Fonte de financiamento conforme Cap. 5]

**f) Orientador:** *(omitir esta alínea se não houver orientador; reordenar letras subsequentes)*
[Nome completo] <[e-mail]>, [Cargo], [Titulação], da [Instituição com sigla], [Cidade], [UF], telefone: [telefone]. Lattes: [URL Lattes].

**g) Título da pesquisa:**
[Título completo da pesquisa]

**h) Objetivo:**
[Objetivo geral]

**i) Custo estimado:**
[Valor em R$ com duas casas decimais, ou declaração de ausência]

**j) Início da coleta de dados:**
[dd/mm/aaaa]

**k) Término da coleta de dados:**
[dd/mm/aaaa]

**l) Data da última modificação:**
[dd/mm/aaaa hh:mm]

---

### Regras de preenchimento das alíneas

- **Alínea f) omitida (sem orientador):** renomear g → f, h → g, i → h, j → i, k → j, l → k. O documento termina com a alínea k).
- **Alínea d) Conflito de interesse com múltiplos pesquisadores:** listar um por linha: `[Nome do pesquisador]: [URL]`.
- **Alínea d) sem URL:** usar "Sem conflito de interesse declarado." ou "Conflito de interesse declarado no Capítulo 11, Anexo 11.5a."
- **Campos com `[a preencher]`:** não bloquear o fluxo; gerar o documento com a marcação e informar ao usuário ao final.

---

## Fase 4 — Sumário

Gerar o sumário com a estrutura padrão do plugin `projeto-pesquisa`. Os números de página são marcados como `[•]` pois só serão conhecidos após a montagem completa do documento.

---

**SUMÁRIO**

```
Informações Gerais ................................................................ [•]
Lista de Abreviaturas, Siglas, Símbolos e Sinais ................................ [•]

Capítulo 1. Introdução ............................................................ [•]
Capítulo 2. Métodos ............................................................... [•]
Capítulo 3. Cronograma de Execução ................................................ [•]
Capítulo 4. Relação de Materiais Necessários ...................................... [•]
Capítulo 5. Orçamento ............................................................. [•]
    5.1. Quadro de recursos, fontes e destinação .................................. [•]
    5.2. Previsão de ressarcimento de gastos aos sujeitos da pesquisa ............. [•]
Capítulo 6. Monitorização da Pesquisa ............................................. [•]
    6.1. Medidas de proteção aos participantes .................................... [•]
    6.2. Monitorização dos dados .................................................. [•]
    6.3. Confidencialidade ........................................................ [•]
    6.4. Critérios de suspensão ................................................... [•]
Capítulo 7. Análise dos Riscos e dos Benefícios ................................... [•]
    7.1. Análise dos riscos ....................................................... [•]
    7.2. Análise dos benefícios ................................................... [•]
    7.3. Relação risco-benefício .................................................. [•]
Capítulo 8. Propriedade Intelectual e Plano de Divulgação ......................... [•]
    8.1. Direitos de propriedade intelectual ...................................... [•]
    8.2. Plano de divulgação ...................................................... [•]
    8.3. Publicação de dados ...................................................... [•]
Capítulo 9. Responsabilidades ..................................................... [•]
    9.1. Pesquisador responsável .................................................. [•]
    9.2. Instituição proponente ................................................... [•]
    9.3. Promotor ................................................................. [•]
    9.4. Patrocinador ............................................................. [•]
Capítulo 10. Autonomia dos Participantes ........................................... [•]
Capítulo 11. Anexos ................................................................ [•]
    11.1.  Termo de Consentimento Livre e Esclarecido (TCLE) ...................... [•]
    11.2.  Formulário de coleta de dados .......................................... [•]
    11.3.  Tabela de dados individuais ............................................ [•]
    11.4.  Curriculum Lattes dos pesquisadores .................................... [•]
    11.5.  Declaração de conflitos de interesse ................................... [•]
    11.6.  Autorização para realização da pesquisa ................................ [•]
    11.7.  Termo de responsabilidade do pesquisador responsável ................... [•]
    11.8.  Termo de responsabilidade do pesquisador colaborador ................... [•]
    11.9.  Termo de responsabilidade da Instituição ............................... [•]
    11.10. Declaração de condições da Instituição ................................. [•]

Referências Bibliográficas ........................................................ [•]
```

*Nota: os números de página ([•]) devem ser preenchidos após a montagem completa do documento no processador de texto (Google Docs ou Microsoft Word).*

---

## Fase 5 — Lista de Abreviaturas, Siglas, Símbolos e Sinais

Ordenar **alfabeticamente** as entradas fornecidas no Bloco B, item 11. Formatar em duas colunas alinhadas:

```
LISTA DE ABREVIATURAS, SIGLAS, SÍMBOLOS E SINAIS

Abreviatura/Sigla   Significado por extenso
───────────────────────────────────────────────────────
[SIGLA 1]           [Significado 1]
[SIGLA 2]           [Significado 2]
[...]
```

Se o usuário informar "Nenhuma" ou não fornecer entradas: gerar a seção com o título e a nota:
`[Preencher com as abreviaturas, siglas, símbolos e sinais utilizados no projeto, em ordem alfabética.]`

---

## Fase 6 — Salvar arquivo DOCX

### 6.1 Levantamento do diretório de saída

Perguntar ao usuário, em uma única mensagem:

1. **Diretório de saída:** caminho completo. Sugestão padrão: Desktop (`C:\Users\[usuário]\Desktop`) ou pasta de sincronização do Google Drive local.
2. **Nome base do arquivo** (sem extensão): padrão sugerido: `elementos-pre-textuais`. O usuário pode personalizar (ex.: `pre-textuais-dm2-ubs`).

Se o usuário não responder, usar o nome padrão e o Desktop como destino.

---

### 6.2 Verificação do pandoc

```bash
pandoc --version
```

Se pandoc não estiver instalado: "O pandoc não foi encontrado. Instale em https://pandoc.org/installing.html e reinicie o terminal."

---

### 6.3 Salvar o arquivo Markdown e converter para DOCX

Usar a ferramenta **Write** para salvar um único arquivo Markdown com os quatro elementos em sequência, separados por `\newpage`. Cabeçalho YAML:

```yaml
---
title: "Elementos Pré-textuais"
lang: pt-BR
---
```

Ordem dos elementos no arquivo:
1. Capa
2. `\newpage`
3. Informações Gerais
4. `\newpage`
5. Sumário
6. `\newpage`
7. Lista de Abreviaturas, Siglas, Símbolos e Sinais

Converter para DOCX:

```bash
pandoc "[diretório]/[nome-base].md" \
  -o "[diretório]/[nome-base].docx" \
  --metadata title="Elementos Pré-textuais" \
  -V lang=pt-BR
```

---

### 6.4 Gerar o arquivo PDF

O PDF deve conter, em todas as páginas: **cabeçalho centralizado** com o texto "Elementos Pré-textuais" e **numeração de página** no rodapé direito.

Tentar os mecanismos de conversão na ordem abaixo, usando o primeiro disponível no sistema:

**Opção A: wkhtmltopdf** (recomendado; instalar em https://wkhtmltopdf.org/downloads.html se necessário):

```bash
# Passo 1: gerar HTML a partir do Markdown
pandoc "[diretório]/[nome-base].md" \
  -o "[diretório]/[nome-base].html" \
  --standalone --embed-resources \
  --css="[diretório]/academico.css" \
  --metadata title="Elementos Pré-textuais" \
  -V lang=pt-BR

# Passo 2: converter HTML para PDF com cabeçalho e numeração
wkhtmltopdf \
  --header-center "Elementos Pré-textuais" \
  --header-font-name "Arial" \
  --header-font-size 10 \
  --header-line \
  --header-spacing 5 \
  --footer-right "[page]" \
  --footer-font-name "Arial" \
  --footer-font-size 10 \
  --footer-spacing 5 \
  --margin-top 25mm \
  --margin-bottom 20mm \
  --margin-left 30mm \
  --margin-right 20mm \
  "[diretório]/[nome-base].html" \
  "[diretório]/[nome-base].pdf"
```

Escrever o arquivo `academico.css` com a ferramenta Write antes da conversão (estilos: Arial 12pt, espaçamento 1.5, tabelas com cabeçalho azul escuro, parágrafos justificados). Não incluir margens no CSS pois elas são definidas pelos flags do wkhtmltopdf.

**Opção B: xelatex** (requer MikTeX ou TeX Live; melhor qualidade tipográfica):

Escrever o arquivo `pre-textuais-header.tex` com a ferramenta Write antes da conversão:

```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\small Elementos Pré-textuais}
\fancyfoot[R]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
```

Em seguida executar:

```bash
pandoc "[diretório]/[nome-base].md" \
  -o "[diretório]/[nome-base].pdf" \
  --pdf-engine=xelatex \
  --include-in-header="[diretório]/pre-textuais-header.tex" \
  -V lang=pt-BR \
  -V fontsize=12pt \
  -V "geometry:top=30mm, bottom=25mm, left=30mm, right=20mm" \
  -V mainfont="Arial" \
  --metadata title="Elementos Pré-textuais"
```

**Opção C: Chrome headless** (se nenhuma das opções anteriores estiver disponível):

```bash
pandoc "[diretório]/[nome-base].md" \
  -o "[diretório]/[nome-base].html" \
  --standalone --embed-resources \
  --css="[diretório]/academico-pre.css" \
  --metadata title="Elementos Pré-textuais" \
  -V lang=pt-BR

"C:/Program Files/Google/Chrome/Application/chrome.exe" \
  --headless=new --no-sandbox --disable-gpu \
  --print-to-pdf="[diretório]/[nome-base].pdf" \
  "[diretório]/[nome-base].html"
```

O arquivo `academico-pre.css` deve incluir:

```css
@page {
  margin: 30mm 20mm 25mm 30mm;
  @top-center {
    content: "Elementos Pré-textuais";
    font-family: Arial, sans-serif;
    font-size: 10pt;
    border-bottom: 0.4pt solid black;
    padding-bottom: 3pt;
  }
  @bottom-right {
    content: counter(page);
    font-family: Arial, sans-serif;
    font-size: 10pt;
  }
}
```

Nota: Chrome headless suporta CSS `@page` apenas via Paged.js. Se o cabeçalho não aparecer, preferir wkhtmltopdf ou xelatex.

**Se nenhum mecanismo de PDF estiver disponível:** informar ao usuário que o DOCX foi gerado com sucesso e orientá-lo a usar **"Arquivo / Baixar como / PDF"** (Google Docs) ou **"Arquivo / Salvar como / PDF"** (Word) para obter o PDF manualmente. Orientar a inserir o cabeçalho "Elementos Pré-textuais" e a numeração de páginas pelo menu de configuração de página do editor.

---

### 6.5 Confirmar ao usuário

```
Elementos Pré-textuais gerados com sucesso.

  DOCX  ->  [caminho completo]/[nome-base].docx
  PDF   ->  [caminho completo]/[nome-base].pdf  (com cabeçalho e numeração de páginas)
  MD    ->  [caminho completo]/[nome-base].md  (arquivo-fonte; manter para edições futuras)

Conteúdo dos arquivos (em ordem):
  1. Capa (folha de rosto)
  2. Informações Gerais  [alíneas a) a l) — ou a) a k) se sem orientador]
  3. Sumário  [números de página marcados como [•]]
  4. Lista de Abreviaturas, Siglas, Símbolos e Sinais

[Se houver campos [a preencher]:]
Campos que requerem complementação antes da submissão ao CEP:
  - [lista dos campos marcados como [a preencher]]

Os elementos pré-textuais estão prontos para integração ao projeto completo.
```

**Próxima etapa:** solicite a skill `/compilacao-final` para integrar todos os capítulos,
verificar coerência e gerar o documento final pronto para submissão ao CEP.

---

## Padrões de qualidade: checklist antes de entregar o documento

- [ ] **Capa:** título em maiúsculas; pesquisador responsável com titulação, e-mail e telefone; orientador presente se houver; cidade e ano presentes
- [ ] **Informações Gerais:** alíneas em ordem sequencial sem repetição de letras; alínea f) presente se houver orientador, omitida (com reordenação) se não houver
- [ ] **Alínea b):** endereço com CEP formatado, cidade, UF, país, telefone e URL
- [ ] **Alínea c):** e-mail entre `< >`, cargo, titulação, instituição com sigla, telefone, URL Lattes
- [ ] **Alínea d):** URL do formulário ICMJE presente ou declaração de ausência explícita
- [ ] **Alínea i):** custo em R$ com duas casas decimais ou declaração textual
- [ ] **Alíneas j) e k):** datas de início e término da coleta presentes
- [ ] **Alínea l):** data + hora da última modificação
- [ ] **Sumário:** todos os capítulos (1–11) e subseções dos capítulos 5, 6, 7, 8, 9 e 11 presentes; números de página marcados como `[•]`; nota de instrução ao final
- [ ] **Lista de abreviaturas:** entradas em ordem alfabética; duas colunas alinhadas
- [ ] Nenhum travessão (—) inserido pelo skill no texto redigido (exceto em endereços geográficos e títulos oficiais)
- [ ] Todos os campos com dados ausentes marcados como `[a preencher]` e listados na confirmação final
- [ ] DOCX gerado sem erro pelo pandoc; caminho confirmado ao usuário
- [ ] PDF gerado com cabeçalho "Elementos Pré-textuais" e numeração de páginas; caminho confirmado ao usuário
