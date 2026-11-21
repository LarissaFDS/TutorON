---
id: logica-equivalencias-e-conectivos
titulo: Equivalências lógicas (≡): leis de transformação, → só com ∧ e ¬, e → com NAND
assunto: logica-03-consequencia-equivalencia
tipo: exercicio
resolucao: sim
questao: Q1-Q2
fonte: Slides de Lógica Clássica Proposicional e Linguagens Proposicionais (Baldoino Fonseca, UFAL); Lista de Questões proposicional, Q1 e Q2
fontes_catalogo: ufal-baldoino-slides-proposicional, ufal-baldoino-lista-proposicional
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

$\alpha\equiv\beta$ (equivalentes) quando têm o mesmo valor em toda valoração; equivale a $\alpha\models\beta$ e $\beta\models\alpha$.

**Leis de transformação:** $p\leftrightarrow q\equiv(p\to q)\land(q\to p)$; $p\to q\equiv\neg p\lor q$; comutatividade e associatividade de $\land$ e $\lor$; distributivas $p\land(q\lor r)\equiv(p\land q)\lor(p\land r)$ e $p\lor(q\land r)\equiv(p\lor q)\land(p\lor r)$; $p\land\top\equiv p$, $p\lor\bot\equiv p$, $p\land\bot\equiv\bot$, $p\lor\top\equiv\top$; $p\land\neg p\equiv\bot$, $p\lor\neg p\equiv\top$; $\neg\neg p\equiv p$; De Morgan $\neg(p\land q)\equiv\neg p\lor\neg q$ e $\neg(p\lor q)\equiv\neg p\land\neg q$; $\neg(p\to q)\equiv p\land\neg q$.

**Q1 (só $\land$ e $\neg$):** $p\to q\equiv\neg p\lor q\equiv\neg(p\land\neg q)$ (De Morgan e dupla negação).

**Q2 (só NAND, $p\uparrow q\equiv\neg(p\land q)$):** $\neg q\equiv q\uparrow q$, então $p\to q\equiv\neg(p\land\neg q)\equiv p\uparrow(q\uparrow q)$.

**Distributividade da implicação (slide):** $A\to(B\to C)\equiv(A\to B)\to(A\to C)$. **Exportação (slides da UFCG):** $(C\land T)\to E\equiv C\to(T\to E)$.

**Verificação:** todas as equivalências deste bloco foram conferidas em Python por tabela-verdade completa.
