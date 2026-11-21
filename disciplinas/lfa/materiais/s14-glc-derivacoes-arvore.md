---
id: lfa-glc-derivacao-arvore-corrigido
titulo: Gramática livre de contexto — definição, aⁿbⁿ, wwᴿ, derivação mais à esquerda e mais à direita, árvore de derivação; correção: duas derivações da mesma árvore não são ambiguidade
assunto: lfa-05-livres-de-contexto
tipo: exercicio_resolvido
questao: exemplo 04
resolucao: sim
fonte: Apostila 03 (Profa. Simone Prado, UNESP), exemplos 01 a 05
fontes_catalogo: unesp-prado-apostilas-tc
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
**GLC:** $G = (V, T, P, S)$ com produções $A \to \alpha$, em que $A \in V$ e $\alpha \in (V \cup T)^*$. Exemplos da apostila:
- $\{a^nb^n \mid n \ge 0\}$: $S \to aSb \mid \varepsilon$;
- $\{ww^R\}$ (palíndromos de comprimento par): $S \to aSa \mid bSb \mid \varepsilon$.

**Derivação mais à esquerda:** em cada passo, troca-se a variável mais à esquerda (à direita: a mais à direita). Uma **árvore de derivação** tem $S$ na raiz, variáveis nos nós internos (filhos = lado direito de uma produção) e terminais ou $\varepsilon$ nas folhas.

**Exemplo 04:** $L = \{a^nb^m \mid n \ne m\}$ com $S \to AT \mid TB$, $T \to aTb \mid \varepsilon$, $A \to aA \mid a$, $B \to bB \mid b$. Para $aaab$:
- à esquerda: $S \Rightarrow AT \Rightarrow aAT \Rightarrow aaT \Rightarrow aaaTb \Rightarrow aaab$;
- à direita: $S \Rightarrow AT \Rightarrow AaTb \Rightarrow Aab \Rightarrow aAab \Rightarrow aaab$.

Exercício da apostila, com correção. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Correção:** a apostila conclui desse exemplo que a gramática é **ambígua**, o que está errado. As duas derivações usam as mesmas produções nos mesmos lugares: são a **mesma árvore**, percorrida em ordens diferentes. Toda palavra de qualquer GLC tem uma derivação à esquerda e uma à direita. Ambiguidade exige **duas árvores diferentes**, ou seja, duas derivações mais à esquerda diferentes. Para $aaab$ há só uma. Esta gramática não é ambígua: $T$ gera os pares $a^jb^j$, e a escolha entre $AT$ (sobram a) e $TB$ (sobram b) é forçada pela palavra.

**Verificação:** o reconhecedor de Earley confirma que a gramática gera exatamente $\{a^nb^m \mid n \ne m\}$ até comprimento 8, e a contagem de derivações mais à esquerda dá 1 para $aaab$ e para todas as palavras até comprimento 8.
