# 70d6475b28bf-q10-10

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 14, 15

10.
No problema do BIN PACKING, a entrada consiste em: n itens com tama-
nhos s1, s2, ..., sn em que si ∈[0, 1]. O objetivo ´e encontrar o menor n´umero de
“bins” (caixas) unit´arias para armazenar os n itens. O algoritmo First Fit
consiste em:


[OCR parcial do recorte p14-fig1.png; conferir símbolos na imagem]
1: procedure ALGORITMo FIRsT FrT(vetor s[1,.., n])
2:
fori+1-ndo
3:
Coloque o item i no bin de menor indice que tenha espaco
dis
ponivel ≥ s;
end for
5:endprocedure


Mostre que o algoritmo ´e 2-aproximado. Dica: O FF n˜ao deixa, ao final, dois
bins com espa¸co utilizado ≤0, 5

Solu¸c˜ao:

Suponha que o algoritmo First-Fit utilize m caixas com m = {W1, W2, ..., Wm}.
Ent˜ao, ao menos (m −1) caixas est˜ao mais do que meio cheias. Isto ´e f´acil ver, pois
se h´a 2 caixas cuja capacidade Wi <
Wimax

2
e
Wj <
Wjmax

2
, n˜ao supera metade

Page xivda capacidade m´axima das caixas correspondentes, ent˜ao, pelo algoritmo First-Fit,
como Wimax = Wjmax, os itens poderiam ser tirados da segunda caixa e colocados
na primeira utilizando o First-Fit pois haveria capacidade, restando apenas 1 caixa
(”m −1”) cuja capacidade alocada ´e, agora, maior que a metade da capacidade
m´axima.
Sendo assim, supondo que o algoritmo First-Fit utiliza m caixas, ent˜ao no m´ınimo
m −1 caixas utilizam mais do que metade da capacidade m´axima. Portanto:

i=n
X

OPT ≥

si > m −1

2

i=1

OPT ≥m −1

2
2 · OPT ≥m −1

∴2 · OPT ≥m

Assim, o bin-packing com estrat´egia First-Fit ´e dito 2-aproximado, pois no pior dos
casos, o custo para construir a solu¸c˜ao ´e 2 vezes o custo da solu¸c˜ao ´otima.

Page xv
