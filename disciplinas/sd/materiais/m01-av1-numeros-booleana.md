---
id: sd-av1-q01-07
titulo: Lista AV1 — operações binárias, complemento de 2, álgebra booleana e Karnaugh (Q1–Q7)
assunto: sd-01-numeracao-aritmetica
tipo: lista
resolucao: sim
questao: 1-7
fonte: Lista de SD AV1.pdf | páginas 1–2 | questões 1 a 7
fontes_catalogo: ufal-sd-lista-av1
autoria: Enunciados: lista de exercícios da disciplina (UFAL). Resoluções: equipe TutorON, conferidas por código (tests_acervo/test_disciplinas.py)
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: aprovado
---
Lista de Exercícios de Sistemas Digitais — AV1 (operações com números binários; álgebra booleana e expressões lógicas)

1. Efetue com números binários: a) 11001 + 1011; b) 10010 − 10001; c) 1100 × 011.
Resolução: a) 25 + 11 = 36 = 100100₂. b) 18 − 17 = 1 = 00001₂. c) 12 × 3 = 36 = 100100₂.

2. Determine o complemento de 2 do número 101010.
Resolução (6 bits): inverter os bits → 010101; somar 1 → 010110. Conferência: 101010₂ = 42 e 2⁶ − 42 = 22 = 010110₂.

3. Determine o complemento de 2 do número −16.
Resolução: depende do número de bits, que a questão não fixa. Em 5 bits, −16 = 10000 (o menor valor representável, de −16 a 15); em 6 bits, 110000; em 8 bits, 11110000. Caminho: 16 = 010000 (6 bits) → inverte 101111 → soma 1 → 110000.

4. Quantas entradas diferentes podemos ter com 4 bits? Resolução: 2⁴ = 16 combinações (0000 a 1111).

5. Determine a expressão do circuito da figura e monte a tabela-verdade. (A figura do circuito não foi transcrita; conferir no original.)

6. Simplifique S = (A⊕B)[B(A + C) + D(A + B + C)] e desenhe o circuito simplificado.
Resolução: S = 1 só nos mintermos 5, 6, 7, 9 e 11 (ordem ABCD). Com A⊕B = 1: se A = 0 e B = 1, o colchete vale C + D; se A = 1 e B = 0, vale D. Logo S = A'B(C + D) + AB'D = **(A⊕B)·D + A'BC**.

7. Simplifique por Veitch-Karnaugh:
a) S = 1 nas linhas ABC = 000, 001, 011, 101, 111 → S = Σm(0,1,3,5,7). Grupos: coluna C = 1 (m1, m3, m5, m7) e par A'B' (m0, m1). **S = C + A'B'**.
b) S = 1 em 000, 011, 101; irrelevante (x) em 001, 100, 110, 111. Usando x: B' cobre m0, m1, m4, m5 e C cobre m1, m3, m5, m7. **S = B' + C** (m2 = 010 continua 0).
