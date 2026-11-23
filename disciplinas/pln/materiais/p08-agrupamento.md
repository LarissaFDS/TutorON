---
id: pln-agrupamento-de-textos-pca-95-por-cento-variancia-k-means-metodo-do-cotovelo
titulo: Agrupamento de textos: PCA preservando 95% da variância (dimensão resultante), k-means com o método do cotovelo (elbow) nos dados projetados e nos originais
assunto: pln-03-topicos-agrupamento-e-embeddings
tipo: lista
questao: Lista 4, questão 2
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 4, questão 2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**PCA com 95% da variância:** projeta os dados nas direções de maior variância; com `PCA(n_components=0.95)`, o scikit-learn escolhe o **menor número de componentes** cuja variância explicada acumulada passa de 95%. A **dimensão resultante** é `pca.n_components_`. Detalhe: o PCA do scikit-learn **centraliza** os dados e não aceita matriz esparsa; converta (`toarray()`) se a base for pequena, ou use `TruncatedSVD` para a matriz TF-IDF esparsa.

Leia a curva `np.cumsum(pca.explained_variance_ratio_)`: em texto, a variância costuma se espalhar por muitas dimensões, e 95% pode exigir centenas.

**k-means e cotovelo:** para $k = 1, 2, \ldots$, rode o k-means e anote a **inércia** (soma dos quadrados das distâncias de cada ponto ao seu centroide). A inércia sempre cai com $k$; escolha o $k$ do **cotovelo**, onde a queda deixa de ser grande. Se o cotovelo for ambíguo, confira com a **silhueta**.

**Projetado × original:** o PCA tira ruído e acelera o k-means; os grupos devem ser parecidos se os 95% guardam a estrutura. Compare os rótulos dos dois agrupamentos (índice de Rand ajustado) e leia exemplos de cada grupo.

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

xp = PCA(n_components=0.95, random_state=0).fit_transform(x_denso)
inercias = [KMeans(k, n_init=10, random_state=0).fit(xp).inertia_ for k in range(1, 11)]
```

**Verificação:** `test_pca_e_cotovelo` confere num conjunto sintético com 3 grupos em 50 dimensões que `n_components_` é o menor número com 95% acumulado, que a inércia cai com $k$ e que o cotovelo (maior queda relativa) indica 3 grupos nos dados projetados e nos originais, com os mesmos grupos.
