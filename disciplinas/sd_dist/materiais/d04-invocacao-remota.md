---
id: sd_dist-invocacao-remota-rpc-rmi-requisicao-resposta
titulo: Invocação remota: protocolo requisição-resposta, chamada de procedimento remoto (RPC) e invocação de método remoto (RMI); vantagem do RPC sobre o requisição-resposta; semânticas de chamada
assunto: sd_dist-02-comunicacao
tipo: prova
questao: AB1 de 2017 Q4-Q5; provas de 2017; AB1 2020.1 Q2; AB1 2020.2
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB1 de 2017 Q4-Q5; provas de 2017; AB1 2020.1 Q2; AB1 2020.2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Requisição-resposta:** troca de **duas mensagens**: o cliente envia a operação e os argumentos codificados (*bytes*); o servidor executa e devolve o resultado codificado. É o padrão mais primitivo e eficiente; o HTTP é um exemplo. O programador cuida da codificação e das mensagens.

**RPC (Remote Procedure Call):** permite chamar um procedimento em **outro espaço de endereçamento** como se fosse **local**. Um **stub** (*proxy*) do cliente codifica os argumentos (*marshalling*), envia a requisição, espera e decodifica o resultado; o **esqueleto** do servidor faz o inverso e chama o procedimento real.

**Vantagem do RPC sobre o requisição-resposta:** **transparência de acesso e de localização**: o programador escreve uma chamada de função; a codificação, a troca de mensagens e o tratamento de reenvios ficam escondidos. Custo: a chamada remota **não é igual** a uma local (latência, falhas parciais, sem ponteiros compartilhados).

**RMI (Remote Method Invocation):** RPC para **objetos**: chama-se um método de um objeto remoto por uma **referência de objeto remoto**; integra-se à linguagem (Java RMI).

**Semânticas de chamada (o que acontece com falhas):**
- *talvez* (*maybe*): sem reenvio; pode não executar;
- *pelo menos uma vez*: reenvia até ter resposta; pode executar **várias vezes** (ok para operações **idempotentes**);
- *no máximo uma vez*: reenvia, mas o servidor filtra duplicatas e guarda a resposta; é a semântica de Java RMI e CORBA.

**Escolha para comunicação direta (provas de 2017):** RPC, pela transparência; requisição-resposta só quando o desempenho é crítico e se aceita tratar as mensagens.

**Verificação:** `test_rpc_e_semanticas` faz um RPC real com `xmlrpc` em localhost e simula perdas de resposta: com *pelo menos uma vez*, um `incrementa` não idempotente executa 3 vezes; com *no máximo uma vez* (filtro por id da requisição), executa 1.
