# Curadoria — Sistemas Operacionais (`so`, ECOM032)

Situação: **MVP** desde 21/11/2026, sem aviso, depois de cumprido o critério de liberação (veja `docs/DISCIPLINAS.md`).

## Disciplina e ementa

- ECOM032, 5º semestre, 60 h (40 teóricas e 20 práticas), Engenharia de Computação da UFAL.
- **Ementa conferida** no PPC de 2014 (`ufal-ppc-ecomp-2014`): conceitos básicos; evolução, estrutura e funções dos sistemas operacionais; gerenciamento de processos; gerência de memória; gerenciamento de entrada e saída; sistemas de arquivos; estudos de caso. Bibliografia básica: Tanenbaum, Silberschatz e Deitel.
- **Autoria dos slides (correção):** os slides SO-01 a SO-07 (`ufal-aquino-slides-so`) são do **Prof. André L. L. Aquino (UFAL)**, sob CC BY-NC-SA 4.0, *baseados* no livro do Prof. Maziero; não são slides do Prof. Maziero. SO-06 e SO-07 também creditam André Lage Freitas (CC BY-NC-SA 3.0 BR). O livro e o caderno de exercícios são do Prof. Maziero (CC BY-NC-SA 3.0).

| Assunto | Ementa | Blocos na busca |
|---|---|---|
| `so-01-conceitos-estrutura` | conceitos, evolução, estrutura | s01–s03 |
| `so-02-tarefas-escalonamento` | processos | s04–s08 |
| `so-03-comunicacao` | processos | s09 |
| `so-04-coordenacao-impasses` | processos | s10–s13 |
| `so-05-memoria` | gerência de memória | s14–s17 |
| `so-06-arquivos` | sistemas de arquivos | s18–s20 |
| `so-07-entrada-saida` | entrada e saída | s21–s23 |

Estudos de caso só aparecem como exemplos dentro dos blocos (Linux, Windows, ext2, FAT).

## Fronteiras

| Tópico | Aqui | Aprofundado em |
|---|---|---|
| MMU, TLB, cache, barramentos e hardware de E/S | uso pelo SO | Organização e Arquitetura de Computadores (`oac`) |
| Filas, listas, árvores | como ferramenta | Estrutura de Dados (`ed`) |
| Linguagem C | exemplos com pthread | Programação 1 (`prog1`) |

`tests_acervo/test_disciplina_so.py` testa o isolamento com OAC e ED nos dois sentidos.

## Material protegido e dados pessoais

- **Os comprovantes da AB1 e da AB2 de 2020.1 trazem o nome e o e-mail de um aluno.** Não foram versionados e nenhum dado pessoal foi copiado; as questões foram parafraseadas.
- Listas resolvidas, resumos de 2017 e o documento de respostas compartilhadas trazem nomes, matrícula e e-mail de alunos: nada disso entrou no acervo. O teste guarda só hashes de nomes e procura e-mails e links de grupo.
- Fotos da Prova 2, PDFs e imagens não estão no repositório.
- Tanenbaum, Silberschatz e Deitel (`tanenbaum`, `silberschatz`, `deitel`) não foram incluídos nem transcritos. OSTEP (`ostep`) é leitura gratuita sem licença aberta: só citado. MIT 6.828 (`mit-ocw-6-828-2012`) e a edição 2019 do Maziero (`maziero-socm-2019`) são citados, não ingeridos. O seminário (`aquino-seminario`) e o arquivo vazio "Cap. 5 - Estudos" (`turma-cap5-estudos-vazio`) ficam só no catálogo.
- As provas do Prof. Aquino não têm licença declarada: os blocos são paráfrases com resolução própria. **Confirmar com a equipe** se o professor autoriza a transcrição.

## Fontes (`fontes.json`)

`ufal-ppc-ecomp-2014`, `ufal-aquino-slides-so`, `ufal-aquino-ab-2020-1`, `ufal-aquino-prova2-fotos`, `turma-resolucao-ab2-variante`, `turma-respostas-so`, `turma-listas-2021`, `turma-resumos-2017`, `maziero-caderno-2014`, `maziero-socm-2013`, `maziero-socm-2019`, `ostep`, `mit-ocw-6-828-2012`, `tanenbaum`, `silberschatz`, `deitel`, `aquino-seminario`, `turma-cap5-estudos-vazio`.

