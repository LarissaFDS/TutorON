---
id: bd-cc-hospital-filtros-juncoes
titulo: Lista 2 de SQL (hospital): pacientes com sarampo, ortopedistas com mais de 40 anos e precedência de AND e OR
assunto: bd-10-juncoes-uniao
tipo: exercicio_resolvido
resolucao: sim
fonte: Lista 2 de exercícios de SQL (esquema de hospital), material da turma de Ciência da Computação (UFAL), questões 1, 2 e 6
curso: Ciência da Computação (UFAL), material de Banco de Dados 1 da turma de CC
fontes_catalogo: ufal-cc-bd-lista2-hospital,sqlite-docs
banco_teste: hospital_cc
autoria: Enunciados: Lista 2 de SQL (autoria não identificada no arquivo), parafraseados; resolução e dados de teste da equipe TutorON com auxílio de IA
licenca: Não declarada (lista de exercícios)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; a lista e o dump da turma não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Status da resolução: pendente de confirmação do professor (resolução da equipe TutorON). Os dados são de teste, inventados pela equipe para conferir o SQL; o dump da turma não foi usado.

Esquema: Ambulatorio(numeroA, andar, capacidade), Medico(CRM, nome, idade, codcidade, especialidade, numeroA), Especialidade(codEsp, nome), Cidade(codCidade, descricao, uf), Paciente(RG, nome, idade, codcidade), Doenca(codDoenca, descricao), Consulta(CRM, RG, data, hora, coddoenca), Funcionario(RG, nome, idade, codcidade, salario).

**Pacientes com sarampo** (questão 1). A doença fica na consulta, então a junção passa por Consulta e Doenca. O DISTINCT evita repetir quem tem duas consultas por sarampo (Gil, nos dados de teste).

```sql
SELECT DISTINCT P.RG, P.nome, P.idade
FROM Paciente P
  JOIN Consulta C ON C.RG = P.RG
  JOIN Doenca D ON D.codDoenca = C.coddoenca
WHERE D.descricao = 'sarampo'
ORDER BY P.RG;
```

Resultado:

| RG | nome | idade |
|---|---|---|
| 22 | Gil | 30 |
| 25 | Hana | 8 |

**Ortopedistas com mais de 40 anos** (questão 2). Especialidade é chave estrangeira: compare pelo nome na tabela Especialidade, não pelo código.

```sql
SELECT M.CRM, M.nome, M.idade
FROM Medico M JOIN Especialidade E ON E.codEsp = M.especialidade
WHERE E.nome = 'ortopedia' AND M.idade > 40;
```

Resultado:

| CRM | nome | idade |
|---|---|---|
| 46 | Carla | 45 |

**Ambulatórios do quarto andar com capacidade 50 ou número maior que 10** (questão 6). AND vem antes de OR: sem os parênteses, o ambulatório 15 (quinto andar) e o 20 (segundo) entrariam pelo número.

```sql
SELECT numeroA, capacidade
FROM Ambulatorio
WHERE andar = 4 AND (capacidade = 50 OR numeroA > 10)
ORDER BY numeroA;
```

Resultado:

| numeroA | capacidade |
|---|---|
| 4 | 50 |
| 12 | 60 |

**Verificação:** as três consultas rodaram no SQLite com o banco de teste `hospital_cc`, e o teste confere as tabelas acima.
