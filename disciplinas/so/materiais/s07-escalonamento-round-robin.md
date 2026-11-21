---
id: so-escalonamento-round-robin
titulo: Round-Robin com quantum 2 — diagrama de Gantt e fila de prontas passo a passo, chegada das tarefas, tempo médio de espera e de vida
assunto: so-02-tarefas-escalonamento
tipo: lista
questao: caderno, cap. 2, questão 17 (f)
resolucao: sim
fonte: Lista 2 da turma (2021), sobre o caderno de exercícios do Prof. Maziero, cap. 2, questão 17
fontes_catalogo: turma-listas-2021,maziero-caderno-2014,ufal-aquino-slides-so
autoria: Exercício do caderno do Prof. Maziero; resolução de aluno conferida por simulação pela equipe TutorON
licenca: Exercício sob CC BY-NC-SA 3.0 (Maziero); resolução de aluno parafraseada
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Round-Robin (revezamento) com quantum $t_q = 2$, sem envelhecimento, para t1 (ingresso 0, duração 5), t2 (0, 4), t3 (3, 5), t4 (5, 6), t5 (7, 4). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Diagrama de Gantt do Round-Robin montado fatia por fatia. Regra: a tarefa executa até 2 unidades e volta ao **fim** da fila. Quem **chega** durante uma fatia entra na fila **antes** da tarefa que acabou de ser preemptada (convenção da resolução, a mesma do simulador).

| Fatia | Executa | Fila de prontas depois da fatia |
|---|---|---|
| [0, 2) | t1 | t2, t1 |
| [2, 4) | t2 | t1, t3, t2 (t3 chegou em 3) |
| [4, 6) | t1 | t3, t2, t4, t1 (t4 chegou em 5) |
| [6, 8) | t3 | t2, t4, t1, t5, t3 (t5 chegou em 7) |
| [8, 10) | t2 | t4, t1, t5, t3 — t2 termina em 10 |
| [10, 12) | t4 | t1, t5, t3, t4 |
| [12, 13) | t1 | t1 termina em 13 (só restava 1) |
| [13, 15) | t5 | t3, t4, t5 |
| [15, 17) | t3 | t4, t5, t3 |
| [17, 19) | t4 | t5, t3, t4 |
| [19, 21) | t5 | t5 termina em 21 |
| [21, 22) | t3 | t3 termina em 22 |
| [22, 24) | t4 | t4 termina em 24 |

Tempos de vida $T_t = \text{fim} - \text{ingresso}$: t1 13, t2 10, t3 19, t4 19, t5 14 → soma 75 → média **15 s**.
Tempos de espera $T_w = T_t - \text{duração}$: t1 8, t2 6, t3 14, t4 13, t5 10 → soma 51 → média **10,2 s**.

Erros comuns: (1) começar a contar a espera em t = 0 para quem chega depois; (2) colocar na fila uma tarefa que ainda não chegou; (3) esquecer que a última fatia de uma tarefa pode ser menor que o quantum.

Quantum pequeno melhora o tempo de resposta das interativas, mas aumenta a proporção de trocas de contexto; quantum muito grande faz o RR virar FCFS.

**Verificação:** $\sum T_t - \sum T_w = 75 - 51 = 24$, a soma das durações; cada tarefa recebe exatamente sua duração nas fatias da tabela. Simulado em `tests_acervo/so_verif.py`.
