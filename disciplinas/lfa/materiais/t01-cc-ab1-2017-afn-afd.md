---
id: lfa-cc-ab1-2017-afn-para-afd-aa-ou-bb
titulo: AB1 de 2017.2 (Ciência da Computação) — AFN com transição vazia para 0*1*, AFN de palavras com aa ou bb convertido em AFD, autômatos para sufixo bb e subpalavra aa
assunto: lfa-02-automatos-finitos
tipo: prova
questao: 2 a 5
resolucao: sim
fonte: AB1 de Teoria da Computação 2017.2, turma de Ciência da Computação da UFAL (foto da prova; professor não identificado), questões 2 a 5
curso: Ciência da Computação (UFAL), turma de Teoria da Computação (COMP376), 2017.2
fontes_catalogo: ufal-cc-tc-provas-2017-2
autoria: Questões da prova (professor não identificado na foto); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, foto não versionada
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
AB1 de 2017.2 da turma de Ciência da Computação, questões 2 a 5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Figura 1 (AFN com movimento vazio):** $q_0$ inicial com laço em 0, transição vazia $q_0 \xrightarrow{\varepsilon} q_f$, $q_f$ final com laço em 1. $M=(\{q_0,q_f\},\{0,1\},\delta,q_0,\{q_f\})$, $\delta(q_0,0)=\{q_0\}$, $\delta(q_0,\varepsilon)=\{q_f\}$, $\delta(q_f,1)=\{q_f\}$. Reconhece $0^*1^*$ (em palavras: alguns zeros e depois alguns uns). Computação de 011: fecho-ε inicial $\{q_0,q_f\}$; lê 0 → $\{q_0,q_f\}$; lê 1 → $\{q_f\}$; lê 1 → $\{q_f\}$: termina em final, aceita.

**Figura 2 (AFN sem movimento vazio):** $q_0$ inicial com laço em a e b; $q_0 \xrightarrow{a} q_2 \xrightarrow{a} q_3$ e $q_0 \xrightarrow{b} q_1 \xrightarrow{b} q_3$; $q_3$ final com laço em a e b. Reconhece as palavras que têm **aa ou bb** como subpalavra. Computação de abb: $\{q_0\} \xrightarrow{a} \{q_0,q_2\} \xrightarrow{b} \{q_0,q_1\} \xrightarrow{b} \{q_0,q_1,q_3\}$: aceita.

**Questão 4 — AFD equivalente (construção de subconjuntos):**

| $\delta'$ | a | b |
|---|---|---|
| → $\{q_0\}$ | $\{q_0,q_2\}$ | $\{q_0,q_1\}$ |
| $\{q_0,q_2\}$ | $\{q_0,q_2,q_3\}$ | $\{q_0,q_1\}$ |
| $\{q_0,q_1\}$ | $\{q_0,q_2\}$ | $\{q_0,q_1,q_3\}$ |
| $\{q_0,q_2,q_3\}$ (final) | $\{q_0,q_2,q_3\}$ | $\{q_0,q_1,q_3\}$ |
| $\{q_0,q_1,q_3\}$ (final) | $\{q_0,q_2,q_3\}$ | $\{q_0,q_1,q_3\}$ |

Cinco estados; os dois finais são equivalentes e podem ser fundidos num estado "já achei aa ou bb" (AFD mínimo com 4 estados).

**Questão 5:** (a) sufixo bb: estados "nenhum b no fim", "um b no fim", "bb no fim" (final); com a volta-se ao início, e "bb no fim" fica onde está com b. (b) subpalavra aa: estados "nada", "um a", "achou aa" (final, com laço em a e b); b volta de "um a" para "nada".

Erros comuns: esquecer o fecho-ε inicial (011 parece rejeitada); achar que a Figura 2 exige terminar em aa ou bb.

**Verificação:** `test_prova_cc_2017_ab1` em `tests_acervo/test_disciplina_lfa.py` gera a tabela por `AFN.subconjuntos()` e compara os autômatos com a definição das linguagens em todas as palavras até comprimento 8.
