# a177bf5bc3c7-q5-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 4, 5, 6

5. Alice quer dar uma festa e est´a decidindo quem chamar. Ela tem n pessoas
   as quais escolher, e ela fez uma lista de quais pares dessas pessoas conhecem
  uma a outra. Ela quer selecionar o maior n´umero de pessoas poss´ıvel, sujeito
  a duas restri¸c˜oes: na festa, cada pessoa deve ter pelo menos outras cinco
  pessoas que ela conhece e outras cinco pessoas que ela n˜ao conhece. Forne¸ca
  um algoritmo eficiente que tome como entrada a lista das n pessoas e a lista
  de pares de quem conhece quem e calcule a melhor escolha de convidados
  para a festa. Dˆe o tempo de execu¸c˜ao em termos de n.


     Solu¸c˜ao:




                                  Page iv[ilegivel] OCR indisponível: TesseractNotFoundErrorO tempo de execu¸c˜ao em termos de n ´e O(n2). Isso se d´a pois no loop for em que se
     recebe e insere as conex˜oes no grafo, ocorre n itera¸c˜oes, a fim de encontrar todas as
     conex˜oes de todos os poss´ıveis convidados, onde cada um pode ter no m´aximo n - 1
     conex˜oes. Al´em disso, h´a outro loop for que verifica se os requisitos (conhecer mais
    de 5 pessoas, e n˜ao conhecer no m´ınimo 5 pessoas) est˜ao sendo cumpridos. Em seu
     pior caso, todos os poss´ıveis convidados foram rejeitados, ent˜ao para cada um deles
     haver´a n itera¸c˜oes para remover da lista de convidados e de todas as suas conex˜oes.
    Sendo assim, justifica-se o tempo polinomial O(n2).
