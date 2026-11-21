---
id: so-impasses-quatro-condicoes
titulo: Impasses (deadlock) — as quatro condições necessárias, prevenção, ordem global de travas, algoritmo do banqueiro; 4 recursos e 3 tarefas com máximo 2
assunto: so-04-coordenacao-impasses
tipo: prova
questao: AB1, questão 10; AB1 2020.1, questão 7
resolucao: sim
fonte: Prova AB1 (respostas compartilhadas da turma) e prova AB1 de 2020.1, Prof. André Aquino (UFAL); slides de coordenação entre tarefas; programa em tests_acervo/c_so/ordem_travas.c
fontes_catalogo: turma-respostas-so,ufal-aquino-ab-2020-1,ufal-aquino-slides-so,maziero-socm-2013
autoria: Provas do Prof. André Aquino (UFAL); respostas de alunos parafraseadas, conferidas e corrigidas pela equipe TutorON
licenca: Não declarada (provas); slides sob CC BY-NC-SA 4.0; paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Provas AB1 do Prof. André Aquino. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Impasse:** um conjunto de tarefas em que cada uma espera um recurso preso por outra do conjunto; nenhuma avança. As **quatro condições necessárias** (todas ao mesmo tempo):
1. **Exclusão mútua:** o recurso só pode ser usado por uma tarefa por vez.
2. **Posse e espera:** a tarefa segura recursos enquanto pede outros.
3. **Não preempção:** o recurso não pode ser tirado de quem o detém.
4. **Espera circular:** existe um ciclo t1 → t2 → … → t1 de esperas.

**Prevenção:** negar uma das quatro. A mais usada na prática quebra a **espera circular** com uma **ordem global**: toda tarefa pede as travas na mesma ordem (em `ordem_travas.c`, sempre `conta_a` antes de `conta_b`, nos dois sentidos da transferência). Quebrar posse e espera: pedir tudo de uma vez. Não preempção: liberar o que tem se o pedido falhar. **Evitar:** só conceder se o estado continuar **seguro** (algoritmo do banqueiro). **Detectar e recuperar:** procurar ciclos no grafo de alocação e abortar ou preemptar.

**AB1, questão 10:** 4 recursos iguais, 3 tarefas, cada uma usa no máximo 2. Prova: impasse exigiria todas esperando, cada uma com no máximo 1 recurso; isso usa no máximo $3 \times 1 = 3 < 4$ recursos, então sobra 1, que completa alguma tarefa; ela termina e libera 2. Regra geral: sem impasse se $n(m - 1) < R$ (aqui $3 \times 1 < 4$).

**Correção:** a resposta da turma "distribui igualmente" os recursos como se o sistema escolhesse a ordem; a prova precisa considerar o **pior caso** de alocação, como acima. Na AB1 de 2020.1 (questão 7), a resposta da turma diz que, para negar a exclusão mútua, um processo gerenciador "elimina a necessidade de acesso exclusivo"; isso é o *spooling*: o acesso continua exclusivo, mas só o gerenciador o detém.

**Verificação:** o estado (alocado 1, 1, 1; máximo 2, 2, 2; livre 1) é seguro pelo banqueiro em `tests_acervo/so_verif.py`; com 3 recursos (livre 0) não é.
