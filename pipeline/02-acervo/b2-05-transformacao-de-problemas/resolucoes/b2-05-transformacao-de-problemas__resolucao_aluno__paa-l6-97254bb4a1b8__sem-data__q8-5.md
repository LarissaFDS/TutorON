# 97254bb4a1b8-q8-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 5, 6

8. O problema das 8 DAMAS consistem em colocar 8 damas em um tabuleiro
de xadrez. Modele este problema utilizando Programa¸c˜ao por Restri¸c˜ao.

Page vSolu¸c˜ao:

Vari´aveis:

1, 2, 3, ..., 8 linhas de um vetor A

O Dom´ınio de cada vari´avel ´e:

1, 2, 3, ..., 8 (n´umeros de 1 a 8)

O valor de cada vari´avel (A[j]) indica a coluna onde uma das dama ´e alocada e a
posi¸c˜ao desta vari´avel no vetor (j) indica a linha que a dama ´e alocada, dessa forma
n˜ao haver´a duas damas na mesma linha. Para garantir que n˜ao haver´a duas damas
na mesma coluna ou na mesma diagonal, aplicaremos as seguintes restri¸c˜oes:

Restri¸c˜oes:

• ∀i, j ∈[1, 2, 3, ..., 8], A[i]̸ = A[j];

Garante que haver´a apenas uma dama em cada coluna;

• ∀i, j ∈[1, 2, 3, ..., 8], A[i] + i̸ = A[j] + j;

• ∀i, j ∈[1, 2, 3, ..., 8], A[i] −i̸ = A[j] −j;

Garantem que haver´a apenas uma dama em cada diagonal.
