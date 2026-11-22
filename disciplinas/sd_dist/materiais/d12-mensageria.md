---
id: sd_dist-rabbitmq-amqp-exchanges-kafka-log-de-eventos
titulo: Para que serve o RabbitMQ (AMQP, exchanges direct, fanout e topic), exemplos e modelos de fila que ele implementa; quando usar Kafka (log distribuído de eventos, partições, grupos de consumidores)
assunto: sd_dist-04-tecnologias
tipo: prova
questao: AB2 2020.1 Q3; AB2 2020.2
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2020.1 e 2020.2
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 2020.1 Q3; AB2 2020.2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**RabbitMQ:** **broker de mensagens** que implementa o protocolo **AMQP**. Produtores publicam numa **exchange**, que roteia para **filas** segundo **ligações** (*bindings*); consumidores leem das filas e confirmam (*ack*) cada mensagem. Mensagens podem ser persistentes e, se o consumidor cai sem confirmar, são reentregues.

**Modelos que ele implementa:**
- **fila de trabalho** (*work queue*): uma fila, vários consumidores; cada mensagem vai para **um** (distribui tarefas pesadas);
- **publicar-assinar** com exchange **`fanout`**: cópia para **todas** as filas ligadas;
- **roteamento** com exchange **`direct`**: vai para a fila cuja chave é **igual** à chave da mensagem (ex.: `erro`, `aviso`);
- **tópicos** com exchange **`topic`**: chaves com padrões (`pedido.*.br`, `log.#`);
- **RPC** sobre filas (fila de resposta e `correlation_id`).

**Exemplos:** fila de envio de e-mails e geração de PDFs fora da requisição web; notificar vários serviços (estoque, cobrança, entrega) quando um pedido é criado.

**Verificação:** `test_exchanges` implementa as exchanges `direct`, `fanout` e `topic` (com `*` e `#`) e confere para quais filas cada mensagem vai.
