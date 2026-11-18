---
id: bd-nota-indices
titulo: Nota da equipe — índices e métodos de acesso: primário, secundário, árvore B+ e hash
assunto: bd-13-indices-acesso
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
A ementa de ECOM041 cita métodos de acesso primário e secundário, mas os slides vistos pela equipe não tratam do tema; esta nota é da equipe e aguarda revisão humana.

- Índice primário (de agrupamento): definido sobre o campo que ordena o arquivo; um por tabela. Secundário: sobre outro campo; pode haver vários.
- Árvore B+: dados (ou ponteiros) só nas folhas, folhas encadeadas; busca, inserção e remoção em O(log n) acessos e boa para intervalos (`BETWEEN`, `ORDER BY`).
- Hash: bom para igualdade, inútil para intervalo.
- `CREATE INDEX idx_cliente_cidade ON cliente (cidade);` acelera consultas por cidade, mas deixa INSERT e UPDATE mais lentos. No SQLite, `EXPLAIN QUERY PLAN` mostra se o índice foi usado.
