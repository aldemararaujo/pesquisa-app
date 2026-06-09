# Referência: Proteção, Monitoramento e Confidencialidade em Pesquisa

Arquivo de suporte para a skill `capitulo-monitorizacao`. Contém fundamentos regulatórios, tabelas técnicas e modelos de frases para redigir o Capítulo 6 — Monitorização da Pesquisa.

---

## 1. Classificação de risco segundo a Resolução CNS nº 466/2012

A Resolução CNS nº 466/2012 (item II.2) define a seguinte escala de risco para pesquisas envolvendo seres humanos:

| Categoria de risco | Definição | Exemplos práticos |
|---|---|---|
| **Risco mínimo** | Procedimentos de rotina que não implicam desconforto ou dano previsível | Entrevistas, questionários autoadministrados, grupos focais, observação sem intervenção, revisão de prontuários sem contato com o participante |
| **Risco menor que o mínimo** | Procedimentos com possibilidade de desconforto leve e transitório, sem risco de dano permanente | Aferição de pressão arterial, medidas antropométricas (peso, estatura, perímetros), punção digital para glicemia capilar, coleta de saliva, aplicação de escala de dor com estímulo leve, entrevista sobre tema sensível |
| **Risco maior que o mínimo** | Procedimentos invasivos, uso de medicamentos, intervenções cirúrgicas, exposição a agentes físicos, químicos ou biológicos, ou procedimentos que possam causar dano temporário ou permanente | Coleta de sangue venoso, biópsia, procedimentos cirúrgicos, uso de fármacos em investigação, exposição à radiação ionizante, intervenções psicológicas para transtornos severos, estudos em populações de alto risco |

**Importante:** A classificação deve ser justificada no protocolo. Estudos com risco maior que o mínimo exigem descrição detalhada das medidas de proteção e podem demandar revisão pela CONEP.

**Referência:** Brasil. Conselho Nacional de Saúde. Resolução nº 466, de 12 de dezembro de 2012, item II.2.

---

## 2. Graus de eventos adversos — CTCAE v5.0

O *Common Terminology Criteria for Adverse Events* (CTCAE), versão 5.0, do National Cancer Institute (2017), classifica os eventos adversos em cinco graus de severidade, aplicável a estudos com intervenções clínicas:

| Grau | Denominação | Critério geral |
|---|---|---|
| **Grau 1** | Leve | Sintoma assintomático ou leve; apenas observação clínica; nenhuma intervenção indicada |
| **Grau 2** | Moderado | Intervenção mínima, local ou não invasiva indicada; limitação de atividades instrumentais da vida diária |
| **Grau 3** | Grave | Hospitalização ou prolongamento de hospitalização indicados; limitação de autocuidado nas atividades diárias; incapacitante |
| **Grau 4** | Risco de vida | Consequências com risco de vida imediato; intervenção urgente indicada |
| **Grau 5** | Morte | Morte relacionada ao evento adverso |

**Eventos adversos sérios (EAS):** qualquer evento adverso que, independentemente do grau, resulte em: morte, risco de vida imediato, hospitalização ou prolongamento de hospitalização já existente, incapacidade ou dano permanente significativo, anomalia congênita ou defeito congênito, ou que requeira intervenção médica para prevenir as situações anteriores.

**Notificação ao CEP:** eventos adversos sérios inesperados (não previstos no protocolo aprovado) devem ser notificados ao CEP no prazo de até **15 dias corridos** após o pesquisador tomar conhecimento do evento, por meio da Plataforma Brasil.

**Referência:** National Cancer Institute. Common Terminology Criteria for Adverse Events (CTCAE), Version 5.0. Bethesda: US Department of Health and Human Services; 2017.

---

## 3. Checklist de qualidade de dados

### 3.1 Verificações automáticas (implementar no banco de dados)

