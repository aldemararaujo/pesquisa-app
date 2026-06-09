---
name: referencias-bibliograficas
description: Compilar, deduplicar e formatar a lista final de referências bibliográficas de um projeto de pesquisa científica no estilo Vancouver, com DOI e URL. Recebe as listas de referências geradas por cada capítulo (pelos demais skills do plugin), remove duplicatas e entrega uma lista única numerada e ordenada alfabeticamente, pronta para submissão ao CEP. Usar quando o usuário solicitar "referências", "lista de referências", "bibliografia", "Vancouver" ou similares.
version: 1.0.0
argument-hint: [cole aqui as listas de referências dos capítulos já redigidos, separadas por capítulo]

---

# Lista de Referências Bibliográficas. Skill de Compilação e Formatação Vancouver

## Objetivo

Compilar as listas de referências geradas pelos demais skills do plugin (`capitulo-metodos`, `etapas-e-cronograma`, `capitulo-monitorizacao`, `capitulo-riscos-beneficios`, `capitulo-propriedade-responsabilidades`, `capitulo-anexos` e outros), eliminar duplicatas e produzir uma **lista única, numerada, em ordem alfabética, no estilo Vancouver completo**, com DOI e URL em todas as referências que os possuem.

A lista final é salva como arquivo DOCX e pode ser inserida no final do projeto ou submetida ao CEP como documento avulso.

---

## Regras tipográficas obrigatórias

**Estrangeirismos em itálico:** toda palavra ou expressão em idioma diferente do português brasileiro deve ser grafada em itálico no texto desta skill. Nas próprias referências, seguir a convenção do documento original (títulos de periódicos e livros em inglês permanecem como estão).

**Proibição de travessões:** não usar travessões (—) em nenhuma hipótese no texto redigido por esta skill. **Exceção:** títulos oficiais de documentos que contêm travessão, como "Norma Operacional nº 001/2013 — CONEP", devem ser preservados exatamente como aparecem nas referências originais.

---

## Fase 1 — Coleta das listas de referências

Carregar o arquivo de referência com Read antes de iniciar:
`references/vancouver-guia.md`

Solicitar ao usuário que cole, em uma única mensagem ou em blocos separados, **todas as listas de referências** geradas pelos capítulos já redigidos. Não é necessário que estejam formatadas em Vancouver: podem estar em qualquer formato (lista simples de títulos, formato ABNT, DOIs avulsos, texto corrido com citações em rodapé, etc.).

**Mensagem de instrução ao usuário:**

"Cole abaixo as listas de referências de todos os capítulos do seu projeto. Aceito qualquer formato (Vancouver, ABNT, lista de títulos, DOIs avulsos, texto corrido). Se um capítulo ainda não foi redigido, pule-o. Quando terminar de colar, escreva 'fim' para eu iniciar o processamento."

Organizar internamente as referências por capítulo de origem (para fins de rastreabilidade durante a deduplicação), mas o usuário não precisa formatá-las previamente.

---

## Fase 2 — Deduplicação

Identificar referências duplicadas utilizando os critérios da **Seção 4 do arquivo de referência** (`references/vancouver-guia.md`), em ordem de prioridade:

1. **DOI idêntico** (maior confiabilidade): se dois registros têm o mesmo DOI, são duplicatas.
2. **PMID idêntico**: se dois registros têm o mesmo PMID, são duplicatas.
3. **Título + ano + primeiro autor** com similaridade > 90%: provável duplicata; processar como duplicata e informar ao usuário.
4. **Título + primeiro elemento institucional** (para legislação e documentos organizacionais).

**Regra de resolução:** quando uma referência aparece em mais de uma versão com completude diferente (ex.: uma com DOI e URL, outra só com título), manter **a versão mais completa**. Se as versões forem igualmente completas, manter a primeira ocorrência.

Ao final da deduplicação, informar ao usuário:
- Número total de referências brutas recebidas.
- Número de duplicatas removidas (listar quais foram removidas e por qual critério).
- Número de referências únicas que compõem a lista final.

---

## Fase 3 — Verificação e complementação

Para cada referência única, verificar os itens do checklist da **Seção 5 do arquivo de referência**. Campos ausentes devem ser marcados como `[a preencher]`.

