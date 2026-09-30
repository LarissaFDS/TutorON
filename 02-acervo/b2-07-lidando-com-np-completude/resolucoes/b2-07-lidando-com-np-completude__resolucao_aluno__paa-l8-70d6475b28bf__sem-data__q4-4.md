# 70d6475b28bf-q4-4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 7, 8

4. De forma similar `a quest˜ao anterior (responda as perguntas!), projete um
algoritmo branch-and-bound para o problema da COBERTURA DE CON-
JUNTO.

Solu¸c˜ao: Considere o grafo G=(V,E). O algoritmo pode ser pensado como uma
busca em profundidade em uma ´arvore, na qual o mesmo busca pela solu¸c˜ao ´otima
recursivamente criando os galhos para um v´ertice e a partir do mesmo criando dois
v´ertices at´e que n˜ao haja mais v´ertices em G. Ou seja, quando o algoritmo ramifica
um v´ertice, ele divide o espa¸co das solu¸c˜oes em um conjunto de subconjuntos menores
calculando assim os limitantes superiores e inferiores relativos para cada n´o, reduzindo
assim o espa¸co de busca.
A entrada para o algoritmo ´e um grafo G, um limitante superior UpperB e uma
solu¸c˜ao candidata S que representa uma cobertura de v´ertices parcial em constru¸c˜ao.
O limitante superior ´e uma superestima¸c˜ao do tamanho da cobertura m´ınima de
v´ertices do subgrafo e pode ser obtido calculando o tamanho da cobertura m´ınima
de v´ertices encontrada at´e o momento.
Quando o tamanho de S (solu¸c˜ao candidata atual da cobertura de v´ertices) somado
ao limitante inferior do subgrafo se tornar maior ou igual ao limitante superior, a
poda ´e ent˜ao realizada na ´arvore de busca e o limitante superior UpperB que ´e o
tamanho da cobertura m´ınima de v´ertices ´e retornado.
Para calcular o limitante inferior 3 m´etodos podem ser utilizados clique bound, de-
gree bound, sat bound.

Page vii• clique bound: Faz uma decomposi¸c˜ao do grafo em um conjunto de cliques dis-
juntas C1, C2, ..., Cr e soma os tamanhos das cliques, de modo que o limitante
inferior ´e:

i=r
X

(|Ci| −1)

cliquebound =

i=1

• degree bound: Seleciona o v´ertice com maior grau, nomeando-o v′
1 e atualiza o
grau dos outros v´ertices, seleciona agora o v´ertice de maior grau e o nomeia v′

2
e assim sucessivamente. Busca-se ent˜ao um v´ertice v′

i tal que

d(v′

1) + d(v′
2) + · · · + d(v′
i) ≥|E|

d(v′

1) + d(v′
2) + · · · + d(v′
i−1) < |E|

Assim o limitante inferior pode ser dado por:

i+1 ∈H

degreebound = ⌊i +
|E′|
d(v′

i + 1)⌋,
v′

onde G\{v′

1, v′
2, ..., v′
i} = (V ′, E′)

• sat bound: Reduz o grafo G = (V,E) a uma instˆancia MaxSAT e se G pode ser
particionado em k cliques disjuntas e existem s subconjuntos inconsistentes na
instˆancia MaxSAT, ent˜ao o limitante inferior ´e dado por:

satbound = |V | + k + s

Assim, o algoritmo pode ser dado por:


[OCR parcial do recorte p8-fig1.png; conferir símbolos na imagem]
defminimun_vertex_cover_b_bound(G,UpperB,S);
if len(S)+max(degree_bound(G)，clique_bound(G),sat_bound(G))>=UpperB：
returnUpperB
if len(G)
==0：
return len(S)
V=select_max_dg_vert(G)
sol1=minimun_vertex_cover_b_bound(remove(G,Neighbourhood(v)),UpperB,S.append(Neighbourhood(v)))
sol2=minimun_vertex_cover_b_bound（remove（G,v),UpperB,S.append(v))
return min(sol1,so12)


Page viii
