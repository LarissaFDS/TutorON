---
id: logica-deducao-natural-exemplos
titulo: Dedução natural: provar p → q ⊢ ¬q → ¬p, modus tollens dentro de caixa e eliminação do ou
assunto: logica-07-deducao-natural
tipo: material_estudo
resolucao: sim
fonte: Slides Lógica Proposicional: Dedução Natural (Tiago Massoni, UFCG), exemplos de →i e de regras de disjunção
fontes_catalogo: ufcg-massoni-slides
autoria: Prof. Tiago Massoni (UFCG; Alloy com Prof. Rohit Gheyi), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Contrapositiva — como provar $p\to q\vdash\neg q\to\neg p$ por dedução natural:** Para concluir uma implicação, use $\to i$: suponha o antecedente $\neg q$ numa caixa e chegue a $\neg p$.
1. $p \to q$ — premissa
2. $\neg q$ — hipótese
3. $\neg p$ — MT 1, 2
4. $\neg q \to \neg p$ — $\to i$ 2–3

**Exemplo dos slides, provar em dedução natural** ($\neg j\to\neg c\vdash c\to\neg\neg j$; $j$: resolve em Java, $c$: resolve em C++):
1. $\neg j \to \neg c$ — premissa
2. $c$ — hipótese
3. $\neg\neg c$ — $\neg\neg i$ 2
4. $\neg\neg j$ — MT 1, 3
5. $c \to \neg\neg j$ — $\to i$ 2–4

**Eliminação do ou, provar em dedução natural** ($a\to d\vdash z\lor a\to z\lor d$; $a$: o método põe 10 na variável, $d$: vale 10, $z$: vale 0):
1. $a \to d$ — premissa
2. $z \lor a$ — hipótese
3. $z$ — hipótese
4. $z \lor d$ — $\lor i_1$ 3
5. $a$ — hipótese
6. $d$ — $\to e$ 1, 5
7. $z \lor d$ — $\lor i_2$ 6
8. $z \lor d$ — $\lor e$ 2, 3–4, 5–7
9. $z \lor a \to z \lor d$ — $\to i$ 2–8

Dica: comece pela forma da conclusão (implicação pede $\to i$; disjunção nas premissas pede $\lor e$ com uma caixa por caso).

**Verificação:** as três provas foram conferidas linha a linha pelo verificador dos testes, incluindo o escopo das caixas.
