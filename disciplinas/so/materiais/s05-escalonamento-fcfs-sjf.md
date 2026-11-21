---
id: so-escalonamento-fcfs-sjf
titulo: Escalonamento FCFS e SJF cooperativos — diagrama de Gantt, tempo médio de vida (turnaround) e de espera
assunto: so-02-tarefas-escalonamento
tipo: lista
questao: caderno, cap. 2, questão 17 (a) e (b)
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
Caderno do Prof. Maziero, cap. 2, questão 17. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

| Tarefa | t1 | t2 | t3 | t4 | t5 |
|---|---|---|---|---|---|
| ingresso | 0 | 0 | 3 | 5 | 7 |
| duração | 5 | 4 | 5 | 6 | 4 |
| prioridade | 2 | 3 | 5 | 9 | 6 |

Convenções: trocas de contexto nulas; empate vai para a tarefa de menor índice; prioridade maior = número maior.

Definições: tempo de vida (*turnaround*) $T_t = \text{fim} - \text{ingresso}$; tempo de espera $T_w = T_t - \text{duração}$ (tempo na fila de prontas).

**(a) FCFS cooperativo** (ordem de chegada, sem preempção). Gantt: t1 [0, 5), t2 [5, 9), t3 [9, 14), t4 [14, 20), t5 [20, 24).
$T_t$: 5, 9, 11, 15, 17 → soma 57 → média **11,4 s**. $T_w$: 0, 5, 6, 9, 13 → soma 33 → média **6,6 s**.

**(b) SJF cooperativo** (entre as **prontas** naquele instante, a mais curta; quem começa vai até o fim).
- t = 0: prontas t1 (5) e t2 (4) → t2 [0, 4).
- t = 4: prontas t1 (5) e t3 (5) → empate, menor índice → t1 [4, 9).
- t = 9: prontas t3 (5), t4 (6), t5 (4) → t5 [9, 13); depois t3 [13, 18) e t4 [18, 24).
$T_t$: t1 9, t2 4, t3 15, t4 19, t5 6 → soma 53 → média **10,6 s**. $T_w$: 4, 0, 10, 13, 2 → soma 29 → média **5,8 s**.

Erro comum: escolher a tarefa mais curta entre **todas**, inclusive as que ainda não chegaram (t5 não pode executar antes de t = 7).

**Verificação:** em cada política a soma das durações é 5 + 4 + 5 + 6 + 4 = 24 = instante de término da última tarefa (não há ociosidade); e $\sum T_t - \sum T_w = 24$ (57 − 33 e 53 − 29). Simulado em `tests_acervo/so_verif.py`.
