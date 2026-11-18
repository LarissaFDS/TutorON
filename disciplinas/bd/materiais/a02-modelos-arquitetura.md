---
id: bd-aula-modelos-arquitetura
titulo: Aula de BD — modelos de dados, esquema e instância, arquitetura três-esquemas e ciclo de vida
assunto: bd-02-modelos-arquitetura
tipo: material_estudo
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 1 "Introdução a Banco de Dados", parte 2
fontes_catalogo: ufal-bd-slides
autoria: Profª Maria Cristina Tenório (slides, com créditos a material dos professores Tarsis Marinho e Patrick Brito), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Modelo de dados é o conjunto de conceitos para descrever a estrutura de um banco (e as operações de consulta e atualização). Categorias: alto nível ou conceitual (ex.: entidade-relacionamento), representacional ou de implementação (ex.: relacional) e baixo nível ou físico (como os dados ficam gravados).

- Esquema: a descrição do banco (estrutura), mostrada no diagrama esquemático; muda pouco.
- Instância: as ocorrências (dados) guardadas.
- Estado do banco: os dados num determinado momento.

Arquitetura três-esquemas (ANSI/SPARC):
- nível interno: estrutura física de armazenamento;
- nível conceitual: estrutura do banco inteiro para a comunidade de usuários;
- nível externo (visões): a parte que interessa a cada grupo de usuários.

Independência de dados é mudar o esquema de um nível sem mudar o do nível acima. Independência lógica: mudar o esquema conceitual sem mudar as visões e os programas. Independência física: mudar o armazenamento sem mudar o esquema conceitual.

Linguagens: DDL (definição de dados), SDL (armazenamento, esquema interno), VDL (visões; na maioria dos SGBDs é a própria DDL) e DML (manipulação). SQL reúne DDL e DML.

Ciclo de vida do banco de dados:
1. Análise de requisitos (entrevistas com quem produz e usa os dados; especificação formal).
2. Projeto lógico: modelagem conceitual (ER ou UML), integração das visões de cada analista numa visão global (sinônimos, agregação, generalização), transformação em tabelas SQL e normalização.
3. Projeto físico: tabelas, visões, índices, usuários, restrições de integridade (referencial, unicidade, domínio) e escolhas de armazenamento.
4. Implementação, monitoração e modificação: cria-se o esquema com a DDL e usa-se a DML para consultar e atualizar.
