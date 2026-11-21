---
id: so-comunicacao-entre-tarefas-ipc
titulo: Comunicação entre tarefas (IPC) — direta e indireta, síncrona e assíncrona, capacidade do canal, pipes, filas de mensagens e memória compartilhada
assunto: so-03-comunicacao
tipo: lista
questao: caderno, cap. 3, questões 1 a 5; AB1 2020.1, questão 5
resolucao: sim
fonte: Slides do Prof. André Aquino (UFAL), comunicação entre tarefas; Lista 3 da turma (2021) sobre o caderno do Prof. Maziero, cap. 3; prova AB1 de 2020.1
fontes_catalogo: ufal-aquino-slides-so,turma-listas-2021,maziero-caderno-2014,maziero-socm-2013,ufal-aquino-ab-2020-1
autoria: Slides do Prof. André Aquino (UFAL) e exercícios do Prof. Maziero; resoluções de aluno parafraseadas e conferidas pela equipe TutorON
licenca: Slides sob CC BY-NC-SA 4.0 (Aquino); caderno sob CC BY-NC-SA 3.0 (Maziero); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Comunicação entre tarefas, como nos slides da disciplina e no cap. 3 do caderno do Prof. Maziero. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Tarefas do **mesmo processo** (threads) já compartilham memória; tarefas em **processos diferentes** precisam de mecanismos do núcleo, chamados de **IPC** (*inter-process communication*); entre computadores, de mecanismos de rede.

**Características de um mecanismo:**
- **Direta ou indireta:** na direta o emissor nomeia o receptor (`enviar(dados, destino)`); na indireta os dois usam um **canal** ou caixa postal (*mailbox*) e não precisam se conhecer.
- **Sincronismo:** síncrona (envio e recepção bloqueiam até a comunicação acontecer), assíncrona (não bloqueiam; exige buffer) ou semissíncrona (bloqueia até um prazo).
- **Formato:** mensagens independentes ou fluxo contínuo de bytes (como um arquivo).
- **Capacidade do canal:** nula (o emissor espera o receptor: *rendez-vous*), finita (bloqueia quando o buffer enche) ou infinita (idealização).
- **Confiabilidade:** o canal entrega todos os dados, na ordem, sem duplicar?
- **Participantes:** 1:1, M:N; uma *mailbox* com vários emissores e um receptor é N:1.

**Exemplos UNIX:**
| Mecanismo | Classificação |
|---|---|
| *pipe* | indireto, fluxo de bytes, capacidade finita, confiável, 1:1 entre processos aparentados |
| fila de mensagens | indireta, orientada a mensagens, capacidade finita, confiável, N:M; envio e recepção bloqueantes ou não |
| memória compartilhada | indireta, sem cópia pelo núcleo depois de mapeada, a mais rápida; **não** tem sincronização própria: exige semáforos ou mutex |

Na AB1 de 2020.1 (prova on-line, uma categoria de sistema à escolha), a resposta da turma indicou fila de mensagens para um sistema multiprocessador; a classificação dada (N:1, confiável, capacidade finita, síncrona ou assíncrona) está correta.

**Verificação:** cada mecanismo da tabela foi conferido contra o cap. 3 do livro do Maziero; a memória compartilhada é o único sem cópia de dados pelo núcleo a cada troca, e por isso o único que precisa de coordenação explícita.
