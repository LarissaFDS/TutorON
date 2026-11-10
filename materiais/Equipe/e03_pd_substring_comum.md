---
id: e03
titulo: Maior substring comum em O(mn)
assunto: b2-04-programacao-dinamica
autoria: Equipe TutorON (não é material do professor)
revisado: false
---
Maior substring comum: dadas x = x_1..x_n e y = y_1..y_m, achar o maior k com x_i..x_{i+k-1} = y_j..y_{j+k-1} (trecho contíguo), em tempo O(mn).
Tabela: L[i][j] = tamanho da maior substring comum que TERMINA exatamente em x_i e em y_j. Índices das strings começam em 1; a linha 0 e a coluna 0 representam prefixo vazio.
Casos base: L[0][j] = 0 e L[i][0] = 0.
Recorrência: se x_i = y_j, L[i][j] = L[i-1][j-1] + 1; senão L[i][j] = 0. Resposta: o MAIOR valor da tabela, não L[n][m].
Por que i-1 e j-1 juntos: L[i-1][j-1] é a substring comum que terminava uma posição antes nas DUAS strings; se x_i = y_j, ela cresce 1. Se x_i != y_j, a contiguidade quebra e volta a 0. (Na maior SUBSEQUÊNCIA comum o desencontro usaria max(L[i-1][j], L[i][j-1]).)
Base 0 x base 1: em C ou Python o primeiro caractere é x[0]. A tabela tem (n+1) x (m+1) posições por causa da linha 0, então a célula L[i][j] compara x[i-1] com y[j-1] no código. Por isso a resolução da Lista 5 escreve "se x[i-1] = y[j-1]": é x_i = y_j em índice base 0, não "o caractere anterior".
Pseudocódigo:
melhor <- 0
para i de 0 até n: L[i][0] <- 0
para j de 0 até m: L[0][j] <- 0
para i de 1 até n:
  para j de 1 até m:
    se x_i = y_j então
      L[i][j] <- L[i-1][j-1] + 1
      melhor <- max(melhor, L[i][j])
    senão L[i][j] <- 0
retorne melhor
Rastreio: x = ABABC (linhas), y = BABCA (colunas); linha e coluna 0 omitidas.
x_i \ y_j | B A B C A
A | 0 1 0 0 1
B | 1 0 2 0 0
A | 0 2 0 0 1
B | 1 0 3 0 0
C | 0 0 0 4 0
Máximo 4 em L[5][4]: a substring termina em x_5 e y_4 e tem 4 letras, então é x_2..x_5 = BABC.
Complexidade: tempo Θ(mn); espaço Θ(mn), ou Θ(m) guardando só a linha anterior.
