---
id: sd-av2-q01-04-07
titulo: Lista AV2 — flip-flop D, máquina de estados e circuitos sequenciais (Q1–Q4 e Q7)
assunto: sd-07-latches-flip-flops
tipo: lista
resolucao: nao
questao: 1-4,7
fonte: Lista de SD AV2.pdf | páginas 1–3 | questões 1, 2, 3, 4 e 7
fontes_catalogo: ufal-sd-lista-av2
autoria: Enunciados: lista de exercícios da disciplina (UFAL); figuras não transcritas
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: aprovado
---
Lista de Exercícios de Sistemas Digitais — AV2 (circuitos sequenciais)

1. Dado o diagrama de tempo de entrada (CLK e D, na figura), mostre o diagrama de tempo da saída Q de um flip-flop D.
Como resolver: o flip-flop D só muda na borda ativa do clock (normalmente a de subida). Em cada borda, Q passa a valer o D daquele instante e fica constante até a próxima borda, mesmo que D mude no meio do ciclo. Pulsos de D que começam e terminam entre duas bordas não aparecem em Q. Antes da primeira borda, Q é desconhecido, a menos que haja reset.

2. Implemente o circuito da máquina de estados da figura. (A mesma questão caiu na Prova 2; ver o bloco sd-prova2-q1-2, que descreve a máquina e traz a resolução.)

3. Explique o funcionamento do circuito da figura em função do controle T, das entradas x e das saídas a. O sinal clock controla o momento em que ocorre o fluxo de dados. (Figura: flip-flops D com MUX na entrada de cada um, selecionados por T; igual à questão 3 da Prova 2.)
Como analisar: para cada valor de T, veja qual entrada do MUX chega ao D de cada flip-flop: a própria saída (manter), a saída do vizinho (deslocar) ou x (carregar). Monte uma tabela T → operação do registrador.

4. Dada a máquina de estados de alto nível da figura, apresente os blocos de controle e operacional e a máquina de estados de baixo nível para implementá-la. (Método RTL: ver os blocos sobre projeto RTL.)

7. Explique resumidamente o que faz o circuito da figura em função da entrada ld e das saídas tc e C. A entrada no triângulo é o clock.
Pista: ld (load) costuma carregar um valor no registrador; tc (terminal count) indica que um contador chegou ao valor final; C é o valor de contagem. Descreva o que acontece em cada borda de clock com ld = 1 e com ld = 0.
