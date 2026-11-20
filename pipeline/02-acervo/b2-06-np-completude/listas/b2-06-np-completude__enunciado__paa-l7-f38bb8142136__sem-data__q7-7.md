# f38bb8142136-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L7.pdf | página(s): 8, 9

7. Uma pipa ´e um grafo sobre um n´umero par de v´ertices, digamos 2n, nos quais
  n dos v´ertices formam uma clique e os restantes n v´ertices s˜ao conectados
  em um “rabo” que consiste em um caminho incidente a um dos v´ertices da


                                  Page viiiclique. Dado um grafo e um objetivo g, o PROBLEMA DA PIPA pede que
   se encontre um subgrafo que seja uma pipa e que contenha 2g n´os. Prove que
  PIPA ´e NP-completo.


     Solu¸c˜ao: Provaremos que o problema da pipa ´e NP-completo ao mostrar uma redu¸c˜ao
     polinomial do problema do clique que, por sua vez, ´e NP-completo. Dado um grafo
    G(V,E) e um objetivo g, n´os desejamos determinar se G cont´em um clique de ta-
    manho g. Para isso, criaremos um grafo auxiliar G’(V’,E’) que deve conter todos os
      v´ertices e arestas de G e uma ”cauda”de tamanho g para cada v´ertice em G. Assim,
    considerando que a cauda adicionada se configura apenas como caminhos e n˜ao con-
    tribuem realmente para um clique, G’ possui um subgrafo de pipa com 2g n´os se e
    somente se existe um clique de tamanho g em G, sendo assim:

     1) Se existe um clique de tamanho g em G, ent˜ao G’ forma um subgrafo que seja
   uma pipa e que cont´em 2g.
     2) Para que exista um subgrafo G’ com um subgrafo de pipa de 2g n´os, ´e necess´ario
    que G tenha um grupo de tamanho g.

   Com isso, provamos que o problema da pipa ´e NP-completo.
                                                ■
