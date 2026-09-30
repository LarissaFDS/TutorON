# c02

Fonte: materiais\c02_gabarito_algoritmo_x_nota_2.md | página(s): não informada na transcrição

Questão 2. O algoritmo X encontra o maior elemento em um vetor. Faremos a prova de sua
corretude utilizando indução forte no tamanho do vetor (n).

Teorema: O algoritmo X retorna corretamente o maior elemento de um vetor.

Caso base: se tivermos um vetor de tamanho n = 1, então inicio = fim e o algoritmo entra
na linha 3, retornando o 1º e único elemento de A.

Hipótese de indução: O algoritmo X determina corretamente o maior elemento de um vetor
de tamanho k ≤ n.

Passo indutivo: Provaremos que X funciona para um vetor de tamanho n + 1.
Para um vetor de tamanho n + 1, o algoritmo divide-o em duas partes a partir do cálculo do
seu índice médio na variável meio. Sendo assim, as duas partes do vetor são inseridas em
duas chamadas recursivas a X. Dessa forma, X calcula o maior valor em cada um dos
subarranjos A[1 .. inicio + (fim − inicio)/2] e A[(inicio + (fim − inicio)/2) + 1 .. n], que são,
portanto, menores do que k.
Assim, segundo a hipótese de indução, as chamadas recursivas a X funcionarão corretamente
e, na linha 8, o algoritmo retornará o maior dentre os dois valores retornados em a e b.
Assim, está provado.

[Correção do professor: ✓ — 2,0]
