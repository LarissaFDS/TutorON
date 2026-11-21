---
id: logica-prova1-q3-alice-betty-carol
titulo: Prova 1 (2013), questão 3, e Lista Q7: argumento de Alice, Betty e Carol (inválido, com contraexemplo)
assunto: logica-03-consequencia-equivalencia
tipo: prova
resolucao: sim
questao: 3
fonte: Prova 1 de Lógica Aplicada à Computação, 15/05/2013 (Profs. Evandro Costa e Baldoino Fonseca, UFAL), questão 3; Lista de Questões proposicional, Q7
fontes_catalogo: ufal-baldoino-prova1-2013, ufal-baldoino-lista-proposicional
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questão de prova (paráfrase do enunciado) com resolução. Prova é atividade avaliativa: o tutor guia, não entrega. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Enunciado (paráfrase):** se Alice é eleita presidente, então Betty é eleita vice ou Carol é eleita tesoureira. Betty é eleita vice. Portanto, se Alice é eleita presidente, Carol não é eleita tesoureira. Formalizar e decidir a validade com um dos teoremas de consequência lógica.

**Formalização:** $A$: Alice presidente; $B$: Betty vice; $C$: Carol tesoureira. Premissas $A\to(B\lor C)$ e $B$; conclusão $A\to\neg C$.

**Resposta: o argumento é inválido.** Pelo T1, $((A\to(B\lor C))\land B)\to(A\to\neg C)$ deveria ser válida, mas é F quando $A$, $B$ e $C$ são todos V: as premissas ficam V e a conclusão $A\to\neg C$ fica V$\to$F = F. Esse é o **contraexemplo**: Alice, Betty e Carol eleitas. Pelo T2, a conjunção das premissas com $\neg(A\to\neg C)\equiv A\land C$ é satisfazível (pelo mesmo modelo).

O "ou" da primeira premissa é inclusivo; o argumento confunde "Betty é eleita" com "Carol não é eleita", o que só valeria com "ou… ou" exclusivo.

**Verificação:** tabela-verdade em Python: das 8 valorações, só $A$=$B$=$C$=V torna as premissas V e a conclusão F.
