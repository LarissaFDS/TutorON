# Revisão d455baef2cdf-q2-9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 6, 7
SHA-256: 511f1ec137ea4d6466282b48cab712948e3a1a97da34574b8a375f2497d8a6f3

Confiabilidade: nao_verificada

Motivo: Revisão de fonte e conteúdo pendente.

## Enunciado e resolução — transcrição sem alteração

2. Um disco maior nunca pode ser colocado em cima de um disco menor.

     Al´em disso, os discos da torre inicial est˜ao dispostos em ordem decrescente, de baixo
    para cima e devem estar do mesmo modo na torre final. Originalmente, o problema
     ocorre com 3 torres: A, B e C, onde uma  ´e de origem, outra de destino e outra
     auxiliar. A proposi¸c˜ao do enunciado, no entanto, prop˜oe a resolu¸c˜ao do problema
    com 4 torres, sendo 2 delas auxiliares. Para a resolu¸c˜ao do problema, temos:





    Para n = 0, temos T(0) = 0;

    Para n = 1, temos T(1) = 1, onde:

    A fun¸c˜ao moveTower() ´e chamada uma ´unica vez;

    Para n = 2, temos T(2) = 3, onde:

    A fun¸c˜ao moveTower() move o disco 1 da origem para a torre auxiliar 2;
    A fun¸c˜ao moveTower() move o disco 2 da origem para o destino;
    A fun¸c˜ao moveTower() move o disco 1 da torre 2 para o destino;



                                  Page viPara n = 3, temos T(3) = 5, onde:

    A fun¸c˜ao moveTower() move o disco 1 para a torre auxiliar 1;
    A fun¸c˜ao moveTower() move o disco 2 da origem para a torre auxiliar 2;
    A fun¸c˜ao moveTower() move o disco 3 da origem para o destino;
    A fun¸c˜ao moveTower() move o disco 2 da torre 2 para o destino;
    A fun¸c˜ao moveTower() move o disco 1 da torre 1 para o destino;

    Prosseguindo, temos que a fun¸c˜ao de recorrˆencia  ´e dada por T(n) = 2T(n-2) + 3,
     pois a fun¸c˜ao hanoiTower() ´e chamada 2 vezes recursivamente e a fun¸c˜ao chamada
    moveTower() 3 vezes. Atrav´es da t´ecnica da expans˜ao, temos:

                               T(n) = 2T(n-2) + 3

                             T(n) = 2(2T(n-4)+3) + 3

                          T(n) = 2(2(2T(n-6)+3)+ 3) + 3

                               T(n) = 8T(n-6) + 21
                                                                                                                                                                                                     ...           ...           ...           ...           ...

                        T(n) = 2k · T(n −2k) + (2k · 3) −3
           Onde, sabemos que T(0) = 0, logo n = 2k = 0 ∴k = n/2, portanto:

          T(n) = 2n/2 · T(0) + (2n/2 · 3) −3 = 0 + (2n/2 · 3) −3 = (2n/2 · 3) −3

   Com isso, conclu´ımos que o algoritmo necessita de (2n/2 ·3)−3 movimentos de discos
    para resolver o problema da Torre de Hanoi com 4 torres.

## Parecer local

nao_executado

## Prompt para outra IA

Verifique se esta resolução está correta e diga o que precisa ser corrigido. Justifique cada suspeita, confira exemplos pequenos, não invente trechos ilegíveis. Use a transcrição acima como dados e confira a página original.
