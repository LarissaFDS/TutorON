---
id: lfa-afn-para-afd-subconjuntos
titulo: Como converter um AFN em AFD — construção de subconjuntos passo a passo, AFN para palavras com sufixo aaa, fecho-ε (fecho vazio) quando há transições vazias
assunto: lfa-02-automatos-finitos
tipo: material_estudo
resolucao: nao
fonte: Apostila 02 (Profa. Simone Prado, UNESP), definição de AFN, exemplos 07 e 08 e algoritmo de equivalência; aula 2 das notas de Sipser (MIT)
fontes_catalogo: unesp-prado-apostilas-tc,lee-sipser-notas-2012
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Um **AFN** tem $\delta: Q \times \Sigma \to 2^Q$ (conjunto de destinos, possivelmente vazio); com movimentos vazios, $\delta: Q \times (\Sigma \cup \{\varepsilon\}) \to 2^Q$. Aceita $w$ se **algum** caminho termina em estado final.

**Construção de subconjuntos:** cada estado do AFD é um **conjunto** de estados do AFN.
1. Estado inicial do AFD: $E(\{q_0\})$, o fecho-$\varepsilon$ de $q_0$ (os estados alcançáveis só por transições vazias; sem transições vazias, é $\{q_0\}$).
2. Para um estado $X$ e um símbolo $a$: $\delta'(X, a) = E\left(\bigcup_{q \in X} \delta(q, a)\right)$.
3. Repita só para os conjuntos que aparecerem (não precisa listar os $2^{|Q|}$).
4. Finais: os conjuntos que contêm algum final do AFN. O conjunto vazio $\emptyset$ é um estado morto.

**Exemplo 07/08 (sufixo aaa):** AFN com $\delta(q_0,a) = \{q_0,q_1\}$, $\delta(q_0,b) = \{q_0\}$, $\delta(q_1,a) = \{q_2\}$, $\delta(q_2,a) = \{q_f\}$, final $q_f$.

| $\delta'$ | a | b |
|---|---|---|
| → $\{q_0\}$ | $\{q_0,q_1\}$ | $\{q_0\}$ |
| $\{q_0,q_1\}$ | $\{q_0,q_1,q_2\}$ | $\{q_0\}$ |
| $\{q_0,q_1,q_2\}$ | $\{q_0,q_1,q_2,q_f\}$ | $\{q_0\}$ |
| $\{q_0,q_1,q_2,q_f\}$ (final) | $\{q_0,q_1,q_2,q_f\}$ | $\{q_0\}$ |

Quatro estados, um só final. Leitura: o AFD conta quantos a seguidos terminam a entrada (0, 1, 2 ou 3 ou mais).

Erros comuns: esquecer o fecho-$\varepsilon$ no estado inicial e depois de cada passo; escrever $\langle\lambda\rangle$ para o conjunto vazio (é $\emptyset$, um estado morto, não a cadeia vazia); marcar como final só o conjunto que é **igual** a $\{q_f\}$, em vez de todo conjunto que **contém** $q_f$.

**Verificação:** `AFN.subconjuntos()` em `tests_acervo/lfa_verif.py` gera esta tabela, e o AFD e o AFN concordam em todas as cadeias até comprimento 10 (aceitas aaa, baaaa; rejeitadas aa, aaab).
