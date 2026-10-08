# 1a81ca283132-q10-10

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 10

Versão derivada corrigida por agente; original SHA-256: 6e6260e16d1f596e5310228ede7d2eecc2f085510a735103320e9704c0e98ab0. Não é aprovação do professor.

Caminho simples máximo entre s e t em grafo geral.
Use DP por subconjuntos: D[S,v] é o maior comprimento/peso de um caminho iniciado em s, com conjunto de vértices visitados exatamente S, terminado em v. Inicialize D[{s},s]=0 e os demais em -infinito. Para cada aresta v->w com w fora de S, atualize D[S union {w},w]=max(D[S union {w},w],D[S,v]+peso(v,w)). A resposta é max(D[S,t]) sobre S; se todos forem -infinito, não existe caminho.
Tempo O(2^n n^2) em representação densa e memória O(2^n n). Trocar min por max no algoritmo de Floyd não impõe a condição de caminho simples: pode combinar trechos que repetem vértices. Em DAG existe uma solução linear por ordenação topológica, mas essa hipótese não está no enunciado geral. Esta nota substitui a alegação polinomial incorreta da resolução.
