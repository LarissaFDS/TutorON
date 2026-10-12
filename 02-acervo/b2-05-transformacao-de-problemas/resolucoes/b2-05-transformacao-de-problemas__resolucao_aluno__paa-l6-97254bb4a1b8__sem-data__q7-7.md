# 97254bb4a1b8-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 5

7. Leia o artigo da wikipedia sobre o puzzle Kakuro https://en.wikipedia.org/wiki/Kakuro
e modele exemplo dado utilizando Programa¸c˜ao por Restri¸c˜ao.

Solu¸c˜ao: Neste caso, modelaremos Kakuro como um par < K, P >, no qual est˜ao
representadas as vari´aveis:
- K: As c´elulas do Kakuro
- P: O conjunto das dicas, definido como um par < K′, n >,
onde K’ ´e um subconjunto de K (c´elulas) e n ´e um inteiro positivo que, para o
subconjunto K’, representa a soma dos elementos nas c´elulas de K’.

Vari´aveis:

Xk|∀k ∈K : Xk ∈[1, 9]

Dom´ınio:

[1, 9]

Restri¸c˜oes:

-∀
< K′, n >
∈P : diferentes entre si({Xk | k ∈K′})

X

-∀
< K′, n >
∈P :

Xk = n

k ∈K′

Ou seja, os elementos de K’ devem ser diferentes entre si e a soma dos elementos de
K’ tem que ser igual ao inteiro n.
