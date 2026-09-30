# a177bf5bc3c7-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 7, 8

7. Considere o seguinte problema.
  Entrada: Grafo n˜ao direcionado G = (V, E ); pesos de arestas we ; subconjunto
  de v´ertices U ⊂V.
   Sa´ıda: A ´Arvore Geradora mais leve na qual os n´os de U s˜ao folhas (pode
  haver outras folhas na ´arvore tamb´em)


     Solu¸c˜ao: Para encontrar a sa´ıda desejada, ou seja, a ´arvore geradora mais leve na
    qual os n´os de U s˜ao folhas, necessitamos fazer alguns passos, descritos a seguir:

   O primeiro ´e a construir¸c˜ao Grafo G′ = (V ′, E′), onde

               V ′ = V −U e E′ = {(u, v) | u, v ∈V −U ∧(u, v) ∈E}

     Ap´os isso, deve-se aplicar o algoritmo de Kruskal a fim de encontrar a ´arvore geradora
    m´ınima de G′, que  ´e T ′. Caso T ′ n˜ao exista, ent˜ao a ´arvore geradora mais leve  ´e
     impratic´avel e n˜ao podemos encontrar uma solu¸c˜ao. Isso ´e explicado pois assumindo
    que h´a duas ´arvores na floresta geradora para o grafo G′, dever´a haver um n´o u ∈U
    que conecte as duas ´arvores na floresta, mas isso far´a com que u deixe de ser uma
     folha, resultando em uma contradi¸c˜ao.

   No entanto, caso T ′ exista, prosseguimos para a constru¸c˜ao de um conjunto de arestas
     E’, onde:

                           E′ : ∀(u, v) ∈E′ | u ∈U ∧v /∈U

   E o pseudo-c´odigo ´e dado a seguir:

        for each u in U:
            generateSet(u) # filtra as arestas pelo seu peso
        for all edges u,v in E # por ordem de peso
            if encontrar(u) != encontrar(v):
                add edge u,v to T'
                union(u,v)
        return T'




                                  Page viiCom isso, encontramos e retornamos T ′, que ´e ´arvore geradora mais leve na qual os
      n´os de U s˜ao folhas.
