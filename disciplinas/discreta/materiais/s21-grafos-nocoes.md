---
id: discreta-grafos
titulo: Noções de grafos — grau, teorema do aperto de mãos, isomorfismo, caminhos, conexidade e árvores
assunto: discreta-12-grafos
tipo: material_estudo
resolucao: sim
fonte: Albertson e Hutchinson, Discrete Mathematics with Algorithms, capítulo 5, seções 5.2 e 5.3 (apenas parafraseado por seção; livro protegido)
fontes_catalogo: albertson-hutchinson
autoria: Michael O. Albertson e Joan P. Hutchinson (livro), parafraseado pela equipe TutorON com auxílio de IA, com exemplos próprios
licenca: Protegido por direito autoral; nada do livro foi transcrito nem versionado
publicacao_transcricao: não se aplica: o bloco só parafraseia conceitos por seção, com exemplos próprios; o livro não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Um **grafo** G = (V, E) tem um conjunto de vértices V e um conjunto de arestas E, cada aresta ligando dois vértices. O **grau** deg(v) é o número de arestas que tocam v.

**Teorema do aperto de mãos**: $\sum_{v \in V} \deg(v) = 2|E|$, porque cada aresta é contada uma vez em cada ponta. Consequência: o número de vértices de grau ímpar é sempre par. Ex.: não existe grafo com graus 3, 3, 3 (soma 9, ímpar).

**Grafo completo** $K_r$: r vértices, todos ligados entre si; tem $\frac{r(r-1)}{2}$ arestas (em palavras: r vezes r menos 1, sobre 2). $K_5$ tem 10.

**Isomorfismo**: G e H são isomorfos se existe uma bijeção entre os vértices que preserva as arestas. Para mostrar que **não** são, basta um invariante diferente: número de vértices, de arestas, sequência de graus, número de componentes. Sequências de graus iguais **não** bastam para garantir isomorfismo: dê a bijeção.

**Caminhos e conexidade**: um caminho é uma sequência de vértices ligados por arestas; o grafo é **conexo** se há caminho entre quaisquer dois vértices. As **componentes** são os pedaços conexos maximais.

**Árvores**: grafo conexo sem ciclos. Com V vértices, uma árvore tem exatamente **E = V − 1** arestas, e entre dois vértices há um único caminho. Uma **floresta** é um grafo sem ciclos (cada componente é árvore); com c componentes, E = V − c. Exemplo de aplicação do livro: ligar computadores de uma rede local com o menor número de cabos dá uma árvore.

Grafos eulerianos e outros tópicos ficam em capítulos posteriores do livro; algoritmos de busca e caminho mínimo são aprofundados em PAA e Estruturas de Dados.

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** a soma dos graus = 2|E|, o número de arestas de $K_r$ (r de 1 a 10) e E = V − 1 em árvores aleatórias foram conferidos por código em Python.
