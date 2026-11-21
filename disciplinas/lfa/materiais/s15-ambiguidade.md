---
id: lfa-ambiguidade-gramatica-linguagem-inerente
titulo: Ambiguidade — gramática ambígua (a+a*a com duas árvores), gramática não ambígua equivalente, linguagem inerentemente ambígua aⁿbᵐcᵐ ∪ aⁿbᵐcⁿ
assunto: lfa-05-livres-de-contexto
tipo: exercicio_resolvido
questao: exemplos 07, 08 e 09
resolucao: sim
fonte: Apostila 03 (Profa. Simone Prado, UNESP), definições 4 e 5 e exemplos 07 a 09
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
Exemplos 07 a 09 da apostila. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Definição precisa:** $G$ é **ambígua** se alguma palavra tem duas **árvores de derivação** diferentes, o que equivale a duas derivações **mais à esquerda** diferentes. A apostila diz "duas ou mais derivações", o que é impreciso: derivações em outra ordem da mesma árvore não contam (veja o bloco de derivações).

**Exemplo 07:** $S \to S+S \mid S*S \mid (S) \mid a$. A palavra $a+a*a$ tem duas derivações mais à esquerda:
- $S \Rightarrow S+S \Rightarrow a+S \Rightarrow a+S*S \Rightarrow \dots$, com o $*$ embaixo do $+$;
- $S \Rightarrow S*S \Rightarrow S+S*S \Rightarrow \dots$, com o $+$ embaixo do $*$.

Logo, a gramática é ambígua. Uma versão não ambígua impõe precedência: $E \to E+T \mid T$, $T \to T*F \mid F$, $F \to (E) \mid a$.

**Exemplo 08:**
- $S \to a \mid S+S$ é ambígua (a palavra $a+a+a$ tem duas árvores).
- $S \to a \mid a+S$ não é ambígua e gera a mesma linguagem.
- Logo, a **linguagem** não é inerentemente ambígua.

**Exemplo 09:** $L = \{a^nb^mc^m\} \cup \{a^nb^mc^n\}$ é **inerentemente ambígua**: toda GLC para ela é ambígua. A gramática $S \to S_1 \mid S_2$ da apostila é ambígua em $a^nb^nc^n$, que tem uma árvore por $S_1$ e outra por $S_2$.

**Correção:** isso mostra só que **essa** gramática é ambígua. Provar que **toda** gramática de $L$ é ambígua exige um argumento sobre todas as gramáticas (o lema de Ogden, em Hopcroft–Ullman). O exemplo ilustra a ideia; não é a prova.

O problema "uma GLC dada é ambígua?" é **indecidível** (por redução do problema da correspondência de Post).

**Verificação:** a contagem de derivações mais à esquerda dá 2 para $a+a*a$ na gramática do exemplo 07 e 1 na gramática com $E, T, F$; as duas geram as mesmas palavras até comprimento 7 sobre $\{a,+,*\}$.
