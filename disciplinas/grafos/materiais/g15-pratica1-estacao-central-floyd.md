---
id: grafos-pratica1-estacao-central-floyd
titulo: Prática 1, cenário 1 — estação central de metrô: Floyd-Warshall em grafo não direcionado com 12 vértices e 22 arestas; vértice com menor soma de distâncias
assunto: grafos-03-percursos-caminhos
tipo: lista
questao: cenário 1
resolucao: sim
fonte: Prática 1 - Grafos (caminho mínimo), Teoria dos Grafos ECOM033, IC-UFAL, com os arquivos de entrada graph1.txt, graph2.txt e grid_example.txt
curso: Engenharia de Computação (UFAL), Teoria dos Grafos (ECOM033)
fontes_catalogo: ufal-ecom033-pratica1-caminho-minimo
autoria: Enunciado e arquivos de entrada: Prática 1 da disciplina ECOM033 (IC-UFAL; professor não identificado no arquivo), parafraseados pela equipe TutorON; resolução da equipe TutorON
licenca: Não declarada (atividade da disciplina); paráfrase, PDF e arquivos de entrada não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Prática 1 de Teoria dos Grafos (ECOM033, IC-UFAL), cenário 1. Enunciado parafraseado. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor; a prática pede que o aluno implemente e compare com o pseudocódigo da aula, então aqui ficam a escolha do algoritmo, o raciocínio e os números para conferir.

**Problema.** Grafo não direcionado com pesos (estações e trechos de metrô), lido de um arquivo com `<vértices> <arestas>` na primeira linha e `<u> <v> <custo>` nas outras. A estação central é o vértice com **menor soma das distâncias mínimas** a todos os outros. A saída pede o vértice, o vetor de distâncias dele, o vértice mais distante e a matriz de distâncias de todos os candidatos.

**Algoritmo: Floyd-Warshall.** O problema pede distâncias entre **todos os pares** (a matriz inteira), e os pesos são positivos. Floyd-Warshall faz isso em O(n³) com três laços: para cada intermediário k, `d[i][j] = min(d[i][j], d[i][k] + d[k][j])`. Dijkstra rodado de cada vértice também serviria; Bellman-Ford é desnecessário, porque não há peso negativo.

**Com o arquivo de exemplo** (12 vértices numerados de 1 a 12, 22 arestas): a menor soma é a do **vértice 9 (219)**, seguido do 6 (224). Distâncias de 9 aos vértices 1 a 12: 39, 22, 37, 16, 19, 7, 17, 10, 0, 12, 15, 25. O mais distante é o **vértice 1, a 39**. Aqui o 9 também é o vértice de menor excentricidade (39), mas os critérios podem divergir: o enunciado usa a soma.

Cuidados: inicializar `d[i][i] = 0` e ∞ onde não há aresta; como o grafo é não direcionado, cada linha do arquivo vale nos dois sentidos; o arquivo numera os vértices a partir de 1.

**Verificação:** `test_pratica1_estacao_central_floyd` recalcula com `networkx.floyd_warshall` e com um Floyd-Warshall próprio.
