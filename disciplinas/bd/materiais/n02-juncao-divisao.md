---
id: bd-nota-juncao-divisao
titulo: Nota da equipe — álgebra relacional: junção (theta, natural) e divisão, com SQL
assunto: bd-06-algebra-relacional
tipo: material_estudo
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: relax,sqlite-docs
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Os slides de álgebra vistos pela equipe param na união; esta nota é da equipe e aguarda revisão humana.

- Junção theta: $R \bowtie_{c} S = \sigma_{c}(R \times S)$. Em SQL, `R JOIN S ON c`.
- Equijunção: a condição só usa igualdade. Junção natural: igualdade em todos os atributos de mesmo nome, que aparecem uma vez só (`NATURAL JOIN`).
- Divisão: $R \div S$ devolve os valores de R associados a todos os valores de S (alunos que cursaram todas as disciplinas obrigatórias). Em SQL, com dupla negação: não existe disciplina obrigatória que o aluno não cursou.

```sql
CREATE TABLE cursou (aluno TEXT, disc TEXT);
CREATE TABLE obrigatoria (disc TEXT);
INSERT INTO cursou VALUES ('Ana', 'BD'), ('Ana', 'ED'), ('Bia', 'BD');
INSERT INTO obrigatoria VALUES ('BD'), ('ED');
SELECT DISTINCT c.aluno FROM cursou c
WHERE NOT EXISTS (SELECT 1 FROM obrigatoria o
                  WHERE NOT EXISTS (SELECT 1 FROM cursou x WHERE x.aluno = c.aluno AND x.disc = o.disc));
```

Resultado:

| aluno |
|---|
| Ana |
