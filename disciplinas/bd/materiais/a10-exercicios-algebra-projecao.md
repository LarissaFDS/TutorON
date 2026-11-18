---
id: bd-aula-exercicios-algebra-projecao
titulo: Exercícios de BD — álgebra relacional, projeção (pi) com seleção no esquema de ambulatórios, médicos e consultas
assunto: bd-06-algebra-relacional
tipo: exercicio_resolvido
resolucao: sim
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 4 "Álgebra Relacional", exercícios de projeção
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
Status da resolução: pendente de confirmação do professor (resolução da equipe TutorON). Dados de teste criados pela equipe; esquema igual ao dos exercícios de seleção.

1. Nome e especialidade de todos os médicos: $\pi_{\text{nome},\,\text{especialidade}}(\text{Medicos})$.
2. Número dos ambulatórios do 3º andar: $\pi_{\text{nroa}}(\sigma_{\text{andar} = 3}(\text{Ambulatorios}))$.
3. Código dos médicos e datas das consultas dos pacientes 122 e 725: $\pi_{\text{codm},\,\text{data}}(\sigma_{\text{codp} = 122 \vee \text{codp} = 725}(\text{Consultas}))$.
4. Ambulatórios com capacidade maior que 50, exceto os do 2º e do 4º andar: $\pi_{\text{nroa}}(\sigma_{\text{capacidade} > 50 \wedge \text{andar} \neq 2 \wedge \text{andar} \neq 4}(\text{Ambulatorios}))$.

A seleção vai dentro e a projeção fora: se projetar primeiro só nroa, a coluna andar some e não dá mais para filtrar.

```sql
SELECT DISTINCT nroa FROM Ambulatorios WHERE andar = 3;
```

Resultado:

| nroa |
|---|
| 3 |
| 6 |

```sql
SELECT DISTINCT codm, data FROM Consultas WHERE codp IN (122, 725);
```

Resultado:

| codm | data |
|---|---|
| 46 | 2024-06-10 |
| 79 | 2024-06-10 |
| 46 | 2024-06-12 |
| 79 | 2024-06-13 |

```sql
SELECT DISTINCT nroa FROM Ambulatorios WHERE capacidade > 50 AND andar NOT IN (2, 4);
```

Resultado (o 2 tem capacidade 60, mas fica no 2º andar):

| nroa |
|---|
| 6 |

Use DISTINCT para ter o mesmo resultado da projeção, que elimina tuplas repetidas.
