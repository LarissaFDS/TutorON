---
id: sd-av1-q14-18
titulo: Lista AV1 — subtratores, overflow, comparador de magnitude e display de 7 segmentos (Q14–Q18)
assunto: sd-05-circuitos-aritmeticos
tipo: lista
resolucao: sim
questao: 14-18
fonte: Lista de SD AV1.pdf | páginas 3–4 | questões 14 a 18
fontes_catalogo: ufal-sd-lista-av1
autoria: Enunciados: lista de exercícios da disciplina (UFAL). Resoluções: equipe TutorON
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: aprovado
---
Lista de SD AV1 — Circuitos Lógico-Aritméticos e Decodificadores

14. Com um somador de 5 bits pronto, faça um subtrator e acrescente um detector de overflow na saída.
Resolução: A − B = A + B' + 1: inverter cada bit de B (5 portas NOT, ou XOR com o sinal de subtração) e pôr Cin = 1. Em complemento de 2, há overflow quando A e B' têm o mesmo sinal e o resultado tem sinal diferente: V = C4 ⊕ C5 (vai-um que entra e que sai do bit de sinal), ou V = a4·b4'·s4' + a4'·b4·s4.

15. Com um subtrator pronto, crie um circuito para MAX(0, X − Y), com X e Y em complemento de 2.
Resolução: calcular D = X − Y; se o bit de sinal de D for 1 (negativo), a saída é 0. Saída = D AND (sinal de D)' bit a bit, ou MUX 2:1 escolhendo entre D e 0. Se puder haver overflow, o sinal correto é d_n ⊕ V.

16. Desenvolva um subtrator de 5 bits com somadores de 5 bits e portas lógicas. Mesmo esquema da Q14: B passa por inversores e Cin = 1.

17. Comparador de magnitude para A e B positivos de 4 bits, com saídas A = B, A > B e A < B.
Resolução: igualdade bit a bit eᵢ = (aᵢ ⊕ bᵢ)'; A = B = e3·e2·e1·e0. A > B = a3b3' + e3·a2b2' + e3e2·a1b1' + e3e2e1·a0b0'. A < B = (A > B + A = B)'.

18. Decodificador para display de 7 segmentos que recebe 2 bits (0 a 3) e mostra o número. Para o 1 acendem os segmentos b e c.
Resolução (x1 x0 → número): 0 = a,b,c,d,e,f; 1 = b,c; 2 = a,b,d,e,g; 3 = a,b,c,d,g. Equações: b = 1; a = d = x1 + x0'; c = x1' + x0; e = x0'; f = x1'·x0'; g = x1.