Para referências de legislação brasileira recorrente (CNS 466/12, CNS 510/16, LGPD, Norma Operacional CONEP etc.) e de diretrizes internacionais amplamente utilizadas (Helsinki, CIOMS, CONSORT, STROBE, PRISMA etc.): consultar o **repositório de referências fixas da Seção 3** do arquivo de referência e usar a versão completa já verificada, substituindo qualquer versão incompleta fornecida pelo usuário.

Ao final da verificação, listar separadamente as referências com campos ausentes (`[a preencher]`), para facilitar o preenchimento posterior pelo usuário.

---

## Fase 4 — Formatação Vancouver final

Aplicar as regras de formatação da **Seção 1 e Seção 2 do arquivo de referência** a todas as referências.

### Ordenação e numeração

1. Ordenar **alfabeticamente** pelo primeiro elemento de entrada:
   - Autores individuais: sobrenome do primeiro autor (letras maiúsculas e minúsculas, sem distinção de acentuação para fins de ordenação).
   - Autores institucionais: primeira palavra significativa do nome (ex.: "Brasil" vem antes de "Council"; "International" vem antes de "National"; "World" vem por último entre esses).
2. Numerar sequencialmente após a ordenação: **1.**, **2.**, **3.** ...

### Formato por tipo de documento

Aplicar o formato correto conforme o tipo de cada referência (Seção 2 do arquivo de referência):

**Artigo de periódico:**
`N. Sobrenome AB, Sobrenome CD. Título do artigo. Nome Abrev Periódico. AAAA;Vol(Num):Pág-Pág. doi:10.XXXX/XXXXX. Disponível em: https://...`

**Livro:**
`N. Sobrenome AB. Título do livro. Nº ed. Cidade: Editora; AAAA. doi:... Disponível em: https://...`

**Capítulo de livro:**
`N. Sobrenome AB. Título do capítulo. In: Sobrenome CD, editor. Título do livro. Nº ed. Cidade: Editora; AAAA. p. X-Y.`

**Documento institucional / relatório:**
`N. Nome da Instituição (sigla). Título do documento. Versão/edição. Cidade: Instituição; AAAA. doi:... Disponível em: https://...`

**Legislação brasileira:**
`N. Brasil. [Órgão]. [Tipo normativo] nº [número], de [DD] de [mês] de [AAAA]. [Ementa]. Diário Oficial da União. AAAA Mês DD;seção N:página. Disponível em: https://...`

**Página de internet sem DOI:**
`N. Autor ou Instituição. Título [Internet]. Cidade: Instituição; AAAA [acesso AAAA Mês DD]. Disponível em: https://...`

### Regras de autoria

- Até 6 autores: listar todos.
- 7 ou mais autores: listar os 6 primeiros, seguidos de `, et al.`
- Autores com mesmo sobrenome: diferenciar pelas iniciais do nome.

### Título do artigo / capítulo

- Apenas a primeira letra da primeira palavra em maiúscula (e nomes próprios, siglas, acrônimos).
- Sem itálico, sem aspas.

### Periódico

- Usar abreviatura NLM quando disponível.
- Se não houver abreviatura padronizada, escrever o título completo do periódico.

---

## Fase 5 — Geração do arquivo DOCX

### 5.1 Levantamento do diretório de saída

Perguntar ao usuário, em uma única mensagem:

1. **Diretório de saída:** caminho completo onde o arquivo deve ser salvo. Sugestão padrão: Desktop (`C:\Users\[usuário]\Desktop`) ou pasta de sincronização do Google Drive local.
2. **Nome base do arquivo** (sem extensão): padrão sugerido: `referencias-bibliograficas`. O usuário pode personalizar.

Se o usuário não responder, usar o nome padrão e o Desktop como destino.

---

### 5.2 Verificação do pandoc

```bash
pandoc --version
```

Se pandoc não estiver instalado, informar:
"O pandoc não foi encontrado no sistema. Instale em https://pandoc.org/installing.html. Após a instalação, reinicie o terminal e execute a Fase 5 novamente."

---

### 5.3 Salvar o arquivo Markdown e converter para DOCX

Usar a ferramenta **Write** para salvar a lista final em arquivo Markdown. Cabeçalho YAML:

