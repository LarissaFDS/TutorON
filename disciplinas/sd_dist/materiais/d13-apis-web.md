---
id: sd_dist-web-services-rest-graphql-grpc-protocol-buffers-envoy
titulo: O que são Web Services e o que é RESTful; GraphQL e ponderações com REST; gRPC e suas vantagens, Protocol Buffers; problemas que o Envoy Proxy resolve (service mesh)
assunto: sd_dist-04-tecnologias
tipo: prova
questao: AB2 2020.1 Q4, Q5, Q8 e Q9; AB2 2020.2
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 2020.1 Q4, Q5, Q8 e Q9; AB2 2020.2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Web Services:** serviços oferecidos pela rede com **tecnologias da Web** (HTTP, XML ou JSON), para serem usados **por outros programas**, independentes de linguagem e plataforma. Estilos: SOAP (mensagens XML com contrato WSDL) e REST.

**REST e RESTful:** REST é um **estilo arquitetural**; uma API é *RESTful* quando segue suas restrições:
- **recursos** identificados por **URIs** (`/alunos/42`);
- **interface uniforme** com os métodos HTTP: `GET` (ler, seguro e idempotente), `PUT` (substituir, idempotente), `POST` (criar), `DELETE` (remover, idempotente);
- **sem estado** (*stateless*): cada requisição traz tudo de que precisa;
- representações (JSON), respostas **cacheáveis** e sistema em camadas.

**GraphQL:** **linguagem de consulta para APIs** com um **esquema tipado**; o cliente pede **exatamente os campos** que quer, num **único *endpoint***. Comparação com REST:
- GraphQL evita **excesso** de dados (*over-fetching*) e **várias idas e voltas** (*under-fetching*): uma consulta junta aluno, disciplinas e notas;
- REST é mais simples, usa o **cache HTTP** naturalmente e tem códigos de estado claros;
- GraphQL dificulta o cache, permite consultas caras (exige limites de profundidade e custo) e precisa de ferramentas próprias.
Bom para telas que agregam muitos dados de vários serviços; REST para recursos simples e públicos.

**Verificação:** `test_rest_idempotencia` sobe uma API REST mínima com `http.server` em localhost: PUT repetido deixa o mesmo estado, POST repetido cria dois recursos.
