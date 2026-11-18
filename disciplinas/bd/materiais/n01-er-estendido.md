---
id: bd-nota-er-estendido
titulo: Nota da equipe — ER estendido: entidade fraca, especialização e generalização, agregação
assunto: bd-04-er-estendido
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
Os slides de BD vistos pela equipe não trazem ER estendido; esta nota é da equipe e aguarda revisão humana.

- Entidade fraca: não tem chave própria; é identificada pela chave da entidade dona mais uma chave parcial (MENSALIDADE de um USUÁRIO, com mês/ano). Desenho de Chen: retângulo e losango duplos. Mapeamento: PK = PK do dono + chave parcial.
- Especialização e generalização: subclasses herdam os atributos da superclasse (PESSOA com ALUNO e PROFESSOR). Restrições: disjunta ou sobreposta; total ou parcial. Mapeamentos usuais: uma tabela por classe com a PK da superclasse como PK e FK nas subclasses; uma tabela só com coluna de tipo; ou só as subclasses, quando a especialização é total e disjunta.
- Agregação: trata um relacionamento como entidade para relacioná-lo com outra.
