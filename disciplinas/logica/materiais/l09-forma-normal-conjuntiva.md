---
id: logica-forma-normal-conjuntiva
titulo: Como converter uma fórmula para forma normal conjuntiva (CNF) e testar validade de uma CNF
assunto: logica-05-formas-normais-horn-sat
tipo: material_estudo
resolucao: sim
fonte: Slides Forma Normal: Transformações (Tiago Massoni, UFCG); slides Linguagens Proposicionais (Baldoino Fonseca, UFAL), notação clausal
fontes_catalogo: ufcg-massoni-slides, ufal-baldoino-slides-proposicional
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL) e Prof. Tiago Massoni (UFCG), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Forma normal conjuntiva (CNF):** conjunção de cláusulas, e cada cláusula é uma disjunção de literais (átomo ou átomo negado). Gramática: $L::=p\mid\neg p$; $D::=L\mid L\lor D$; $C::=D\mid D\land C$.

**Método 1, pela tabela-verdade:** para cada linha em que a fórmula dá F, forme uma disjunção com $p$ se $p$ é F nessa linha e $\neg p$ se $p$ é V; a conjunção dessas disjunções é uma CNF equivalente.

**Método 2, transformação direta** (cada passo dá fórmula equivalente):
1. eliminar $\leftrightarrow$ e $\to$: $A\to B\equiv\neg A\lor B$;
2. empurrar a negação até os átomos (De Morgan) e cortar dupla negação;
3. distribuir $\lor$ sobre $\land$: $A\lor(B\land C)\equiv(A\lor B)\land(A\lor C)$.

**Exemplo dos slides:** $T\lor E\to T$ vira $\neg(T\lor E)\lor T$, depois $(\neg T\land\neg E)\lor T$, depois $(\neg T\lor T)\land(\neg E\lor T)$.
**Outro (Baldoino):** $P\leftrightarrow(Q\land R)$ em CNF é $(\neg P\lor Q)\land(\neg P\lor R)\land(\neg Q\lor\neg R\lor P)$; em notação clausal, $\{\{\neg P,Q\},\{\neg P,R\},\{\neg Q,\neg R,P\}\}$.

**Para que serve:** uma cláusula é válida se e somente se contém um literal e sua negação; uma CNF é válida se e somente se todas as cláusulas são. Ex.: $(\neg Q\lor P\lor R\lor Q)\land(\neg P\lor R\lor P)$ é válida (a 1ª tem $Q$ e $\neg Q$; a 2ª, $P$ e $\neg P$). Nos slides, o "não é válida" seguinte refere-se a outro exemplo mostrado em figura. Satisfazibilidade de CNF em geral é difícil (problema SAT).

**Verificação:** as duas CNFs foram comparadas com as fórmulas originais em todas as linhas da tabela-verdade (Python), e o exemplo foi confirmado válido.
