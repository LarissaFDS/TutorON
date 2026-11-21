---
id: logica-formalizacao-primeira-ordem-exercicios
titulo: Formalizar em primeira ordem: dragões do zoológico, cachorros e vampiros, água e multas
assunto: logica-09-primeira-ordem-formalizacao
tipo: exercicio
resolucao: sim
questao: Q2, Q5, Q7
fonte: Listas de Questões de lógica de primeira ordem (Baldoino Fonseca, UFAL), questões de formalização (dragões, cachorros, água) com gabarito de uma das listas
fontes_catalogo: ufal-baldoino-lista-primeira-ordem
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Exercício da turma (paráfrase do enunciado) com resolução. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Dragões** ($D$ dragão, $A$ animal, $V$ vive no zoológico, $F$ feliz, $Z$ visitante, $B$ pessoa bondosa, $E(x,y)$: $x$ encontra $y$):
- S1 "todo dragão que vive no zoológico não é feliz": $\forall x(D(x)\land V(x)\to\neg F(x))$.
- S2 "todo animal que encontra pessoas bondosas é feliz": $\forall x\forall y(A(x)\land B(y)\land E(x,y)\to F(x))$.
- S3 "todo visitante é bondoso": $\forall x(Z(x)\to B(x))$. S4 "todo animal do zoológico encontra todo visitante": $\forall x(A(x)\land V(x)\to\forall y(Z(y)\to E(x,y)))$.
- S5 "todo dragão é animal": $\forall x(D(x)\to A(x))$. S6 "existe pelo menos um visitante": $\exists x\,Z(x)$. S7 "nenhum dragão vive no zoológico": $\neg\exists x(D(x)\land V(x))$.

**Cachorros** ($C$, $H$ humano, $V$ vampiro, $G(x,y)$: $x$ gosta de $y$):
- S1 "alguns cachorros gostam de todos os humanos": $\exists x(C(x)\land\forall y(H(y)\to G(x,y)))$.
- S2 "nenhum cachorro gosta de vampiro algum": $\neg\exists x(C(x)\land\exists y(V(y)\land G(x,y)))$.
- S3 "nenhum humano é vampiro": $\neg\exists x(H(x)\land V(x))$.

**Água** ($A$ água, $M$ multa, $DE(x,y)$: $x$ desperdiça $y$, $G(x,y)$: $x$ ganha $y$):
- "todo mundo que desperdiça água ganha uma multa": $\forall x(\exists y(DE(x,y)\land A(y))\to\exists z(M(z)\land G(x,z)))$.
- "não há multas": $\neg\exists x\,M(x)$. "Ninguém desperdiça água": $\forall x\forall y(DE(x,y)\to\neg A(y))$.

Note o padrão: "todo" com $\to$, "algum" com $\land$, "nenhum" como $\neg\exists$ com $\land$. As consequências (S1–S6 implicam S7; S1, S2 implicam S3; as duas primeiras de água implicam a terceira) estão provadas por resolução em outros blocos.

**Verificação:** as três consequências foram confirmadas sem contramodelo em universos de até 2 ou 3 elementos (busca exaustiva em Python) e por refutação conferida passo a passo.
