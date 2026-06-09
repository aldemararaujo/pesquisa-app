# Análise Estatística em Pesquisa Clínica e Epidemiológica

## 1. Cálculo do tamanho da amostra

### 1.1 Parâmetros fundamentais

| Parâmetro | Símbolo | Valor convencional | Significado |
|---|---|---|---|
| Nível de significância | α | 0,05 (5%) | Probabilidade de rejeitar H₀ quando ela é verdadeira (erro tipo I) |
| Poder estatístico | 1−β | 0,80 ou 0,90 (80% ou 90%) | Probabilidade de detectar o efeito quando ele existe |
| Erro tipo II | β | 0,20 ou 0,10 | Probabilidade de não detectar o efeito quando ele existe |
| Diferença mínima clinicamente relevante | DMCR | Definida pelo pesquisador | Menor diferença entre grupos que seria clinicamente importante |
| Desvio-padrão | DP ou σ | Estimado da literatura ou estudo piloto | Variabilidade da medida do desfecho na população |

**Zα/2 para teste bilateral α = 0,05**: 1,96  
**Zβ para poder 80% (β = 0,20)**: 0,842  
**Zβ para poder 90% (β = 0,10)**: 1,282  

### 1.2 Fórmulas por tipo de desfecho

#### Desfecho contínuo — dois grupos independentes (RCT paralelo 1:1)

```
n (por grupo) = 2 × [(Zα/2 + Zβ)² × σ²] / δ²
```

Onde:
- σ = desvio-padrão do desfecho (do grupo controle ou médio)
- δ = diferença mínima clinicamente relevante (DMCR) entre os grupos
- n total = 2 × n por grupo

**Exemplo**: DMCR = 5 pontos; σ = 10; α = 0,05 bilateral; poder = 80%  
n = 2 × [(1,96 + 0,842)² × 100] / 25 = 2 × [7,85 × 100] / 25 ≈ 63 por grupo → **126 total**  
Com 20% de perda: 126 / 0,80 = **158 participantes (79 por grupo)**

#### Desfecho dicotômico — dois grupos independentes

```
n (por grupo) = [Zα/2 × √(2 × p̄ × (1−p̄)) + Zβ × √(p1(1−p1) + p2(1−p2))]² / (p1−p2)²
```

Onde:
- p1 = proporção esperada de eventos no grupo intervenção
- p2 = proporção esperada de eventos no grupo controle
- p̄ = (p1 + p2) / 2

**Fórmula simplificada de Fleiss**:
```
n = [Zα/2 + Zβ]² × [p1(1−p1) + p2(1−p2)] / (p1−p2)²
```

#### Estudo transversal (prevalência)

```
n = Z²α/2 × p × (1−p) / e²
```

Onde:
- p = prevalência esperada (proporção)
- e = erro amostral tolerado (precisão desejada; tipicamente 0,03 a 0,05)
- Z_α/2 = 1,96 para 95% de confiança

**Exemplo**: p = 0,30; e = 0,05; Z = 1,96  
n = (1,96)² × 0,30 × 0,70 / (0,05)² = 3,84 × 0,21 / 0,0025 = **323 participantes**

#### Estudo de coorte (comparação de incidências)

```
n (por grupo) = (Zα/2 + Zβ)² × (p1 + p2) / (p1 − p2)²
```

Onde p1 e p2 são as proporções de desfecho esperadas nos grupos exposto e não exposto.

#### Estudo caso-controle (OR)

```
n (casos) = [Zα/2 √((r+1)/r × p̄(1−p̄)) + Zβ √(p1(1−p1)/r + p2(1−p2))]² / (p1−p2)²
```

Onde:
- r = razão controles:casos (r = 1 para 1:1; r = 2 para 2:1, etc.)
- p2 = proporção de exposição esperada nos controles
- p1 = p2 × OR / [1 + p2 × (OR − 1)]

### 1.3 Softwares para cálculo amostral

| Software | Acesso | Referência |
|---|---|---|
| **G*Power 3.1** | Gratuito (gpower.hhu.de) | Faul F et al. Behav Res Methods 2009;41(4):1149-60 |
| **OpenEpi** | Gratuito online (openepi.com) | Dean AG et al. |
| **PASS** | Pago (NCSS, LLC) | — |
| **R — pacote `pwr`** | Gratuito | Cohen J. Statistical Power Analysis for the Behavioral Sciences, 2ª ed., 1988 |
| **R — pacote `epiR`** | Gratuito | — |
| **Epi Info** | Gratuito (CDC) | — |

