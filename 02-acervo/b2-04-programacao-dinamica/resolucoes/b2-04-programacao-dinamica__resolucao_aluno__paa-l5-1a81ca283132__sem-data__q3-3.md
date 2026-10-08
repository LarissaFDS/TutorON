# 1a81ca283132-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 2, 3

Versão derivada corrigida por agente; original SHA-256: cdd6b9946b202b3084c2c6bcfffba1501a26c6077f6f2b9052c4f7a130387f61. Não é aprovação do professor.

Caminho mais longo em um DAG, medido em número de arestas.
Faça uma ordenação topológica. Inicialize d[v]=0 para todos os vértices se o início puder ser qualquer vértice. Processe u nessa ordem e relaxe cada aresta u->v: d[v]=max(d[v],d[u]+1). O resultado é max(d). Para origem fixa s, inicialize d[s]=0 e os demais em -infinito.
A ordem topológica assegura que todos os predecessores já tenham sido processados. Tempo O(|V|+|E|), memória O(|V|). O método depende da ausência de ciclos.
