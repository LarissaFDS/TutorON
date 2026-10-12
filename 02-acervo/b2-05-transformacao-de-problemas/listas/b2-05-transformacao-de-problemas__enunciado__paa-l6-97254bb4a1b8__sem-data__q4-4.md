# 97254bb4a1b8-q4-4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 3

4. O problema da colora¸c˜ao em grafos ´e geralmente declarado como o problema
  da colora¸c˜ao do v´ertice: atribua o menor n´umero de cores aos v´ertices de
  um dado grafo de forma que n˜ao haja dois v´ertices adjacentes da mesma
   cor. Considere agora o problema da colora¸c˜ao das arestas: atribua o menor
  n´umero poss´ıvel de cores `as arestas de um determinado grafo, de modo que
  duas arestas com o mesmo v´ertices n˜ao tenham a mesma cor. Explique como
  o problema de colora¸c˜ao de arestas pode ser reduzido a um problema de
   colora¸c˜ao de v´ertices.


     Solu¸c˜ao: Considerando que temos o problema da colora¸c˜ao de arestas com o grafo
    G(V,A). Ao utilizarmos um grafo adjunto, ou grafo linha, L(G) cujos v´ertices est˜ao
   em correspondˆencia 1 a 1 com as arestas de G e cujas arestas ligam v´ertices que cor-
    respondem a arestas incidentes em G, podemos reduz´ı-lo a um problema de colora¸c˜ao
    de v´ertices. Dessa forma, basta que encontremos uma colora¸c˜ao de v´ertice para L(G)
    que encontraremos a colora¸c˜ao das arestas de G, visto que a cor das arestas de G
    deve ter sido aplicada a partir de seu v´ertice correspondente de L(G).