### 1.4 Referências metodológicas para citar no texto

- Cohen J. *Statistical Power Analysis for the Behavioral Sciences*. 2ª ed. Hillsdale, NJ: Lawrence Erlbaum; 1988.
- Lwanga SK, Lemeshow S. *Sample size determination in health studies: a practical manual*. Genebra: WHO; 1991.
- Faul F, Erdfelder E, Lang AG, Buchner A. G*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. *Behav Res Methods*. 2007;39(2):175-91.
- Schoenfeld DA. Sample-size formula for the proportional-hazards regression model. *Biometrics*. 1983;39(2):499-503. (para estudos de sobrevivência)

---

## 2. Tabela de escolha do teste estatístico

### 2.1 Comparação entre grupos independentes

| Tipo de variável | Distribuição | 2 grupos | ≥ 3 grupos |
|---|---|---|---|
| Contínua | Normal | Teste t de Student independente | ANOVA de uma via + Tukey |
| Contínua | Não normal | Mann-Whitney U | Kruskal-Wallis + Dunn |
| Dicotômica / categórica | — | Qui-quadrado de Pearson ou exato de Fisher | Qui-quadrado |
| Ordinal | — | Mann-Whitney U | Kruskal-Wallis |
| Sobrevivência (tempo ao evento) | — | Log-rank | Log-rank |

### 2.2 Comparação entre grupos pareados / medidas repetidas

| Tipo de variável | Distribuição | 2 tempos | ≥ 3 tempos |
|---|---|---|---|
| Contínua | Normal | Teste t de Student pareado | ANOVA de medidas repetidas |
| Contínua | Não normal | Wilcoxon pareado | Friedman |
| Dicotômica | — | McNemar | Q de Cochran |

### 2.3 Análise de correlação

| Tipo de variável | Distribuição | Teste |
|---|---|---|
| Contínua × Contínua | Ambas normais | Pearson (r) |
| Contínua × Contínua | Qualquer | Spearman (ρ) |
| Ordinal × qualquer | — | Spearman (ρ) |
| Dicotômica × Dicotômica | — | Phi (φ) ou Tetrachoric |

### 2.4 Análise multivariada (modelos de regressão)

| Desfecho | Modelo | Medida de efeito |
|---|---|---|
| Contínuo | Regressão linear múltipla (OLS) | Coeficiente β (diferença de médias ajustada) |
| Dicotômico (baixa prevalência < 10%) | Regressão logística binária | Odds ratio (OR) com IC 95% |
| Dicotômico (alta prevalência ≥ 10%) | Regressão de Poisson com variância robusta | Razão de prevalências (RP) com IC 95% |
| Tempo ao evento (sobrevivência) | Regressão de Cox | Hazard ratio (HR) com IC 95% |
| Contado (count data) | Regressão de Poisson ou binomial negativa | Rate ratio com IC 95% |
| Ordinal | Regressão logística ordinal (proporcional) | OR acumulativo com IC 95% |
| Longitudinal / painel | Modelo linear misto (random effects) | Coeficiente β ajustado |

---

## 3. Interpretação do tamanho de efeito

O tamanho de efeito quantifica a **magnitude clínica** da diferença, independentemente da significância estatística. Um p < 0,05 em amostra grande não implica relevância clínica.

### 3.1 d de Cohen (diferença entre médias contínuas)

```
d = (μ₁ − μ₂) / σ_pooled
```

| d | Interpretação |
|---|---|
| 0,20 | Efeito pequeno |
| 0,50 | Efeito médio |
| 0,80 | Efeito grande |
| > 1,00 | Efeito muito grande |

### 3.2 r de Pearson / Spearman (correlação)

| |r| | Interpretação |
|---|---|
| 0,10–0,29 | Correlação fraca |
| 0,30–0,49 | Correlação moderada |
| ≥ 0,50 | Correlação forte |

### 3.3 Odds Ratio (OR) e Risco Relativo (RR)

| Valor | Interpretação |
|---|---|
| OR ou RR = 1,0 | Sem associação |
| OR ou RR = 1,5 | Aumento de 50% no risco |
| OR ou RR = 2,0 | Dobrando o risco (aumento de 100%) |
| OR ou RR = 0,5 | Redução de 50% no risco (proteção) |

