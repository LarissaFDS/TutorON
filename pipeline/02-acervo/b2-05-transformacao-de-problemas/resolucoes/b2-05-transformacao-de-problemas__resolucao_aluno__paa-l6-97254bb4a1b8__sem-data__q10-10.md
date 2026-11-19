# 97254bb4a1b8-q10-10

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 7

Versão derivada corrigida por agente; original SHA-256: 694562f74893e510581264d50f19a8619648a0ffbffc63579aa2bcd43a47c1f0. Não é aprovação do professor.

Clique máxima como programa linear inteiro binário.
Para cada vértice i, variável x_i em {0,1} indica participação na clique. Maximize sum_i x_i. Para cada par distinto não adjacente {i,j}, imponha x_i+x_j<=1. Não há restrição desse tipo para pares adjacentes. Todo conjunto escolhido é clique e qualquer clique satisfaz o modelo.
A restrição original h_j*x_j+sum_{i não vizinho de j}x_i<=1 é incorreta quando h_j>1: impede escolher o próprio j. Uma forma agregada equivalente válida é h_j*x_j+sum_{i não vizinho de j}x_i<=h_j, com h_j igual à quantidade de não vizinhos distintos e sem autoarestas; para h_j=0 a restrição é dispensável.
O modelo por pares é mais simples e tem O(n^2) restrições. Clique de G corresponde a conjunto independente no grafo complementar, não necessariamente no próprio G.
