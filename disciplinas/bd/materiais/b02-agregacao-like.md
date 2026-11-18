---
id: bd2-aula-agregacao-like
titulo: Aula de BD2 — funções de agregação (COUNT, SUM, AVG, MIN, MAX), BETWEEN, IN, LIKE e curingas
assunto: bd-09-consultas-agregacao
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), aulas 1 e 2 "Refinamento da consulta" e "Wildcards"
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
Funções de agregação resumem várias linhas num valor: COUNT, SUM, AVG, MIN e MAX. `COUNT(*)` conta linhas; `COUNT(coluna)` e as outras funções ignoram NULL.

```sql
SELECT COUNT(*), COUNT(cidade) FROM cliente;
```

Resultado (o cliente 6 não tem cidade):

| COUNT(*) | COUNT(cidade) |
|---|---|
| 8 | 7 |

```sql
SELECT AVG(preco), SUM(preco), MIN(preco), MAX(preco) FROM produto;
```

Resultado:

| AVG | SUM | MIN | MAX |
|---|---|---|---|
| 18 | 90 | 3 | 35 |

`BETWEEN a AND b` inclui os extremos; `IN (lista)` e `NOT IN (lista)` testam pertencer à lista.

```sql
SELECT nome FROM produto WHERE preco BETWEEN 10 AND 20 OR id_fornecedor NOT IN (1, 3) ORDER BY nome;
```

Resultado:

| nome |
|---|
| Caderno |
| Cartaz |
| Pincel |

LIKE compara com um padrão: `%` é qualquer sequência (até vazia) e `_` é exatamente um caractere. No SQLite, LIKE não diferencia maiúsculas de minúsculas nas letras ASCII.

```sql
SELECT nome FROM cliente WHERE cidade LIKE 'M%' OR cidade LIKE '_orto' ORDER BY nome;
```

Resultado:

| nome |
|---|
| Ana Lima |
| Carla Dias |
| Davi Melo |

Colchetes (`[abc]`, `[a-c]`, `[!abc]`) não são do LIKE padrão: são do SQL Server e do Access. No SQLite, use GLOB, que diferencia maiúsculas e usa `*` e `?` no lugar de `%` e `_`:

```sql
SELECT nome FROM cliente WHERE cidade GLOB '[LO]*' ORDER BY nome;
```

Resultado:

| nome |
|---|
| Elisa Nunes |
| Hana Ito |

Correções da equipe
- No slide, os modelos de BETWEEN e de NOT IN repetem os de COUNT e MAX; a forma certa está acima.
