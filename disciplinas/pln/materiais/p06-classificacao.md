---
id: pln-classificacao-de-textos-regressao-logistica-naive-bayes-matriz-de-confusao-70-30
titulo: Classificação binária de textos: rótulos, CountVectorizer e TF-IDF, regressão logística, Naive Bayes e outro classificador, divisão 70/30, matriz de confusão, acurácia, precisão, recall e F1
assunto: pln-02-representacao-e-classificacao
tipo: lista
questao: Lista 3, questão 2; Lista 5, questão 2a; Lista 6, questão 1
resolucao: sim
fonte: Listas de exercícios 1 a 6 de Processamento de Linguagem Natural, Prof. Thales Vieira (IC-UFAL), 2021.1
curso: Ciência da Computação (UFAL), eletiva Processamento de Linguagem Natural; turma 2021.1 (listas de out/2021 a fev/2022)
fontes_catalogo: ufal-vieira-listas-pln,scikit-learn-pln
autoria: Questões do Prof. Thales Vieira (IC-UFAL); explicação e exemplo parecido da equipe TutorON
licenca: Não declarada (listas); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 3, questão 2; Lista 5, questão 2a; Lista 6, questão 1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Montar o problema:** escolha duas classes bem definidas e coerentes com a base (ex.: notícias de esporte × política; avaliações positivas × negativas) e veja se estão **balanceadas**.

**Pipeline** (o vetorizador é ajustado **só no treino**, para não vazar o vocabulário do teste):
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

xtr, xte, ytr, yte = train_test_split(textos, rotulos, test_size=0.3,
                                      stratify=rotulos, random_state=0)
modelo = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))
modelo.fit(xtr, ytr)
print(confusion_matrix(yte, modelo.predict(xte)))
print(classification_report(yte, modelo.predict(xte)))
```
Troque o vetorizador (`CountVectorizer`) e o classificador (`MultinomialNB`, `LinearSVC`) para os seis resultados.

**Métricas** (classe positiva): precisão $= \frac{VP}{VP + FP}$, recall $= \frac{VP}{VP + FN}$, $F_1 = \frac{2PR}{P + R}$, acurácia $= \frac{VP + VN}{\text{total}}$. Na matriz do scikit-learn, linhas são a classe **real** e colunas a **prevista**.

**Comparar:** uma divisão 70/30 só tem variância; repita com várias sementes ou use validação cruzada estratificada e compare médias. Naive Bayes costuma ir bem com contagens; regressão logística e SVM linear, com TF-IDF.

**Verificação:** `test_classificacao_textos` roda o pipeline numa base pequena de frases de esporte e de política com semente fixa: os três classificadores passam de 80% de acurácia no teste, e precisão, recall e F1 conferem com a matriz de confusão.