| Tipo de verificação | Descrição | Exemplo |
|---|---|---|
| **Range check** | Valor fora da faixa biologicamente plausível → alerta para revisão | Estatura: < 50 cm ou > 250 cm; IMC: < 10 ou > 80 kg/m²; frequência cardíaca: < 20 ou > 250 bpm |
| **Logic check** | Inconsistência lógica entre variáveis relacionadas | Data de nascimento incompatível com idade declarada; diagnóstico de diabetes sem glicemia basal registrada; gestante com sexo masculino |
| **Completeness check** | Campo obrigatório não preenchido | Identificação do participante, data da avaliação, variável primária |
| **Duplicate check** | Mesmo participante registrado mais de uma vez | Mesmo código ou mesmo nome/data de nascimento em registros distintos |
| **Sequence check** | Violação da ordem cronológica de avaliações | Data da avaliação T2 anterior à data da avaliação T1 |

### 3.2 Processo de dupla entrada de dados (*double data entry*)

1. Dois digitadores independentes inserem 100% dos dados no banco eletrônico a partir das fichas originais
2. Software de gestão de dados compara automaticamente as duas entradas e gera relatório de discrepâncias
3. Discrepâncias são investigadas por consulta às fichas originais de coleta
4. Discordâncias persistentes são resolvidas por reunião de consenso entre os pesquisadores responsáveis, com registro em ata
5. Taxa de discordância aceitável (definir no protocolo; referência: < 0,5% de campos com erro)

### 3.3 Auditoria periódica — itens a verificar

- [ ] Completude dos registros (% de campos obrigatórios preenchidos)
- [ ] Conformidade com os critérios de inclusão/exclusão para todos os participantes
- [ ] Coerência entre ficha original e dado digitado (amostra aleatória de 10–20% dos registros)
- [ ] Ausência de desvios de protocolo não documentados
- [ ] Atualização do log de *queries* e resolução de inconsistências dentro do prazo
- [ ] Integridade dos backups (verificação de restauração)

---

## 4. Comitê de Monitoramento de Dados (DSMB/DSMC)

### 4.1 Quando é indicado

O DSMB (*Data Safety Monitoring Board*) ou DSMC (*Data Safety Monitoring Committee*) é indicado para:
- Ensaios clínicos de fase III com desfechos de mortalidade ou morbidade grave
- Estudos com possibilidade de dano significativo relacionado à intervenção
- Estudos com análises interinas pré-especificadas de eficácia ou dano
- Estudos multicêntricos de longa duração com risco de perda de *equipoise*

Não é habitualmente necessário para: estudos observacionais de risco mínimo; ensaios de fase I/II de curta duração; estudos com desfechos exclusivamente laboratoriais de risco baixo.

### 4.2 Composição recomendada

| Membro | Perfil | Papel |
|---|---|---|
| Clínico especialista | Especialista na área clínica do estudo | Avaliação da relevância clínica dos achados |
| Bioestatístico independente | Especialista em bioestatística clínica | Análise dos dados intermediários; avaliação das regras de parada |
| Especialista em ética em pesquisa | Profissional com expertise em bioética | Avaliação do equilíbrio entre riscos e benefícios |

Todos os membros devem ser independentes da equipe de pesquisa e do patrocinador do estudo.

### 4.3 Regras de parada interina — modelos principais

#### Fronteira de O'Brien-Fleming (para eficácia)
- Conservadora: exige forte evidência nas análises precoces; nivela-se ao α convencional na análise final
- Gasto de alpha nas análises intermediárias: menor (preserva poder para a análise final)
- Exemplo (2 análises interinas + 1 final, α = 0,05 bilateral):
  - Análise 1 (50% do recrutamento): p < 0,005
  - Análise 2 (75% do recrutamento): p < 0,014
  - Análise final (100%): p < 0,045

#### Fronteira de Pocock (para eficácia)
- Liberal: p-value constante em todas as análises
- Exemplo (3 análises igualmente espaçadas, α = 0,05 bilateral): p < 0,022 em cada análise

#### Regra de parada por dano
- Pré-especificar o limiar de taxa de eventos adversos sérios inesperados que determinará revisão imediata pelo DSMB
- Exemplo: "O DSMB será convocado para reunião extraordinária caso a taxa de eventos adversos de grau ≥ 3 relacionados ao procedimento supere [X]% no grupo intervenção, ou caso ocorra [Y] ou mais eventos adversos sérios inesperados em qualquer grupo"

