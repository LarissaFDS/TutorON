---
id: e02
titulo: SUBSET SUM por programação dinâmica (pseudo-polinomial)
assunto: b2-04-programacao-dinamica
autoria: Equipe TutorON (não é material do professor)
revisado: false
---
SUBSET SUM: dados inteiros positivos a_1..a_n e um alvo t, existe subconjunto com soma exatamente t?
Tabela: S[i][s] = verdadeiro se algum subconjunto dos i primeiros elementos soma exatamente s. Linha i = elementos considerados (0..n); coluna s = soma desejada (0..t).
Casos base: S[0][0] = V (conjunto vazio soma 0); S[0][s] = F para s > 0.
Recorrência: S[i][s] = S[i-1][s] OU (a_i <= s E S[i-1][s-a_i]). Resposta: S[n][t].
Por que i-1: S[i-1][s] é não usar a_i (a soma s sai dos anteriores). S[i-1][s-a_i] é usar a_i: o resto s-a_i tem de sair dos elementos 1..i-1, então a_i não é usado duas vezes.
Pseudocódigo:
S[0][0] <- V; para s de 1 até t: S[0][s] <- F
para i de 1 até n:
  para s de 0 até t:
    S[i][s] <- S[i-1][s]
    se a[i] <= s e S[i-1][s-a[i]] então S[i][s] <- V
retorne S[n][t]
Rastreio: A = {3, 34, 4, 12, 5, 2}, t = 9 (1 = V, 0 = F).
i (a_i) \ s | 0 1 2 3 4 5 6 7 8 9
0 | 1 0 0 0 0 0 0 0 0 0
1 (3) | 1 0 0 1 0 0 0 0 0 0
2 (34) | 1 0 0 1 0 0 0 0 0 0
3 (4) | 1 0 0 1 1 0 0 1 0 0
4 (12) | 1 0 0 1 1 0 0 1 0 0
5 (5) | 1 0 0 1 1 1 0 1 1 1
6 (2) | 1 0 1 1 1 1 1 1 1 1
S[6][9] = V: sim, por exemplo 4 + 5. Para achar o subconjunto, volte de (n, t): se S[i-1][s] já é V, a_i ficou de fora; senão a_i entrou e s <- s - a_i.
Versão de uma linha (a da Lista 5): possivel[s], com s de t até a_i em ordem decrescente: possivel[s] <- possivel[s] ou possivel[s-a_i]. A ordem decrescente faz possivel[s-a_i] ainda ser o valor da linha i-1.
Complexidade: tempo Θ(nt); espaço Θ(nt), ou Θ(t) na versão de uma linha. É pseudo-polinomial: t pode ser exponencial no número de bits da entrada. SUBSET SUM é NP-completo; esta PD não prova P = NP.
