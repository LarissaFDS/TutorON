---
id: bd2-aula-group-by-having
titulo: Aula de BD2 — GROUP BY e HAVING: filtrar grupos, diferença entre WHERE e HAVING, HAVING com JOIN
assunto: bd-09-consultas-agregacao
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), aula "JOIN, HAVING e PROCEDURE" (HAVING)
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
GROUP BY junta as linhas com o mesmo valor nas colunas indicadas e as funções de agregação são calculadas por grupo. Toda coluna do SELECT que não está numa agregação deve estar no GROUP BY.

WHERE filtra linhas antes de agrupar e não aceita funções de agregação; HAVING filtra grupos depois de agrupar e aceita. Ordem lógica: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY.

Exemplo da aula: número de clientes por país, só países com mais de um cliente, em ordem decrescente.

```sql
SELECT pais, COUNT(id_cliente) AS clientes
FROM cliente
GROUP BY pais
HAVING COUNT(id_cliente) > 1
ORDER BY clientes DESC;
```

Resultado (o Japão tem um cliente só):

| pais | clientes |
|---|---|
| Brasil | 5 |
| Portugal | 2 |

HAVING com JOIN: vendedores que registraram pelo menos dois pedidos. Os vendedores 1 e 3 têm o mesmo sobrenome (Ramos), então o agrupamento tem de ser pela chave:

```sql
SELECT v.id_vendedor, v.sobrenome, COUNT(p.id_pedido) AS pedidos
FROM pedido p JOIN vendedor v ON v.id_vendedor = p.id_vendedor
GROUP BY v.id_vendedor, v.sobrenome
HAVING COUNT(p.id_pedido) >= 2
ORDER BY v.id_vendedor;
```

Resultado:

| id_vendedor | sobrenome | pedidos |
|---|---|---|
| 1 | Ramos | 3 |
| 2 | Freitas | 2 |

Se agrupar só por sobrenome, os dois Ramos viram um grupo com 4 pedidos, e o vendedor 3, que tem um pedido só, entraria no resultado somado ao vendedor 1.

Para filtrar por nome antes de contar (o exemplo da aula com dois sobrenomes), o filtro de linha vai no WHERE: `WHERE v.sobrenome IN ('Ramos', 'Freitas')`, e só a contagem vai no HAVING.

Correções da equipe
- O exemplo de HAVING com JOIN do slide agrupa pelo sobrenome do funcionário; com homônimos os pedidos se somam. Agrupe pela chave (e pelo sobrenome, para mostrá-lo).
