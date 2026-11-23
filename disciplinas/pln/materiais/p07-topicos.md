---
id: pln-modelagem-de-topicos-lda-svd-lsa-nmf-numero-de-topicos-palavras-relevantes
titulo: Modelagem de tópicos: comparar LDA, SVD (LSA) e NMF, escolher o número de tópicos, 5 palavras mais relevantes de cada tópico e 3 tópicos mais relevantes de um documento
assunto: pln-03-topicos-agrupamento-e-embeddings
tipo: lista
questao: Lista 4, questão 1
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 4, questão 1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Ideia:** cada documento é uma mistura de **tópicos**; cada tópico é uma distribuição (ou combinação) de palavras. Fatora-se a matriz documentos × termos $X$ em $X \approx W H$: $W$ (documentos × tópicos) diz quanto de cada tópico há em cada documento; $H$ (tópicos × termos), quanto cada palavra pesa em cada tópico.

**Métodos:**
- **LDA** (alocação latente de Dirichlet): modelo **probabilístico** gerativo; use **contagens** (`CountVectorizer`); tópicos são distribuições de probabilidade;
- **SVD truncado** (LSA, análise semântica latente): decomposição em valores singulares; aceita TF-IDF; os componentes podem ter **pesos negativos**, o que dificulta a interpretação;
- **NMF** (fatoração em matrizes não negativas): $W, H \ge 0$; tópicos costumam ser fáceis de ler; use TF-IDF.

**Número de tópicos** (empírico): rode vários $k$ e compare um critério: **coerência** dos tópicos (as palavras do topo aparecem juntas nos documentos?), **perplexidade** do LDA no teste, **erro de reconstrução** do NMF ou **variância explicada** do SVD (procure o cotovelo).

**Top palavras:** para o tópico $j$, os índices das 5 maiores entradas da linha $H_j$ mapeados no vocabulário. **Top tópicos de um documento:** as 3 maiores entradas da linha de $W$.

```python
from sklearn.decomposition import NMF
nmf = NMF(n_components=k, random_state=0)
w = nmf.fit_transform(x_tfidf)       # documentos × tópicos
h = nmf.components_                  # tópicos × termos
```

**Verificação:** `test_topicos` gera uma base com dois assuntos (esporte e culinária) e confere que NMF e LDA com 2 tópicos separam as palavras dos dois assuntos nas 5 primeiras de cada tópico e que o tópico dominante de cada documento é o assunto dele; no SVD, os documentos projetados também se separam por assunto.
