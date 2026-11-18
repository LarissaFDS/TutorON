---
id: bd2-aula-sql-revisao-dml
titulo: Aula de BD2 — revisão de SQL: INSERT, UPDATE, DELETE, SELECT, WHERE, DISTINCT e ORDER BY
assunto: bd-08-sql-ddl-dml
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), aulas 1 e 2 "Revisão SQL"
fontes_catalogo: ufal-bd2-slides,sqlite-docs
banco_teste: loja
autoria: Profª Cristina Tenório (slides), reescrito pela equipe TutorON com auxílio de IA; dados de exemplo da equipe no lugar do banco Northwind
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
SQL (Structured Query Language) tem comandos de definição (DDL: CREATE, ALTER, DROP) e de manipulação (DML: INSERT, UPDATE, DELETE, SELECT). A ferramenta base de BD2 é o SQLite; outro SGBD pode ser usado se for compatível.

- `INSERT INTO tabela (col1, col2) VALUES (v1, v2);` — a lista de valores vai entre parênteses; dá para inserir em todas as colunas ou só em algumas (as outras ficam NULL ou com o valor padrão).
- `UPDATE tabela SET col1 = v1 WHERE condição;` — sem WHERE, altera todas as linhas.
- `DELETE FROM tabela WHERE condição;` — sem WHERE, apaga todas as linhas.
- `SELECT col1, col2 FROM tabela WHERE condição ORDER BY col1 DESC;` — `SELECT *` traz todas as colunas e `SELECT DISTINCT` tira linhas repetidas.
- Operadores no WHERE: =, <>, <, >, <=, >=, BETWEEN, LIKE, IN, IS NULL, com AND, OR e NOT.

```sql
INSERT INTO cliente (id_cliente, nome, cidade, pais) VALUES (9, 'Iara Prado', 'Penedo', 'Brasil');
UPDATE cliente SET cidade = 'Arapiraca' WHERE id_cliente = 6;
DELETE FROM cliente WHERE id_cliente = 8;
SELECT id_cliente, nome, cidade FROM cliente
WHERE pais = 'Brasil' AND cidade IS NOT NULL
ORDER BY id_cliente;
```

Resultado:

| id_cliente | nome | cidade |
|---|---|---|
| 1 | Ana Lima | Maceió |
| 2 | Bruno Costa | Recife |
| 4 | Davi Melo | Maceió |
| 6 | Fábio Rocha | Arapiraca |
| 7 | Gil Souza | Recife |
| 9 | Iara Prado | Penedo |

O cliente 6 não tinha cidade (NULL) e passou a ter; o 8 (do Japão) foi apagado. `cidade = NULL` nunca é verdadeiro: use `IS NULL` ou `IS NOT NULL`.

Correções da equipe
- No exemplo de INSERT do slide, a lista depois de VALUES está sem parênteses, o que dá erro de sintaxe; aqui ela está entre parênteses.
- Na lista de operadores do slide, "maior ou igual" está com os símbolos invertidos; o operador é `>=`.