## Blocos

| Bloco | Status | Observação |
|---|---|---|
| `so-conceitos-objetivos-tipos` | corrigida | |
| `so-nucleo-interrupcoes-chamadas-sistema` | corrigida | divisão por zero é exceção, não interrupção de hardware |
| `so-arquiteturas-monolitico-micronucleo` | validada | |
| `so-tarefas-processos-threads-estados` | corrigida | |
| `so-escalonamento-fcfs-sjf` | validada | simulado |
| `so-escalonamento-srtf-prioridades` | validada | simulado |
| `so-escalonamento-round-robin` | validada | fila a cada quantum |
| `so-ab1-lote-jobs-fcfs-sjf` | corrigida | |
| `so-comunicacao-entre-tarefas-ipc` | validada | |
| `so-condicao-de-disputa-secao-critica` | — | material de estudo; código C testado com TSan |
| `so-exclusao-mutua-espera-ocupada` | corrigida | TSL não é instrução privilegiada |
| `so-semaforos-produtor-consumidor` | — | material de estudo; código C testado |
| `so-impasses-quatro-condicoes` | corrigida | |
| `so-paginacao-bits-endereco-traducao` | pendente_professor | a tabela de páginas da figura não foi descrita |
| `so-alocacao-first-best-worst-fit` | validada | |
| `so-substituicao-paginas-fifo-lru-otimo` | — | material de estudo; simulado |
| `so-belady-envelhecimento-localidade-thrashing` | validada | |
| `so-alocacao-arquivos-contigua-encadeada-indexada` | corrigida | |
| `so-fat-cluster-ext2-tamanho-maximo` | corrigida | a lista chamou bytes de bits |
| `so-estrutura-arquivos-acesso-diretorios` | corrigida | |
| `so-escalonamento-disco-subindo` | validada | |
| `so-ab2-escalonamento-disco-descendo` | corrigida | SCAN sem ir à borda; LOOK com a ordem do C-LOOK; FCFS 363 → 423 |
| `so-entrada-saida-controlador-driver-dma-raid` | corrigida | |

Fora da busca (`nota_da_equipe_ia`, `candidato`): `so-nota-filas-multinivel-realimentacao`.

## Resoluções e conferência

Todas as resoluções são da equipe TutorON, **não gabarito do professor**. `tests_acervo/so_verif.py` simula escalonamento (FCFS, SJF, SRTF, prioridades, RR), substituição de páginas (FIFO, LRU, ótimo), envelhecimento, alocação contígua, disco, ext2 e o banqueiro. Os programas de `tests_acervo/c_so/` compilam com `gcc -pthread -Wall -Wextra -Werror`; com `-fsanitize=thread` só `disputa.c` acusa condição de disputa, como esperado.

Revisão humana e do professor: **pendentes** em todos os blocos.

## Complemento de Ciência da Computação (22/11/2026)

O material da turma de Ciência da Computação (pasta `18. COMP378 - Sistemas Operacionais`) foi conferido arquivo por arquivo contra o catálogo de `fontes.json`: são os mesmos slides do Prof. Aquino, o livro e o caderno do Prof. Maziero, as provas AB1, AB2 e reavaliação de 2020.1, as fotos da Prova 2, as listas de 2021, os resumos de 2017, o seminário e o arquivo vazio "Cap. 5 - Estudos". **Nada novo:** nenhum bloco foi criado e a situação não mudou (MVP).

- **Ementa:** no PPC de Ciência da Computação (matriz 2011, `ufal-ppc-cc-2011`), CCOM034 Sistemas Operacionais (60 h) tem o **mesmo texto de ementa** de ECOM032 e a mesma bibliografia básica (Tanenbaum, Silberschatz, Deitel). O código COMP378 vem do nome da pasta e não aparece no PPC de 2011. Não há motivo para separar disciplinas.
- Os blocos atuais servem às duas turmas; o campo `curso:` não foi acrescentado porque nenhum bloco veio só do material de CC.
