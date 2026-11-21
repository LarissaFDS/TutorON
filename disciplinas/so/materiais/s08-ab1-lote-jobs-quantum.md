---
id: so-ab1-lote-jobs-fcfs-sjf
titulo: AB1 — lote de jobs de 100, 30, 20, 240 e 120 s chegando juntos (FCFS × job mais curto primeiro); quantum grande ou pequeno; aging e inversão de prioridade
assunto: so-02-tarefas-escalonamento
tipo: prova
questao: 7 e 8
resolucao: sim
fonte: Prova AB1 (questões abertas), Prof. André Aquino (UFAL), conforme as respostas compartilhadas da turma; caderno do Prof. Maziero, cap. 2
fontes_catalogo: turma-respostas-so,maziero-caderno-2014,ufal-aquino-slides-so
autoria: Prova do Prof. André Aquino (UFAL); respostas da turma parafraseadas, conferidas e corrigidas pela equipe TutorON
licenca: Não declarada (prova e respostas da turma); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Prova AB1, questão 7 (parafraseada): cinco jobs de 100, 30, 20, 240 e 120 s chegam juntos (t = 0), nessa ordem. Qual o tempo médio de vida (*turnaround*) com FCFS e com o job mais curto primeiro (SJF)? Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**FCFS:** terminam em 100, 130, 150, 390 e 510 s. Média de vida $= (100 + 130 + 150 + 390 + 510)/5 = 1280/5 =$ **256 s**. Espera: 0, 100, 130, 150, 390 → média **154 s**.

**SJF:** ordem 20, 30, 100, 120, 240; terminam em 20, 50, 150, 270, 510. Média de vida $= 1000/5 =$ **200 s**. Espera: 0, 20, 50, 150, 270 → média **98 s**.

Como todos chegam juntos, o SJF minimiza o tempo médio de espera: os curtos deixam de esperar atrás dos longos.

**Questão 8 (quantum):** a favor do quantum **pequeno**: melhor tempo de resposta para tarefas interativas, e uma tarefa longa não segura o processador. A favor do quantum **grande**: menos trocas de contexto, então menos tempo perdido; tarefas orientadas a processamento terminam com menos sobrecarga. **Correção:** a resposta da turma diz que o quantum pequeno "evita inanição" e que o grande "favorece threads"; no Round-Robin ninguém sofre inanição com qualquer quantum, e o argumento correto é o da sobrecarga das trocas de contexto. A eficiência com troca de contexto $t_{tc}$ é $\frac{t_q}{t_q + t_{tc}}$ (fração útil de cada ciclo, para tarefas que usam o quantum todo).

**Aging:** a prioridade dinâmica de quem espera aumenta com o tempo, até que a tarefa seja escolhida; evita inanição. **Inversão de prioridade:** uma tarefa de alta prioridade espera um recurso preso por uma de baixa, que por sua vez é preemptada por uma de prioridade média (caso da sonda Mars Pathfinder). A **herança de prioridade** eleva temporariamente a tarefa de baixa prioridade à prioridade de quem espera.

**Verificação:** nas duas ordens a última tarefa termina em 510 s (soma das durações); a soma das esperas é a soma dos tempos de vida menos 510 (1280 − 510 = 770 → 154; 1000 − 510 = 490 → 98).
