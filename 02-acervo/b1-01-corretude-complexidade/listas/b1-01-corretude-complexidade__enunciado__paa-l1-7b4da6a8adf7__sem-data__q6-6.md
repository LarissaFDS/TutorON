# 7b4da6a8adf7-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 9, 10

6. Prove a corretude do algoritmo de Horner para a avalia¸c˜ao de polinˆomios.
  P(x) = anxn+ an−1xn−1+ ··· +a1x + a0.





     Solu¸c˜ao:

    Teorema: O algoritmo de Horner est´a correto, ou seja, retorna corretamente o
      c´alculo do polinˆomio para um valor real dado.

    Prova:
      Considere o seguinte invariante de la¸co:

                                            n
                                  p = X Aj xj−i

                                                  j=i

        Inicializa¸c˜ao: Neste caso, fica garantido, pela linha (2) que, antes de execu-
      tarmos o la¸co de itera¸c˜ao propriamento dito, p resulta no coeficiente do termo
      de maior grau do polinˆomio informado, isto ´e: A[n]. Assim, considerando que a
        opera¸c˜ao antes do la¸co de repeti¸c˜ao torna i = n (para fins de simplifica¸c˜ao), a
       2ª linha de c´odigo mostra que o invariante de la¸co est´a correto antes do loop for.
      Manuten¸c˜ao:  ´E poss´ıvel ent˜ao prosseguir para a execu¸c˜ao do la¸co nos passos
       seguintes, onde “i” ´e decrementado uma unidade em cada itera¸c˜ao e, de mesmo
      modo, a linha (4) garante que o valor do pr´oximo termo do invariante ser´a
        inclu´ıdo na soma, assim como o valor do termo atual. Sendo que o resultado



                                  Page ixda opera¸c˜ao do termo atual pelo valor real x, informado pelo usu´ario, vai sendo
parcialmente computado em cada la¸co de itera¸c˜ao. Desse modo, para:

                                  n
                     i = n −1 :  X Aj xj−i = An−1x0 + Anx1
                               j= n−1


                             n
              i = n −2 :  X Aj xj−i = An−2x0 + An−1x1 + Anx2
                          j= n−2


                                               ...                      ...                      ...
                 n
      i = 1 :  X Aj xj−i = A1 x0 + A2 x1 + ... + AN−1 xN−2 + AN xN−1

                 j=1

Sendo assim, ao longo da execu¸c˜ao dos la¸cos de repeti¸c˜ao

                                     n
                            p = X Aj xj−i

                                      j=1

T´ermino: Sabendo que a vari´avel “i” est´a sendo decrementada e avaliada de
n−1 at´e 0, e considerando que a inicializa¸c˜ao e manuten¸c˜ao do la¸co de repeti¸c˜ao
s˜ao v´alidas. Ap´os a execu¸c˜ao da ´ultima itera¸c˜ao “i = 0”, temos que o valor de p
´e:
         n
  X Aj xj−i = A0 x0 + A1 x1−0 + ... + AN−1 x(N−1)−0 + AN xN−0

        j=0

          = A0 x0 + A1 x1 + ... + AN−1 xN−1 + AN xN

Portanto, conclui-se que o algoritmo de Horner est´a correto e ´e capaz de calcular
o valor do polinˆomio de Grau N dado para um determinado valor de x.

                                            ■





                             Page x
