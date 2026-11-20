# 97254bb4a1b8-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 1

Versão derivada corrigida por agente; original SHA-256: b7f7d5a0e358009fbb2c6d4260305c9692f8b118e3397cb09d2ab18d17592dcc. Não é aprovação do professor.

Número faltante entre 1 e n, ouvindo n-1 inteiros distintos válidos.
Inicialize faltante=n(n+1)/2 e subtraia cada número ouvido. Ao final, resta exatamente o omitido. São O(n) operações e O(1) palavras de memória no modelo RAM; representar os acumuladores exige O(log n) bits. Valide as hipóteses de intervalo e distinção se a entrada não for garantida.
Em tipos inteiros de tamanho fixo, a multiplicação n(n+1) pode transbordar mesmo quando a soma final cabe: divida um dos fatores pares por 2 antes de multiplicar e use um tipo suficientemente largo. Uma alternativa é XOR de 1..n combinado com XOR dos números recebidos; todos os presentes cancelam, deixando o faltante. XOR evita a soma intermediária, mas ainda exige um tipo capaz de representar n.
