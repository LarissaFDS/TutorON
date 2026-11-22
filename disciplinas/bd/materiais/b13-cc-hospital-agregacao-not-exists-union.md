---
id: bd-cc-hospital-agregacao-not-exists-union
titulo: Lista 2 de SQL (hospital): médicos por especialidade com COUNT e LEFT JOIN, médicos sem consulta com NOT EXISTS e UNION de três tabelas
assunto: bd-11-subconsultas
tipo: exercicio_resolvido
resolucao: sim
fonte: Lista 2 de exercícios de SQL (esquema de hospital), material da turma de Ciência da Computação (UFAL), questões 3, 4 e 13
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

**Como contar o número de médicos de cada especialidade** (questão 3)? Com GROUP BY. LEFT JOIN com COUNT(coluna) mostra também especialidade sem médico (com 0); COUNT(*) contaria 1 nesse caso.

```sql
SELECT E.nome, COUNT(M.CRM) AS total
FROM Especialidade E LEFT JOIN Medico M ON M.especialidade = E.codEsp
GROUP BY E.codEsp, E.nome
ORDER BY E.nome;
```

Resultado:

| nome | total |
|---|---|
| cardiologia | 1 |
| ortopedia | 2 |
| pediatria | 1 |

**Como listar os médicos que não têm consultas** (questão 4)? Com NOT EXISTS. NOT EXISTS não sofre com NULL; `CRM NOT IN (SELECT CRM FROM Consulta)` falharia se alguma consulta tivesse CRM nulo.

```sql
SELECT M.nome
FROM Medico M
WHERE NOT EXISTS (SELECT 1 FROM Consulta C WHERE C.CRM = M.CRM);
```

Resultado:

| nome |
|---|
| Fábio |

**Médicos, pacientes e funcionários que moram em Florianópolis** (questão 13). Três SELECTs com as mesmas colunas unidos por UNION; o ORDER BY vale para o resultado todo.

```sql
SELECT M.nome, M.idade FROM Medico M JOIN Cidade C ON C.codCidade = M.codcidade WHERE C.descricao = 'Florianópolis'
UNION
SELECT P.nome, P.idade FROM Paciente P JOIN Cidade C ON C.codCidade = P.codcidade WHERE C.descricao = 'Florianópolis'
UNION
SELECT F.nome, F.idade FROM Funcionario F JOIN Cidade C ON C.codCidade = F.codcidade WHERE C.descricao = 'Florianópolis'
ORDER BY nome;
```

Resultado:

| nome | idade |
|---|---|
| Davi | 38 |
| Elisa | 52 |
| Hana | 8 |
| Júlia | 29 |

**Verificação:** as três consultas rodaram no SQLite com o banco de teste `hospital_cc`, e o teste confere as tabelas acima.