**Referências:** DeMets DL et al., 2006; Ellenberg SS et al., 2019.

---

## 5. LGPD — Requisitos aplicados à pesquisa em saúde

### 5.1 Bases legais para tratamento de dados pessoais sensíveis (dados de saúde)

A LGPD (Lei nº 13.709/2018) enquadra dados de saúde como dados pessoais sensíveis (art. 5º, II). As bases legais para tratamento em pesquisa são:

| Base legal | Artigo | Aplicação em pesquisa |
|---|---|---|
| **Consentimento do titular** | Art. 11, I | TCLE assinado pelo participante — base mais comum em pesquisa clínica |
| **Pesquisa científica** | Art. 11, II, "c" | Permite tratamento sem consentimento individual quando impraticável, mediante aprovação do CEP e anonimização quando possível |
| **Proteção da vida** | Art. 11, II, "e" | Aplicável em emergências |

### 5.2 Obrigações do controlador dos dados

- Nomear formalmente o **controlador** (pesquisador principal ou instituição proponente) e o **operador** (terceiro que processa dados por conta do controlador, quando houver)
- Documentar o tratamento de dados no TCLE (finalidade, prazo de guarda, compartilhamento, direitos do titular)
- Implementar medidas técnicas e administrativas de segurança (art. 46)
- Notificar a Autoridade Nacional de Proteção de Dados (ANPD) em caso de incidente de segurança em prazo razoável (art. 48)

### 5.3 Direitos do titular (art. 18)

O participante da pesquisa tem direito a:
- Confirmar a existência do tratamento de seus dados
- Acessar os dados tratados
- Corrigir dados incompletos, inexatos ou desatualizados
- Obter anonimização, bloqueio ou eliminação de dados desnecessários
- Solicitar portabilidade dos dados
- Obter informação sobre compartilhamento com terceiros
- Revogar o consentimento a qualquer momento, sem prejuízo ao tratamento realizado antes da revogação

### 5.4 Prazo de guarda dos dados em pesquisa

- **Mínimo de 5 anos** após o encerramento da pesquisa, conforme Resolução CNS nº 466/2012, item XIII.4
- Para ensaios clínicos regulatórios (ANVISA): prazo mínimo de **15 anos** após o encerramento
- Após o prazo legal, os documentos devem ser destruídos de forma segura e irreversível

---

## 6. Modelos de frases por subseção e tipo de estudo

### 6.1 Medidas de proteção — modelos por procedimento

**Para medidas antropométricas (peso e estatura):**
"Os procedimentos de mensuração do peso corporal e da estatura serão realizados por avaliadores previamente treinados e certificados, seguindo o protocolo padronizado descrito nas Diretrizes do Sistema de Vigilância Alimentar e Nutricional (Brasil, Ministério da Saúde, 2011). Cada procedimento será detalhado verbalmente ao participante antes de sua execução; o participante será orientado sobre a posição correta a adotar e terá oportunidade de formular dúvidas. A pesquisa apresenta risco mínimo aos participantes, uma vez que os procedimentos de avaliação antropométrica não são invasivos e não implicam desconforto previsível além do habitual em exames de rotina (Brasil, 2012; World Medical Association, 2013)."

**Para coleta de sangue venoso:**
"A coleta de sangue venoso periférico será realizada por enfermeiro ou biomédico com habilitação legal e treinamento específico para o procedimento. O participante será informado sobre a técnica, o volume a ser coletado e os riscos potenciais — hematoma local, dor transitória no local da punção e, raramente, lipotimia — antes da realização do procedimento. Será assegurada a disponibilidade de material para atendimento de intercorrências (kit de emergência, maca para decúbito em caso de lipotimia). O procedimento classifica-se como risco menor que o mínimo, conforme a Resolução CNS nº 466/2012. Quaisquer eventos adversos, incluindo hematoma > 2 cm ou dor persistente, serão registrados em formulário padronizado e notificados ao CEP conforme os critérios da Resolução CNS nº 466/2012 (International Council for Harmonisation, 2016; National Cancer Institute, 2017)."

