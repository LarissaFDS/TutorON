---
id: lfa-expressoes-regulares-sem-aa-cada-a-com-b
titulo: Expressões regulares — definição, ER sem aa como subpalavra sobre {a,b,c} e ER em que cada a é precedido ou seguido imediatamente por b
assunto: lfa-03-expressoes-gramaticas-regulares
tipo: lista
questao: revisão sobre linguagens regulares, questão 1 (a) e (b)
resolucao: sim
fonte: Atividade teórica de Teoria da Computação 2015.1 (Prof. Thyago, UFAL), revisão sobre linguagens regulares, questão 1
fontes_catalogo: ufal-thyago-atividade-2015-1,unesp-prado-apostilas-tc
autoria: Atividade do Prof. Thyago Tenório Martins de Oliveira (UFAL); resolução da equipe TutorON
licenca: Não declarada (atividade); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
**Expressão regular** sobre $\Sigma$: $\emptyset$, $\varepsilon$ e cada símbolo são ER; se $r$ e $s$ são ER, também são $r + s$ (união), $rs$ (concatenação) e $r^*$ (fecho). Precedência: $*$, depois concatenação, depois $+$. Uma linguagem é regular se, e só se, é denotada por uma ER (teorema de Kleene).

Atividade 2015.1, questão 1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**(a) Palavras sobre $\{a,b,c\}$ sem $aa$.** Ideia: todo $a$ que não está no fim é seguido de b ou c. Blocos: $b$, $c$, $ab$, $ac$; no fim, pode sobrar um $a$:
$$(b + c + a(b+c))^*(\varepsilon + a)$$
Em palavras: repetições de "b", "c", "ab" ou "ac", e opcionalmente um "a" no final.

**(b) Palavras sobre $\{a,b\}$ em que cada $a$ é precedido ou seguido imediatamente por $b$.**
- Uma sequência de três ou mais a tem um a do meio sem b ao lado, então não pode aparecer.
- Um par $aa$ só vale entre dois b: $baab$.
- Um a isolado precisa de um b de um dos lados; a palavra "a" sozinha não vale.

Dividindo a palavra em blocos que começam por b:
$$\varepsilon + (\varepsilon + a)(b + ba + baa)^*(b + ba)$$
O último bloco não pode ser $baa$, porque o segundo a ficaria sem b depois.

Para conferir uma ER: liste palavras curtas que **devem** estar (b, ab, ba, baab, bab) e que **não devem** (a, aa, aab, baa, baaab) e teste cada uma. Uma ER que aceita algo proibido costuma ter um bloco que "consome" o b de que o bloco seguinte precisava.

**Verificação:** as duas ER foram convertidas em AFN (Thompson) e comparadas com o teste direto da propriedade em todas as palavras até comprimento 7 em (a) e 11 em (b); uma tentativa anterior com o bloco $baab$ falhava em $baaba$.
