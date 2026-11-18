---
id: bd2-aula-joins-inner-left
titulo: Aula de BD2 — junções: INNER JOIN e LEFT JOIN com as tabelas FUNCIONARIO e CARGO
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
Tabelas da aula: CARGO(CodCargo, NomeCargo, ValorCargo) com C1 CAIXA 800, C2 VENDEDOR 1200, C3 GERENTE 2400; FUNCIONARIO(Matricula, NomeFuncionario, CodCargo) com 100 JOÃO C1, 110 MARIA C2, 120 CARLOS C1 e 130 TADEU sem cargo (NULL). Nos slides o tipo de ValorCargo é MONEY, do SQL Server; aqui é NUMERIC.

INNER JOIN devolve só as combinações em que a condição do ON é verdadeira: quem não tem par fica de fora.

```sql
SELECT F.NomeFuncionario, C.NomeCargo
FROM FUNCIONARIO F INNER JOIN CARGO C ON F.CodCargo = C.CodCargo
ORDER BY F.Matricula;
```

Resultado (TADEU não tem cargo e GERENTE não tem funcionário):

| NomeFuncionario | NomeCargo |
|---|---|
| JOÃO | CAIXA |
| MARIA | VENDEDOR |
| CARLOS | CAIXA |

LEFT JOIN (ou LEFT OUTER JOIN) devolve todas as linhas da tabela da esquerda; quando não há par, as colunas da direita vêm NULL.

```sql
SELECT F.NomeFuncionario, C.NomeCargo
FROM FUNCIONARIO F LEFT JOIN CARGO C ON F.CodCargo = C.CodCargo
ORDER BY F.Matricula;
```

Resultado:

| NomeFuncionario | NomeCargo |
|---|---|
| JOÃO | CAIXA |
| MARIA | VENDEDOR |
| CARLOS | CAIXA |
| TADEU | NULL |

Cuidado: um filtro sobre a tabela da direita no WHERE descarta as linhas com NULL e o LEFT vira INNER. Para manter todos os funcionários e só mostrar cargos acima de 1000, o filtro vai no ON:

```sql
SELECT F.NomeFuncionario, C.NomeCargo
FROM FUNCIONARIO F LEFT JOIN CARGO C ON F.CodCargo = C.CodCargo AND C.ValorCargo > 1000
ORDER BY F.Matricula;
```

Resultado:

| NomeFuncionario | NomeCargo |
|---|---|
| JOÃO | NULL |
| MARIA | VENDEDOR |
| CARLOS | NULL |
| TADEU | NULL |

Correções da equipe
- Um slide escreve a palavra OUTER antes de LEFT; a ordem certa é LEFT OUTER JOIN (ou só LEFT JOIN).
- O texto chama a coluna por outro nome; nas tabelas ela é CodCargo.
