---
id: bd-aula-exercicios-algebra-selecao
titulo: Exercícios de BD — álgebra relacional, seleção (sigma) no esquema de ambulatórios, médicos, pacientes e consultas
assunto: bd-06-algebra-relacional
tipo: exercicio_resolvido
resolucao: sim
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 4 "Álgebra Relacional", exercícios de seleção
fontes_catalogo: ufal-bd-slides,relax,sqlite-docs
banco_teste: hospital
autoria: Profª Maria Cristina Tenório (enunciados); resolução e dados de teste da equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Status da resolução: pendente de confirmação do professor (resolução da equipe TutorON). Os dados abaixo são de teste, criados pela equipe para conferir o SQL.

Esquema: Ambulatórios(nroa, andar, capacidade), Médicos(codm, CPF, nome, idade, cidade, especialidade, nroa), Pacientes(codp, CPF, nome, idade, cidade, doença), Consultas(codm, codp, data, hora), Funcionários(codf, CPF, nome, idade, cidade, salário).

1. Pacientes com sarampo: $\sigma_{\text{doenca} = \text{'sarampo'}}(\text{Pacientes})$.
2. Ortopedistas com mais de 55 anos: $\sigma_{\text{especialidade} = \text{'ortopedia'} \wedge \text{idade} > 55}(\text{Medicos})$.
3. Consultas, exceto as dos médicos 46 e 79: $\sigma_{\text{codm} \neq 46 \wedge \text{codm} \neq 79}(\text{Consultas})$.
4. Ambulatórios do 4º andar com capacidade 50 ou número maior que 10: $\sigma_{\text{andar} = 4 \wedge (\text{capacidade} = 50 \vee \text{nroa} > 10)}(\text{Ambulatorios})$. Os parênteses são necessários: sem eles, o AND seria avaliado antes do OR.

```sql
SELECT codm, codp FROM Consultas WHERE codm <> 46 AND codm <> 79;
```

Resultado:

| codm | codp |
|---|---|
| 13 | 300 |
| 22 | 410 |

```sql
SELECT nroa FROM Ambulatorios WHERE andar = 4 AND (capacidade = 50 OR nroa > 10);
```

Resultado (o ambulatório 5 está no 4º andar, mas tem capacidade 8 e número 5):

| nroa |
|---|
| 4 |
| 12 |

```sql
SELECT codm, nome FROM Medicos WHERE especialidade = 'ortopedia' AND idade > 55;
```

Resultado:

| codm | nome |
|---|---|
| 79 | Pedro |
| 22 | Ana |

Observação: "número superior a 10" foi lido como o número do ambulatório (nroa); se for a capacidade, troque `nroa > 10` por `capacidade > 10`.
