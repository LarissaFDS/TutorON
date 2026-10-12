# 5ee2f9c93b11-qincerta-1

Fonte: materiais\Disponiveis\RAG PAA\gabaritoprova.webp | página(s): 1

```markdown
# Questão 2
O algoritmo X apresenta o maior elemento em um vetor. Fazemos a prova de sua raciocínio utilizando indução forte no tamanho do vetor (n).

Teorema: O algoritmo X determina corretamente o maior elemento de um vetor.

Caso base: Se tivermos um vetor de tamanho n = 1, então início = fim e o algoritmo entra na linha 3, ordenando o 1º e único elemento de A.

Hipótese de indução: O algoritmo X determina corretamente o maior elemento de um vetor de tamanho k ≤ n.

Passo analítico: Prova que X funciona para um vetor de tamanho k + 1. Para um vetor de tamanho k + 1, o algoritmo divide-o em duas partes a partir do cálculo do seu índice médio, não variável mais. Sendo assim, as duas partes do vetor são unidas em duas chamadas recursivas à X. Nesta forma, X calcula o maior valor em cada um dos subvetores A[1...n/2 + (fim-início)/2] e A[(n/2 + (fim-início)/2) + 1...n], que são, portanto, menores que k. Assim, portanto, segundo a hipótese de indução, as chamadas recursivas à X funcionam corretamente. Na linha 8, o algoritmo retornará o maior dentre os dois valores retornados em a e b.

Afirmar, está provado.

# Questão 3
3.1 Segundo a definição formal, T(n) é O(f(n)), sendo T(n) e f(n) funções dos inteiros nos reais, se existem constantes c e no, pertencentes aos reais, tal que,
\[ O(f(n)) = \{T(n) ≤ c·f(n) | n ≥ no\} \]

Portanto, uma função T(n) pertence ao conjunto O(f(n)) quando para qualquer valor real de n maior que no, T(n) é no máximo igual a c·f(n).
```
