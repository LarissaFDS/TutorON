# 1a81ca283132-q4-4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 4

Versão derivada corrigida por agente; original SHA-256: 0891ccf6d17d3f6b8a0b19533d10ee42f8cde20e1dbe6956093c645ef3144d25. Não é aprovação do professor.

Subsequência contígua de soma máxima com subsequência vazia permitida (Lista 5).
Defina fim[0]=0 e fim[j]=max(0,fim[j-1]+a_j). Defina melhor[0]=0 e melhor[j]=max(melhor[j-1],fim[j]). O resultado é melhor[n]. É possível manter apenas fim e melhor em O(1) de memória; o tempo é O(n). Guarde índices de início/fim se for necessário retornar a subsequência.
Para [5,15,-30,10,-5,40,10], a resposta é [10,-5,40,10] com soma 55. Para [-5,-2,-8], a resposta é a subsequência vazia, soma 0. Inicializar o melhor valor em -infinito e exigir um elemento muda a convenção da fonte e é inadequado aqui.