**IC 95% que não inclui 1,0 → significância estatística para OR e RR**

### 3.4 NNT e NNH (para desfechos dicotômicos em RCTs)

```
NNT (Number Needed to Treat) = 1 / (p_controle − p_intervenção) = 1 / RA
```

Onde RA = Redução Absoluta do Risco (ARR — Absolute Risk Reduction)

```
NNH (Number Needed to Harm) = 1 / (p_intervenção − p_controle)
```

| NNT | Interpretação clínica |
|---|---|
| 1–5 | Efeito muito grande |
| 6–10 | Efeito grande |
| 11–50 | Efeito moderado |
| > 50 | Efeito pequeno |

### 3.5 η² (Eta-quadrado) — ANOVA

```
η² = SS_between / SS_total
```

| η² | Interpretação |
|---|---|
| 0,01 | Efeito pequeno |
| 0,06 | Efeito médio |
| 0,14 | Efeito grande |

---

## 4. Análise de intenção de tratar (ITT) e per-protocol

### Intention-to-treat (ITT)

- Todos os participantes randomizados são analisados nos grupos nos quais foram originalmente alocados, independentemente de:
  - Terem completado o protocolo ou desistido
  - Terem aderido à intervenção
  - Terem recebido a intervenção correta
- **Preserva os benefícios da randomização** (balanceia fatores de confundimento conhecidos e desconhecidos entre grupos)
- **É a análise primária obrigatória em RCTs** conforme CONSORT 2010
- Requer estratégia para lidar com dados ausentes de participantes que abandonaram o estudo

### Modified ITT (mITT)

- Variação do ITT que exclui participantes que nunca iniciaram o tratamento ou que não têm nenhum dado pós-baseline
- Deve ser pré-especificada no protocolo e justificada

### Per-protocol (PP)

- Inclui apenas participantes que completaram o estudo conforme o protocolo (aderência satisfatória, sem violações de protocolo)
- **Análise de sensibilidade** — complementa mas não substitui a ITT
- Tendência a superestimar o efeito do tratamento (sobrestimação)

### Como reportar no texto:

"Os dados serão analisados por intenção de tratar (ITT), incluindo todos os participantes randomizados nos grupos aos quais foram originalmente alocados. A análise per-protocol será realizada como análise de sensibilidade, incluindo apenas os participantes que completaram o protocolo de tratamento com aderência ≥ 80%."

---

## 5. Abordagem de dados ausentes (missing data)

### 5.1 Classificação dos mecanismos

| Mecanismo | Sigla | Descrição | Implicação |
|---|---|---|---|
| Missing Completely At Random | MCAR | A ausência é independente dos dados observados e não observados | Complete case analysis válida |
| Missing At Random | MAR | A ausência depende dos dados observados, não dos dados ausentes em si | Imputação múltipla adequada |
| Missing Not At Random | MNAR | A ausência depende dos dados ausentes (ex: abandonam estudo por piora clínica) | Imputação múltipla não resolve; sensibilidade necessária |

### 5.2 Estratégias de manejo

#### Complete Case Analysis (CCA)
- Inclui apenas participantes com dados completos
- Válida quando: MCAR e < 5% de dados ausentes
- Pode introduzir viés se MAR ou MNAR

#### Imputação múltipla (MI — Multiple Imputation)
- Recomendada para dados ausentes > 5% sob mecanismo MAR
- Cria m conjuntos de dados completos (tipicamente m = 20–50), analisa cada um separadamente e combina os resultados pelas regras de Rubin

**Software**:
- R: pacote `mice` (Van Buuren S & Groothuis-Oudshoorn K. J Stat Softw 2011;45(3):1-67)
- SPSS: Analyze → Missing Value Analysis → Multiple Imputation
- Stata: `mi impute chained`

#### Last Observation Carried Forward (LOCF)
- Substitui o dado ausente pela última observação disponível do participante
- **Não recomendada** como análise primária: pode introduzir viés em qualquer direção
- Pode ser usada como análise de sensibilidade conservadora

#### Worst Case / Best Case Analysis
- Sensibilidade: assume o pior cenário para o grupo intervenção (ou controle)
- Useful para verificar robustez dos achados

### 5.3 Como reportar no texto:

