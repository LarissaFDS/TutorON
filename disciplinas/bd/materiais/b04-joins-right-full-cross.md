---
id: bd2-aula-joins-right-full-cross
titulo: Aula de BD2 — junções: RIGHT JOIN, FULL OUTER JOIN e CROSS JOIN com as tabelas FUNCIONARIO e CARGO
assunto: bd-10-juncoes-uniao
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), aula "JOIN, HAVING e PROCEDURE"
fontes_catalogo: ufal-bd2-slides,sqlite-docs
banco_teste: funcionario_cargo
autoria: Profª Cristina Tenório (slides), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Mesmas tabelas FUNCIONARIO e CARGO (4 funcionários, TADEU sem cargo; 3 cargos, GERENTE sem funcionário).

RIGHT JOIN devolve todas as linhas da tabela da direita; quando não há par, as colunas da esquerda vêm NULL. `A RIGHT JOIN B` dá o mesmo que `B LEFT JOIN A`. O SQLite aceita RIGHT e FULL a partir da versão 3.39.

```sql
SELECT F.NomeFuncionario, C.NomeCargo
FROM FUNCIONARIO F RIGHT JOIN CARGO C ON F.CodCargo = C.CodCargo
ORDER BY C.CodCargo, F.Matricula;
```

Resultado:

| NomeFuncionario | NomeCargo |
|---|---|
| JOÃO | CAIXA |
| CARLOS | CAIXA |
| MARIA | VENDEDOR |
| NULL | GERENTE |

FULL OUTER JOIN devolve os pares e também as linhas sem par dos dois lados:

```sql
SELECT F.NomeFuncionario, C.NomeCargo
FROM FUNCIONARIO F FULL OUTER JOIN CARGO C ON F.CodCargo = C.CodCargo;
```

Resultado (5 linhas, em qualquer ordem):

| NomeFuncionario | NomeCargo |
|---|---|
| JOÃO | CAIXA |
| MARIA | VENDEDOR |
| CARLOS | CAIXA |
| TADEU | NULL |
| NULL | GERENTE |

CROSS JOIN é o produto cartesiano: cada funcionário com cada cargo, sem condição.

```sql
SELECT COUNT(*) FROM FUNCIONARIO CROSS JOIN CARGO;
```

Resultado (4 × 3):

| COUNT(*) |
|---|
| 12 |

Correções da equipe
- A definição de RIGHT JOIN no slide fala da tabela da esquerda duas vezes; o RIGHT preserva a tabela da direita.
- Um slide escreve OUTER antes de FULL; a ordem é FULL OUTER JOIN. O nome RIGHT também aparece com letras trocadas.
- A imagem do resultado do CROSS JOIN mostra só 9 linhas; o produto tem 12.
