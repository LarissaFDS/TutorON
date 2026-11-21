---
id: logica-resolucao-cachorros-agua
titulo: Lista de primeira ordem: provar por resolução que nenhum humano é vampiro e que ninguém desperdiça água
assunto: logica-12-forma-clausal-unificacao-resolucao
tipo: exercicio
resolucao: sim
questao: Q1, Q10
fonte: Listas de Questões de lógica de primeira ordem (Baldoino Fonseca, UFAL), Q1 (cachorros e vampiros) e Q10 (água e multas)
fontes_catalogo: ufal-baldoino-lista-primeira-ordem
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exercício da turma (paráfrase do enunciado) com resolução. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Q1 (cachorros):** S1, S2 implicam S3 (formalização em outro bloco). Cláusulas de S1, S2 e $\neg$S3: 1. $C(a)$; 2. $\neg H(y)\lor G(a,y)$; 3. $\neg C(x)\lor\neg V(y)\lor\neg G(x,y)$; 4. $H(b)$; 5. $V(b)$.
- 6. $G(a,b)$ (2, 4; $y/b$)
- 7. $\neg V(y)\lor\neg G(a,y)$ (1, 3; $x/a$)
- 8. $\neg G(a,b)$ (5, 7; $y/b$)
- 9. $\square$ (6, 8)
Pelo procedimento de Herbrand: as instâncias básicas $\neg H(b)\lor G(a,b)$ e $\neg C(a)\lor\neg V(b)\lor\neg G(a,b)$, com $C(a)$, $H(b)$, $V(b)$, já são insatisfazíveis em lógica proposicional.

**Q10 (água):** $\alpha$: todo mundo que desperdiça água ganha multa; $\beta$: não há multas; $\gamma$: ninguém desperdiça água. Em $\alpha$, $\exists z$ não depende de $y$ (pode ir para fora de $\forall y$), então a função de Skolem é $g(x)$. Cláusulas: 1. $\neg DE(x,y)\lor\neg A(y)\lor M(g(x))$; 2. $\neg DE(x,y)\lor\neg A(y)\lor G(x,g(x))$; 3. $\neg M(w)$ (de $\beta$); de $\neg\gamma\equiv\exists x\exists y(DE(x,y)\land A(y))$: 4. $DE(b,c)$; 5. $A(c)$.
- 6. $\neg A(c)\lor M(g(b))$ (1, 4; $x/b$, $y/c$)
- 7. $M(g(b))$ (5, 6)
- 8. $\square$ (3, 7; $w/g(b)$)
A cláusula 2 não é usada.

**Verificação:** as duas refutações foram conferidas passo a passo em Python (u.m.g. e resolventes recalculados).
