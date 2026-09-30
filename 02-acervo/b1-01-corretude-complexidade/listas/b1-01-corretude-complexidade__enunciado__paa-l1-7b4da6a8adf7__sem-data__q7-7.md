# 7b4da6a8adf7-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 11, 12

7. Prove a corretude do algoritmo Conversor Decimal-Bin´ario.





     Solu¸c˜ao:

    Teorema: O algoritmo Conversor Decimal-Bin´ario est´a correto, ou seja, retorna
    corretamente a convers˜ao em bin´ario para um n´umero natural dado.

    Prova:
      Sendo:
         - mk ´e o inteiro que representa o estado atual do vetor b, ap´os k itera¸c˜oes, tal que:

                    0,  se k = 0
                                                      mk =      i=k
                P b[i] 2i−1,  se k ≥1                                     i=1

         - tk representa o valor de t ao final do k-´esimo loop.

      Considere o seguinte invariante de la¸co, onde na itera¸c˜ao k, o vetor b[1...k] re-
       presenta um inteiro mk tal que:

                                 n(k) = mk + tk.2k, ∀k

        Inicializa¸c˜ao: Neste caso, a vari´avel t  ´e inicializada com o n´umero natural a
        ser convertido n, o contador k = 0 e o vetor b est´a vazio. Al´em disso, a itera¸c˜ao
      na inicializa¸c˜ao ´e:

                  para k = 0:   n(0) = t0.20 + m0 = n.1 + 0 ∴n(0) = n





                                  Page xiDessa forma, a defini¸c˜ao de invariante na inicializa¸c˜ao est´a satisfeita.

Manuten¸c˜ao: Prosseguimos ent˜ao para a execu¸c˜ao do la¸co nos passos seguintes,
onde k  ´e incrementado uma unidade a cada itera¸c˜ao e, dessa forma, o vetor b na
posi¸c˜ao k  ´e atualizado com o valor da opera¸c˜ao modular com 2, isto ´e, tk mod
