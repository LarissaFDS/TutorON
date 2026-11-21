---
id: lfa-problema-da-parada-indecidivel
titulo: Por que o problema da parada é indecidível — A_TM por diagonalização (máquina D que contradiz a si mesma), HALT_TM por redução de A_TM, reconhecível mas não decidível
assunto: lfa-08-decidibilidade-parada
tipo: material_estudo
resolucao: nao
fonte: Aulas 8 e 9 das notas de Sipser (MIT, Holden Lee), A_TM indecidível e problema da parada; ementa de ECOM014
fontes_catalogo: lee-sipser-notas-2012,mit-ocw-18-404j,ufal-ppc-ecomp-2014
autoria: Aulas de Michael Sipser (MIT) nas notas de Holden Lee; paráfrase da equipe TutorON
licenca: Notas sem licença declarada; paráfrase. Curso aberto MIT OCW 18.404J sob CC BY-NC-SA 4.0
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
revisao_humana: pendente
---
$A_{TM} = \{\langle M, w\rangle \mid M$ é MT e aceita $w\}$ e $HALT_{TM} = \{\langle M, w\rangle \mid M$ para sobre $w\}$.

**Teorema 1: $A_{TM}$ é indecidível** (diagonalização).
1. Suponha que existe um decisor $H$: $H(\langle M, w\rangle)$ aceita se $M$ aceita $w$, e rejeita se não aceita (rejeita ou fica em laço).
2. Construa $D$: com entrada $\langle M\rangle$, rode $H(\langle M, \langle M\rangle\rangle)$ e responda o **contrário**.
3. Rode $D$ sobre $\langle D\rangle$. $D$ aceita $\langle D\rangle$ se, e só se, $H$ diz que $D$ **não** aceita $\langle D\rangle$, se e só se $D$ não aceita $\langle D\rangle$. Contradição.
4. Logo, $H$ não existe.

É a diagonal de Cantor: a linha $M$, coluna $\langle N \rangle$ da tabela diz se $M$ aceita $\langle N\rangle$, e $D$ inverte a diagonal.

**Teorema 2: o problema da parada, $HALT_{TM}$, é indecidível** (redução de $A_{TM}$).
1. Suponha um decisor $R$ para $HALT_{TM}$.
2. Construa um decisor $S$ para $A_{TM}$. Com entrada $\langle M, w\rangle$:
   - rode $R(\langle M, w\rangle)$; se $R$ rejeitar ($M$ não para), **rejeite**;
   - se $R$ aceitar, simule $M$ sobre $w$ (agora se sabe que termina) e responda o que $M$ responder.
3. $S$ sempre para e decide $A_{TM}$, o que contradiz o Teorema 1.

A **direção** da redução é a parte importante: reduzimos o problema já sabido indecidível ($A_{TM}$) ao novo ($HALT_{TM}$). "Se eu resolvesse HALT, resolveria $A_{TM}$."

Por que a parada é indecidível, em uma frase: um decisor da parada daria um decisor de $A_{TM}$, que não existe. Os dois são **reconhecíveis**: simule $M$ sobre $w$ e aceite quando ela aceitar (ou parar). Os complementos não são reconhecíveis.

Erro comum: tentar "provar" a indecidibilidade mostrando que um programa específico entra em laço. A indecidibilidade diz que nenhum programa **único** acerta para **todas** as entradas.

**Verificação:** prova conferida passo a passo pela equipe contra as notas de aula; não há conta a executar. A tabela finita da diagonal (8 máquinas × 8 entradas) é conferida em teste: a linha invertida difere de todas.
