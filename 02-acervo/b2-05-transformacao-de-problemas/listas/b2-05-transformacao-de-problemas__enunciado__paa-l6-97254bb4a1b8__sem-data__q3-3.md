# 97254bb4a1b8-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 2

3. V´arias fam´ılias saem para jantar juntas. Para aumentar sua intera¸c˜ao social,
   eles gostariam de sentar-se  `a mesa, de modo que dois membros da mesma
   fam´ılia n˜ao estivessem na mesma mesa.  Mostre como encontrar uma dis-
   posi¸c˜ao dos assentos que atenda a esse objetivo (ou prove que n˜ao existe tal
   disposi¸c˜ao) usando o problema de fluxo m´aximo. Suponha que o jantar tenha
  p fam´ılias e que a i-´esima fam´ılia tenha ai membros. Suponha que q mesas
   s˜ao dispon´ıveis e que a meja j-´esima mesa possui capacidade bj


     Solu¸c˜ao: Para encontrar uma disposi¸c˜ao dos assentos que atenda a esse objetivo
    usando o problema de fluxo m´aximo podemos come¸car definindo o grafo G(V, A),
    onde:

    V = {s, t} ∪{ui | 1 ≤i ≤p} ∪{cj ≤j ≤q}

   A = {(s, ui) | 1 ≤i ≤p} ∪{(ui, vi) | 1 ≤i ≤p, 1 ≤j ≤q} ∪{(vj, t) | 1 ≤j ≤q}

     Al´em disso, temos que as capacidades est˜ao definidas a seguir:

                            c(s, ui) = ai;   c(ui, vj) = 1;   c(vj, t) = bj;

   Um fluxo que vai de ui at´e vj  ´e ’0’ ou ’1’ e significa que um membro da familia i
     sentar´a na mesa j. Com isso e utilizando uma solu¸c˜ao integral com o uso do problema
    de fluxo m´aximo ´e poss´ıvel dar uma solu¸c˜ao para a disposi¸c˜ao das fam´ılias nas mesas,
    tendo em vista que esse problema maximiza o n´umero de pessoas que podem sentar
    considerando as restri¸c˜oes dadas.



                                   Page ii
