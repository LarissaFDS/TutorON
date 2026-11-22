---
id: sd_dist-comunicacao-indireta-publicar-assinar-filas-de-mensagens-desacoplamento
titulo: Comunicação indireta: o que é, desacoplamento espacial e temporal, quando usar; publicar-assinar (publisher/subscriber) × filas de mensagens (message queues); comunicação em grupo, espaço de tuplas
assunto: sd_dist-02-comunicacao
tipo: prova
questao: AB1 de 2017 Q5; AB2 de 2017 Q5; AB1 2020.1 Q4; AB1 2020.2
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2017 a 2020.2
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB1 de 2017 Q5; AB2 de 2017 Q5; AB1 2020.1 Q4; AB1 2020.2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Comunicação indireta:** as entidades se comunicam **por meio de um intermediário**, sem acoplamento direto entre remetente e destinatário. Dois desacoplamentos:
- **espacial**: o remetente **não precisa saber quem** (nem onde) são os destinatários;
- **temporal**: remetente e destinatário **não precisam existir ao mesmo tempo** (a mensagem espera no intermediário).

**Quando usar:** muitos destinatários (um para muitos), destinatários que mudam ou ficam desligados, sistemas guiados por **eventos**, integração entre sistemas heterogêneos, distribuição de carga entre trabalhadores. Preço: um salto a mais (latência) e o intermediário como ponto a gerenciar.

**Publicar-assinar (*publish/subscribe*):** publicadores emitem **eventos** sobre um **tópico** (ou conteúdo); assinantes registram interesse; o serviço entrega **cada evento a todos os assinantes interessados**: relação **1 para N**. Ex.: cotações da bolsa.

**Filas de mensagens (*message queues*):** produtores colocam mensagens numa **fila** persistente; **cada mensagem é consumida por um único consumidor**, em geral em ordem FIFO: comunicação **ponto a ponto**. Vários consumidores na mesma fila dividem o trabalho (*work queue*).

Diferença-chave: no pub/sub, um evento vai para **todos** os assinantes; na fila, cada mensagem vai para **um** consumidor.

**Outras técnicas:** **comunicação em grupo** (mensagem ao identificador do grupo, entregue a todos os membros, com garantias de confiabilidade e ordem); **espaço de tuplas** (processos escrevem tuplas num espaço persistente e outros leem ou retiram por padrão, como no Linda); **memória compartilhada distribuída**.

**Verificação:** `test_pubsub_e_fila` implementa os dois modelos com threads: 3 assinantes recebem os 5 eventos cada (15 entregas); 3 consumidores de uma fila recebem juntos as 5 mensagens exatamente uma vez (5 entregas).
