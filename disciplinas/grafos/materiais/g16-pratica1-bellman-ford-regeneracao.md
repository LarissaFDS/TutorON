---
id: grafos-pratica1-bellman-ford-regeneracao
titulo: Prática 1, cenário 2 — carro elétrico com regeneração: pesos negativos, Bellman-Ford de 0 a 6 em digrafo de 7 vértices; caminho 0 → 3 → 5 → 6 com custo 8
assunto: grafos-03-percursos-caminhos
tipo: lista
questao: cenário 2
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
Prática 1 de Teoria dos Grafos (ECOM033, IC-UFAL), cenário 2. Enunciado parafraseado. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor; a prática pede que o aluno implemente e compare com o pseudocódigo da aula, então aqui ficam a escolha do algoritmo, o raciocínio e os números para conferir.

**Problema.** Digrafo de energia (Wh): subidas e arranques consomem (peso positivo), descidas com frenagem regenerativa devolvem (peso negativo). O grafo é direcionado porque a energia não é simétrica por sentido. Pede-se o caminho de menor energia líquida do vértice 0 ao 6 e o custo total.

**Algoritmo: Bellman-Ford.** Com pesos negativos, **Dijkstra não serve**: ele fecha um vértice assumindo que nenhum caminho posterior pode melhorá-lo, o que um peso negativo desmente. Bellman-Ford relaxa todas as arestas n − 1 vezes (O(n·m)) e, numa n-ésima rodada, detecta ciclo negativo (se ainda houver melhora, o mínimo não existe). Floyd-Warshall também aceita pesos negativos, mas calcularia todos os pares sem necessidade.

**Com o arquivo de exemplo** (7 vértices, 14 arestas): não há ciclo negativo, e o caminho mínimo é **0 → 3 → 5 → 6**, custo −8 + 11 + 5 = **8 Wh**. Comparação: 0 → 1 → 4 → 6 custa 25 − 10 + 8 = 23, e 0 → 2 → 3 → 5 → 6 custa 12 − 5 + 11 + 5 = 23. O trecho regenerativo 0 → 3 (−8) compensa o 3 → 5 caro.

Cuidados: guardar o predecessor de cada vértice para reconstruir o caminho; o arquivo de exemplo usa TAB como separador.

**Verificação:** `test_pratica1_bellman_ford_regeneracao` confere com `networkx.bellman_ford_path`, com um Bellman-Ford próprio e enumerando todos os caminhos simples de 0 a 6.
