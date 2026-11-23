---
id: sd_dist-kafka-log-distribuido-particoes-grupos-de-consumidores-quando-usar
titulo: Quando usar Kafka: log distribuído de eventos, partições, offsets, grupos de consumidores; Kafka × RabbitMQ
assunto: sd_dist-04-tecnologias
tipo: prova
questao: AB2 2020.2
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2020.2
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 2020.2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Kafka:** plataforma de **streaming de eventos** baseada num **log distribuído só de acréscimo**. Os tópicos são divididos em **partições** replicadas; a ordem é garantida dentro da partição. As mensagens **ficam guardadas** por um prazo e **não somem ao ser lidas**: cada **grupo de consumidores** guarda o próprio *offset* e pode **reler** a história.

**Quando usar Kafka (e não RabbitMQ):**
- **grande volume** contínuo de eventos (cliques, telemetria, logs) com alta vazão;
- **vários consumidores independentes** do mesmo fluxo (análise, auditoria, busca), cada um no seu ritmo;
- **reprocessar** eventos antigos ou reconstruir estado (*event sourcing*);
- processamento de fluxos em tempo real (Kafka Streams, Flink).
RabbitMQ é melhor para **roteamento flexível** de tarefas, prioridade e entrega por mensagem com confirmação. A resposta que só descreveu o Kafka, sem dizer **quando** escolhê-lo, ganhou meio ponto em 2020.2.

**Verificação:** `test_log_com_offsets` implementa um log com *offsets* por grupo: dois grupos leem todas as mensagens, dentro de um grupo cada mensagem vai a um consumidor, e um consumidor que volta o *offset* relê.
