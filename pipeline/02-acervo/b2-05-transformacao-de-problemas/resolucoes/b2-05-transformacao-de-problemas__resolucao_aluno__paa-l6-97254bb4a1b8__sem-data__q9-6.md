# 97254bb4a1b8-q9-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 6, 7

9. Modele o problema da MOCHILA utilizando programa¸c˜ao linear inteira.

Solu¸c˜ao:
Considerando p como a quantidade de itens, C como a capacidade m´axima da mo-
chila, xi como a optatividade pelo item i, pi como o peso do item i e vi o valor de
utilidade do item i.

VARI´AVEIS:

- i ∈1, 2, ..., p
- pi ∈N
- xi ∈{0, 1}
- vi ∈R
- C ∈N

FUNC¸ ˜AO OBJETIVO:

i=p
X

maximizar :

(vi · xi)

i=1

i=p
X

sujeito `a :

(pi · xi) ≤C

i=1

Page viDeseja-se, portanto, maximizar o valor dos itens recolhidos na mochila, de modo
que o peso de cada item e disponibilidade dos mesmos esteja sujeita `a restri¸c˜ao da
capacidade da mochila.
