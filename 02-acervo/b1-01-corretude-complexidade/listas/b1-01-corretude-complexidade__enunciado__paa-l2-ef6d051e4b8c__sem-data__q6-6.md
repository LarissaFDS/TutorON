# ef6d051e4b8c-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L2.pdf | página(s): 7

6. Descreva um algoritmo de tempo Θ(n lg n) que, dado um conjunto S de n
   inteiros e um outro inteiro x, determine se existe ou n˜ao dois elementos em
  S cuja soma seja exatamente x.


     Solu¸c˜ao:





    Nesse algoritmo, podemos observar a fun¸c˜ao verifySum, que recebe como parˆametros
    o inteiro x e o conjunto S de inteiros. Inicialmente, ordenamos o conjunto S atrav´es
    do algoritmo Merge Sort, cuja complexidade ´e Θ(n lg n). Em seguida, presumimos
    que size(S) retorna n, visto que ´e o tamanho de S, e percorremos o conjunto em busca
    de dois inteiros nele que somando resulte no valor de x. As opera¸c˜oes que sucedem
    o Merge Sort tem complexidade Θ(n). Portanto, conclui-se que o algoritmo acima
     possui complexidade dominante Θ(n lg n).
