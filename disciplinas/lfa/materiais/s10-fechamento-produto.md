---
id: lfa-fechamento-uniao-intersecao-complemento
titulo: Propriedades de fechamento das linguagens regulares — união e interseção pelo autômato produto, complemento trocando finais, concatenação e estrela por AFN
assunto: lfa-03-expressoes-gramaticas-regulares
tipo: material_estudo
resolucao: nao
fonte: Apostila 02 (Profa. Simone Prado, UNESP), fechamento para união e exemplo 19; aula 2 das notas de Sipser (MIT)
fontes_catalogo: unesp-prado-apostilas-tc,lee-sipser-notas-2012
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
As linguagens regulares são **fechadas** sob união, interseção, complemento, concatenação, estrela e reverso: aplicar a operação a regulares dá uma regular.

**Produto (união e interseção):** dados AFD totais $M_1 = (Q_1, \Sigma, \delta_1, q_1, F_1)$ e $M_2$, o AFD produto tem estados $Q_1 \times Q_2$, início $(q_1, q_2)$ e $\delta((p,q), a) = (\delta_1(p,a), \delta_2(q,a))$. Ele roda os dois em paralelo.
- União: finais $\{(p,q) \mid p \in F_1$ **ou** $q \in F_2\}$.
- Interseção: finais com **e**.

**Exemplo 19 da apostila:** $L_1$ = palavras sobre $\{a,b\}$ que começam com a; $L_2$ = palavras que terminam com a.
- $M_1$: $q_0 \xrightarrow{a} q_1$ (final, laço em a e b), $q_0 \xrightarrow{b} q_2$ (morto).
- $M_2$: $r_0 \xrightarrow{a} r_1$ (final), $r_1 \xrightarrow{b} r_0$, laços $r_0 \xrightarrow{b} r_0$ e $r_1 \xrightarrow{a} r_1$.

O produto atingível tem 5 estados: $(q_0,r_0)$, $(q_1,r_1)$, $(q_2,r_0)$, $(q_1,r_0)$, $(q_2,r_1)$.
- Para a união, todos são finais menos $(q_0, r_0)$ e $(q_2, r_0)$.
- Para a interseção (começa **e** termina com a), só $(q_1, r_1)$ é final: aceita a, aba, aa e rejeita ab, ba.

**Complemento:** num AFD **total**, troque finais e não finais. Num AFN isso não funciona: determinize antes.

**Concatenação e estrela:** ligue os AFN com transições vazias (como na construção de Thompson).

Uso típico: provar que uma linguagem **não** é regular por fechamento. Se $L \cap a^*b^* = \{a^n b^n\}$ e $a^*b^*$ é regular, então $L$ regular faria $a^n b^n$ regular, o que é falso.

**Verificação:** o produto de `tests_acervo/test_disciplina_lfa.py` é comparado com "começa com a e/ou termina com a" em todas as palavras até comprimento 9, com 5 estados atingíveis.
