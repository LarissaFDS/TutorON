# 7b4da6a8adf7-q5-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 7, 8, 9

5. Prove a corretude do algoritmo bubblesort:


[OCR parcial do recorte p7-fig1.png; conferir símbolos na imagem]
1: procedure ALGORITMO BUBBLESORT(vetor A[1,...,n])
2:
fori←n-1→1do
3:
for j ← 0 → i - 1 do
4:
if A[j] < A[j +1] then
5:
troca(A[j],A[j+1])]
6:
endif
7:
end for
8:
end for
9: end procedure


Solu¸c˜ao:

Para provar a corretude do algoritmo Bubblesort ´e necess´ario provar os dois invari-
antes das estruturas de repeti¸c˜ao presentes no mesmo. Primeiro, o la¸co interno e,
por fim, a propriedade do primeiro la¸co servir´a de base para a prova do la¸co externo.
Assim, dando continuidade para a prova:

Invariante do la¸co interno:

Teorema: Depois da itera¸c˜ao j do loop interno, o menor elemento do vetor A[0, 1, ..., j]
estar´a na posi¸c˜ao j .

A prova ser´a feita por indu¸c˜ao:

(Inicializa¸c˜ao)

Passo Base (j=0)

Neste caso, o passo base ocorre antes da itera¸c˜ao do loop, pois no caso onde j=0,
temos o vetor A[0, ..., 0], constitu´ıdo apenas pelo elemento a0, desse modo, ele ´e o
menor elemento do vetor e, portanto, P(j=0) ´e verdadeiro.

(Manuten¸c˜ao)

Hip´otese da Indu¸c˜ao:

Como hip´otese indutiva, vamos assumir primeiramente que ap´os a itera¸c˜ao j, o menor
elemento do vetor esteja na posi¸c˜ao j.

Passo Indutivo (j ≥0):

Assim, para concluir, ´e necess´ario mostrar que ap´os a itera¸c˜ao j+1, o menor elemento
do vetor A[0, 1, ..., j, j + 1] estar´a na posi¸c˜ao j+1.

Sabemos pela hip´otese de indu¸c˜ao que ap´os a itera¸c˜ao j, o elemento da posi¸c˜ao j (aj)
´e o menor elemento. Sendo assim, na itera¸c˜ao j+1, ou o menor elemento no vetor
A[0, 1, ..., j, j + 1] ´e aj ou ´e aj+1.

Page viiDe todo modo, pela linha (4) o algoritmo verifica e garante que se aj < aj+1, ocorra
a troca dos mesmos, de modo a preservar o menor elemento na posi¸c˜ao j+1 e, assim,
fica assegurado que se h´a j+1 posi¸c˜oes no vetor A[0, 1, ..., j, j + 1], ent˜ao, ap´os j+1
itera¸c˜oes, o menor elemento estar´a na posi¸c˜ao j+1.

(T´ermino)

Portanto, por indu¸c˜ao, ap´os j itera¸c˜oes o menor elemento encontra-se na posi¸c˜ao
j. Em outras palavras, ao final da execu¸c˜ao do la¸co de repeti¸c˜ao, a posi¸c˜ao j ser´a
ocupada pelo menor elemento do vetor A[0, 1, ..., j].

Invariante do la¸co externo:

Teorema: Ap´os a itera¸c˜ao “i” do loop externo, os “n −i” menores elementos do
vetor A[0, 1, ..., n −1] estar˜ao em ordem decrescente nas posi¸c˜oes i at´e n-1, ocupando
portanto, o vetor A[i, ..., n −1].

(Inicializa¸c˜ao)

De fato, na itera¸c˜ao n−1 do loop externo os 1 menores elementos ocupam as posi¸c˜oes
do vetor A[n −1, ..., n −1], que s´o possui um elemento nas posi¸c˜oes previamente
citadas (n −1 at´e n −1) e consequentemente est´a em ordem decrescente. Portanto,
o invariante ´e v´alido.

(Manuten¸c˜ao)

O invariante de la¸co ´e valido para a inicializa¸c˜ao, ou primeira itera¸c˜ao, pois de fato,
s´o h´a um elemento, consequentemente em ordem decrescente, ocupando a posi¸cao
n-1. Logo, resta analisar as pr´oximas “i” itera¸c˜oes.

Sendo assim, sabendo que o la¸co interno garante que o menor elemento do vetor
A[0, ..., i] estar´a na posi¸c˜ao i e que ao fim do la¸co externo o i ´e decrementado para
i −1. Analogamente, na pr´oxima itera¸c˜ao o subvetor A[0, ..., i −1], ter´a seu menor
valor posicionado em A[i −1] e assim sucessivamente. Desse modo, ´e f´acil observar
que ap´os estas itera¸c˜oes, a seguinte proposi¸c˜ao ´e verdadeira:

ai−1 ≥ai

Logo, ´e poss´ıvel concluir tamb´em que os elementos comparados at´e ent˜ao estar˜ao,
com base na linha (4), em ordem decrescente, mantendo a propriedade de ordena¸c˜ao
durante a execu¸c˜ao do la¸co de repeti¸c˜ao.

(T´ermino)

Ap´os o t´ermino do la¸co de repeti¸c˜ao externo, onde i=1, ´e importante lembrar que o
la¸co de repeti¸c˜ao interno foi executado, analisando os elementos do vetor A[0, ..i], logo
A[0, ..., 1], e consequentemente posicionando o elemento de menor valor na posi¸c˜ao
1 do vetor. Portanto, considerando que a inicializa¸c˜ao e manuten¸c˜ao foram v´alidas,
todos os n −i menores elementos do vetor A[0, ..., n −1] est˜ao nas posi¸c˜oes 1 at´e
n −1, consequentemente o elemento a0 ´e o maior elemento do vetor A[0, ..., n −1].

Page viiiPortanto, a seguinte proposi¸c˜ao est´a correta:

a0 ≥a1 ≥... ≥an−2 ≥an−1

Consequentemente, os elementos do vetor A[0, ..., n −1], est˜ao ordenados de maneira
decrescente.

■
