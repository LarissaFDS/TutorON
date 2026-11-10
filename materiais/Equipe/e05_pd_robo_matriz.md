---
id: e05
titulo: Robô coletor de moedas na matriz (PD)
assunto: b2-04-programacao-dinamica
autoria: Equipe TutorON (não é material do professor)
revisado: false
---
Robô coletor de moedas: matriz com r linhas e c colunas; m[i][j] = 1 se há moeda na célula (i, j), senão 0. O robô sai de (1, 1), só anda para a direita ou para baixo, e termina em (r, c). Qual o máximo de moedas que ele coleta?
Tabela: F[i][j] = máximo de moedas coletadas ao chegar na célula (i, j). Linha i e coluna j são as da própria matriz (a partir de 1).
Casos base: F[1][1] = m[1][1]. Primeira linha: F[1][j] = F[1][j-1] + m[1][j]. Primeira coluna: F[i][1] = F[i-1][1] + m[i][1].
Recorrência: para i >= 2 e j >= 2, F[i][j] = m[i][j] + max(F[i-1][j], F[i][j-1]). Resposta: F[r][c].
Por que i-1 e j-1: o robô só chega em (i, j) vindo de cima, a célula (i-1, j), ou da esquerda, a célula (i, j-1). São as duas únicas origens possíveis, e escolhemos a que trouxe mais moedas. Na primeira linha só existe a da esquerda; na primeira coluna, só a de cima.
Pseudocódigo:
F[1][1] <- m[1][1]
para j de 2 até c: F[1][j] <- F[1][j-1] + m[1][j]
para i de 2 até r:
  F[i][1] <- F[i-1][1] + m[i][1]
  para j de 2 até c:
    F[i][j] <- m[i][j] + max(F[i-1][j], F[i][j-1])
retorne F[r][c]
Rastreio: moedas m (3 x 4):
0 1 0 1
1 0 1 0
0 1 1 0
Tabela F:
i\j | 1 2 3 4
1 | 0 1 1 2
2 | 1 1 2 2
3 | 1 2 3 3
Ex.: F[3][3] = m[3][3] + max(F[2][3], F[3][2]) = 1 + max(2, 2) = 3. Resposta F[3][4] = 3.
Caminho: comece em (r, c) e volte sempre para o vizinho (de cima ou da esquerda) com F maior, até (1, 1); depois inverta a ordem.
Complexidade: tempo Θ(rc); espaço Θ(rc), ou Θ(c) guardando só a linha anterior se não precisar do caminho.
Pegadinha: a recursão direta sem tabela recalcula as mesmas células e fica exponencial.
