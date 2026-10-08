# 1a81ca283132-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 6, 7

Versão derivada corrigida por agente; original SHA-256: fbb18de37435d6a856784e02d56e436daa3ddeec4a966c0bb7feee093b5eee84. Não é aprovação do professor.

Cobertura mínima de vértices de uma árvore.
Uma cobertura S satisfaz S subseteq V e contém uma extremidade de cada aresta. Enraíze a árvore. Para cada v, incl[v]=1+sum(min(incl[u],excl[u])) sobre seus filhos u; excl[v]=sum(incl[u]). Para folhas, incl=1 e excl=0. A resposta é min(incl[raiz],excl[raiz]).
Se v não for escolhido, todos os filhos precisam ser escolhidos; se v for escolhido, cada filho pode usar sua melhor opção. Tempo O(|V|), memória O(|V|). A figura com vértices nomeados ainda exige conferência; esta nota não inventa suas arestas.
