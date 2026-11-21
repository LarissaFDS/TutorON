---
id: so-tarefas-processos-threads-estados
titulo: Tarefas — diferença entre processo e thread, PCB/TCB, estados e transições, troca de contexto, modelos de threads N:1, 1:1 e N:M
assunto: so-02-tarefas-escalonamento
tipo: lista
questao: caderno, cap. 2, questões 1 a 12
resolucao: sim
fonte: Lista 2 da turma (2021) e respostas compartilhadas da turma, sobre o caderno do Prof. Maziero, cap. 2; slides do Prof. André Aquino (UFAL), gerência de tarefas
fontes_catalogo: turma-listas-2021,turma-respostas-so,maziero-caderno-2014,maziero-socm-2013,ufal-aquino-slides-so
autoria: Resoluções de alunos sobre exercícios do caderno do Prof. Maziero; paráfrase, conferência e correção da equipe TutorON
licenca: Exercícios do caderno sob CC BY-NC-SA 3.0 (Maziero); resoluções de alunos sem licença declarada, parafraseadas
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
Exercícios do cap. 2 do caderno do Prof. Maziero. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor. O livro chama de **tarefa** cada fluxo de execução gerenciado pelo sistema.

**Processo × thread:** o **processo** é a unidade de recursos: espaço de memória próprio, arquivos abertos, credenciais. A **thread** é um fluxo de execução **dentro** de um processo: tem pilha, registradores e contador de programa próprios, mas compartilha a memória e os arquivos com as outras threads do processo. Criar e trocar threads é mais barato; em troca, um erro numa thread afeta o processo todo e o acesso a dados compartilhados exige coordenação.

**Correção:** respostas da turma descrevem a thread como "um processo que contém outros processos" e dizem que threads "mascaram subprocessos"; o certo é o contrário: o processo contém as threads.

**Descritor (PCB/TCB):** identificador, estado, contexto salvo (registradores, PC, ponteiro de pilha), áreas de memória, arquivos abertos, prioridade e contadores de uso.

**Estados:** nova → pronta → executando → terminada; executando → suspensa (espera E/S, semáforo ou evento) → pronta. Executando → pronta ocorre ao fim do *quantum* (preempção). Não existem suspensa → executando (passa antes por pronta) nem pronta → suspensa (só quem executa pode pedir algo que bloqueia).

**Troca de contexto:** salvar o contexto da tarefa atual no seu descritor, escolher a próxima (escalonador) e restaurar o contexto dela (despachante). No compartilhamento de tempo, o temporizador gera interrupções periódicas (*ticks*) que disparam a troca.

**Modelos de threads:** N:1 (muitas threads de usuário numa só de núcleo): simples e leve, mas se uma bloquear todas esperam e não usa vários processadores. 1:1 (cada thread de usuário tem uma no núcleo, como no Windows NT e no Linux): usa várias CPUs, pode pesar no núcleo. N:M: multiplexa threads de usuário num conjunto de threads de núcleo; é o mais complexo.

**Verificação:** cada transição possível tem um evento que a causa (fim de quantum, pedido de E/S, fim da E/S); as impossíveis não têm.