**Para aplicação de questionários sobre temas sensíveis:**
"A aplicação dos questionários que abordam temas de saúde mental, histórico de trauma, comportamento sexual ou uso de substâncias psicoativas poderá gerar desconforto emocional transitório em alguns participantes. Para mitigar esse risco, o aplicador será orientado a interromper a entrevista imediatamente se o participante manifestar angústia, choro ou recusa, e a oferecer encaminhamento para serviço de apoio psicológico disponível na instituição. A participação poderá ser retomada em outra data ou encerrada definitivamente, a critério exclusivo do participante, sem qualquer prejuízo ao seu atendimento (Brasil, 2012; Council for International Organizations of Medical Sciences, 2016)."

---

### 6.2 Monitorização de dados — modelos por tipo de banco

**Para banco de dados em Microsoft Excel:**
"Os dados coletados serão armazenados em planilha eletrônica desenvolvida especificamente para este estudo (Microsoft Excel, versão [XX], Microsoft Inc., Redmond, WA, EUA), com proteção por senha de abertura e de modificação, em arquivo salvo em servidor institucional com backup automático diário. A planilha disporá de validação de dados (*data validation*) para os campos numéricos, bloqueando automaticamente a inserção de valores fora da faixa plausível pré-estabelecida (Society for Clinical Data Management, 2013)."

**Para banco de dados em REDCap:**
"Os dados coletados serão armazenados na plataforma REDCap (*Research Electronic Data Capture*), versão [XX] (Harris PA et al., 2009), hospedada em servidor da [instituição] com autenticação de dois fatores, criptografia de dados em trânsito (TLS 1.2) e em repouso, e backup automático diário. O REDCap oferece funcionalidades nativas de *range checks*, *logic checks* e *branching logic*, que serão configurados para este estudo, minimizando erros de entrada (Society for Clinical Data Management, 2013; International Council for Harmonisation, 2016)."

---

### 6.3 Confidencialidade — modelos gerais

**Parágrafo de abertura:**
"A confidencialidade das informações dos participantes será rigorosamente preservada durante todas as fases da pesquisa — coleta, armazenamento, análise e disseminação dos resultados. Em nenhuma circunstância será divulgada publicamente qualquer informação que permita, direta ou indiretamente, a identificação individual dos participantes da pesquisa (Brasil, 2012; World Medical Association, 2013)."

**Pseudonimização:**
"A cada participante será atribuído um código alfanumérico único, gerado por sequência aleatória, que substituirá o nome e demais dados de identificação em todas as fichas de coleta, formulários de avaliação e no banco de dados eletrônico. A lista de correspondência entre o código atribuído e a identidade real do participante será mantida em arquivo físico trancado, sob custódia exclusiva do pesquisador principal, separado do banco de dados principal (Brasil, 2018; Brasil, 2012)."

---

### 6.4 Critérios de suspensão — modelos de limite numérico

**Meta de recrutamento (ajustar N e semanas ao protocolo):**
"A pesquisa será temporariamente suspensa caso a taxa de recrutamento de novos participantes seja inferior a [N] participantes por semana durante dez semanas consecutivas, indicando incapacidade de atingir o tamanho amostral calculado dentro do período de coleta previsto. Nessa situação, o pesquisador principal realizará diagnóstico das causas da baixa adesão e, se pertinente, submeterá emenda ao protocolo ao CEP propondo ajustes na estratégia de recrutamento, no período de coleta ou no tamanho amostral, antes da retomada das atividades (Brasil, 2012)."

**Eventos adversos (ajustar limiar ao tipo de estudo):**
"A coleta de dados será imediatamente suspensa caso a taxa de eventos adversos de grau ≥ 3 (conforme CTCAE v5.0) possivelmente relacionados ao procedimento do estudo supere [X]% dos participantes avaliados, ou caso ocorram [Y] ou mais eventos adversos sérios inesperados em qualquer grupo. O pesquisador principal notificará o CEP em até 15 dias corridos e aguardará orientação antes de retomar qualquer atividade com participantes (National Cancer Institute, 2017; International Council for Harmonisation, 2016; Brasil, 2012)."

