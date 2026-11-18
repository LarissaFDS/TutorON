---
id: bd2-aula-union
titulo: Aula de BD2 — UNION e UNION ALL: combinar o resultado de dois SELECT, com e sem repetições
assunto: bd-10-juncoes-uniao
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), aula "JOIN, HAVING e PROCEDURE" (UNION)
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
UNION combina as linhas de dois ou mais SELECT e elimina as repetidas; UNION ALL mantém todas. Regras: os SELECT têm o mesmo número de colunas, na mesma ordem e com tipos compatíveis. Os nomes das colunas do resultado vêm do primeiro SELECT, e um ORDER BY só pode aparecer no fim, valendo para o resultado inteiro.

Exemplo da aula, com os nossos dados: cidades de Portugal das tabelas de clientes e de fornecedores. Clientes de Portugal moram no Porto e em Lisboa; o fornecedor de Portugal fica no Porto.

```sql
SELECT cidade FROM cliente WHERE pais = 'Portugal'
UNION
SELECT cidade FROM fornecedor WHERE pais = 'Portugal'
ORDER BY cidade;
```

Resultado (sem repetição):

| cidade |
|---|
| Lisboa |
| Porto |

```sql
SELECT cidade FROM cliente WHERE pais = 'Portugal'
UNION ALL
SELECT cidade FROM fornecedor WHERE pais = 'Portugal'
ORDER BY cidade;
```

Resultado (Porto aparece uma vez por tabela):

| cidade |
|---|
| Lisboa |
| Porto |
| Porto |

Para listar clientes e fornecedores juntos e saber de onde veio cada linha, acrescente uma coluna constante:

```sql
SELECT 'Fornecedor' AS tipo, nome FROM fornecedor WHERE pais = 'Portugal'
UNION
SELECT 'Cliente', nome FROM cliente WHERE pais = 'Portugal'
ORDER BY tipo, nome;
```

Resultado:

| tipo | nome |
|---|---|
| Cliente | Carla Dias |
| Cliente | Elisa Nunes |
| Fornecedor | Gráfica Norte |

UNION é a união da álgebra relacional e JOIN combina colunas: a união empilha linhas, a junção junta colunas lado a lado.

Correções da equipe
- O enunciado do slide escreve o nome da tabela de fornecedores com uma letra a menos; no banco de exemplo ela se chama Suppliers.
