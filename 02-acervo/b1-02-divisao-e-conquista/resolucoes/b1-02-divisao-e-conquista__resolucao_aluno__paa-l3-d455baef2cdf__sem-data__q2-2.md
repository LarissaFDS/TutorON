# d455baef2cdf-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 3

Versão derivada corrigida por agente; original SHA-256: 00b9d2989348b9118b67ca93985df51b27babd645e956526cce79d8bc4b8289e. Não é aprovação do professor.

Ordenar times de um torneio sem empates de modo que cada time vença o próximo.
Represente cada time por um vértice; para cada par existe exatamente uma aresta dirigida do vencedor ao perdedor. Construa uma lista por inserção: para um novo time x, percorra a lista até o primeiro time y que x venceu; insira x imediatamente antes de y. Se x perdeu para todos os times da lista, insira no fim.
Invariante: cada elemento da lista vence o seguinte. Antes da posição de inserção, todos venceram x; o primeiro time encontrado perdeu para x. Essas são as únicas duas adjacências novas, logo o invariante é preservado. Obtém-se um caminho hamiltoniano do torneio em O(n^2) consultas aos resultados e O(n) memória para a lista, além da representação dos resultados. Listar os pares vencedor/perdedor das partidas não satisfaz a tarefa.
