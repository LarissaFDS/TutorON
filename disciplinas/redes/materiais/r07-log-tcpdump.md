---
id: redes-log-tcpdump-handshake-dados-encerramento
titulo: O que aconteceu na conexão do log do Wireshark/TCPDump — handshake de três vias (SYN, SYN-ACK, ACK), requisição HTTP de 605 bytes, resposta em segmentos de 1440 bytes, ACKs e encerramento com FIN
assunto: redes-04-transporte-tcp
tipo: prova
questao: AB1 2017 Q6
resolucao: sim
fonte: Prova 1 de 2017 de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL), questão 6 (log transcrito da foto)
curso: Ciência da Computação (UFAL), Redes de Computadores 1 (COMP — Prof. Leandro Melo de Sales); provas de 2017
fontes_catalogo: ufal-leandro-provas-redes
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), AB1 2017 Q6 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

O log mostra um cliente `192.168.1.9.53123` (porta efêmera) e um servidor `194.57.88.66.80` (porta 80: **HTTP**). Os números depois do primeiro segmento são **relativos** (o tcpdump subtrai o número inicial).

1. **Handshake de três vias:** cliente → `Flags [S]` (SYN), seq 3455997603; servidor → `[S.]` (SYN+ACK), com ack 3455997604 (o SYN conta como 1 byte); cliente → `[.]` ack 1. Nas opções: MSS 1460 do cliente e 1452 do servidor, escala de janela, SACK permitido e *timestamps*.
2. **Requisição:** cliente → `[P.] seq 1:606`, ou seja, **605 bytes** (a requisição HTTP). O servidor confirma com ack 606.
3. **Resposta:** o servidor envia `1:1441` e `1441:2881` (dois segmentos de **1440 bytes**, limitados pelo MSS menos as opções) e `2881:4036` (1155 bytes, com PSH). O cliente confirma com ack 2881 e ack 4036 (ACK cumulativo).
4. **Segunda requisição na mesma conexão (HTTP persistente):** cliente `606:1152` (546 bytes); servidor responde `4036:4931` (895 bytes); o cliente confirma com ack 4931.
5. **Encerramento:** cada lado envia `[F.]` (FIN) e o outro confirma com ack + 1 (o FIN também conta 1 byte), como em `ack 4932` e `ack 1153`.
6. A última linha mostra um **novo SYN** de outra porta (53124): o navegador abre outra conexão.

Resumo: uma conexão TCP para HTTP, com duas requisições e respostas e fechamento nos dois sentidos.

**Verificação:** `test_log_tcpdump` lê as linhas do log transcritas no teste, identifica SYN, SYN-ACK, FIN e PSH pelas flags e confere as contas: 606 − 1 = 605, 1441 − 1 = 1440, 4036 − 2881 = 1155, 1152 − 606 = 546, 4931 − 4036 = 895 e cada ack igual ao fim do segmento confirmado.
