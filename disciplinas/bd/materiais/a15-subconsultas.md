---
id: bd-aula-subconsultas
titulo: Aula de BD — subconsultas (consultas aninhadas): no WHERE, com IN, com comparação e correlacionadas
assunto: bd-11-subconsultas
tipo: material_estudo
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 8 "Subconsultas"
fontes_catalogo: ufal-bd-slides,sqlite-docs,postgresql-docs
banco_teste: estudante_nota
autoria: Profª Maria Cristina Tenório (slides, com créditos a material dos professores Tarsis Marinho e Patrick Brito), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Subconsulta (consulta interna ou aninhada) é um SELECT entre parênteses dentro de outro comando, quase sempre no WHERE. Ela pode aparecer em SELECT, INSERT, UPDATE e DELETE, e dentro de outra subconsulta.

- Com =, <, > e afins, a subconsulta deve devolver um único valor (uma linha e uma coluna).
- Se devolver várias linhas, use IN, EXISTS, ou ANY/ALL nos SGBDs que têm esses operadores.
- Não correlacionada: não usa colunas da consulta de fora; o resultado é o mesmo para todas as linhas. Correlacionada: usa coluna da consulta de fora e é avaliada para cada linha.

Exemplo da aula: alunos com nota melhor que a do aluno V002 (nota 80). Tabelas estudante(id_estudante, nome) e nota(id_estudante, nota_total), com V001 95, V002 80, V003 74 e V004 81.

```sql
SELECT e.id_estudante, e.nome, n.nota_total
FROM estudante e JOIN nota n ON n.id_estudante = e.id_estudante
WHERE n.nota_total > (SELECT nota_total FROM nota WHERE id_estudante = 'V002')
ORDER BY e.id_estudante;
```

Resultado:

| id_estudante | nome | nota_total |
|---|---|---|
| V001 | Alice | 95 |
| V004 | Diego | 81 |

Correlacionada, no SELECT: quantos alunos têm nota maior que a de cada um (a posição menos 1).

```sql
SELECT e.nome, (SELECT COUNT(*) FROM nota m WHERE m.nota_total > n.nota_total) AS acima
FROM estudante e JOIN nota n ON n.id_estudante = e.id_estudante
ORDER BY acima;
```

Resultado:

| nome | acima |
|---|---|
| Alice | 0 |
| Diego | 1 |
| Bento | 2 |
| Cecília | 3 |

Correções da equipe
- Os slides dizem que ORDER BY não pode estar na subconsulta e que GROUP BY faz o mesmo papel. SQLite e PostgreSQL aceitam ORDER BY na subconsulta (útil com LIMIT); GROUP BY agrupa, não ordena.
- Os slides dizem que BETWEEN não aceita subconsulta; `x BETWEEN (SELECT ...) AND (SELECT ...)` funciona quando cada subconsulta devolve um valor.
- "A interna roda antes da externa" só vale para a não correlacionada.
- Na tabela do slide a coluna da nota tem outro nome em inglês; na consulta ela é nota_total, como aqui.
