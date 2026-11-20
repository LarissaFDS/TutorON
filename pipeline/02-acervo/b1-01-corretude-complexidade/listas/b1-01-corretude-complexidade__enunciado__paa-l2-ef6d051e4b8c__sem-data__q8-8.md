# ef6d051e4b8c-q8-8

Fonte: materiais\Disponiveis\RAG PAA\PAA_L2.pdf | página(s): 8

8. Considere o seguinte trecho de c´odigo:





  Seja T (n) o n´umero de vezes que a palavra OI ´e impressa quando Prog1  ´e
  chamado com parˆametro n. Calcule T (1) e determine uma rela¸c˜ao entre T (n)
  e T (n −1) para n > 1. Com base na rela¸c˜ao encontrada, utilize indu¸c˜ao para
  mostrar que T (n) ≤n2, para todo n maior ou igual a 1.


     Solu¸c˜ao:

    Para n = 1, a palavra “OI” ´e impressa apenas uma vez, portanto, T(1) = 1.

    Para n > 1, a palavra “OI” ´e inicialmente impressa n vezes, atrav´es do loop for. Em
     seguida, ela ´e impressa T(n-1) vezes. Portanto, T(n) = n + T(n-1).

    Sendo assim,
                    (                                            1, se n = 1
                        T(n) =
                            n + T(n −1), se n > 1

    Dando continuidade, devemos mostrar que T(n) ≤n2, para todo n maior ou igual a