"Os dados ausentes serão classificados quanto ao mecanismo de perda (MCAR, MAR ou MNAR) por meio do teste de Little. Para dados com mecanismo MAR e proporção de ausências ≥ 5%, será realizada imputação múltipla por equações encadeadas (MICE), com 30 conjuntos de dados imputados e combinação dos resultados pelas regras de Rubin (Van Buuren & Groothuis-Oudshoorn, 2011). A análise de casos completos será apresentada como análise de sensibilidade."

---

## 6. Correção para múltiplas comparações

### Por que corrigir
Ao realizar m testes simultâneos com α = 0,05, a probabilidade de ao menos um resultado falso-positivo é 1 − (0,95)^m. Para m = 20 testes, essa probabilidade é ≈ 64%.

### Correção de Bonferroni
- α corrigido = α / m (onde m = número de comparações)
- Conservadora; aumenta o erro tipo II
- Adequada para número pequeno de comparações (m ≤ 5)

### FDR — False Discovery Rate (Benjamini-Hochberg)
- Controla a proporção esperada de falsos positivos entre as hipóteses rejeitadas
- Menos conservadora que Bonferroni; melhor para múltiplos testes simultâneos (análises ômicas, questionários com múltiplos itens)
- Procedimento: ordenar os p-valores; o p-valor ajustado de posto k é p(k) × m / k

### Quando reportar no texto:

"Dado o caráter exploratório das análises de desfechos secundários, adotar-se-á a correção de Benjamini-Hochberg (controle da taxa de falsa descoberta — FDR) para as comparações múltiplas entre as [X] variáveis secundárias, mantendo-se a taxa de FDR em 5%."

---

## 7. Análise de sobrevivência

### Quando usar
Quando o desfecho é o **tempo até um evento** (morte, recidiva, cura, hospitalização), especialmente quando há censura (participantes que não chegaram ao evento ao final do seguimento).

### Estimador de Kaplan-Meier
- Estima a função de sobrevivência S(t) = probabilidade de não ter o evento até o tempo t
- Representação gráfica: curva em degraus

### Teste de log-rank
- Compara curvas de sobrevivência entre grupos
- Hipótese: H₀: as curvas de sobrevivência são iguais
- Não assume proporcionalidade dos riscos

### Modelo de regressão de Cox (proportional hazards)
- Relaciona covariáveis ao risco de evento (hazard)
- Pressuposto fundamental: **proporcionalidade dos hazards** (a razão de riscos é constante ao longo do tempo)
- Verificação do pressuposto: teste de Schoenfeld; gráfico log[-log(S(t))]
- Resultado: Hazard Ratio (HR) com IC 95%

### Como reportar:
"A probabilidade de sobrevivência será estimada pelo método de Kaplan-Meier, com as curvas dos grupos comparadas pelo teste de log-rank. A associação entre as covariáveis e o desfecho será avaliada por meio de análise multivariada com o modelo de regressão de Cox, com verificação do pressuposto de proporcionalidade dos hazards pelo método dos resíduos de Schoenfeld."

---

## 8. Análise de subgrupos

### Quando realizar
Apenas quando pré-especificada no protocolo (antes do início da coleta). Análises post-hoc de subgrupos são exploratórias e devem ser interpretadas com cautela extrema.

### Como testar a interação
O teste correto para subgrupos é o **teste de interação** (heterogeneidade do efeito), não a comparação de p-valores dentro de cada subgrupo.

```
Modelo com interação: Y ~ grupo + subgrupo + grupo × subgrupo
```

p_interação < 0,05 indica que o efeito do tratamento difere entre os subgrupos.

### Como reportar:
"As análises de subgrupos foram pré-especificadas e serão realizadas para as seguintes variáveis: [lista]. A interação entre o tratamento e cada variável modificadora de efeito será avaliada mediante inclusão de termo de interação nos modelos de regressão, sendo os resultados apresentados em formato de forest plot."

---

## 9. Comandos básicos em R e SPSS

### R — Exemplos de código

