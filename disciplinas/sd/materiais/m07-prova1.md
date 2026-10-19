---
id: sd-prova1
titulo: Prova 1 — conversor D/A, atraso, jogo BATALHA, if/else em hardware e subtrator sem sinal
assunto: sd-05-circuitos-aritmeticos
tipo: prova
resolucao: sim
questao: 1-5
fonte: prova1.docx | questões 1 a 5 (figuras do circuito de alarme não transcritas)
fontes_catalogo: ufal-sd-prova1
autoria: Enunciados: prova da disciplina (UFAL). Resoluções: equipe TutorON, conferidas por código
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
revisao_humana: pendente
---
Prova 1 — Sistemas Digitais

1. (1,5) Um conversor D/A de cinco bits tem saída em corrente. Para a entrada 10100₂ produz 10 mA. Qual a corrente para 11101₂?
Resolução: a saída é proporcional ao valor digital. 10100₂ = 20 → 10 mA, logo 0,5 mA por degrau. 11101₂ = 29 → 29 × 0,5 = **14,5 mA**.

2. (1,5) Circuito de alarme de um sistema de tempo real com atrasos típicos AND = 3, OR = 4 e NOT = 1 (u.t.). Após simplificar o circuito, qual o atraso máximo? (O circuito está em figura não transcrita.) Método: simplificar a expressão e somar os atrasos das portas no caminho mais longo da entrada à saída.

3. (2,0) Jogo BATALHA: palavras A (A1A0) e B (B1B0) de 2 bits, botão Enable E e LEDs LEDA e LEDB. Com E = 0 os LEDs ficam apagados. Com E = 1, acende o LED de quem tiver a maior carta; no empate, os dois.
Resolução: comparador de 2 bits. LEDA = E·(A ≥ B) e LEDB = E·(B ≥ A), com A > B = A1B1' + (A1 ⊙ B1)·A0B0' e A = B = (A1 ⊙ B1)(A0 ⊙ B0), onde ⊙ é XNOR.

4. (2,5) Projete o circuito de: if (F == G) result = y + x; else result = z + w; com x, y, w, z de 4 bits e F, G de 8 bits. Não é preciso detalhar MUX e comparadores; indique a largura de cada linha.
Resolução: comparador de igualdade de 8 bits (F, G → eq). Opção econômica: dois MUX 2:1 de 4 bits escolhem os operandos (y ou z; x ou w) com seleção eq, e um único somador de 4 bits gera result com 5 bits (4 + vai-um). Opção direta: dois somadores e um MUX 2:1 de 5 bits na saída.

5. (2,5) Subtrator de 4 bits para números SEM SINAL, com o segundo número sempre menor que o primeiro (resultado positivo).
Resolução: S = A + B' + 1, com somador de 4 bits, inversores em B e Cin = 1. O vai-um final é descartado (vale 1 sempre que A ≥ B). Como A ≥ B, não há resultado negativo.
