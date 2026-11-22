---
id: projsw-ordem-construtores-metodo-polimorfico
titulo: Ordem dos construtores na herança (Refeicao, Almoco, AlmocoPortatil, MistoQuente) e o perigo de chamar método polimórfico no construtor (atributo ainda null)
assunto: projsw-03-heranca-composicao
tipo: notas
questao: "o que vocês acham que acontecerá?" (exemplo do misto quente)
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seção "Reuso por composição e herança"
curso: Ciência da Computação (UFAL), pasta da turma de Programação 2 / Projeto de Software (COMP372); notas de aula da UFCG usadas pela turma
fontes_catalogo: ufcg-notas-programacao2
autoria: Notas de aula dos Profs. Jacques Sauvé, Raquel Lopes e Dalton Serey (DSC-UFCG); resolução e código da equipe TutorON
licenca: Copyright da UFCG nos exemplos; paráfrase, PDF não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase e código próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Notas de aula de Programação II da UFCG, seção "Reuso por composição e herança" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Pergunta da aula:** `MistoQuente` herda de `AlmocoPortatil`, que herda de `Almoco`, que herda de `Refeicao`; `MistoQuente` tem atributos `Pao`, `Queijo` e `Presunto` criados na declaração. Em que ordem os construtores rodam?

**Regra:** (1) todo construtor começa chamando, explícita ou implicitamente (`super()`), o construtor da superclasse, até chegar em `Object`; (2) depois os atributos da própria classe são inicializados; (3) só então roda o corpo do construtor. Saída: `Refeicao()`, `Almoco()`, `AlmocoPortatil()`, `Pao()`, `Queijo()`, `Presunto()`, `MistoQuente()`.

**Segunda versão:** cada construtor chama `prepara()`, que cada classe sobrescreve. A ligação é **dinâmica** também dentro do construtor: os três `prepara()` executam o de `MistoQuente`. Nas duas primeiras chamadas, os atributos de `MistoQuente` ainda não foram inicializados (`pao` vale `null`), porque o corpo de `Almoco` roda antes da etapa (2) de `MistoQuente`. Se `prepara()` usasse `pao.algo()`, daria `NullPointerException`.

**Conclusão das notas:** não chame, no construtor, métodos que possam ser sobrescritos; use métodos `private` ou `final`.

Erro comum: achar que dentro do construtor de `Almoco` roda `Almoco.prepara()`.

**Verificação:** `test_ordem_dos_construtores` compila e roda `tests_acervo/projsw_java/construtores` e compara as 13 linhas da saída, incluindo as duas chamadas com `pao` ainda `null`.
