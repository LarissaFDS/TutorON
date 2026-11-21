---
id: logica-deducao-natural-regras
titulo: Dedução natural proposicional: sequent, regras de introdução e eliminação, caixas de hipótese
assunto: logica-07-deducao-natural
tipo: material_estudo
resolucao: sim
fonte: Slides Lógica Proposicional: Dedução Natural (Tiago Massoni, UFCG)
fontes_catalogo: ufcg-massoni-slides
autoria: Prof. Tiago Massoni (UFCG; Alloy com Prof. Rohit Gheyi), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: corrigida (resolução da equipe TutorON, não é gabarito do professor; conferida com Python; o original tem erro apontado abaixo).

**Sequent** $\varphi_1,\dots,\varphi_n\vdash\psi$: "de $\varphi_1,\dots,\varphi_n$ **deriva-se** $\psi$" aplicando regras de prova, sem tabela-verdade. Testar argumentos por tabela-verdade não escala; a dedução natural raciocina pela forma.

**Regras** (Huth e Ryan, usadas nos slides):
- $\land i$: de $\varphi$ e $\psi$, $\varphi\land\psi$. $\land e_1$/$\land e_2$: de $\varphi\land\psi$, $\varphi$ (ou $\psi$).
- $\neg\neg i$ / $\neg\neg e$: de $\varphi$, $\neg\neg\varphi$; de $\neg\neg\varphi$, $\varphi$.
- $\to e$ (modus ponens): de $\varphi$ e $\varphi\to\psi$, $\psi$. **MT** (modus tollens): de $\varphi\to\psi$ e $\neg\psi$, $\neg\varphi$.
- $\to i$: abra uma **caixa** com a hipótese $\varphi$; se chegar a $\psi$ dentro dela, feche e conclua $\varphi\to\psi$.
- $\lor i_1$/$\lor i_2$: de $\varphi$, $\varphi\lor\psi$. $\lor e$: de $\varphi\lor\psi$, de uma caixa $\varphi\ldots\chi$ e de outra $\psi\ldots\chi$, conclua $\chi$.
- $\neg e$: de $\varphi$ e $\neg\varphi$, $\bot$. $\neg i$: caixa $\varphi\ldots\bot$ dá $\neg\varphi$. $\bot e$: de $\bot$, qualquer fórmula. **PBC** (prova por contradição): caixa $\neg\varphi\ldots\bot$ dá $\varphi$. **LEM**: $\varphi\lor\neg\varphi$.

Linhas de uma caixa fechada não podem ser citadas fora dela. Teorema é um sequent sem premissas: $\vdash p\to p$.

**Exemplo dos slides:** $p,\;\neg\neg(c\land d)\vdash\neg\neg p\land c$.
1. $p$ — premissa
2. $\neg\neg(c \land d)$ — premissa
3. $\neg\neg p$ — $\neg\neg i$ 1
4. $c \land d$ — $\neg\neg e$ 2
5. $c$ — $\land e_1$ 4
6. $\neg\neg p \land c$ — $\land i$ 3, 5

**Correção:** os slides citam $\land e_2$ na linha 5 (e, em outro exemplo, uma linha errada na regra $\to e$); com $c\land d$, quem extrai $c$ é $\land e_1$.

**Verificação:** a prova foi conferida linha a linha pelo verificador de dedução natural dos testes (cada linha segue das citadas).
