---
id: bd2-aula-case
titulo: Aula de BD2 — expressão CASE (como um IF-THEN-ELSE no SELECT e no ORDER BY)
assunto: bd-09-consultas-agregacao
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), aula "JOIN, HAVING e PROCEDURE" (CASE)
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
CASE testa as condições na ordem e devolve o valor da primeira verdadeira, como um IF-THEN-ELSE. Se nenhuma for verdadeira, devolve o ELSE; sem ELSE, devolve NULL. CASE é uma expressão: pode estar no SELECT, no WHERE, no ORDER BY e dentro de agregações.

Exemplo da aula: classificar a quantidade de cada item em relação a 30.

```sql
SELECT id_pedido, id_produto, quantidade,
       CASE WHEN quantidade > 30 THEN 'acima de 30'
            WHEN quantidade = 30 THEN 'igual a 30'
            ELSE 'abaixo de 30' END AS faixa
FROM item_pedido
WHERE quantidade >= 10
ORDER BY id_pedido, id_produto;
```

Resultado:

| id_pedido | id_produto | quantidade | faixa |
|---|---|---|---|
| 101 | 1 | 10 | abaixo de 30 |
| 102 | 2 | 10 | abaixo de 30 |
| 104 | 3 | 30 | igual a 30 |
| 105 | 1 | 40 | acima de 30 |
| 106 | 5 | 10 | abaixo de 30 |

Exemplo da aula: ordenar os clientes pela cidade, mas pelo país quando a cidade é NULL.

```sql
SELECT nome FROM cliente
ORDER BY (CASE WHEN cidade IS NULL THEN pais ELSE cidade END), nome;
```

Resultado (Fábio não tem cidade e entra pela palavra "Brasil"):

| nome |
|---|
| Fábio Rocha |
| Elisa Nunes |
| Ana Lima |
| Davi Melo |
| Hana Ito |
| Carla Dias |
| Bruno Costa |
| Gil Souza |

A condição do CASE usa `IS NULL`; `CASE cidade WHEN NULL THEN ...` nunca é verdadeiro, porque compara com =. `COALESCE(cidade, pais)` dá o mesmo resultado em menos texto.

Contagem condicional com CASE dentro de agregação:

```sql
SELECT SUM(CASE WHEN preco < 20 THEN 1 ELSE 0 END) AS baratos, COUNT(*) AS total FROM produto;
```

Resultado:

| baratos | total |
|---|---|
| 3 | 5 |
