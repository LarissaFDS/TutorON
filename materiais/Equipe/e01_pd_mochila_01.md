---
id: e01
titulo: Mochila 0/1 por programação dinâmica
assunto: b2-04-programacao-dinamica
autoria: Equipe TutorON (não é material do professor)
revisado: false
---
Mochila 0/1: n itens, o item i tem peso w_i e valor v_i (inteiros positivos); capacidade W. Cada item entra no máximo uma vez. Qual o maior valor?
Tabela: V[i][c] = maior valor usando só os itens 1..i com capacidade c. Linha i = quantos itens já foram considerados (0..n); coluna c = capacidade disponível (0..W). A linha 0 é "nenhum item".
Recorrência com casos base: V[0][c] = 0 para todo c. Para i >= 1: se w_i > c, V[i][c] = V[i-1][c]; senão V[i][c] = max(V[i-1][c], v_i + V[i-1][c-w_i]). Resposta: V[n][W].
Por que i-1: V[i-1][c] é deixar o item i de fora, com a mesma capacidade. V[i-1][c-w_i] é levar o item i: sobra c-w_i para os itens 1..i-1. As duas opções olham a linha i-1, e é isso que impede usar o item i duas vezes. Com V[i][c-w_i] seria a mochila ilimitada.
Pseudocódigo:
para c de 0 até W: V[0][c] <- 0
para i de 1 até n:
  para c de 0 até W:
    V[i][c] <- V[i-1][c]
    se w[i] <= c e v[i] + V[i-1][c-w[i]] > V[i][c] então
      V[i][c] <- v[i] + V[i-1][c-w[i]]
retorne V[n][W]
Rastreio: itens (peso, valor) = (1, 1), (3, 4), (4, 5); W = 7.
i\c | 0 1 2 3 4 5 6 7
0 | 0 0 0 0 0 0 0 0
1 | 0 1 1 1 1 1 1 1
2 | 0 1 1 4 5 5 5 5
3 | 0 1 1 4 5 6 6 9
Ex.: V[3][7] = max(V[2][7], 5 + V[2][3]) = max(5, 9) = 9 (itens 2 e 3, peso 7).
Reconstrução: de i = n até 1, se V[i][c] != V[i-1][c] o item i entrou e c <- c - w_i.
Complexidade: tempo e espaço Θ(nW); espaço Θ(W) com um vetor só, percorrendo c de W até w_i (ordem decrescente). É pseudo-polinomial: W ocupa só cerca de log W bits na entrada.
Pegadinhas: escolher por valor/peso (guloso) só é ótimo na mochila fracionária; na versão 1D, percorrer c em ordem crescente reutiliza o item i.