```yaml
---
title: "Referências Bibliográficas"
lang: pt-BR
---
```

Estrutura do arquivo Markdown:

```markdown
# Referências Bibliográficas

1. [Referência 1 completa em Vancouver]
2. [Referência 2 completa em Vancouver]
...
N. [Referência N completa em Vancouver]

---
*Lista gerada a partir das referências dos Capítulos 1 a 11. Total: N referências únicas (N duplicatas removidas).*
*Campos marcados como [a preencher] requerem complementação antes da submissão ao CEP.*
```

Converter para DOCX com python-docx (ou pandoc se disponível):

```
python-docx   → pip install python-docx
docx2pdf      → pip install docx2pdf
```

Gerar `[nome-base].docx` com python-docx (Calibri 11pt; título "Referências Bibliográficas"
bold 14pt azul `#1F497D`; margens 2,5 cm sup/inf e 3 cm lat; espaçamento 1,5).
Em seguida, converter para `[nome-base].pdf` com docx2pdf; se falhar, usar reportlab.
Nome base: `referencias-bibliograficas_[AAAAMMDD]`. [O sistema gerará o arquivo para download]

---

### 5.4 Confirmar ao usuário

```
Referências Bibliográficas geradas com sucesso.

  Total de referências brutas recebidas:  N
  Duplicatas removidas:                   N
  Referências únicas na lista final:      N
  Referências com campos [a preencher]:   N

Arquivos salvos:
  MD    ->  C:\Users\aldem\[nome-base].md   (arquivo-fonte; manter para edições futuras)
  DOCX  ->  C:\Users\aldem\[nome-base].docx
  PDF   ->  C:\Users\aldem\[nome-base].pdf

Para importar no Google Drive:
  1. Acesse drive.google.com
  2. Clique em "+ Novo" / "Fazer upload de arquivo"
  3. Selecione o arquivo .docx
  4. Clique com o botão direito / "Abrir com" / "Documentos Google"
```

Se houver referências com `[a preencher]`, listá-las separadamente ao final da confirmação, numeradas, para facilitar o preenchimento pelo usuário.

**Próxima etapa:** solicite a skill `/elementos-pre-textuais` para gerar a capa, o sumário e a lista de abreviaturas — última etapa do projeto.

---

## Padrões de qualidade: checklist antes de entregar a lista

- [ ] Todas as referências fornecidas pelo usuário processadas (nenhuma omitida sem justificativa)
- [ ] Deduplicação realizada e relatório de duplicatas apresentado ao usuário
- [ ] Legislação brasileira recorrente (CNS 466/12, 510/16, LGPD, CONEP) verificada contra o repositório fixo
- [ ] Diretrizes internacionais recorrentes (Helsinki, CIOMS, CONSORT, STROBE, PRISMA etc.) verificadas contra o repositório fixo
- [ ] Ordenação: estritamente alfabética pelo primeiro elemento de entrada
- [ ] Numeração: sequencial, começando em 1, sem pular números
- [ ] Formato Vancouver aplicado conforme tipo de documento de cada referência
- [ ] DOI presente em todas as referências que o possuem (formato `doi:10.XXXX/XXXXX`)
- [ ] URL presente em todas as referências (mesmo quando há DOI)
- [ ] Autores com mais de 6: truncados com `, et al.`
- [ ] Títulos de artigos e capítulos: apenas primeira letra maiúscula
- [ ] Campos ausentes marcados como `[a preencher]`
- [ ] Nenhum travessão inserido pelo skill (exceto em títulos oficiais de documentos)
- [ ] DOCX gerado sem erro pelo pandoc; caminho confirmado ao usuário

---

## Arquivo de referência desta skill

- `references/vancouver-guia.md`: regras gerais de formatação Vancouver; formatos por tipo de documento (artigo, livro, capítulo, relatório, legislação, página web, tese); repositório de referências fixas verificadas (CNS 466/12, 510/16, LGPD, CONEP, Helsinki, CIOMS, ICH E6(R2), ICMJE, CONSORT, STROBE, PRISMA, COREQ, ISO 31000, CTCAE, FAIR Principles); critérios de deduplicação; checklist de qualidade por referência.


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
