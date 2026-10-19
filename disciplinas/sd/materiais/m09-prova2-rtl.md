---
id: sd-prova2-q3-4
titulo: Prova 2 — registrador com MUX controlado por T e projeto RTL da soma com limite 5096 (Q3–Q4)
assunto: sd-10-projeto-rtl
tipo: prova
resolucao: sim
questao: 3-4
fonte: Prova 2.pdf | página 1 | questões 3 e 4 (figuras descritas pela equipe)
fontes_catalogo: ufal-sd-prova2
autoria: Enunciado: prova da disciplina (UFAL). Descrição das figuras e esboço de resolução: equipe TutorON
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: candidato
natureza: material_da_disciplina
verificacao: nao_verificada
revisao_humana: pendente
---
Prova 2 — Sistemas Digitais (continuação)

3. (2,0) Explique o funcionamento do circuito em função do controle T, das entradas x e das saídas a. O clock controla quando há fluxo de dados.
Figura: três flip-flops D em cadeia (saídas a2, a1, a0), cada um com um MUX 4:1 na entrada D, todos selecionados por T; a entrada x chega ao primeiro MUX. A função exata de cada entrada do MUX (manter, deslocar, carregar x ou zerar) deve ser lida na figura original. Método: para cada valor de T, siga qual sinal chega ao D de cada flip-flop e descreva a operação do registrador na borda do clock.

4. (3,0) Dada a máquina de estados de alto nível, apresente os blocos de controle e operacional e a máquina de baixo nível.
Entradas: A, B, C (16 bits); comece, rst (bit). Saída: S (16 bits). Registrador local: soma.
FSM da figura: S0 (S = 0, soma = 0) → S1, que espera comece (fica com comece', avança com comece) → S2 (soma = A + B) → S3 (soma = soma + C) → S4, que volta a S2 se soma < 5096 e a S0 se (soma < 5096)'. A figura não mostra outra atribuição a S; confira no original.

Esboço de resolução:
- Bloco operacional: registrador soma (16 bits) com soma_ld e soma_clr; somadores A + B e soma + C; MUX 2:1 na entrada de soma (soma_sel escolhe A + B ou soma + C); comparador soma < 5096 (constante 0001 0011 1110 1000₂), que gera o status soma_lt; registrador S com S_clr.
- FSM de baixo nível: S0: soma_clr = 1, S_clr = 1. S1: espera comece. S2: soma_sel = 0, soma_ld = 1. S3: soma_sel = 1, soma_ld = 1. S4: transição por soma_lt.
- Cada atribuição da FSM de alto nível vira sinal de carga/seleção e cada condição vira um sinal de status do bloco operacional.
