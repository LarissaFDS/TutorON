---
id: lfa-alfabetos-cadeias-operacoes
titulo: Alfabeto, cadeia (palavra), linguagem, comprimento, prefixo, sufixo, reverso, concatenação, potência, fecho de Kleene L* e L+, palavras de {ε, a}^n
assunto: lfa-01-linguagens-chomsky
tipo: lista
questao: atividade teórica, revisão sobre linguagens, questões 1 e 2
resolucao: sim
fonte: Apostila 01 (Profa. Simone Prado, UNESP) e atividade teórica de Teoria da Computação 2015.1 (Prof. Thyago, UFAL), revisão sobre linguagens
fontes_catalogo: unesp-prado-apostilas-tc,ufal-thyago-atividade-2015-1
autoria: Apostila da Profa. Simone Prado (UNESP) e atividade do Prof. Thyago (UFAL); paráfrase e resolução da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
**Definições.** Um **alfabeto** $\Sigma$ (sigma) é um conjunto finito de símbolos. Uma **cadeia** ou palavra é uma sequência finita de símbolos de $\Sigma$; a cadeia vazia é $\varepsilon$ (a apostila escreve $\lambda$). $|w|$ é o comprimento. $\Sigma^*$ é o conjunto de todas as cadeias; $\Sigma^+ = \Sigma^* - \{\varepsilon\}$. Uma **linguagem** é um subconjunto de $\Sigma^*$.

Operações: prefixo, sufixo e subcadeia (trecho contíguo); reverso $w^R$; concatenação $w \circ v$ (associativa, com $\varepsilon$ como elemento neutro); potência $w^0 = \varepsilon$, $w^n = w\,w^{n-1}$. Para linguagens: $L_1 L_2 = \{xy \mid x \in L_1, y \in L_2\}$, $L^0 = \{\varepsilon\}$, $L^* = L^0 \cup L^1 \cup L^2 \cup \dots$ (fecho de Kleene) e $L^+ = L^1 \cup L^2 \cup \dots$; união, interseção, diferença e complemento $\overline{L} = \Sigma^* - L$.

Exemplo da apostila: $L = \{0, 11, 10\}$ dá $L^2$ com 9 cadeias (00, 011, 010, 110, 1111, 1110, 100, 1011, 1010).

Atividade 2015.1, revisão sobre linguagens. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.
- **Palavras de $\{\varepsilon, a\}^n$:** cada um dos $n$ fatores contribui $\varepsilon$ ou $a$, então $\{\varepsilon, a\}^n = \{\varepsilon, a, aa, \dots, a^n\}$, isto é, $\{a^k \mid 0 \le k \le n\}$ ($n+1$ palavras).
- **$L^*$ ou $L^+$ vazios?** $L^*$ nunca é vazio: sempre contém $\varepsilon$. $L^+$ é vazio só se $L = \emptyset$.
- **$L^*$ finito** só se $L = \emptyset$ ou $L = \{\varepsilon\}$ (nos dois casos $L^* = \{\varepsilon\}$); se $L$ tem uma palavra não vazia $w$, então $w, ww, www, \dots$ são todas diferentes. **$L^+$ finito** só se $L = \emptyset$ ($L^+ = \emptyset$) ou $L = \{\varepsilon\}$ ($L^+ = \{\varepsilon\}$).

Erro comum: confundir $\emptyset$ (linguagem sem palavras) com $\{\varepsilon\}$ (linguagem com a palavra vazia); $|\{\varepsilon\}| = 1$.

**Verificação:** enumeração em `tests_acervo/test_disciplina_lfa.py`: $\{\varepsilon,a\}^n$ tem $n+1$ palavras para $n \le 6$ e $L^2$ do exemplo tem 9 cadeias distintas.
