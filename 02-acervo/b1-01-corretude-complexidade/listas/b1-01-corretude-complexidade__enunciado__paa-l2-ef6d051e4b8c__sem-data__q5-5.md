# ef6d051e4b8c-q5-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L2.pdf | página(s): 6, 7

5. Resolva a recorrˆencia:


                (                                     2, se n = 2
                   T(n) =
                            2 · T(n2) + n, se n = 2k, para k > 1


     Solu¸c˜ao:

    Desenvolvendo a recorrˆencia obtemos as seguintes fun¸c˜oes:
    T(n) = 2 · T(n2) + n  (1)
    T(n/2) = 2 · T(n4) + n/2  (2)
    T(n/4) = 2 · T(n8) + n/4  (3)
    Sabendo disso, temos que a partir de (1) e (2):
    T(n) = 2 · T(n2) + n
    T(n) = 2 · 2 · T(n4) + n2 + n
    T(n) = 22 · T(n4) + 2n  (4)

   De (3) e (4):
    T(n) = 22 · T(n4) + 2n
    T(n) = 22 · 2 · T(n8) + n4 + 2n
    T(n) = 23 · T(n8) + 3n
                      ...                      ...                      ...                      ...                      ...                      ...                      ...                      ...
   ⇒T(n) = 2k · T( n ) + kn                            2k

   A recorrˆencia encerra, desse modo, quando:
     n = 2 ⇒2k+1 = n ⇒k + 1 = log2(n) ⇒k = log2(n) −1      2k
  ⇒k = log2(n) −log2(2) ⇒k = log2(n2)

  ⇒  T(n) = n                      2                               · T(2) + log2(n2) · n



                                  Page vi⇒  T(n) = n + log2  n2   · n ⇒  T(n) = n + (log2(n) −log2(2)) · n
  ⇒  T(n) = n −n + n · log2(n)   ∴  T(n) = n · log2(n)
