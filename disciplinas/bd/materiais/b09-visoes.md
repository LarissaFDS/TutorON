---
id: bd2-aula-visoes
titulo: Aula de BD2 — visões (VIEW): criar, consultar, substituir e apagar; diferenças entre SGBDs
assunto: bd-12-visoes-procedures-triggers
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), avaliação AB2 "View (Visão)"
fontes_catalogo: ufal-bd2-slides,sqlite-docs,postgresql-docs
banco_teste: loja
autoria: Profª Cristina Tenório (slides), reescrito pela equipe TutorON com auxílio de IA; dados de exemplo da equipe no lugar do banco Northwind
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Visão (VIEW) é uma tabela virtual definida por um SELECT. Ela não guarda os dados: o SGBD roda o SELECT da visão sempre que ela é consultada, por isso mostra os dados atualizados. Pode usar WHERE, JOIN e funções e serve para simplificar consultas e limitar o que cada usuário vê (nível externo da arquitetura três-esquemas).

Exemplo da aula: visão dos clientes do Brasil.

```sql
CREATE VIEW clientes_brasil AS
SELECT nome, cidade FROM cliente WHERE pais = 'Brasil';
SELECT nome, cidade FROM clientes_brasil ORDER BY nome;
```

Resultado:

| nome | cidade |
|---|---|
| Ana Lima | Maceió |
| Bruno Costa | Recife |
| Davi Melo | Maceió |
| Fábio Rocha | NULL |
| Gil Souza | Recife |

Exemplo da aula: produtos com preço acima da média (a média dos cinco é 18).

```sql
CREATE VIEW produtos_acima_media AS
SELECT nome, preco FROM produto WHERE preco > (SELECT AVG(preco) FROM produto);
SELECT nome, preco FROM produtos_acima_media ORDER BY preco;
```

Resultado:

| nome | preco |
|---|---|
| Cartaz | 22 |
| Tinta azul | 35 |

Para mudar uma visão, o SQLite não tem `CREATE OR REPLACE VIEW` (MySQL e PostgreSQL têm; o SQL Server usa `ALTER VIEW` ou `CREATE OR ALTER VIEW`). No SQLite apaga-se e cria-se de novo:

```sql
CREATE VIEW clientes_brasil AS SELECT nome FROM cliente WHERE pais = 'Brasil';
DROP VIEW IF EXISTS clientes_brasil;
CREATE VIEW clientes_brasil AS SELECT nome, cidade, id_cliente FROM cliente WHERE pais = 'Brasil';
SELECT COUNT(*) FROM clientes_brasil WHERE cidade = 'Recife';
```

Resultado:

| COUNT(*) |
|---|
| 2 |

`DROP VIEW` apaga só a definição da visão; os dados continuam nas tabelas.

Correções da equipe
- O slide de visão põe o nome entre colchetes, que é do SQL Server, junto com `CREATE OR REPLACE VIEW`, que o SQL Server não aceita. Use um nome sem espaço (ou aspas duplas, no padrão) e o comando de substituição do seu SGBD.