---

## 8. Matriz de risco — metodologia e exemplos

### 8.1 Fundamentos da metodologia

A matriz de risco é um instrumento de gestão de riscos que organiza e visualiza os riscos identificados segundo duas dimensões: **probabilidade de ocorrência** e **severidade do dano potencial**. A combinação dessas dimensões gera o **nível de risco resultante**, que orienta a priorização das medidas de mitigação.

**Base normativa aplicada à pesquisa em saúde:**
- ISO 31000:2018 — define o framework de gestão de riscos (identificação → análise → avaliação → tratamento)
- CIOMS 2016, Diretriz 4 — determina que os riscos de pesquisa devem ser minimizados e justificados pelo valor científico e social
- Resolução CNS nº 466/2012, item II.2 — classifica o risco global do estudo em: mínimo / menor que o mínimo / maior que o mínimo

---

### 8.2 Critérios para classificar a probabilidade

| Nível | Definição | Referência prática |
|---|---|---|
| **Muito baixa** | Ocorrência rara; reportada apenas em situações excepcionais na literatura | Taxa < 1% em estudos similares; ou nunca documentada com os procedimentos planejados |
| **Baixa** | Ocorrência possível mas improvável nas condições do estudo | Taxa entre 1% e 10% em estudos com procedimentos similares |
| **Moderada** | Ocorrência esperada em uma parcela dos participantes | Taxa entre 10% e 30%; ou bem documentada na literatura para o procedimento |
| **Alta** | Ocorrência frequente; afetará a maioria dos participantes | Taxa > 30%; ou inerente ao procedimento sem variação metodológica |

---

### 8.3 Critérios para classificar a severidade

| Nível | Definição | Exemplos na pesquisa | Relação com CNS 466/12 |
|---|---|---|---|
| **Mínima** | Nenhum desconforto perceptível ou desconforto desprezível e imediato | Constrangimento leve, desconforto postural < 1 minuto | Risco mínimo |
| **Leve** | Desconforto transitório e autolimitado; sem necessidade de intervenção | Dor local leve, hematoma pequeno, desconforto emocional passageiro | Risco menor que o mínimo |
| **Moderada** | Desconforto que requer atenção ou intervenção, mas sem sequela permanente | Hematoma extenso, lipotimia com recuperação espontânea, exposição de dados sensíveis | Risco menor que o mínimo / maior que o mínimo |
| **Grave** | Dano com potencial de sequela permanente, hospitalização ou risco de vida | Infecção sistêmica, reação anafilática, hospitalização, dano psicológico duradouro | Risco maior que o mínimo — exige submissão à CONEP |

---

### 8.4 Grade de nível de risco resultante

| Probabilidade ↓ \ Severidade → | **Mínima** | **Leve** | **Moderada** | **Grave** |
|---|---|---|---|---|
| **Alta** | Moderado | Alto | Crítico | Crítico |
| **Moderada** | Baixo | Moderado | Alto | Crítico |
| **Baixa** | Baixo | Baixo | Moderado | Alto |
| **Muito baixa** | Aceitável | Baixo | Baixo | Moderado |

---

### 8.5 Exemplo de matriz preenchida — estudo observacional transversal com antropometria

**Tabela 2 — Matriz de registro de riscos (exemplo: antropometria)**

