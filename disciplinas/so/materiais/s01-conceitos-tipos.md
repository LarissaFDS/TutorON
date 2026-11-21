---
id: so-conceitos-objetivos-tipos
titulo: Objetivos de um sistema operacional e tipos de sistema (batch, tempo real, embarcado, distribuído, multiusuário, desktop, servidor)
assunto: so-01-conceitos-estrutura
tipo: lista
questao: caderno, cap. 1, questões 1, 4 e 12
resolucao: sim
fonte: Lista 1 da turma (2021) e respostas compartilhadas da turma, sobre o caderno de exercícios do Prof. Carlos Maziero, cap. 1; slides do Prof. André Aquino (UFAL), aula 1
fontes_catalogo: turma-listas-2021,turma-respostas-so,maziero-caderno-2014,ufal-aquino-slides-so
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

**Dois objetivos de um sistema operacional:** (1) **abstração de recursos**: oferecer interfaces simples e uniformes (arquivo, tarefa, socket) que escondem os detalhes de cada dispositivo; (2) **gerência de recursos**: definir políticas para repartir processador, memória e dispositivos entre as aplicações e resolver disputas.

**Tipos de sistema e o traço que identifica cada um:**
- **Batch (lote):** os trabalhos são enfileirados com seus dados e executados sem interação com o usuário.
- **Tempo real:** o essencial é o comportamento temporal **previsível** (prazo conhecido), mais que a rapidez. *Soft*: perder um prazo degrada o serviço (vídeo). *Hard*: perder um prazo pode causar dano grave (freio, aviônica).
- **Embarcado:** compacto, para hardware com poucos recursos e aplicação específica; a gerência de energia é importante.
- **Distribuído:** a localização física dos recursos é **transparente** para o usuário.
- **Multiusuário:** cada recurso tem um proprietário e há regras de acesso (permissões).
- **Desktop:** prioriza a interface gráfica e a interação com o usuário (o macOS é o exemplo típico).
- **Servidor:** gerencia com eficiência grandes volumes de recursos (banco de dados de uma empresa).

**Correção:** nas respostas da turma ao exercício de relacionar afirmações a tipos, "prioriza a interface gráfica e a interação com o usuário" foi marcado como distribuído; o correto é **desktop**. No verdadeiro ou falso do mesmo capítulo, "a localização dos recursos é transparente" descreve o sistema **distribuído**, não o de rede, e um sistema de tempo real **não** prioriza as tarefas interativas, e sim os prazos.

**Verificação:** cada tipo foi conferido com a definição do livro do Maziero (cap. 1); a palavra-chave de cada um (previsível, transparente, proprietário, poucos recursos) aparece uma só vez na lista.
