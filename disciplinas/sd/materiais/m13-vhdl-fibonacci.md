---
id: sd-vhdl-fibonacci-controle
titulo: VHDL — controlador (FSM) do Fibonacci em RTL, com pontos de atenção
assunto: sd-11-hdl-vhdl
tipo: resolucao
resolucao: sim
fonte: fibonacci_vhdl.vhd | entidade FibonacciControl (resumo do código; autoria do arquivo não identificada)
fontes_catalogo: ufal-sd-fibonacci-vhdl
autoria: Código: arquivo de resolução recebido pela equipe (autor não identificado). Resumo e análise: equipe TutorON
licenca: Não declarada (material original da disciplina)
publicacao_transcricao: autorizada pela responsável pela curadoria em 2026-10-21, só para esta transcrição Markdown; não é licença aberta; arquivo original fora do repositório; aprovação do professor ou monitor não declarada
curadoria: aprovado
natureza: material_da_disciplina
verificacao: nao_verificada
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Controlador VHDL do Fibonacci (questão 8 da Lista AV2)

Entidade FibonacciControl: entradas clk, reset, comece e o status i_lt_n (i < N, vindo do bloco operacional); saídas de controle load_a, load_b, load_i, load_a_initial, load_b_initial, load_i_initial, load_counter_initial, load_counter_increment, load_temp, load_resultado.

Estados (type state_type): IDLE, INIT, COMPUTE1, COMPUTE2, COMPUTE3, DONE.

Estrutura em três processos:
1. Registrador de estado: process(clk, reset) com reset assíncrono para IDLE; em rising_edge(clk), state <= next_state.
2. Próximo estado (combinacional), process(state, comece, i_lt_n): IDLE → INIT se comece = '1'; INIT → COMPUTE1 → COMPUTE2 → COMPUTE3; COMPUTE3 → COMPUTE1 se i_lt_n = '1', senão DONE; DONE → IDLE; when others → IDLE.
3. Saídas: em rising_edge(clk), todas as saídas vão a '0' e depois o case liga as do estado: IDLE carrega os valores iniciais (load_*_initial, load_a, load_b, load_i); COMPUTE1: load_temp (temp = a + b); COMPUTE2: load_a; COMPUTE3: load_b e load_counter_increment; DONE: load_resultado.

Pontos de atenção (análise da equipe; confira com o professor):
- As saídas são geradas dentro de rising_edge(clk), então ficam registradas: cada sinal sai um ciclo depois de o estado mudar. Em uma FSM de Moore comum, as saídas dependem só de state em um processo combinacional (process(state)). Do jeito que está, o bloco operacional recebe load_temp quando a FSM já está em COMPUTE2, e assim por diante.
- O estado IDLE ativa as cargas iniciais em todo ciclo de espera. Funciona, mas é mais claro inicializar só no estado INIT, que hoje só repete zeros já atribuídos.
- use ieee.std_logic_unsigned não é padrão IEEE; em código novo prefira ieee.numeric_std.
