---
id: c06
fonte: "Lista de Exercícios 2, questão 10(a) — resolução de alunos (método de desenvolver/iterar a recorrência)"
tipo: resolucao_lista
topico: recorrências, método da iteração
---
10. (a) Mostre que a solução de T(n) = T(n − 1) + n; T(1) = 1 é O(n²).

Solução: Desenvolvendo a recorrência, temos que:
  T(n)     = T(n − 1) + n        (1)
  T(n − 1) = T(n − 2) + n − 1    (2)
  T(n − 2) = T(n − 3) + n − 2    (3)
De (1) e (2): T(n) = T(n − 2) + (n − 1) + n
De (3) e (4): T(n) = T(n − 3) + (n − 2) + (n − 1) + n
  ...
  T(n) = T(n − k) + (n − k + 1) + (n − k + 2) + ... + (n − 1) + n
Neste caso, o algoritmo encerra quando n − k = 1 ⇒ k = n − 1
  T(n) = T(1) + 2 + 3 + ... + (n − 2) + (n − 1) + n
  T(n) = 1 + 2 + 3 + ... + (n − 2) + (n − 1) + n  ⇒  T(n) = n·(n + 1)/2
Para mostrar que T(n) é O(n²) basta definir f(n) = n·(n+1)/2 e g(n) = n², sendo assim basta
encontrar n0 e c, tais que f(n) < c·g(n), ∀n ≥ n0; neste sentido, basta tomar n0 = 1 e c = 3,
por exemplo. Neste caso, vemos que T(n) = O(n²).
