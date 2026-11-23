---
id: comp-conjuntos-first-e-follow-condicoes-ll1-gramatica-e-linguagem-ll1-exemplos-de-prova
titulo: Conjuntos FIRST e FOLLOW e as condições LL(1): definição, cálculo e exemplos de prova (2010 e AB1 de 2017.1)
assunto: comp-02-analise-sintatica
tipo: exercicio_resolvido
questao: questões de LL(1) da prova de 2010 e da AB1 de 2017.1
resolucao: sim
fonte: Provas de Compiladores do Prof. Marcus Ramos (2009 e 2010), cópias da pasta da turma
curso: Ciência da Computação (UFAL), COMP263 Compiladores; provas de 2013 a 2017.1 e trabalhos de 2017.1 (o código ECOM045 aparece no cabeçalho da AB1 de 2017.1)
fontes_catalogo: ramos-provas-compiladores,ufal-compiladores-provas
autoria: Questões e respostas das provas do Prof. Marcus Ramos; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Compiladores (Ciência da Computação), questões de LL(1) da prova de 2010 e da AB1 de 2017.1 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**FIRST($\alpha$):** terminais que podem começar uma cadeia derivada de $\alpha$ (e $\varepsilon$ se $\alpha \Rightarrow^* \varepsilon$). **FOLLOW($A$):** terminais que podem vir logo depois de $A$ numa forma sentencial (inclui o fim de cadeia `$` se $A$ pode terminar a sentença).

**Gramática LL(1):** para cada não-terminal $A$ com alternativas $A \to \alpha \mid \beta$:
- FIRST($\alpha$) e FIRST($\beta$) disjuntos;
- se $\beta \Rightarrow^* \varepsilon$, então FIRST($\alpha$) e FOLLOW($A$) disjuntos.
Ou seja: sem recursão à esquerda, fatorada, e o próximo token decide a produção. **Linguagem LL(1)** é a gerada por alguma gramática LL(1).

**Prova de 2010 (é LL(1)):** $S \to bXc \mid aaYcb \mid ccZaa$, $X \to abc \mid \varepsilon$, $Y \to aY \mid bY \mid \varepsilon$, $Z \to Xb \mid cYc$.
- $S$: FIRST $= \{b\}, \{a\}, \{c\}$;
- $X$: FIRST$(abc) = \{a\}$ e FOLLOW$(X) = \{b, c\}$ (de $bXc$ e de $Xb$);
- $Y$: $\{a\}, \{b\}$ e FOLLOW$(Y) = \{c\}$;
- $Z$: FIRST$(Xb) = \{a, b\}$ e FIRST$(cYc) = \{c\}$. Tudo disjunto.

**Prova de 2010 (não é LL(1)):** $S \to abXc \mid aaYbc \mid ccZaa$: duas alternativas começam com $a$; além disso $X \to Xc$ tem recursão à esquerda.

**AB1 de 2017.1:**
- $S = A\,'b'$, $A = 'a' \mid B \mid \varepsilon$, $B = 'b' \mid \varepsilon$ **não** é LL(1): $A \to B$ e $A \to \varepsilon$ derivam a vazia, e FIRST$(B) = \{b\}$ cruza FOLLOW$(A) = \{b\}$;
- $S = 'a' S 'e' \mid B$, $B = 'b' B 'e' \mid C$, $C = 'c' B 'e' \mid 'd'$ **é** LL(1): os FIRST $\{a\}$ e $\{b, c, d\}$, $\{b\}$ e $\{c, d\}$, $\{c\}$ e $\{d\}$ são disjuntos.

**Verificação:** `test_first_follow_ll1` calcula FIRST, FOLLOW e os conflitos das quatro gramáticas.
