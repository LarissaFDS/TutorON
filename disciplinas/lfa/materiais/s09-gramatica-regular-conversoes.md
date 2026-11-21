---
id: lfa-gramatica-regular-e-conversoes
titulo: Gramática regular (linear à direita), conversão entre AFD e gramática regular, ER para AFN (Thompson) e AFD para ER por eliminação de estados (AFNG)
assunto: lfa-03-expressoes-gramaticas-regulares
tipo: material_estudo
resolucao: nao
fonte: Apostila 02 (Profa. Simone Prado, UNESP), gramática regular; aulas 2 e 3 das notas de Sipser (MIT), ER ↔ autômato
fontes_catalogo: unesp-prado-apostilas-tc,lee-sipser-notas-2012
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
**Gramática regular** (linear à direita): $G = (V, T, P, S)$ com produções $A \to aB$, $A \to a$ ou $A \to \varepsilon$. Ela gera exatamente as linguagens regulares.

**AFD → gramática:** cada estado vira uma variável, e o inicial vira $S$.
- Para cada transição $\delta(A, a) = B$, crie $A \to aB$.
- Para cada estado final $A$, crie $A \to \varepsilon$.

Exemplo, AFD do número par de zeros ($p$ inicial e final, $i$):
$$P \to 0I \mid 1P \mid \varepsilon \qquad I \to 0P \mid 1I$$
Derivação de 1001: $P \Rightarrow 1P \Rightarrow 10I \Rightarrow 100P \Rightarrow 1001P \Rightarrow 1001$.

**Gramática → AFN:** o caminho inverso. Cada variável vira um estado. $A \to aB$ vira uma transição de A para B com a. $A \to a$ vai para um final novo. $A \to \varepsilon$ torna A final.

**ER → AFN (Thompson):**
- símbolo: dois estados ligados pelo símbolo;
- $r + s$: um início novo com transições vazias para os dois AFN;
- $rs$: o final de $r$ ligado por vazio ao início de $s$;
- $r^*$: um início novo que também é final, com transições vazias para o início de $r$ e do fim de $r$ de volta.

O AFN resultante tem no máximo 2 estados por símbolo ou operador da ER.

**AFD → ER (eliminação de estados, como em Sipser):**
1. Acrescente um início novo e um final único, ligados por transições vazias.
2. Remova um estado $q$ de cada vez. Para cada par $p \to q \to r$, o rótulo de $p \to r$ vira $R_{pq}(R_{qq})^* R_{qr} + R_{pr}$.
3. Quando sobram só o início e o final, o rótulo entre eles é a ER.

Erro comum: misturar produções lineares à direita ($A \to aB$) e à esquerda ($A \to Ba$) na mesma gramática. Ela pode deixar de ser regular.

**Verificação:** a gramática do exemplo e o AFD geram as mesmas palavras até comprimento 8 (Earley em `tests_acervo/lfa_verif.py`); o AFN de Thompson de $(1^*01^*0)^*1^*$ é equivalente ao AFD do número par de zeros.
