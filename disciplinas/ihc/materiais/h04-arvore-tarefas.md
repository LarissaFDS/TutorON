---
id: ihc-arvore-de-tarefas-caminho-previsto-modelo-mental-do-usuario-comparar-desvios
titulo: Árvore de tarefas: decompor a tarefa em subtarefas, prever o caminho do usuário, comparar com o modelo mental observado no teste e registrar desvios
assunto: ihc-02-avaliacao-de-usabilidade
tipo: exercicio
questao: projeto AB1 e AB2 (listar as tarefas numa árvore e verificar se o previsto coincide com o modelo mental)
resolucao: sim
fonte: Etapas do projeto de microteste de usabilidade pedidas pelo Prof. Fábio Paraguaçu (IC-UFAL), 2020.2, conhecidas pelos enunciados citados nos trabalhos entregues
curso: Ciência da Computação (UFAL), COMP395 Interação Homem-Máquina (ênfase Sistemas de Informação); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-ihc-etapas-projeto
autoria: Etapas do projeto do Prof. Fábio Paraguaçu (IC-UFAL); explicação e exemplo parecido da equipe TutorON
licenca: Não declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Interação Humano-Computador (IC-UFAL, 2020.2), projeto AB1 e AB2 (listar as tarefas numa árvore e verificar se o previsto coincide com o modelo mental) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

O projeto é **avaliativo** e feito em grupo: aqui vão o método e um exemplo parecido, não o trabalho pronto.

**Árvore de tarefas** (análise hierárquica de tarefas): a raiz é o **objetivo** do usuário, os filhos são **subtarefas** e as folhas são **ações** na interface (clicar, digitar, rolar). A ordem dos filhos é a ordem esperada. Alternativas, como "pela busca" ou "pela página inicial", são ramos diferentes.

**Exemplo parecido** (comprar um ingresso de cinema num aplicativo):
- objetivo: comprar ingresso
  - escolher o filme: abrir o aplicativo → tocar em "Em cartaz" → tocar no filme
  - escolher a sessão: escolher a data → escolher o horário
  - escolher o assento: tocar no mapa → confirmar
  - pagar: escolher a forma → confirmar o pagamento

**Modelo mental:** a ideia que o usuário tem de como o sistema funciona e de onde as coisas estão. No teste, compare o **caminho previsto** com o **caminho real**:
- **coincidiu**: o design combina com o modelo mental;
- **desvio**: o usuário procurou noutro lugar. Pode indicar rótulo ou posição ruins, ou um caminho alternativo que vale oferecer;
- **abandono**: o usuário não terminou. Anote em qual nó parou e por quê (pela fala no pensamento em voz alta).

Uma falha pode vir de **habilidades motoras** (teclado, *mouse*) e não do caminho. Registre isso separado: é um achado de acessibilidade e letramento digital.

Para iniciante, intermediário e avançado, a árvore muda. O avançado usa atalhos, filtros e configurações; o iniciante, o caminho mais visível.

**Verificação:** `test_comparar_caminho_previsto` compara o caminho previsto com dois caminhos observados e conta passos a mais, nós fora da árvore e o ponto de abandono.
