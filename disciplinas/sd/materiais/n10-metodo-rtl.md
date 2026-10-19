---
id: sd-nota-rtl
titulo: Nota — método de projeto RTL: FSM de alto nível, bloco operacional e bloco de controle
assunto: sd-10-projeto-rtl
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor); organiza o método usado nas listas e provas da disciplina
fontes_catalogo: vahid-sistemas-digitais,mit-ocw-6004,free-range-vhdl
autoria: Equipe TutorON, redigida com auxílio de IA, com texto próprio; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Projeto RTL (nível de transferência entre registradores)

Objetivo: transformar um algoritmo (com laços, variáveis e comparações) em hardware: bloco operacional (datapath) + bloco de controle (FSM).

Passo 1 — FSM de alto nível: estados com ações sobre registradores (soma = A + B; i = i + 1) e transições com condições sobre dados (i < N; a > b). Defina entradas, saídas e registradores locais com suas larguras em bits. Um estado de espera típico: "fica enquanto comece' e avança com comece".

Passo 2 — Bloco operacional: para cada registrador, um registrador de n bits com ld (e clr, se zera). Para cada operação, um componente (somador, subtrator, incrementador, deslocador). Para cada condição, um comparador que gera um sinal de status (i_lt_n, a_gt_b). Quando um registrador recebe valores de mais de uma fonte (soma = 0, soma = A + B ou soma = soma + C), coloque um MUX na entrada e um sinal de seleção. Indique a largura de cada ligação.

Passo 3 — Ligação: liste os sinais de controle (FSM → datapath: _ld, _clr, _sel, leitura e escrita de memória) e os de status (datapath → FSM).

Passo 4 — FSM de baixo nível: a mesma FSM, trocando cada ação por valores nos sinais de controle (soma = A + B vira soma_sel = 0, soma_ld = 1) e cada condição pelo sinal de status (i < N vira i_lt_n). Sinais não citados num estado valem 0. Depois, implemente como qualquer FSM (registrador de estado + lógica de próximo estado e de saída) ou em VHDL.

Cuidados de temporização: a atribuição feita num estado só aparece no registrador na borda de saída desse estado. Uma comparação feita no estado seguinte já enxerga o valor novo, mas não no mesmo estado em que o registrador foi carregado.

Exemplos clássicos da disciplina: média de dois números, soma de valores com limite, Fibonacci (a, b, i, N), MDC por subtrações sucessivas e média de um array em memória (endereço = base + i, soma acumulada, divisão por 2ᵏ com deslocamento).
