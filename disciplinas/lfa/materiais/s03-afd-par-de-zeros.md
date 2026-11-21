---
id: lfa-afd-numero-par-de-zeros
titulo: Como construir um AFD — número par de zeros, quíntupla (Q, Σ, δ, q0, F), tabela de transição, função estendida δ*, paridade de a e de b com 4 estados
assunto: lfa-02-automatos-finitos
tipo: material_estudo
resolucao: nao
fonte: Apostila 02 (Profa. Simone Prado, UNESP), definição de AFD e exemplos 04 e 05; aula 1 das notas de Sipser (MIT)
fontes_catalogo: unesp-prado-apostilas-tc,lee-sipser-notas-2012
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Um **autômato finito determinístico** é a quíntupla $M = (Q, \Sigma, \delta, q_0, F)$: estados $Q$ finitos, alfabeto $\Sigma$, função de transição $\delta: Q \times \Sigma \to Q$ (um destino para **cada** par estado–símbolo), estado inicial $q_0 \in Q$ e finais $F \subseteq Q$. A apostila escreve "$F \in Q$"; o correto é $F \subseteq Q$. $M$ aceita $w$ se $\delta^*(q_0, w) \in F$, em que $\delta^*$ (delta estendida) aplica $\delta$ símbolo a símbolo.

**Método:** cada estado guarda **o que é preciso lembrar** do prefixo lido. Para "número par de zeros" sobre $\{0,1\}$, basta a paridade dos zeros: $Q = \{p, i\}$ (par, ímpar), $q_0 = p$, $F = \{p\}$.

| $\delta$ | 0 | 1 |
|---|---|---|
| → $p$ (final) | $i$ | $p$ |
| $i$ | $p$ | $i$ |

Cadeia $1001$: $p \xrightarrow{1} p \xrightarrow{0} i \xrightarrow{0} p \xrightarrow{1} p$, aceita. Cadeia $010$: $p \xrightarrow{0} i \xrightarrow{1} i \xrightarrow{0} p$, aceita (dois zeros).

**Paridade de a e de b** (exemplo 05 da apostila): guarde as duas paridades, 4 estados $q_{00}, q_{01}, q_{10}, q_{11}$ (paridade de a, paridade de b); ler $a$ troca o primeiro índice e ler $b$ troca o segundo. "Número par de a **e** par de b" tem $F = \{q_{00}\}$; "ímpar de a e ímpar de b" tem $F = \{q_{11}\}$.

Erros comuns: deixar um símbolo sem transição em algum estado (o AFD fica parcial); esquecer de marcar o inicial como final quando $\varepsilon$ pertence à linguagem (zero zeros é par).

**Verificação:** simulado em `tests_acervo/lfa_verif.py` contra a contagem direta para todas as cadeias até comprimento 10: aceitas $\varepsilon$, 1, 00, 1001, 010; rejeitadas 0, 01, 000, 10100.
