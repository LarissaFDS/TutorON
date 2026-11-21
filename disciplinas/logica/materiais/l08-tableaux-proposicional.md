---
id: logica-tableaux-proposicional
titulo: Método dos tableaux analíticos: regras, ramo fechado e exemplos (João e Maria, chimarrão)
assunto: logica-04-tableaux
tipo: material_estudo
resolucao: sim
fonte: Slides Linguagens Proposicionais (Baldoino Fonseca, UFAL), método dos tableaux analíticos
fontes_catalogo: ufal-baldoino-slides-proposicional
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

O **método dos tableaux** (tableaux analíticos) funciona assim: um **tableau** é uma árvore: a raiz tem as fórmulas do conjunto; as regras decompõem fórmulas em mais simples, seguindo a tabela-verdade. Regras que **não ramificam**: $A\land B$ dá $A$ e $B$; $\neg(A\lor B)$ dá $\neg A$ e $\neg B$; $\neg(A\to B)$ dá $A$ e $\neg B$; $\neg\neg A$ dá $A$. Regras que **ramificam**: $A\lor B$ abre $A\mid B$; $A\to B$ abre $\neg A\mid B$; $\neg(A\land B)$ abre $\neg A\mid\neg B$; $A\leftrightarrow B$ abre ($A,B$) $\mid$ ($\neg A,\neg B$).

Um ramo **fecha** quando contém uma fórmula e sua negação; fica **aberto** caso contrário; está **completo** quando não há mais o que decompor.

**Teoremas:** se um tableau para $\Gamma\cup\{\neg\alpha\}$ tem todos os ramos fechados, então $\Gamma\models\alpha$ (correção); se $\Gamma\models\alpha$, todo tableau completo para $\Gamma\cup\{\neg\alpha\}$ fecha (completude). Um ramo aberto e completo dá um contramodelo.

**João e Maria:** raiz $B\to A$, $A\to\neg B$, $\neg A\to B$, $\neg A$. De $\neg A\to B$: ramo $\neg\neg A$ fecha com $\neg A$; ramo $B$. De $B\to A$: $\neg B$ fecha com $B$; $A$ fecha com $\neg A$. Tudo fechado: vale $A$.

**Chimarrão:** "João gosta de chimarrão se é gaúcho" ($A\to B$), "João é gaúcho ou seu pai é nordestino" ($A\lor D$), "o pai é gaúcho, mas João não gosta de chimarrão" ($C\land\neg B$). O tableau tem um ramo **aberto** ($\neg A$, $D$, $C$, $\neg B$): o conjunto é satisfazível, porque nada na formalização liga $C$ (pai gaúcho) a $D$ (pai nordestino). Acrescentando $\neg(C\land D)$, todos os ramos fecham.

**Verificação:** em Python, a consequência de João e Maria vale; o conjunto do chimarrão tem o modelo $A$=F, $B$=F, $C$=V, $D$=V e fica insatisfazível com $\neg(C\land D)$.
