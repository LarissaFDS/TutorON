---
id: logica-deducao-natural-primeira-ordem
titulo: Dedução natural com quantificadores: ∀e, ∀i, ∃i, ∃e e exemplos
assunto: logica-11-deducao-natural-primeira-ordem
tipo: material_estudo
resolucao: sim
fonte: Slides Lógica de predicados: Dedução (Tiago Massoni, UFCG)
fontes_catalogo: ufcg-massoni-slides
autoria: Prof. Tiago Massoni (UFCG; Alloy com Prof. Rohit Gheyi), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

Valem todas as regras proposicionais, mais as de quantificadores ($\varphi[t/x]$ é $\varphi$ com o termo $t$ no lugar de $x$ livre):
- $\forall x\,e$: de $\forall x\,\varphi$, conclua $\varphi[t/x]$ para qualquer termo $t$.
- $\forall x\,i$: abra uma caixa com uma variável **nova** $x_0$; se provar $\varphi[x_0/x]$ sem hipótese sobre $x_0$, conclua $\forall x\,\varphi$.
- $\exists x\,i$: de $\varphi[t/x]$, conclua $\exists x\,\varphi$.
- $\exists x\,e$: de $\exists x\,\varphi$ e de uma caixa que supõe $\varphi[x_0/x]$ ($x_0$ novo) e chega a $\chi$ **sem** $x_0$, conclua $\chi$.

**Exemplo** ($H$: escrito em linguagem funcional; $M$: em linguagem OO): $\forall x(H(x)\to\neg M(x)),\;H(s)\vdash\neg M(s)$.
1. $\forall x(H(x)\to\neg M(x))$ — premissa; 2. $H(s)$ — premissa; 3. $H(s)\to\neg M(s)$ — $\forall x\,e$ 1; 4. $\neg M(s)$ — $\to e$ 3, 2.

**Exemplo com $\exists e$:** $\forall x(P(x)\to Q(x)),\;\exists x\,P(x)\vdash\exists x\,Q(x)$. 1. premissa; 2. premissa; 3. $P(x_0)$ — hipótese ($x_0$ novo); 4. $P(x_0)\to Q(x_0)$ — $\forall x\,e$ 1; 5. $Q(x_0)$ — $\to e$ 4, 3; 6. $\exists x\,Q(x)$ — $\exists x\,i$ 5; 7. $\exists x\,Q(x)$ — $\exists x\,e$ 2, 3–6.

**Exercício dos slides:** $\forall x(F(x)\land G(x))\vdash\forall x\,F(x)\land\forall x\,G(x)$. Caixa com $x_0$: $F(x_0)\land G(x_0)$ por $\forall x\,e$, $F(x_0)$ por $\land e_1$, feche com $\forall x\,i$; repita para $G$; junte com $\land i$.

Erro comum: usar em $\forall x\,i$ uma variável que aparece numa premissa, ou deixar $x_0$ na conclusão do $\exists e$.

**Verificação:** pela corretude, cada sequent foi conferido como consequência lógica: nenhum contramodelo em universos de até 3 elementos (busca exaustiva em Python).
