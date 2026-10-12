# c01

Fonte: materiais\c01_prova1_2023-03_q2_algoritmo_x.md | página(s): não informada na transcrição

Questão 2 [2 pontos]: Considere o seguinte algoritmo:

1: procedure ALGORITMO X(vetor A[1, ..., n], inicio, fim)
2:   if inicio = fim then
3:     return A[inicio]
4:   end if
5:   meio ← inicio + (fim − inicio)/2
6:   a ← X(A, inicio, meio)
7:   b ← X(A, meio + 1, fim)
8:   if a < b then
9:     return b
10:  else
11:    return a
12:  end if
13: end procedure

Explique o que ele faz e prove sua corretude.
