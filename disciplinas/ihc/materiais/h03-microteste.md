---
id: ihc-microteste-de-usabilidade-perfil-iniciante-intermediario-avancado-pensamento-em-voz-alta
titulo: Microteste de usabilidade: escolher a interface, perfil do usuário (iniciante, intermediário, avançado), tarefas reais, gravação da tela, protocolo de pensamento em voz alta (think aloud), consentimento e sugestão de melhorias
assunto: ihc-02-avaliacao-de-usabilidade
tipo: exercicio
questao: projeto AB1 e AB2 (microteste com iniciante, intermediário e avançado)
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
Interação Humano-Computador (IC-UFAL, 2020.2), projeto AB1 e AB2 (microteste com iniciante, intermediário e avançado) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

O projeto é **avaliativo** e feito em grupo: aqui vão o método e um exemplo parecido, não o trabalho pronto.

**Microteste:** um teste de usabilidade pequeno, com **um usuário** por perfil e poucas tarefas, gravado. Não mede estatística. Serve para **achar problemas** e discutir.

**Passos:**
1. **escolha a interface** e justifique: público grande, tarefas claras;
2. **defina o perfil**:
   - iniciante: nunca ou quase nunca usou;
   - intermediário: usa o básico;
   - avançado: usa atalhos e recursos menos visíveis;
3. **monte as tarefas** de cada perfil numa árvore de tarefas e **preveja o caminho**;
4. **conduza:** peça o **pensamento em voz alta** (*think aloud*), em que o usuário fala o que procura, o que espera e o que estranha. **Não ajude** nem corrija durante a tarefa, só lembre de continuar falando. Grave a tela e o áudio **com consentimento**, sem expor o rosto ou os dados do participante sem autorização;
5. **compare** o caminho real com o previsto. Anote onde parou, voltou ou desistiu;
6. **sugira melhorias** ligadas ao que foi observado, de preferência com a heurística violada.

**Exemplo parecido** (não é a interface do trabalho): num aplicativo de banco, a tarefa do iniciante é "ver o saldo". O usuário procura "saldo" no menu, mas ele está atrás de um ícone de olho sem rótulo. Sugestão: rótulo visível ("Mostrar saldo"), ligado a reconhecer em vez de lembrar.

**Erros comuns:**
- ensinar o usuário durante o teste;
- escolher para "iniciante" alguém que já usa;
- concluir "a interface é ruim" sem dizer **onde** e **por quê**.

**Verificação:** `test_sucesso_e_tempo_por_tarefa` calcula a taxa de sucesso e o tempo médio de um registro de tarefas de exemplo, as medidas básicas para comparar perfis.
