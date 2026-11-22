---
id: sd-ecom012-listas-1-3
titulo: Circuitos Digitais (ECOM012), listas das aulas 1 a 3 — bases, complemento de 2, famílias lógicas, funções booleanas e NAND
assunto: sd-01-numeracao-aritmetica
tipo: lista
resolucao: sim
questao: aulas 1-3
fonte: Listas de exercícios das aulas 1, 2 e 3 de Circuitos Digitais (UFAL) | enunciados parafraseados
fontes_catalogo: ufal-ecom012-listas
autoria: Enunciados: listas da disciplina Circuitos Digitais (UFAL), professor não identificado. Resoluções: equipe TutorON com apoio de IA
licenca: Não declarada (lista da disciplina; original não versionado)
publicacao_transcricao: não autorizada; enunciados parafraseados, figuras descritas em texto
curadoria: aprovado
natureza: material_da_disciplina
revisao_humana: pendente
verificacao: parcial
---
Circuitos Digitais (ECOM012) — listas das aulas 1 a 3

Aula 1. (1) 1001101001₂ em decimal, octal e hexadecimal: **617**, **1151₈**, **269₁₆**. (2) Converta 1984, 4000 e 8192 para binário, octal e hexadecimal e de volta: 1984 = 11111000000₂ = 3700₈ = 7C0₁₆; 4000 = 111110100000₂ = 7640₈ = FA0₁₆; 8192 = 2¹³ = 10000000000000₂ = 20000₈ = 2000₁₆. (3) 100 = 1100100₂ = 144₈ = 64₁₆. (4) Com k dígitos na base R há Rᵏ valores (0 a Rᵏ − 1), ou seja, Rᵏ − 1 inteiros positivos. (5) Em 8 bits, complemento de 2: 11111111 = −1 e 00000000 = 0. A ordem dos operandos da subtração não fica clara no PDF: 00000000 − 11111111 = 0 − (−1) = **00000001**; 11111111 − 00000000 = **11111111** (−1). Soma: 11111111 + 11111111 = −2 = **11111110**; o vai-um final é descartado e não há overflow, porque os carries que entram e saem do bit de sinal valem 1.

Aula 2. Famílias lógicas são tecnologias de construção de portas (TTL, CMOS, ECL), com tensões, atraso e consumo próprios. O produto velocidade × potência compara famílias: ganhar velocidade costuma custar consumo. Circuitos digitais não são imunes a ruído, mas o toleram dentro da margem de ruído dos níveis lógicos. Pela tabela-verdade, X = XY + XY' (vale X nas 4 linhas).

Aula 3. Há 2^(2^n) funções de n variáveis: **256** com 3 e **65 536** com 4. AND = NAND seguida de NAND usada como inversor (2 portas). OR = NAND(A', B'), com as duas negações feitas por NAND (3 portas). XOR com 4 NAND: N = NAND(A,B); saída = NAND(NAND(A,N), NAND(B,N)).

**Verificação:** contas e portas conferidas em tests_acervo/test_sd_ecom012.py; as respostas discursivas da aula 2 não têm conferência por código.
