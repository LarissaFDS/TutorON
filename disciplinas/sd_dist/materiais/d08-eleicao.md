---
id: sd_dist-eleicao-de-lider-algoritmo-valentao-anel-exclusao-mutua
titulo: Para que servem os algoritmos de eleição de líder, com exemplo de aplicação; algoritmo do valentão (bully) e do anel; exclusão mútua distribuída
assunto: sd_dist-03-coordenacao-e-falhas
tipo: prova
questao: AB2 de 2017 Q3; resumo da AB2 (coordenação e acordo)
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2017
fontes_catalogo: ufal-leandro-provas-sd
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 de 2017 Q3; resumo da AB2 (coordenação e acordo) (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Para que servem:** escolher, **por consenso**, um único processo de um grupo para um **papel especial** (coordenador, servidor central, primário de uma réplica, dono de um *lock*). Todos devem concordar com o mesmo eleito, que costuma ser o de **maior identificador** entre os vivos. Roda-se a eleição no início e **sempre que o líder falha** (detectado por um detector de falhas).

**Exemplo de aplicação:** num banco de dados replicado com **primário e cópias**, só o primário aceita escritas. Se ele cai, as cópias elegem um novo primário. Outros: o servidor central de exclusão mútua, o coordenador do relógio no algoritmo de Berkeley, o líder do Raft (etcd, usado pelo Kubernetes).

**Algoritmo do anel (Chang e Roberts):** processos num anel lógico. Quem nota a falha envia `eleição(id)` ao sucessor. Cada processo repassa o **maior** entre o id recebido e o seu. Quando um processo recebe o **próprio id**, sabe que é o maior e anuncia `eleito(id)` pelo anel. São $O(n)$ mensagens no melhor caso.

**Algoritmo do valentão (*bully*), supõe sistema síncrono:** quem detecta a falha envia `eleição` aos processos de **id maior**. Se ninguém responde no prazo, ele se declara coordenador e avisa todos. Se algum maior responde, este assume a eleição. O maior vivo sempre vence. No pior caso são $O(n^2)$ mensagens.

**Exclusão mútua distribuída** (mesmo capítulo): servidor central com fila; anel com *token*; Ricart-Agrawala (pede a todos, com relógios de Lamport, e entra com $n - 1$ respostas).

**Verificação:** `test_eleicao_anel_e_valentao` simula os dois algoritmos com ids 3, 7, 2, 9, 5 e o 9 morto: ambos elegem o 7, e no anel o número de mensagens de eleição é igual ao de processos vivos mais os saltos até o 7.
