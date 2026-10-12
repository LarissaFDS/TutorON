---
id: c05
fonte: "Lista de Exercícios 2 (Cap. 2 — Complexidade de Algoritmos), questão 9 — resolução de alunos"
tipo: resolucao_lista
topico: recorrências, contagem
---
9. Considere o algoritmo recursivo ASTERISCO(n). Para um dado valor de n, quantos asteriscos
serão impressos em uma chamada de ASTERISCO(n)?

Solução: Considerando A(n) como a quantidade de asteriscos impressos dado um valor n, temos que:

  A(n) = 0,                se n = 0
  A(n) = 2^(n+1) − (n + 2), se n ≥ 1

Como exemplo, temos:
  Para n = 1, 2^2 − (1+2) = 4 − 3 = 1 asterisco impresso;
  Para n = 2, 2^3 − (2+2) = 8 − 4 = 4 asteriscos impressos;
  Para n = 3, 2^4 − (3+2) = 16 − 5 = 11 asteriscos impressos;
  Para n = 4, 2^5 − (4+2) = 32 − 6 = 26 asteriscos impressos;
  ...
  Para n = i, 2^(i+1) − (i+2) asteriscos impressos.
