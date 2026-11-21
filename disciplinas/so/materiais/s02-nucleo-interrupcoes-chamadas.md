---
id: so-nucleo-interrupcoes-chamadas-sistema
titulo: Núcleo, modo usuário e modo núcleo, interrupções, exceções e traps, chamadas de sistema (fopen, printf)
assunto: so-01-conceitos-estrutura
tipo: lista
questao: caderno, cap. 1, questões 5 a 15; AB1 (respostas da turma), questão 3
resolucao: sim
fonte: Lista 1 da turma (2021) e respostas compartilhadas da turma, sobre o caderno do Prof. Maziero, cap. 1; slides do Prof. André Aquino (UFAL), aula 1
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
Exercícios do cap. 1 do caderno do Prof. Maziero, resolvidos pela turma. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Núcleo:** a parte do sistema que executa em **modo núcleo** (privilegiado), gerencia o hardware e implementa as abstrações (tarefas, memória, arquivos). Utilitários e bibliotecas executam em **modo usuário**, onde instruções privilegiadas são proibidas. Sem níveis de privilégio no processador, qualquer programa poderia reprogramar a MMU ou desligar as interrupções: não haveria proteção.

**Interrupção, exceção e trap:**
- **Interrupção (de hardware):** evento externo e assíncrono (tecla, pacote de rede, fim de leitura do disco); o processador desvia para a rotina de tratamento.
- **Exceção:** gerada pelo próprio processador ao executar uma instrução com problema (divisão por zero, acesso inválido, falta de página).
- **Trap (interrupção de software):** instrução executada **de propósito** para entrar no núcleo; é o mecanismo das chamadas de sistema.

**Correção:** uma das respostas da turma chamou de interrupção de software a divisão por zero; isso é uma **exceção**. A interrupção de software é a instrução intencional.

**Chamada de sistema ou biblioteca?** `fopen` é **função de biblioteca** (libc): prepara os parâmetros e invoca a chamada de sistema `open`. Exigem chamada de sistema as ações sobre recursos protegidos: enviar um pacote pela rede, remover um arquivo, ler o relógio de hardware. Calcular uma potência ou zerar a própria memória não exigem.

Sequência de `printf("Hello world")`: o processo chama `printf` → a biblioteca processa a string → prepara os registradores para `write` → aciona a interrupção de software → o tratador no núcleo é ativado → a escrita no terminal é feita ou agendada → o escalonador escolhe a tarefa → o controle volta à `printf` em modo usuário → `printf` retorna ao código do processo. A interrupção do disco **não** faz parte dessa sequência (a saída vai ao terminal).

**Verificação:** a ordem respeita "modo usuário → trap → núcleo → retorno"; nenhuma etapa executa instrução privilegiada em modo usuário.