| Nº | Risco identificado | Probabilidade | Severidade | **Nível de risco** | Medida de mitigação principal | Responsável |
|---|---|---|---|---|---|---|
| 1 | Lipotimia/tontura transitória durante avaliação ortostática | Muito baixa | Leve | **Baixo** | Sala climatizada; maca disponível; participante nunca sozinho; orientação para comunicar sintomas | Avaliador |
| 2 | Desconforto relacionado à exposição corporal | Baixa | Mínima | **Baixo** | Sala reservada com biombo; avaliador do mesmo sexo quando solicitado; orientação prévia; direito de interromper | Avaliador |
| 3 | Comprometimento da imagem corporal | Baixa | Leve | **Baixo** | Comunicação não estigmatizante; avaliador com treinamento empático; encaminhamento para psicólogo | Avaliador |
| 4 | Violação da confidencialidade dos dados | Baixa | Moderada | **Moderado**¹ | Pseudonimização; banco criptografado; senha individual; transmissão segura (ver seção 6.3) | Pesquisador principal |
| 5 | Perda ou dano irreversível dos dados | Muito baixa | Moderada | **Baixo** | Backup semanal em mídia externa; procedimento de encerramento (ver seção 6.4) | Coordenador |

*¹ Detalhamento narrativo obrigatório (Elemento 4 da seção 7.1).*

**Conclusão do exemplo:** O estudo apresenta perfil de risco **Baixo/Moderado**. Quatro riscos são Baixo ou Aceitável; um risco é Moderado com mitigações documentadas. Classificação global: **risco menor que o mínimo** (Resolução CNS nº 466/2012). A relação risco-benefício é favorável.

---

### 8.6 Exemplo de matriz preenchida — ensaio clínico com coleta de sangue venoso

**Tabela 2 — Matriz de registro de riscos (exemplo: ensaio clínico com coleta de sangue)**

| Nº | Risco identificado | Probabilidade | Severidade | **Nível de risco** | Medida de mitigação principal | Responsável |
|---|---|---|---|---|---|---|
| 1 | Infecção local no sítio de punção | Muito baixa | Moderada | **Baixo** | Materiais descartáveis; antissepsia com álcool 70°; técnica asséptica rigorosa | Profissional habilitado |
| 2 | Lipotimia vasovagal pós-punção | Baixa | Leve | **Baixo** | Punção com participante sentado/deitado; monitoração 5 min pós-procedimento; kit de emergência disponível | Profissional habilitado |
| 3 | Dor local e hematoma no sítio de punção | Moderada | Leve | **Moderado**¹ | Escalpe de menor calibre; pressão local 3–5 min; orientação sobre sinais de hematoma; canal de contato para intercorrências | Profissional habilitado |
| 4 | Violação da confidencialidade dos dados | Baixa | Moderada | **Moderado**² | Pseudonimização; criptografia; senhas individuais (ver seção 6.3) | Pesquisador principal |
| 5 | Evento adverso grave inesperado relacionado à intervenção | Muito baixa | Grave | **Moderado**³ | Protocolo de notificação ao CEP em 15 dias; suspensão imediata da coleta; avaliação pelo DSMB | Pesquisador principal / DSMB |
| 6 | Perda ou dano dos dados | Muito baixa | Moderada | **Baixo** | Backup semanal; procedimento de encerramento (ver seção 6.4) | Coordenador |

*¹ ² ³ Detalhamentos narrativos obrigatórios (Elemento 4 da seção 7.1).*

**Conclusão do exemplo:** O estudo apresenta perfil de risco **Baixo a Moderado**. Três riscos são Baixo; três são Moderado com mitigações documentadas. Nenhum risco Alto ou Crítico. Classificação global: **risco menor que o mínimo** (Resolução CNS nº 466/2012). A relação risco-benefício é favorável mediante as medidas de mitigação descritas.

---

## 7. Lista de referências completa — estilo Vancouver com DOI e URL

Brasil. Conselho Nacional de Saúde. Resolução nº 466, de 12 de dezembro de 2012. Aprova as diretrizes e normas regulamentadoras de pesquisas envolvendo seres humanos. Diário Oficial da União, Brasília, DF, 13 jun. 2013; Seção 1:59. Disponível em: https://conselho.saude.gov.br/resolucoes/2012/Reso466.pdf

Brasil. Conselho Nacional de Saúde. Resolução nº 510, de 7 de abril de 2016. Dispõe sobre as normas aplicáveis a pesquisas em Ciências Humanas e Sociais. Diário Oficial da União, Brasília, DF, 24 maio 2016; Seção 1:44. Disponível em: https://conselho.saude.gov.br/resolucoes/2016/Reso510.pdf

