# d455baef2cdf-q5-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 5

5. Suponha que esteja escolhendo entre os seguintes trˆes algoritmos:

     • Algoritmo A resolve problemas dividindo-os em cinco subproblemas de
      metade do tamanho, solucionando cada subproblema recursivamente e,
        ent˜ao, combinando as solu¸c˜oes em tempo linear.
     • Algoritmo B resolve problemas de tamanho n resolvendo recursivamente
       dois subproblemas de tamanho n 1 e, ent˜ao, combinando as solu¸c˜oes em
     tempo constante.
     • Algoritmo C soluciona problemas de tamanho n dividindo-os em nove
      subproblemas de tamanho n/3, resolvendo recursivamente cada subpro-
      blema e, ent˜ao, combinando as respostas em tempo O(n2).

  Qual o tempo de execu¸c˜ao de cada um desses algoritmos (em nota¸c˜ao O) e
  qual vocˆe escolheria?


     Solu¸c˜ao:

     Utilizando o Teorema Mestre para os algoritmos A e C e resolvendo a recorrˆencia
    para o algoritmo B, temos que:
    TA(n) = 5 · T  n2 + O(n) ⇒TA(n) = O(nlog2(5)) = O(n2.32)
    TB(n) = 2 · T (n −1) + O(1) ⇒TB(n) = O(2n)
    TC(n) = 9 · T  n3 + O(n2) ⇒TC(n) = O(n2 · log2(n))

   A escolha seria o algoritmo C, que funciona em tempo de execu¸c˜ao O(n2 log2(n).
