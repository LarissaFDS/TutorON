# f38bb8142136-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L7.pdf | página(s): 8

Versão derivada corrigida por agente; original SHA-256: 8d7464cb75bb1af15754d043ad7d931535f798524b1341af0bf4587c3434baee. Não é aprovação do professor.

Árvore geradora com grau máximo k, para cada constante k>=2.
A versão de decisão pergunta se tal árvore existe. Ela pertence a NP: verificar conectividade, ausência de ciclos, cobertura dos vértices e os graus é polinomial.
Para k=2, uma árvore de grau máximo 2 é um caminho, logo o problema equivale a CAMINHO HAMILTONIANO.
Para k>2, a partir de G adicione exatamente k-2 folhas privadas a cada vértice original. Todas as arestas dessas folhas são obrigatórias em qualquer árvore geradora. Se a árvore nova tiver grau máximo k, removê-las deixa uma árvore geradora de G com grau máximo 2, isto é, um caminho hamiltoniano. Reciprocamente, um caminho hamiltoniano de G mais todas essas folhas tem grau máximo k. A construção é polinomial para k fixo.
Portanto a decisão é NP-completa e a tarefa de encontrar tal árvore é NP-difícil. A resolução original alternava k-1 e k-2 folhas; o valor correto é k-2.
