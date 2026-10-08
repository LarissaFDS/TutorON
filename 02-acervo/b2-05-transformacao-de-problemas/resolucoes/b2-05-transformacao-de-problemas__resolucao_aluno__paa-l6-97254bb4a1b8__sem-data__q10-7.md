# 97254bb4a1b8-q10-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 7

10. Modele o problema da CLIQUE M´AXIMA utilizando programa¸c˜ao linear
inteira.

Solu¸c˜ao: Como os problemas da CLIQUE M´AXIMA e CONJUNTO INDEPEN-
DENTE M´AXIMO s˜ao complementares, podemos definir um problema em termos
do outro. Neste sentido, seja G=(V,E) um grafo simples, onde V = v1, v2, ..., vn.
Seja ∆uma clique no grafo G e U o conjunto de v´ertices de ∆. Al´em disso, dada a
existˆencia da vari´avel bin´aria xi, onde i ∈{1, 2, . . . , n} tal que xi ∈{0, 1}

(

xi =

0, se vi /∈U
1, se vi ∈U

Definimos tamb´em a nota¸c˜ao NVj, que denota o conjunto dos v´ertices n˜ao-vizinhos
ao v´ertice j em G. De modo que vj /∈NVj, assim a cardinalidade de NVj pode ser
definida por hj da seguinte maneira:

(

hj =

|NVj|, se NVj̸ = ∅
1, se NVj = 0

Desse modo, o programa linear ´e dado pelas seguintes equa¸c˜oes e restri¸c˜oes:

i=n
X

m´aximizar :

xi

i=1

X

xi ≤1, para cada 1 ≤j ≤n

sujeita `a :
hjxj +

i ∈NVj

Logo, a solu¸c˜ao do programa linear resolve o problema da clique m´axima.

Page vii
