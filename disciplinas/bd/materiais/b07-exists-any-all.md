---
id: bd2-aula-exists-any-all
titulo: Aula de BD2 — EXISTS, NOT EXISTS, IN, ANY e ALL com subconsultas; NOT IN com NULL
assunto: bd-11-subconsultas
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), aula "JOIN, HAVING e PROCEDURE" (EXISTS, ANY e ALL)
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
EXISTS é verdadeiro se a subconsulta devolve ao menos uma linha. Exemplo da aula: fornecedores com algum produto de preço menor que 20.

```sql
SELECT f.nome FROM fornecedor f
WHERE EXISTS (SELECT 1 FROM produto p WHERE p.id_fornecedor = f.id_fornecedor AND p.preco < 20)
ORDER BY f.nome;
```

Resultado:

| nome |
|---|
| Papelaria Sul |
| Tintas Leste |

Cuidado com NOT IN: se a subconsulta tiver um NULL, nenhuma linha passa (comparar com NULL dá desconhecido). Um cliente não tem cidade, então "fornecedores de cidades sem clientes" com NOT IN volta vazio:

```sql
SELECT nome FROM fornecedor WHERE cidade NOT IN (SELECT cidade FROM cliente);
```

Resultado: nenhuma linha.

```sql
SELECT f.nome FROM fornecedor f
WHERE NOT EXISTS (SELECT 1 FROM cliente c WHERE c.cidade = f.cidade);
```

Resultado:

| nome |
|---|
| Livraria Oeste |

`x = ANY (subconsulta)` é verdadeiro se x for igual a algum valor (o mesmo que IN); `x > ALL (subconsulta)` exige x maior que todos. Se a subconsulta for vazia, ALL é verdadeiro e ANY é falso. O SQLite não tem ANY nem ALL: o trecho abaixo é de PostgreSQL (conferido no DuckDB).

```sql
-- dialeto: postgresql
SELECT nome FROM produto
WHERE id_produto = ALL (SELECT id_produto FROM item_pedido WHERE quantidade = 30);
```

Resultado (só o produto 3 tem item com quantidade 30):

| nome |
|---|
| Cartaz |

No SQLite, `= ANY` vira IN e `> ALL` vira `NOT EXISTS` com a comparação invertida, ou `> (SELECT MAX(...))` quando a subconsulta não for vazia nem tiver NULL.

Correções da equipe
- O slide explica que ALL testa se todos os registros da tabela de itens têm quantidade 10. Não é isso: compara o id de cada produto com todos os ids devolvidos pela subconsulta. Com quantidade 10 há vários ids, nenhum produto é igual a todos e nada sai; se nenhum item tivesse quantidade 10, sairiam todos os produtos.
