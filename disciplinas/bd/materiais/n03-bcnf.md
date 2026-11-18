---
id: bd-nota-bcnf
titulo: Nota da equipe — forma normal de Boyce-Codd (BCNF) e decomposição sem perda
assunto: bd-07-dependencia-normalizacao
tipo: material_estudo
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: watt-dbdesign
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Os slides de normalização vistos pela equipe vão até a 3FN; esta nota é da equipe e aguarda revisão humana.

BCNF: para toda DF não trivial X → Y, X é superchave. Toda relação na BCNF está na 3FN; o contrário nem sempre. Exemplo clássico: Aula(aluno, disciplina, professor) com professor → disciplina e {aluno, disciplina} → professor. Está na 3FN (disciplina é atributo primário), mas não na BCNF, porque professor não é superchave. Decompondo em (professor, disciplina) e (aluno, professor), a junção recupera a relação sem perda, mas a DF {aluno, disciplina} → professor deixa de ser conferida numa tabela só.
