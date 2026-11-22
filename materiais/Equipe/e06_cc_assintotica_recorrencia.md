---
id: e06
titulo: Comparar funções com O, Ω e Θ e resolver T(n) = n³ + T(n/3) (prova 1 de PAA, Ciência da Computação)
assunto: b1-01-corretude-complexidade
autoria: Equipe TutorON (não é material do professor); enunciado parafraseado de uma prova 1 de PAA da turma de Ciência da Computação da UFAL (2012), resolução da equipe com auxílio de IA
revisado: false
---
Curso: Ciência da Computação (UFAL), prova 1 de PAA de 2012. Status da resolução: validada pela equipe (contas conferidas em Python); revisão humana pendente.
Para cada par (A, B), diga se A é O, Ω ou Θ de B. Regra prática: calcule lim A/B quando n → ∞. Limite constante positivo → Θ; limite 0 → O (e não Ω); limite infinito → Ω (e não O).
(a) A = n^4 + 100n^3, B = n^3 + 100n^4: A/B → 1/100. A = Θ(B).
(b) A = 2^n, B = 3^(n/2) = (√3)^n ≈ 1,732^n: A/B = (2/√3)^n → ∞. A = Ω(B), mas não Θ.
(c) A = log_3(n^2) = 2 log_3 n, B = log_2(n^3) = 3 log_2 n: a razão é a constante 2/(3 log_2 3) ≈ 0,42. A = Θ(B): mudar a base do log só muda a constante.
(d) A = (log_2 n)^2, B = log_2(n^2) = 2 log_2 n: A/B = (log_2 n)/2 → ∞. A = Ω(B).
(e) A = n log_3 n, B = n log_4 n: razão constante log 4/log 3 ≈ 1,26. A = Θ(B).
(f) A = log_2 log_2 n, B = √(log_2 n): com m = log_2 n, log m/√m → 0. A = O(B).
(g) A = log_2(n!), B = log_2(3^n) = n log_2 3: pela fórmula de Stirling, log n! = Θ(n log n), então A/B → ∞. A = Ω(B).
Recorrência: T(n) = T(n/3) + n^3, T(1) = 0 (inspeciona n^3 elementos e chama com n/3).
Teorema Mestre: a = 1, b = 3, f(n) = n^3 e n^(log_3 1) = n^0 = 1. f(n) = Ω(n^(0+ε)) com ε = 3: caso 3. Regularidade: a f(n/b) = (n/3)^3 = n^3/27 ≤ c f(n) com c = 1/27 < 1. Logo T(n) = Θ(n^3).
Por iteração, com n = 3^x: T(n) = n^3 (1 + 1/27 + 1/27^2 + ... + 1/27^(x-1)) = (27/26)(n^3 − 1).
Pegadinha: "a função chama a si mesma log n vezes" não é a complexidade; o que manda é a soma dos custos de cada nível.
**Verificação:** a fórmula fechada bate com a recorrência para n = 3, 9, 27 e 81 (T(3) = 27, T(9) = 756), e os limites foram conferidos numericamente em Python.
