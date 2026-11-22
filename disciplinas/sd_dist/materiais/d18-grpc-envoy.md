---
id: sd_dist-grpc-protocol-buffers-vantagens-envoy-proxy-service-mesh
titulo: gRPC e suas vantagens, Protocol Buffers (serialização binária) e os problemas que o Envoy Proxy resolve (sidecar, service mesh)
assunto: sd_dist-04-tecnologias
tipo: prova
questao: AB2 2020.1 Q5 e Q9
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2020.1
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 2020.1 Q5 e Q9 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**gRPC:** framework de **RPC** do Google sobre **HTTP/2**, com contratos em **Protocol Buffers**. Vantagens: mensagens **binárias compactas** e rápidas, **geração de código** cliente e servidor em várias linguagens, *streaming* nos dois sentidos, *deadlines* e cancelamento. Muito usado **entre microsserviços**. **Protocol Buffers:** formato e IDL de **serialização binária**, neutro de linguagem: define-se a mensagem num `.proto` com campos numerados e o compilador gera o código. É menor e mais rápido que XML ou JSON, e campos novos não quebram versões antigas.

**Envoy Proxy:** *proxy* de serviço que roda **ao lado de cada serviço** (*sidecar*, base de *service meshes* como o Istio). Resolve: **descoberta de serviços** e **balanceamento de carga**; **novas tentativas, timeouts e circuit breakers**; **TLS mútuo** entre serviços; **observabilidade** (métricas, logs, rastreamento distribuído). Tudo sem mudar o código das aplicações.

**Verificação:** `test_serializacao_binaria` codifica a mesma mensagem em JSON e em binário com `struct` (campos numerados, como no Protocol Buffers), confere que o binário é menor e que decodifica de volta igual.
