---
id: sd-av2-q05-06-08
titulo: Lista AV2 — média (A+B)/2, controle de bomba d'água e Fibonacci em RTL (Q5, Q6 e Q8)
assunto: sd-10-projeto-rtl
tipo: lista
resolucao: sim
questao: 5,6,8
fonte: Lista de SD AV2.pdf | páginas 2–3 | questões 5, 6 e 8
fontes_catalogo: ufal-sd-lista-av2
autoria: Enunciados: lista de exercícios da disciplina (UFAL). Resoluções: equipe TutorON
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Lista de SD AV2

5. Implemente um circuito que calcula a média de dois números A e B de 4 bits, (A + B)/2. A divisão por dois pode ser feita por deslocamento de bits (shift right). Todos os blocos devem ser implementados e mostrados.
Resolução: somador de 4 bits feito com somadores completos (ripple-carry), gerando Cout S3 S2 S1 S0. O deslocamento à direita é só fiação: média = Cout S3 S2 S1. Não descarte o Cout: 15 + 15 = 30 e 30/2 = 15 = 1111.

6. A mãe de Marquinhos quer um circuito que encha a caixa d'água sozinho. S0 e S1 são sensores de nível (1 quando detectam água). A bomba deve ligar quando a caixa estiver vazia e desligar quando estiver cheia; dois LEDs indicam bomba ligada e bomba desligada.
Resolução: precisa de memória, porque entre "vazia" e "cheia" a bomba mantém o estado anterior (histerese). Supondo S0 o sensor de baixo e S1 o de cima: liga quando S0 = 0 (vazia), desliga quando S1 = 1 (cheia) e mantém nos outros casos. Com um flip-flop B (bomba): B+ = S0' + B·S1'. LED_ligada = B; LED_desligada = B'. Confira a posição dos sensores no esquema do original.

8. Dada a máquina de estados de alto nível que implementa Fibonacci, apresente os blocos de controle e operacional e a máquina de estados de baixo nível. Entradas: N (16 bits), comece (1 bit). Saída: c (16 bits). Registradores: a, b, c (16 bits cada).
Resolução (esboço): bloco operacional com registradores a, b, c e um contador i, somador de 16 bits a + b, comparador i < N e MUX nas entradas dos registradores para escolher entre valor inicial e valor calculado. A FSM de baixo nível troca cada atribuição por sinais de controle (a_ld, a_sel, b_ld, i_ld, i_clr, c_ld) e cada condição por um sinal de status (i_lt_n). Implementação em VHDL do controlador: bloco sd-vhdl-fibonacci-controle.
