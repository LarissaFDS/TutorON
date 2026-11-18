---
id: bd-nota-transacoes
titulo: Nota da equipe — transações: propriedades ACID, COMMIT e ROLLBACK, concorrência e recuperação
assunto: bd-14-transacoes-concorrencia-recuperacao
tipo: material_estudo
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: sqlite-docs,cmu-15445
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Transações estão na ementa e nos objetivos de BD2, mas não nos slides vistos pela equipe; esta nota é da equipe e aguarda revisão humana.

Transação é uma unidade lógica de trabalho. Propriedades ACID: atomicidade (tudo ou nada), consistência (de um estado válido a outro), isolamento (transações concorrentes não se enxergam pela metade) e durabilidade (o que teve COMMIT sobrevive a falhas).

```sql
CREATE TABLE conta (id INTEGER PRIMARY KEY, saldo NUMERIC NOT NULL CHECK (saldo >= 0));
INSERT INTO conta VALUES (1, 500), (2, 0);
BEGIN TRANSACTION;
UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
UPDATE conta SET saldo = saldo + 100 WHERE id = 2;
COMMIT;  -- ou ROLLBACK para desfazer as duas
SELECT id, saldo FROM conta ORDER BY id;
```

Resultado:

| id | saldo |
|---|---|
| 1 | 400 |
| 2 | 100 |

Problemas de concorrência: atualização perdida, leitura suja, leitura não repetível e fantasma. Controle: bloqueio em duas fases (2PL) e níveis de isolamento. Recuperação: log de escrita antecipada (WAL), checkpoints, refazer (redo) o que teve COMMIT e desfazer (undo) o resto.
