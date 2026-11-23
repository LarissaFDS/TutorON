---
id: sd_dist-middleware-servico-sistema-operacional-compartilhamento
titulo: Middleware: o que é, por que é importante, se um sistema operacional é middleware; o que é um serviço em sistemas distribuídos e por que compartilhar funções de software
assunto: sd_dist-01-caracterizacao-e-modelos
tipo: prova
questao: AB1 de 2017 Q4; AB1 2020.1 Q1-Q3; AB1 2020.2
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB1 de 2017 Q4; AB1 2020.1 Q1-Q3; AB1 2020.2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Middleware:** camada de software **entre as aplicações e o sistema operacional** (e a rede) de cada máquina. Ela **esconde a heterogeneidade** (hardware, SO, linguagens, redes) e oferece um **modelo de programação uniforme**: invocação remota, objetos distribuídos, eventos, filas. Ex.: Java RMI, gRPC, RabbitMQ.

**Por que é importante:** o programador escreve a lógica da aplicação sem tratar *sockets*, codificação de dados (*marshalling*), localização de serviços e falhas de rede em cada programa. Isso dá transparência de acesso e localização, reuso e interoperabilidade entre sistemas diferentes.

**Um sistema operacional é middleware? Não** (questão de 2020.2). O SO **gerencia os recursos de uma máquina** (processos, memória, arquivos, dispositivos) e oferece chamadas de sistema locais. O middleware roda **sobre** os SOs de várias máquinas e usa esses serviços para dar uma abstração **distribuída**. Um *SO distribuído* (que gerenciasse todas as máquinas como uma só) seria outra categoria; na prática, usa-se SO de rede mais middleware.

**Serviço:** parte de um sistema que **gerencia uma coleção de recursos** e oferece a funcionalidade por uma **interface bem definida** de operações, acessível pela rede (arquivos, nomes, uma API web). Clientes só conhecem a interface, não a implementação.

**Compartilhar funções de software:** em vez de cada aplicação reimplementar uma função (autenticação, pagamento, ordenação), ela é oferecida como serviço remoto e reusada por muitos clientes. Isso evita duplicação, centraliza correções e permite cobrar pelo uso (*utility computing*). A forma de usá-la é a **invocação remota** (ver o bloco de RPC).

**Verificação:** `test_middleware_esconde_a_rede` usa o `xmlrpc` da biblioteca padrão do Python como middleware: o cliente chama `proxy.soma(2, 3)` como se fosse local e recebe 5 de um servidor em outra thread, sem escrever código de rede.
