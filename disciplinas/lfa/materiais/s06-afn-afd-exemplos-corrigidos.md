---
id: lfa-afn-para-afd-exemplos-corrigidos
titulo: AFN para AFD — exemplos 09 e 11 da apostila com o conjunto de estados finais F' corrigido; estado vazio ∅ em vez de <λ>
assunto: lfa-02-automatos-finitos
tipo: exercicio_resolvido
questao: exemplos 09 e 11
resolucao: sim
fonte: Apostila 02 (Profa. Simone Prado, UNESP), exemplos 09 e 11 de equivalência entre AFN e AFD
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
Exemplos resolvidos da apostila, conferidos pela construção de subconjuntos. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Exemplo 09.** AFN sobre $\{0,1\}$, final $q_f$: $\delta(q_0,0) = \{q_0,q_f\}$, $\delta(q_0,1) = \{q_f\}$, $\delta(q_f,0) = \delta(q_f,1) = \{q_1\}$, $\delta(q_1,1) = \{q_1\}$, $\delta(q_1, 0) = \emptyset$.

| $\delta'$ | 0 | 1 |
|---|---|---|
| → $\{q_0\}$ | $\{q_0,q_f\}$ | $\{q_f\}$ |
| $\{q_0,q_f\}$ | $\{q_0,q_1,q_f\}$ | $\{q_1,q_f\}$ |
| $\{q_f\}$ | $\{q_1\}$ | $\{q_1\}$ |
| $\{q_0,q_1,q_f\}$ | $\{q_0,q_1,q_f\}$ | $\{q_1,q_f\}$ |
| $\{q_1,q_f\}$ | $\{q_1\}$ | $\{q_1\}$ |
| $\{q_1\}$ | $\emptyset$ | $\{q_1\}$ |
| $\emptyset$ | $\emptyset$ | $\emptyset$ |

**Correção:** a apostila lista $F' = \{\langle q_f\rangle, \langle q_0,q_f\rangle, \langle q_0,q_1,q_f\rangle\}$ e esquece $\{q_1, q_f\}$, que contém $q_f$. O certo são **quatro** finais: $\{q_f\}$, $\{q_0,q_f\}$, $\{q_0,q_1,q_f\}$ e $\{q_1,q_f\}$. Sem ele, a cadeia 01 seria rejeitada, mas o AFN a aceita ($q_0 \xrightarrow{0} q_0 \xrightarrow{1} q_f$). A apostila também escreve $\langle\lambda\rangle$ para o estado sem nenhum estado do AFN; é o conjunto vazio $\emptyset$.

**Exemplo 11** (aa ou bb como subcadeia, AFN com $\delta(q_0,a) = \{q_0,q_1\}$, $\delta(q_0,b) = \{q_0,q_2\}$, $\delta(q_1,a) = \{q_f\}$, $\delta(q_2,b) = \{q_f\}$, $q_f$ com laço em a e b): os estados atingíveis são $\{q_0\}$, $\{q_0,q_1\}$, $\{q_0,q_2\}$, $\{q_0,q_1,q_f\}$, $\{q_0,q_2,q_f\}$. **Correção:** a apostila copia como $F'$ a lista de finais do exemplo anterior ($\langle q_0,q_f\rangle, \langle q_1,q_f\rangle, \dots$), que nem são estados deste AFD; o certo é $F' = \{\{q_0,q_1,q_f\}, \{q_0,q_2,q_f\}\}$. Minimizado, esse AFD tem 4 estados, o mesmo número do AFD direto do bloco de aa ou bb.

**Verificação:** `tests_acervo/test_disciplina_lfa.py` refaz as duas construções, confere os finais e compara AFN e AFD em todas as cadeias até comprimento 10; com o $F'$ da apostila, 01 seria rejeitada.
