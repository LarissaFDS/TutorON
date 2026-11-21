---
id: logica-consequencia-logica-teoremas
titulo: Consequência lógica (⊨): como provar por tabela-verdade e os teoremas T1 (validade) e T2 (inconsistência)
assunto: logica-03-consequencia-equivalencia
tipo: material_estudo
resolucao: sim
fonte: Slides de Lógica Clássica Proposicional (Baldoino Fonseca, UFAL), consequência lógica e aplicações de T1 e T2
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

**Consequência lógica:** $\Gamma\models\alpha$ (lê-se "alfa é consequência lógica de gama") quando toda valoração que torna verdadeiras todas as fórmulas de $\Gamma$ torna $\alpha$ verdadeira. É uma noção **semântica**, de modelos; não fala de regras de prova (essa é a derivação $\vdash$).

**Teoremas** (com $\Gamma=\{\rho_1,\dots,\rho_n\}$): $\Gamma\models\alpha$ se e somente se
- **T1:** $(\rho_1\land\dots\land\rho_n)\to\alpha$ é **válida**;
- **T2:** $\rho_1\land\dots\land\rho_n\land\neg\alpha$ é **insatisfazível** (inconsistente).

**Exemplo dos slides (Paris):** "se é inverno em Paris, é verão em Brasília" ($P\to Q$), "se é verão em Brasília, chove" ($Q\to R$), "é inverno em Paris" ($P$). Por T1, $((P\to Q)\land(Q\to R)\land P)\to R$ é V nas 8 linhas; por T2, a conjunção com $\neg R$ é F nas 8. Logo $\{P\to Q,\;Q\to R,\;P\}\models R$.

**Por equivalências:** $\{P\lor H,\;\neg H\}\models P$. Por T1: $((P\lor H)\land\neg H)\to P\equiv\neg((P\lor H)\land\neg H)\lor P\equiv(\neg P\land\neg H)\lor H\lor P$, e $\neg P\land\neg H$ junto de $H\lor P$ é $\neg(P\lor H)\lor(P\lor H)\equiv\top$: válida.

**Também nos slides:** $((P\to\neg Q)\land(R\leftrightarrow\neg P)\land Q)\to R$ é válida.

**Como provar por tabela-verdade, linha a linha:** para provar $(\neg P\to Q)\land(R\to\neg P)\models Q\lor\neg R$, monte as 8 linhas de $P,Q,R$ com colunas $\neg P\to Q$, $R\to\neg P$ e $Q\lor\neg R$ e procure linhas com premissas V e conclusão F. A conclusão só é F com $Q$=F e $R$=V; aí $R\to\neg P$ exige $P$=F, e então $\neg P\to Q$ é F. Nenhuma linha é contraexemplo: a consequência vale.

**Verificação:** as quatro consequências foram conferidas por tabela-verdade completa em Python (T1 válida e T2 insatisfazível em todas).
