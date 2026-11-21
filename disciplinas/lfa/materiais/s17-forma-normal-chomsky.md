---
id: lfa-forma-normal-de-chomsky
titulo: Forma Normal de Chomsky (FNC) — produções A → BC ou A → a, algoritmo em três etapas, exemplo S → S+S | S*S | [S] | x; algoritmo CYK; Forma Normal de Greibach
assunto: lfa-05-livres-de-contexto
tipo: exercicio_resolvido
questao: exemplo 14
resolucao: sim
fonte: Apostila 03 (Profa. Simone Prado, UNESP), seção 6.1 e exemplo 14
fontes_catalogo: unesp-prado-apostilas-tc
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exemplo 14 da apostila, conferido. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**FNC:** toda produção é $A \to BC$ (duas variáveis) ou $A \to a$ (um terminal); se $\varepsilon \in L$, admite-se só $S \to \varepsilon$. Toda GLC tem uma equivalente na FNC.

**Algoritmo:**
1. Simplifique: tire as produções vazias, as unitárias e os símbolos inúteis.
2. Em lados direitos de comprimento $\ge 2$, troque cada terminal $a$ por uma variável nova $C_a$, com $C_a \to a$.
3. Quebre lados direitos com 3 ou mais variáveis em pares: $A \to B_1B_2B_3$ vira $A \to B_1D$ e $D \to B_2B_3$.

**Exemplo 14:** $S \to S+S \mid S*S \mid [S] \mid x$.
- Etapa 2: $S \to SC_+S \mid SC_*S \mid C_[SC_] \mid x$, com $C_+ \to +$, $C_* \to *$, $C_[ \to [$ e $C_] \to ]$.
- Etapa 3: $S \to SD_1 \mid SD_2 \mid C_[D_3 \mid x$, com $D_1 \to C_+S$, $D_2 \to C_*S$ e $D_3 \to SC_]$.

Todas as produções têm agora a forma $A \to BC$ ou $A \to a$.

**Para que serve:** na FNC, uma palavra de comprimento $n \ge 1$ tem derivação de exatamente $2n - 1$ passos. Isso dá o algoritmo **CYK** ($O(n^3)$), que decide se $w \in L(G)$ preenchendo uma tabela de subcadeias.

**Forma Normal de Greibach:** toda produção é $A \to a\alpha$, com $\alpha$ só de variáveis. Cada passo da derivação gera exatamente um terminal; é a base da construção do autômato com pilha sem transições vazias de leitura.

Erro comum: trocar terminal por variável também em $A \to a$ (essas produções já estão na forma certa).

**Verificação:** a gramática original e a FNC geram exatamente as mesmas palavras até comprimento 5 sobre $\{x, +, *, [, ]\}$ (Earley); a FNC tem 11 produções, todas da forma $A \to BC$ ou $A \to a$.
