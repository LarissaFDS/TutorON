---
id: pln-projecao-multidimensional-t-sne-umap-visualizar-grupos-tempo-e-qualidade
titulo: Projeção multidimensional para visualização: t-SNE e UMAP, cores pelos grupos do k-means, comparar tempo e qualidade visual
assunto: pln-03-topicos-agrupamento-e-embeddings
tipo: lista
questao: Lista 4, questão 3
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 4, questão 3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Objetivo:** levar os dados de alta dimensão para **2D** e ver se os grupos do k-means aparecem separados.

**t-SNE:** converte distâncias em probabilidades de vizinhança (gaussiana no espaço original, $t$ de Student no plano) e minimiza a divergência de Kullback-Leibler entre elas. Preserva bem a **vizinhança local**; distâncias entre grupos e tamanhos de grupos no gráfico **não** têm significado confiável. Parâmetro principal: **perplexidade** (número efetivo de vizinhos, tipicamente 5 a 50). Custo alto em bases grandes; resultado muda com a semente.

**UMAP:** constrói um grafo de vizinhos e otimiza um layout que preserve sua estrutura; em geral é **mais rápido** que o t-SNE e preserva um pouco mais da estrutura global. Parâmetros: `n_neighbors` e `min_dist`. Biblioteca `umap-learn`.

**Como comparar:**
- **tempo:** meça com `time.perf_counter()` nas mesmas entradas;
- **qualidade visual:** grupos do k-means separados? pontos de cores diferentes misturados?
- **numérica:** `sklearn.manifold.trustworthiness` (quanto os vizinhos no plano eram vizinhos no original, de 0 a 1) e a silhueta dos grupos no plano.

Fixe a semente nos dois métodos e não tire conclusões de distâncias entre grupos no t-SNE.

```python
from sklearn.manifold import TSNE, trustworthiness
emb = TSNE(n_components=2, perplexity=30, random_state=0).fit_transform(xp)
print(trustworthiness(xp, emb, n_neighbors=5))
```

**Verificação:** `test_tsne` projeta com t-SNE (semente fixa) um conjunto com 3 grupos em 20 dimensões e confere que a confiabilidade passa de 0,9 e que os grupos continuam separados no plano (silhueta acima de 0,5). O UMAP não roda nos testes porque a biblioteca não está instalada.
