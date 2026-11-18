---
id: bd2-aula-procedures
titulo: Aula de BD2 — stored procedures (procedimentos armazenados) com parâmetros, em T-SQL (SQL Server)
assunto: bd-12-visoes-procedures-triggers
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), aula "JOIN, HAVING e PROCEDURE" (Stored Procedures)
fontes_catalogo: ufal-bd2-slides,sqlite-docs
autoria: Profª Cristina Tenório (slides), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
revisao_humana: pendente
---
Stored procedure (procedimento armazenado) é um conjunto de comandos SQL guardado no banco com um nome, que aceita parâmetros e é executado de uma vez, como uma função. Usos citados na aula: reaproveitar a mesma operação em aplicações de linguagens diferentes, reduzir tráfego de rede e dar segurança, pois o usuário pode ter permissão para executar a procedure sem acesso direto às tabelas.

Os exemplos dos slides são em T-SQL, do SQL Server: parâmetros começam com @, `GO` separa lotes e `EXEC` executa.

```sql
-- dialeto: sqlserver
CREATE PROCEDURE ClientesDaCidade @Cidade nvarchar(30)
AS
SELECT nome, cidade FROM cliente WHERE cidade = @Cidade;
GO

EXEC ClientesDaCidade @Cidade = 'Recife';
```

Com mais de um parâmetro, eles são separados por vírgula na definição e na chamada:

```sql
-- dialeto: sqlserver
CREATE PROCEDURE ClientesDaCidadePais @Cidade nvarchar(30), @Pais nvarchar(30)
AS
SELECT nome FROM cliente WHERE cidade = @Cidade AND pais = @Pais;
GO

EXEC ClientesDaCidadePais @Cidade = 'Porto', @Pais = 'Portugal';
```

Os trechos T-SQL não foram executados (não há SQL Server no ambiente de testes do TutorON); verificação parcial.

Em outros SGBDs: MySQL usa `CREATE PROCEDURE nome(IN cidade VARCHAR(30)) BEGIN ... END` e `CALL nome('Recife')`; PostgreSQL usa `CREATE PROCEDURE` ou `CREATE FUNCTION` em PL/pgSQL. O SQLite, ferramenta base de BD2, não tem procedures: a lógica fica na aplicação (consulta com parâmetro `?`), numa visão ou numa trigger.

Correções da equipe
- `GO` não é comando SQL: é o separador de lotes das ferramentas da Microsoft. O servidor nunca o recebe.
- Os slides criam várias procedures com o mesmo nome em sequência. A segunda criação falha se a primeira existir; use `CREATE OR ALTER PROCEDURE` (SQL Server 2016 SP1 em diante), `ALTER PROCEDURE` ou `DROP PROCEDURE` antes.
