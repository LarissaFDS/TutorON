---
id: lfa-linguagem-regular-vazia-finita-infinita
titulo: Linguagem regular vazia, finita ou infinita — teorema com n estados (palavras de comprimento menor que n; entre n e 2n), exemplo com aabaa
assunto: lfa-04-nao-regularidade
tipo: exercicio_resolvido
questao: teorema 04 e exemplo 18
resolucao: sim
fonte: Apostila 02 (Profa. Simone Prado, UNESP), teorema 04 e exemplo 18
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
Teorema 04 e exemplo 18 da apostila. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Teorema.** Seja $M$ um autômato finito com $n$ estados que aceita $L$. Então:
- $L$ é **vazia** se, e só se, $M$ não aceita nenhuma palavra com $|w| < n$;
- $L$ é **infinita** se, e só se, $M$ aceita alguma palavra com $n \le |w| < 2n$;
- $L$ é **finita** caso contrário.

Ideia: uma palavra aceita com $|w| \ge n$ passa duas vezes por um estado, e esse ciclo pode ser repetido (é o bombeamento). Uma palavra aceita muito longa pode ter o ciclo encurtado até cair na faixa de $n$ a $2n - 1$.

Os dois testes são **algoritmos**, porque só testam um número finito de palavras. Por isso os problemas "$L(M)$ é vazia?" e "$L(M)$ é infinita?" são decidíveis.

**Exemplo 18:** $M = (\{q_0,q_1,q_2\}, \{a,b\}, \delta, q_0, \{q_2\})$ com $\delta(q_0,a) = q_1$, $\delta(q_1,a) = q_2$ e $\delta(q_2,b) = q_0$. As transições ausentes rejeitam.

| $\delta$ | a | b |
|---|---|---|
| → $q_0$ | $q_1$ | — |
| $q_1$ | $q_2$ | — |
| $q_2$ (final) | — | $q_0$ |

Com $n = 3$, procure palavra aceita com $3 \le |w| < 6$. Encontra-se $aabaa$, de comprimento 5: $q_0 \to q_1 \to q_2 \to q_0 \to q_1 \to q_2$. Logo $L$ é infinita; de fato, $L = aa(baa)^*$.

Na prática, um algoritmo melhor do que testar palavras é olhar o grafo:
- $L$ é vazia se nenhum final é atingível a partir de $q_0$;
- $L$ é infinita se existe um ciclo atingível a partir de $q_0$ do qual se chega a um final.

**Verificação:** entre as palavras até comprimento 6, o autômato aceita exatamente aa e aabaa; e $aa(baa)^k$ é aceita para $k$ até 5.
