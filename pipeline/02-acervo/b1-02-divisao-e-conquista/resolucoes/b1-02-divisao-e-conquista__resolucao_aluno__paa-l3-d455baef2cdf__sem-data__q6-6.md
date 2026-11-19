# d455baef2cdf-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 5

Versão derivada corrigida por agente; original SHA-256: cd8a29c63b4a5795b11f57f8a3876a4f7dc96e018f827c951939db2e8a320621. Não é aprovação do professor.

Ponto fixo A[i]=i em vetor ordenado de inteiros distintos, índices de 1 a n.
Faça busca binária: m=floor((l+r)/2). Se A[m]=m, retorne m. Se A[m]<m, procure somente à direita; se A[m]>m, procure somente à esquerda. Se o intervalo ficar vazio, não há ponto fixo.
Como os valores são inteiros estritamente crescentes, para i<m temos A[i]<=A[m]-(m-i), e para i>m temos A[i]>=A[m]+(i-m). Portanto A[m]<m elimina todos os índices à esquerda; A[m]>m elimina todos à direita. Tempo O(log n), memória O(1) na versão iterativa. Valores repetidos ou números reais eliminam essa justificativa.
