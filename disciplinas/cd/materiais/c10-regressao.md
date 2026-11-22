---
id: cd-regressao-linear-multipla-logistica-quando-usar-selecao-de-variaveis-predicao
titulo: Regressão linear múltipla × regressão logística: em que problemas usar cada uma, vantagens da logística, uso da regressão para seleção de variáveis e predição de novas instâncias
assunto: cd-03-metodos
tipo: prova
questao: Final 2020.1 Q3; REAV 2 2020.1 Q1; AB1 2020.2 Q6; REAV AB1 2020.2 Q5; AB1 2021.1 Q6
resolucao: sim
fonte: Provas e listas de Ciência de Dados do Prof. Bruno Pimentel (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Ciência de Dados (COMP401); turmas 2020.1, 2020.2 e 2021.1
fontes_catalogo: ufal-pimentel-provas-cd
autoria: Questões do Prof. Bruno Pimentel (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Ciência de Dados, Prof. Bruno Pimentel (UFAL), Final 2020.1 Q3; REAV 2 2020.1 Q1; AB1 2020.2 Q6; REAV AB1 2020.2 Q5; AB1 2021.1 Q6 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Regressão linear múltipla:** variável resposta **contínua**:
$$y = \beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p + \varepsilon$$
Os coeficientes saem por **mínimos quadrados** (minimizam a soma dos quadrados dos resíduos). Ex.: prever o **preço de um imóvel** pela área, quartos e bairro; a demanda de energia pela temperatura.

**Regressão logística:** resposta **binária** (ou categórica): modela a **probabilidade** da classe 1,
$$P(y = 1 \mid x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p)}}$$
Em palavras: a função sigmoide de uma combinação linear dos atributos. Ex.: **inadimplência** (paga ou não), diagnóstico (doente ou não), *churn*.

**Vantagens da logística:** devolve **probabilidades** (permite escolher o limiar conforme o custo dos erros); coeficientes interpretáveis como **razão de chances** ($e^{\beta_i}$: quanto as chances se multiplicam quando $x_i$ aumenta 1); treino rápido e estável; base forte para comparar com modelos mais complexos.

**Seleção de variáveis:** usar a significância dos coeficientes (teste $t$, valor $p$), a **regularização L1 (Lasso)**, que zera coeficientes de variáveis inúteis, e procedimentos passo a passo (para frente, para trás) com critério AIC ou validação. Com os atributos padronizados, o tamanho do coeficiente indica a força do efeito. Cuidado com **multicolinearidade**: variáveis correlacionadas tornam os coeficientes instáveis.

**Predição de novas instâncias:** aplica-se a equação ajustada aos atributos do novo caso (com os mesmos pré-processamentos) e avalia-se o erro em dados de teste (RMSE na linear; acurácia, AUC na logística).

**Verificação:** `test_regressao` gera dados com $y = 3 + 2x_1 - x_2$ mais ruído e 3 variáveis inúteis: o `LinearRegression` recupera 3, 2 e −1 (tolerância 0,1), o Lasso zera as inúteis, e a `LogisticRegression` devolve probabilidades entre 0 e 1 que crescem com $x_1$.
