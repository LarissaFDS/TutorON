# Curadoria — Sistemas Distribuídos

Situação: **em validação**. Revisão humana pendente em todos os blocos.

O id é `sd_dist` porque `sd` já é Sistemas Digitais.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `Sistemas Distribuidos`). No PPC de CC
(matriz 2011), a disciplina é a **CCOM044**, 60 h, 7º semestre. A ementa cobre:
- caracterização e modelos de sistemas distribuídos;
- processos e objetos distribuídos;
- sincronização e coordenação;
- serviços;
- segurança;
- novos modelos;
- algoritmos distribuídos;
- replicação e tolerância a falhas.

A bibliografia é Coulouris et al. e Tanenbaum e van Steen.

## O que entrou
18 blocos (`materiais/d01`–`d18`) com as questões das provas do Prof. Leandro Melo de Sales.

**Provas de 2017.** Os enunciados foram reconstruídos a partir das respostas e dos resumos da turma. Assuntos:
- caracterização e middleware;
- modelos arquiteturais;
- invocação remota;
- comunicação indireta;
- P2P;
- modelo síncrono e detectores de falhas;
- eleição;
- replicação.

**AB1 e AB2 de 2020.1 e 2020.2.** Assuntos:
- serviço e compartilhamento de funções;
- publicar-assinar × filas;
- utility computing;
- Docker, Swarm e Kubernetes;
- blockchain e prova de trabalho;
- RabbitMQ e Kafka;
- REST e GraphQL;
- gRPC e Protocol Buffers;
- IPFS e Envoy;
- cloud functions;
- "SO é middleware?".

Os enunciados são parafraseados e as resoluções são da equipe TutorON. O que pode ser executado
(RPC com `xmlrpc`, REST com `http.server`, publicar-assinar e filas com threads, eleição, detector de
falhas, disponibilidade, prova de trabalho e endereçamento por conteúdo com `hashlib`) é conferido em
`tests_acervo/test_disciplina_sd_dist.py`.

Três blocos têm verificação `parcial`, porque são conceituais ou dependem de ferramentas que não
rodam nos testes:
- `d01` (caracterização);
- `d10` (containers e Docker);
- `d15` (Kubernetes e cloud functions).

## O que não entrou
- Formulários respondidos de 2020.2, porque trazem nome e e-mail do aluno. Só os enunciados foram
  parafraseados, e os comentários de correção foram usados como critério.
- Respostas de alunos (AB1, AB2, "Provas AB1"), resumos e planilhas, que só servem de evidência dos
  tópicos. Os resumos traduzem trechos do livro.
- Slides dos seminários dos alunos (Kafka, Blockchain, Containers, DevOps, gRPC, IPFS, nuvem,
  proxies, RabbitMQ, REST e GraphQL, microsserviços), por serem trabalho de aluno.
- Livros de Coulouris e de Tanenbaum e van Steen, que são protegidos: só entram como referência por
  capítulo.
- Segurança em sistemas distribuídos e sincronização de relógios (Cristian, Berkeley, Lamport) não
  têm questão de prova na pasta e ficaram sem bloco.

## Decisões
- Ligado em `disciplinas/cursos.json` no 7º período de CC, que não está entre os períodos fixados
  em `backend/tests/test_versao_final.py`. O 7º período de CC não listava a disciplina; foi
  acrescentada com o nome da ementa.
- **Pendente:** a ECOM044 (Sistemas Distribuídos de Engenharia, 8º período) não foi ligada, porque
  a ementa de Engenharia não foi conferida.