Brasil. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). Diário Oficial da União, Brasília, DF, 15 ago. 2018. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

Brasil. Ministério da Saúde. Conselho Nacional de Saúde. Norma Operacional nº 001/2013 — CONEP. Dispõe sobre a organização e funcionamento do sistema CEP/CONEP e sobre os procedimentos para submissão, avaliação e acompanhamento da pesquisa e de desenvolvimento científico e tecnológico envolvendo seres humanos no Brasil. Brasília: Ministério da Saúde; 2013. Disponível em: https://conselho.saude.gov.br/web_comissoes/conep/aquivos/normativa/normaoperacional001_2013_conep.pdf

Council for International Organizations of Medical Sciences (CIOMS). International Ethical Guidelines for Health-related Research Involving Humans. 4th ed. Geneva: CIOMS; 2016. doi:10.56759/rgxl7429. Disponível em: https://cioms.ch/publications/product/international-ethical-guidelines-for-health-related-research-involving-humans/

DeMets DL, Furberg CD, Friedman LM. Data Monitoring in Clinical Trials: A Case Studies Approach. New York: Springer; 2006. doi:10.1007/978-0-387-27771-8

Ellenberg SS, Fleming TR, DeMets DL. Data Monitoring Committees in Clinical Trials: A Practical Perspective. 2nd ed. Chichester: Wiley; 2019. doi:10.1002/9781119512592

Harris PA, Taylor R, Thielke R, Payne J, Gonzalez N, Conde JG. Research electronic data capture (REDCap) — a metadata-driven methodology and workflow process for providing translational research informatics support. J Biomed Inform. 2009;42(2):377–81. doi:10.1016/j.jbi.2008.08.010. Disponível em: https://www.sciencedirect.com/science/article/pii/S1532046408001226

International Council for Harmonisation (ICH). ICH E6(R2): Guideline for Good Clinical Practice. Step 4 version. Geneva: ICH; 2016. Disponível em: https://www.ich.org/page/efficacy-guidelines

International Organization for Standardization. ISO 31000:2018 — Risk management: guidelines. Geneva: ISO; 2018. Disponível em: https://www.iso.org/standard/65694.html

Moher D, Hopewell S, Schulz KF, Montori V, Gøtzsche PC, Devereaux PJ, et al. CONSORT 2010 explanation and elaboration: updated guidelines for reporting parallel group randomised trials. BMJ. 2010;340:c869. doi:10.1136/bmj.c869. Disponível em: https://www.bmj.com/content/340/bmj.c869

National Cancer Institute. Common Terminology Criteria for Adverse Events (CTCAE), Version 5.0. Bethesda (MD): US Department of Health and Human Services; 2017. Disponível em: https://ctep.cancer.gov/protocoldevelopment/electronic_applications/docs/CTCAE_v5_Quick_Reference_5x7.pdf

O'Brien PC, Fleming TR. A multiple testing procedure for clinical trials. Biometrics. 1979;35(3):549–56. doi:10.2307/2530245

Pocock SJ. Group sequential methods in the design and analysis of clinical trials. Biometrika. 1977;64(2):191–9. doi:10.1093/biomet/64.2.191

Society for Clinical Data Management (SCDM). Good Clinical Data Management Practices (GCDMP). Version 4.0. Milwaukee: SCDM; 2013. Disponível em: https://scdm.org/gcdmp/

Wheatley K, Clayton D. Be skeptical about unexpected large apparent treatment effects: the case of an MRC AML12 randomization. Control Clin Trials. 2003;24(1):66–70. doi:10.1016/S0197-2456(02)00273-X

World Medical Association. Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Subjects. Adopted by the 18th WMA General Assembly (1964); last amendment by the 64th WMA General Assembly, Fortaleza, Brazil, October 2013. Disponível em: https://www.wma.net/policies-post/wma-declaration-of-helsinki-ethical-principles-for-medical-research-involving-human-subjects/
