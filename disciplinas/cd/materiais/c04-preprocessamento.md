---
id: cd-pre-processamento-valores-faltantes-duplicatas-ruido-outliers-reducao-de-dados
titulo: Importância do pré-processamento: valores faltantes, instâncias repetidas, ruído e outliers (técnicas de remoção, IQR, z-escore), redução de dimensionalidade e de numerosidade; caso dos dados de expressão gênica
assunto: cd-02-preparacao-e-avaliacao
tipo: prova
questao: AB1 2020.1 Q4; REAV 1 Q3; REAV AB1 2020.2 Q3; AB1 2021.1 Q3; Lista 1 Q6-Q7
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
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB1 2020.1 Q4; REAV 1 Q3; REAV AB1 2020.2 Q3; AB1 2021.1 Q3; Lista 1 Q6-Q7 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Por que pré-processar:** "lixo entra, lixo sai". Erros, faltantes e escalas diferentes distorcem estatísticas e modelos; a maior parte do tempo de um projeto vai aqui.

**Caso da prova (expressão gênica):** faltantes, repetidas, ruído, outliers e centenas de milhares de variáveis.
- **Faltantes:** remover a linha (simples, mas perde dados), imputar pela **média ou mediana** (rápido, reduz a variância), pela **média da classe** (mais preciso no treino; nunca use a classe do teste) ou por modelo (k-NN, regressão). Com genes, imputação por k-NN entre amostras parecidas é comum.
- **Repetidas:** remover duplicatas exatas, para não dar peso artificial a uma amostra.
- **Ruído:** **suavização por compartimentos** (*binning*: substitui por média ou mediana do intervalo; vantagem: simples; desvantagem: perde detalhe) e **regressão** (ajusta uma função; desvantagem: supõe a forma).
- **Outliers**, duas técnicas:
  - **IQR:** fora de $[Q_1 - 1{,}5\,\text{IQR},\ Q_3 + 1{,}5\,\text{IQR}]$, com $\text{IQR} = Q_3 - Q_1$; robusto, não supõe normalidade;
  - **z-escore:** $|z| = |x - \bar{x}|/s > 3$; supõe dados aproximadamente normais, e o próprio outlier infla $s$.
  Antes de remover, pergunte se é **erro** ou **caso raro real** (em fraudes, o outlier é o alvo).
- **Muitas variáveis:** **redução de dimensionalidade** (filtrar genes por variância ou correlação com a classe, PCA). **Redução de numerosidade**: menos linhas com amostragem estratificada, agregação ou histogramas, para caber em memória e acelerar.

**Verificação:** `test_preprocessamento` confere com pandas e scikit-learn a remoção de duplicatas, a imputação pela média e pelo k-NN, e que o IQR e o z-escore marcam o valor 100 numa amostra normal de 200 valores (o z-escore com o limiar 3).
