# 7b4da6a8adf7-q10-11

Fonte: materiais\Disponiveis\RAG PAA\PAA_L1.pdf | página(s): 16, 17

10. Considere o algoritmo de Ulam, ele termina? De fato, conjectura-se que
   seguindo o algoritmo, sempre ser´a obtida a sequencia 4, 2, 1 (Conjectura
   de Collatz).  Ex: Para o valor a = 22, ser´a obtida a seguinte sequencia:
    22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1. Como a prova do
    t´ermino do algoritmo consiste em um dif´ıcil problema matem´atico em aberto.
   Implemente um teste exaustivo mostrando que para qualquer unsigned shot
    int (1 a 65535) de entrada o algoritmo para.  Escreva um pequeno relato
   informando o tamanho da maior sequˆencia encontrada, o valor na qual a
   maior sequˆencia foi obtida, a m´edia dos tamanhos das sequˆencias e o tempo
   de execu¸c˜ao.





      Solu¸c˜ao: Ap´os a implementa¸c˜ao do algoritmo e da execu¸c˜ao de um teste exaustivo
     contendo 65535 entradas, ou seja, cobrindo a possibilidade de entrada de qualquer
     unsigned short int, pudemos observar que, de fato, o algoritmo para de executar e ´e,
      portanto, finito. Al´em disso, assim como ilustra a figura abaixo, algumas informa¸c˜oes
     foram coletadas:

       • O tamanho da maior sequˆencia equivale a 340 n´umeros;
       • O valor de N para a maior sequˆencia ´e 52527;
       • A m´edia dos tamanhos das sequˆencias obtidas ´e 104,21 n´umeros;
       • O tempo de execu¸c˜ao do algoritmo ´e 0.06200 segundos.





                                   Page xvi[ilegivel] OCR indisponível: TesseractNotFoundError
