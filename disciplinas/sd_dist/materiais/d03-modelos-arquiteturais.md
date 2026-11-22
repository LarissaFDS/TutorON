---
id: sd_dist-modelos-arquiteturais-entidades-padroes-camadas-tiers-desempenho
titulo: Modelos arquiteturais: entidades (objetos distribuídos, componentes, serviços Web) para substituir em tempo de execução, paradigma de comunicação e padrão arquitetônico quando o princípio é desempenho ou tolerância a falhas
assunto: sd_dist-01-caracterizacao-e-modelos
tipo: prova
questao: AB1 de 2017 Q2; AB2 de 2017 Q1; provas de 2017
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2017
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB1 de 2017 Q2; AB2 de 2017 Q1; provas de 2017 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

O modelo arquitetural responde a quatro perguntas: **quais entidades** se comunicam, **como** se comunicam, **que papéis** têm e **onde** ficam.

**Entidades (abstração de programação):** **objetos distribuídos** (interface de métodos, Java RMI); **componentes** (objetos com **dependências explícitas** de interfaces requeridas e fornecidas, montados por um contêiner); **serviços Web** (interfaces publicadas na Web, HTTP, independentes de linguagem).

**Entidades que devem ser substituídas em tempo de execução:** **componentes** são a resposta mais defendida. Como as dependências são explícitas e um contêiner gerencia o ciclo de vida, troca-se um componente por outro com a mesma interface sem parar o resto. **Serviços Web** também são aceitáveis, por serem fracamente acoplados. Objetos distribuídos são a pior escolha: as dependências ficam implícitas no código.

**Paradigmas de comunicação:** comunicação entre processos (*sockets*); **invocação remota** (requisição-resposta, RPC, RMI); **comunicação indireta** (grupo, publicar-assinar, filas, espaço de tuplas, memória compartilhada distribuída).

**Padrões arquitetônicos:** **camadas** (*layering*: cada camada usa a de baixo); **tiers** (2 ou 3 camadas físicas: apresentação, lógica e dados); **cliente magro** (*thin client*); **proxy**, **intermediação** (*brokerage*) e **reflexão**.

**Se o princípio é desempenho:** comunicação **direta** (requisição-resposta ou RPC sobre conexões já abertas; cada intermediário acrescenta latência) e arquitetura **cliente-servidor em 2 ou 3 tiers**, com cache e replicação. **Se é tolerância a falhas:** **comunicação em grupo** (entrega a todos os membros, mesmo se alguns falharem) e **replicação**.

**Verificação:** `test_custo_de_intermediarios` simula uma chamada direta e a mesma chamada passando por um intermediário, com 1 ms por salto, e confere que a indireta custa o dobro da latência de ida e volta.
