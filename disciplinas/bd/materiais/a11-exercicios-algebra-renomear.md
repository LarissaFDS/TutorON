---
id: bd-aula-exercicios-algebra-renomear
titulo: Exercícios de BD — álgebra relacional, renomear (rho) e autojunção: comparar uma tabela com ela mesma
assunto: bd-06-algebra-relacional
tipo: exercicio_resolvido
resolucao: sim
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 4 "Álgebra Relacional", exercícios de renomear
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
Status da resolução: pendente de confirmação do professor (resolução da equipe TutorON). Dados de teste criados pela equipe.

Para comparar linhas da mesma relação, renomeia-se uma cópia (ρ) e faz-se o produto cartesiano (×) com seleção. Em SQL, a cópia é um apelido (alias).

1. Ambulatórios com capacidade maior que a do ambulatório 100:
$$\text{A100} \leftarrow \rho_{\text{A100}}(\sigma_{\text{nroa} = 100}(\text{Ambulatorios}))$$
$$\pi_{\text{Ambulatorios.nroa}}(\sigma_{\text{Ambulatorios.capacidade} > \text{A100.capacidade}}(\text{Ambulatorios} \times \text{A100}))$$

```sql
SELECT a.nroa FROM Ambulatorios a, Ambulatorios a100
WHERE a100.nroa = 100 AND a.capacidade > a100.capacidade;
```

Resultado (o 100 tem capacidade 40):

| nroa |
|---|
| 2 |
| 3 |
| 4 |
| 6 |

2. Nome e CPF dos funcionários com salário menor ou igual ao do funcionário de CPF 1001 (ele mesmo entra no resultado):

```sql
SELECT f.nome, f.CPF FROM Funcionarios f, Funcionarios r
WHERE r.CPF = '1001' AND f.salario <= r.salario;
```

Resultado:

| nome | CPF |
|---|---|
| Rita | 1001 |
| Caio | 1002 |
| Nina | 1004 |

3. Pares de médicos diferentes com consulta na mesma data. Com `c1.codm < c2.codm`, cada par sai uma vez (sem "João, João" e sem repetir "Pedro, João"):

```sql
SELECT DISTINCT m1.nome, m2.nome
FROM Consultas c1 JOIN Consultas c2 ON c1.data = c2.data AND c1.codm < c2.codm
JOIN Medicos m1 ON m1.codm = c1.codm JOIN Medicos m2 ON m2.codm = c2.codm;
```

Resultado:

| médico 1 | médico 2 |
|---|---|
| João | Pedro |
| Maria | Ana |
