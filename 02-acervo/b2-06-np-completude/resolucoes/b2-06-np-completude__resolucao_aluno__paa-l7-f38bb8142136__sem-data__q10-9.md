# f38bb8142136-q10-9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L7.pdf | página(s): 11, 12

10. SUBGRAFO DENSO: dados um grafo G e dois inteiros a e b, encontre um
conjunto de a v´ertices de G tal que exista pelo menos b arestas entre eles.
Prove que o problema ´e NP-completo.

Solu¸c˜ao: Para provarmos que o problema do subgrafo denso ´e NP-completo, deve-
mos efetuar duas provas:

1. Devemos provar que o problema do subgrafo denso ´e NP: Para isso, teremos
um verificador de tempo polinomial que ir´a pegar G(G, k, y) e H = (V’, E’)
como certificados e ent˜ao verificar se H ´e um subgrafo de F, |V ′| = k, |E′| ≥y.

Page xi2. Devemos provar que existe um problema NP-completo conhecido que pode ser
polinomialmente reduzido a A: Para isso, sabemos que esse problema ´e uma
generaliza¸c˜ao do problema do clique. Sendo assim, dado uma instˆancia (G, k)
consideramos a = k, b = k(k-1)/2. Dessa forma, qualquer subgrafo de G com k
v´ertices e contendo k(k-1)/2 arestas deve ter uma aresta entre cada par poss´ıvel
desses k v´ertices e, portanto, deve ser um clique. Similarmente, um clique com
k v´ertices deve conter k(k-1)/2 arestas.

■

Page xii
