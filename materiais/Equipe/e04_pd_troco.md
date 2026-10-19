---
id: e04
titulo: Troco com o menor número de moedas por programação dinâmica
assunto: b2-04-programacao-dinamica
autoria: Equipe TutorON (não é material do professor)
revisado: false
---
Troco: moedas d_1..d_k (cada uma com quantidade ilimitada) e um valor V. Qual o menor número de moedas que somam exatamente V?
Tabela: C[v] = menor número de moedas que somam exatamente v, para v = 0..V. Uma dimensão basta: o subproblema é só "quanto falta pagar".
Recorrência com caso base: C[0] = 0. Para v >= 1: C[v] = 1 + min{ C[v - d] : d moeda com d <= v }; se nenhuma moeda cabe, C[v] = infinito.
Por que v - d: pense na ÚLTIMA moeda usada, d. Depois de tirá-la, falta pagar v - d, e esse resto também tem de ser pago com o mínimo de moedas (subestrutura ótima). Testamos todas as moedas como última e ficamos com a melhor.
Pseudocódigo:
C[0] <- 0
para v de 1 até V:
  C[v] <- infinito
  para cada moeda d:
    se d <= v e C[v-d] + 1 < C[v] então
      C[v] <- C[v-d] + 1
      ultima[v] <- d
retorne C[V]
Rastreio: moedas {1, 3, 4}, V = 6.
v | 0 1 2 3 4 5 6
C[v] | 0 1 2 1 1 2 2
ultima[v] | - 1 1 3 4 1 3
Ex.: C[6] = 1 + min(C[5], C[3], C[2]) = 1 + min(2, 1, 2) = 2.
Reconstrução: 6 -> última 3 -> falta 3 -> última 3 -> falta 0. Troco {3, 3}: 2 moedas.
Guloso (maior moeda primeiro): 4, depois 1, 1 = 3 moedas. Ele erra porque {1, 3, 4} não é um sistema canônico; no sistema brasileiro o guloso acerta, mas isso precisa de prova.
Complexidade: tempo Θ(kV), espaço Θ(V). Pseudo-polinomial no valor V.
Pegadinhas: C[v] é o mínimo para EXATAMENTE v (não "até v"); com moedas sem a de valor 1, alguns valores são impossíveis (infinito).
