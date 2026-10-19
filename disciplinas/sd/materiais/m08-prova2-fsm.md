---
id: sd-prova2-q1-2
titulo: Prova 2 — saída Q do flip-flop D e implementação da máquina de estados A, B, C, D (Q1–Q2)
assunto: sd-09-maquinas-de-estados
tipo: prova
resolucao: sim
questao: 1-2
fonte: Prova 2.pdf | página 1 | questões 1 e 2 (transições lidas da figura)
fontes_catalogo: ufal-sd-prova2
autoria: Enunciado: prova da disciplina (UFAL). Descrição da figura e resolução: equipe TutorON, conferidas por simulação em código
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: aprovado
---
Prova 2 — Sistemas Digitais

1. (1,0) Dado o diagrama de tempo (CLK e D), mostre o diagrama da saída Q de um flip-flop D. Método: Q copia D em cada borda de subida do clock e fica constante até a próxima borda.

2. (2,0) Implemente o circuito da máquina de estados. Entradas a, b; saída y.
Máquina da figura (Moore): estado inicial A (y = 0). Em A: a → fica em A; a'b → B; a'b' → C. Em B (y = 1): a' → fica em B; a → C. Em C (y = 1): b' → fica em C; b → D. Em D (y = 0): vai para A no próximo clock.

Resolução. Codificação s1s0: A = 00, B = 01, C = 10, D = 11 (dois flip-flops D).
Tabela de próximo estado (n1 n0):
- A (00): a = 1 → 00; a = 0, b = 1 → 01; a = 0, b = 0 → 10.
- B (01): a = 0 → 01; a = 1 → 10.
- C (10): b = 0 → 10; b = 1 → 11.
- D (11): → 00.

Equações:
- n1 = s1'·s0'·a'·b' + s1'·s0·a + s1·s0'
- n0 = s1'·s0'·a'·b + s1'·s0·a' + s1·s0'·b
- y = s1'·s0 + s1·s0' = s1 ⊕ s0 (vale 1 só em B e C)

Circuito: registrador de estado com 2 flip-flops D (clock comum e reset para 00), lógica combinacional de n1 e n0 nas entradas D e uma XOR para y.

**Verificação:** simulando as 16 combinações (estado, a, b), as equações reproduzem todas as transições da figura (teste automatizado em tests_acervo/test_disciplinas.py).
