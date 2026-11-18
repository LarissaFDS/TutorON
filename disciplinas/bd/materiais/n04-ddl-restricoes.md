---
id: bd-nota-ddl-restricoes
titulo: Nota da equipe — DDL: CREATE TABLE com restrições (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, NOT NULL, DEFAULT) e ALTER TABLE
assunto: bd-08-sql-ddl-dml
tipo: material_estudo
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: sqlite-docs,postgresql-docs
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Os slides de BD2 revisam a DML; a DDL com restrições é nota da equipe e aguarda revisão humana.

```sql
PRAGMA foreign_keys = ON;
CREATE TABLE curso (id INTEGER PRIMARY KEY, nome TEXT NOT NULL UNIQUE);
CREATE TABLE aluno (
    matricula INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nota NUMERIC CHECK (nota >= 0 AND nota <= 10),
    situacao TEXT DEFAULT 'ativo',
    id_curso INTEGER REFERENCES curso (id) ON DELETE RESTRICT
);
ALTER TABLE aluno ADD COLUMN email TEXT;
INSERT INTO curso VALUES (1, 'Engenharia de Computação');
INSERT INTO aluno (matricula, nome, nota, id_curso) VALUES (10, 'Rui', 8.5, 1);
SELECT nome, situacao, email FROM aluno;
```

Resultado:

| nome | situacao | email |
|---|---|---|
| Rui | ativo | NULL |

Inserir nota 11 ou um id_curso inexistente dá erro de restrição. No SQLite, a FK só é conferida com o PRAGMA ligado e o ALTER TABLE é limitado (não remove restrições).