```r
# Estatística descritiva
mean(x, na.rm = TRUE)
median(x, na.rm = TRUE)
sd(x, na.rm = TRUE)
IQR(x, na.rm = TRUE)
table(x)

# Normalidade
shapiro.test(x)  # Shapiro-Wilk (recomendado para n ≤ 50)

# Comparação de dois grupos
t.test(x ~ grupo, data = dados)  # Paramétrico independente
wilcox.test(x ~ grupo, data = dados)  # Não paramétrico independente
t.test(x, y, paired = TRUE)  # Paramétrico pareado
wilcox.test(x, y, paired = TRUE)  # Não paramétrico pareado

# Qui-quadrado
chisq.test(table(grupo, desfecho))
fisher.test(table(grupo, desfecho))  # Quando esperados < 5

# ANOVA
summary(aov(x ~ grupo, data = dados))
TukeyHSD(aov(x ~ grupo, data = dados))  # Post-hoc

# Kruskal-Wallis
kruskal.test(x ~ grupo, data = dados)

# Regressão logística
modelo <- glm(desfecho ~ var1 + var2, data = dados, family = binomial)
exp(coef(modelo))  # OR
exp(confint(modelo))  # IC 95%

# Regressão de Cox
library(survival)
modelo_cox <- coxph(Surv(tempo, evento) ~ var1 + var2, data = dados)
summary(modelo_cox)  # HR e IC 95%

# Imputação múltipla
library(mice)
imp <- mice(dados, m = 30, method = "pmm", seed = 123)
fit <- with(imp, glm(desfecho ~ var1 + var2, family = binomial))
summary(pool(fit))
```

### SPSS — Caminhos dos menus

| Análise | Caminho |
|---|---|
| Estatística descritiva | Analyze → Descriptive Statistics → Descriptives / Frequencies / Explore |
| Shapiro-Wilk | Analyze → Descriptive Statistics → Explore → Plots → Normality plots with tests |
| Teste t independente | Analyze → Compare Means → Independent-Samples T Test |
| Mann-Whitney U | Analyze → Nonparametric Tests → Legacy Dialogs → 2 Independent Samples |
| ANOVA | Analyze → Compare Means → One-Way ANOVA |
| Kruskal-Wallis | Analyze → Nonparametric Tests → Legacy Dialogs → K Independent Samples |
| Qui-quadrado | Analyze → Descriptive Statistics → Crosstabs → Statistics → Chi-square |
| Regressão logística | Analyze → Regression → Binary Logistic |
| Regressão de Cox | Analyze → Survival → Cox Regression |
| Kaplan-Meier | Analyze → Survival → Kaplan-Meier |
| Imputação múltipla | Analyze → Multiple Imputation → Impute Missing Data Values |

---

## 10. Referências bibliográficas para a seção de análise estatística

- Cohen J. *Statistical Power Analysis for the Behavioral Sciences*. 2ª ed. Hillsdale, NJ: Lawrence Erlbaum; 1988.
- Faul F, Erdfelder E, Lang AG, Buchner A. G*Power 3: A flexible statistical power analysis for the social, behavioral, and biomedical sciences. *Behav Res Methods*. 2007;39(2):175-91.
- Fleiss JL, Levin B, Paik MC. *Statistical Methods for Rates and Proportions*. 3ª ed. New York: Wiley-Interscience; 2003.
- Lwanga SK, Lemeshow S. *Sample size determination in health studies: a practical manual*. Genebra: WHO; 1991.
- Van Buuren S, Groothuis-Oudshoorn K. mice: Multivariate Imputation by Chained Equations in R. *J Stat Softw*. 2011;45(3):1-67.
- Szklo M, Nieto FJ. *Epidemiology: Beyond the Basics*. 4ª ed. Burlington, MA: Jones & Bartlett Learning; 2019.
- Rothman KJ, Greenland S, Lash TL. *Modern Epidemiology*. 3ª ed. Philadelphia: Lippincott Williams & Wilkins; 2008.
- Hosmer DW Jr, Lemeshow S, Sturdivant RX. *Applied Logistic Regression*. 3ª ed. Hoboken, NJ: Wiley; 2013.
- Klein JP, Moeschberger ML. *Survival Analysis: Techniques for Censored and Truncated Data*. 2ª ed. New York: Springer; 2003.
- Rubin DB. *Multiple Imputation for Nonresponse in Surveys*. New York: Wiley; 1987.
- Benjamini Y, Hochberg Y. Controlling the false discovery rate: a practical and powerful approach to multiple testing. *J R Stat Soc Series B Methodol*. 1995;57(1):289-300.
- R Core Team. *R: A language and environment for statistical computing*. Vienna, Austria: R Foundation for Statistical Computing; 2024. Disponível em: https://www.R-project.org/
- IBM Corp. *IBM SPSS Statistics for Windows*. Version 29.0. Armonk, NY: IBM Corp.; 2022.
