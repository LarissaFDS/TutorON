# 70d6475b28bf-q5-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 9

5. No problema da ´ARVORE DE STEINER M´INIMA, a entrada consiste em:
  um grafo completo G = (V, E ) com distˆancias duv entre todos os pares de
   n´os; e um determinado conjunto de v´ertices terminais V ⊆V  . O objetivo ´e
  encontrar uma ´arvore de custo m´ınimo que inclua os v´ertices V . Essa ´arvore
  pode ou n˜ao incluir n´os em V \V ′  . Sabe-se que este problema ´e NP-dif´ıcil,
  proponha uma heur´ıstica construtiva para gerar uma solu¸c˜ao vi´avel para o
  problema (note que a solu¸c˜ao pode n˜ao ser ´otima).


     Solu¸c˜ao: Iremos supor que a distˆancia entre as entradas atende  `as defini¸c˜oes de
     m´etrica e, com isso, provaremos que uma solu¸c˜ao para a ´arvore de steiner m´ınima
    pode ser obtida atrav´es de um algoritmo de aproxima¸c˜ao ao ignorarmos os n´os n˜ao
     terminais e retornarmos a ´arvore geradora m´ınima em V’.
    Para isso, consideremos T como a ´Arvore Steiner M´ınima possuindo custo C e, com
      isso, podemos moldar a ´arvore steiner para obter custo 2C ao passar por todos os
      v´ertices. Sendo i, j e j v´ertices adjacentes no caminho, usamos a desigualdade trian-
     gular dik ≤dij + djk.

   Com isso, n´os podemos desviar de um v´ertice intermediario  ’j’ e conectar  ’i’ e ’k’
     diretamente, sem aumentar o custo. Com essa t´ecnica, podemos desviar de todos os
      v´ertices que n˜ao est˜ao em V’ e est˜ao presentes no caminho, e de todos os v´ertices de
    V’ que  j´a foram visitados duas vezes.  Isso resulta em um caminho de custo de no
    m´aximo 2C, passando por todos os v´ertices de V’ exatamente uma vez.

     Portanto, esse caminho ´e uma ´arvore geradora para V’ de custo 2C, o que implica
    que o custo da ´Arvore de Steiner M´ınima ser´a menor ou igual a 2C, assim nos dando
    a prova da aproxima¸c˜ao desejada.
