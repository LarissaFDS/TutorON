# 97254bb4a1b8-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 4, 5

6.
Mostre que o problema do troco (Exerc´ıcio ??) pode ser formulado como
um programa linear inteiro. Minimize o n´umero de moedas.

Solu¸c˜ao: O problema do troco no qual dado um estoque ilimitado de moedas de
valores x1, x2, ..., xn, queremos dar um troco de v usando no m´aximo k moedas. Logo,
o problema pode ser modelado como um programa linear inteiro e isso pode ser visto
a seguir:

Page ivConsiderando um sistema finito m1 < m2 < ... < mn de inteiros positivos que
representem n tipos de moedas e um inteiro positivo, desejamos determinar os inteiros
positivos xi | 1 ≤i ≤t e, que minimizam a seguinte equa¸c˜ao:

n
X

xi
(1)

i=1

Sujeita `as as seguintes restri¸c˜oes:

n
X

n
X

x =

xici

xi ≤k
(2)

i=1

i=1

Tendo em vista que uma representa¸c˜ao ´e a sequˆencia dos coeficientes x + 1, ..., xn,
podemos consider´a-la ´otima se ela ´e de tamanho m´ınimo.
