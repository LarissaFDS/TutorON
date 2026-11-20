# a177bf5bc3c7-q10-10

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 9, 10

10. Prove que o problema da mochila pode ser resolvido em tempo polinomial
   por um algoritmo guloso, se o peso wi de cada item i for unit´ario.


      Solu¸c˜ao: Nesse problema, temos uma mochila com capacidade de aguentar certo
     peso W e i itens de peso unit´ario wi, mas com valores distintos - sendo alguns mais
      valiosos que outros. Seu objetivo ´e escolher os itens que resultar˜ao em um maior lucro
     para o dono na mochila, caso este deseje vender. Uma maneira de resolvˆe-lo (por´em
    nem sempre t˜ao eficiente)  ´e atrav´es de um algoritmo guloso, que  ´e caracterizado
     por tomar a decis˜ao com a vantagem imediata mais ´obvia.  Nesse caso, podemos
      ver ent˜ao que essa vantagem  ´e a escolha dos itens que possuem maior valor, sem
      levar em considera¸c˜ao o seu peso, visto que todos possuem o mesmo. Sendo assim,
      necessitamos inicialmente ordenar de maneira decrescente os itens com base em seu
      valor e em seguida pegar os primeiros W itens, de forma a encher a mochila at´e seu
     m´aximo e, assim, obter m´aximo lucro.





     Desse modo, como o algoritmo acima envolve uma ordena¸c˜ao O(n log(n)) e uma
       verifica¸c˜ao O(n) temos que a complexidade final  ´e O(n log (n)). Al´em disso, como
     O(n) < O(n log (n)) < O(n2), ´e poss´ıvel concluir que a complexidade ´e limitada de
    modo inferior e superior por duas fun¸c˜oes polinomiais (linear e quadr´atica). Logo,



                                   Page ixa complexidade linear-logar´ıtimica ´e melhor que quadr´atica e pior que linear (estas
sendo fun¸c˜oes polinomiais).





                               Page x
