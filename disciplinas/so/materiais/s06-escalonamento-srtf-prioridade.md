---
id: so-escalonamento-srtf-prioridades
titulo: Escalonamento SJF preemptivo (SRTF) e por prioridades cooperativo e preemptivo — passo a passo
assunto: so-02-tarefas-escalonamento
tipo: lista
questao: caderno, cap. 2, questão 17 (c), (d) e (e)
resolucao: sim
fonte: Lista 2 da turma (2021), sobre o caderno de exercícios do Prof. Maziero, cap. 2, questão 17
fontes_catalogo: turma-listas-2021,maziero-caderno-2014,ufal-aquino-slides-so,ufal-aquino-prova2-fotos
autoria: Exercício do caderno do Prof. Maziero; resolução de aluno conferida por simulação pela equipe TutorON
licenca: Exercício sob CC BY-NC-SA 3.0 (Maziero); resolução de aluno parafraseada
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Mesmas tarefas da questão 17 do caderno: t1 (ingresso 0, duração 5, prioridade 2), t2 (0, 4, 3), t3 (3, 5, 5), t4 (5, 6, 9), t5 (7, 4, 6); prioridade maior = número maior. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**(c) SRTF (SJF preemptivo):** a cada chegada, compara a duração da que chegou com o **tempo restante** da que executa.
- t2 [0, 4). Em t = 3 chega t3 (5) e t2 só tem 1 restante: continua.
- t = 4: t1 (5) e t3 (5) → empate, t1 [4, 9). Em t = 5 chega t4 (6 > 4 restantes); em t = 7 chega t5 (4 > 2 restantes): t1 não é interrompida.
- t5 [9, 13), t3 [13, 18), t4 [18, 24).
Aqui SRTF dá o mesmo resultado que o SJF cooperativo: média de vida **10,6 s**, de espera **5,8 s**.

**(d) PRIO cooperativo:** t2 [0, 4) (prioridade 3 > 2); t = 4: t3 (5) > t1 → t3 [4, 9); t = 9: t4 (9) → [9, 15); t5 (6) [15, 19); t1 [19, 24).
$T_t$: t1 24, t2 4, t3 6, t4 10, t5 12 → média **11,2 s**. $T_w$: 19, 0, 1, 4, 8 → média **6,4 s**.

**(e) PRIO preemptivo:** quem chega com prioridade maior toma o processador.
- t2 [0, 3); t3 chega (5 > 3) → t3 [3, 5); t4 chega (9) → t4 [5, 11); em t = 7, t5 (6) não supera t4.
- t = 11: t5 (6) → [11, 15); t3 [15, 18); t2 [18, 19); t1 [19, 24).
$T_t$: t1 24, t2 19, t3 15, t4 6, t5 8 → média **14,4 s**. $T_w$: 19, 15, 10, 0, 4 → média **9,6 s**.

Observe a **inanição**: t1, de menor prioridade, espera 19 s. O envelhecimento (*aging*) aumenta a prioridade de quem espera para evitar isso. Por isso, na Prova 2 do Prof. André Aquino (questão 2, gabarito da turma conferido), a afirmação incorreta é a de que prioridades com múltiplas filas garantem a todas as tarefas sua fatia de tempo: sem envelhecimento, as filas de baixa prioridade podem sofrer inanição.

**Verificação:** nas três políticas $\sum T_t - \sum T_w = 24$, a soma das durações (53 − 29, 56 − 32, 72 − 48); simulado em `tests_acervo/so_verif.py`.
