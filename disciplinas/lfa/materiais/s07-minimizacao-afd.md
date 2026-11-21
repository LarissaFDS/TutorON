---
id: lfa-minimizacao-afd-tabela-de-pares
titulo: Minimização de AFD — pré-requisitos (determinístico, sem inacessíveis, função total), tabela de pares, marcação de estados distinguíveis e unificação; exemplo de 6 para 4 estados
assunto: lfa-02-automatos-finitos
tipo: exercicio_resolvido
questao: exemplo de minimização (numerado 11 na apostila)
resolucao: sim
fonte: Apostila 02 (Profa. Simone Prado, UNESP), redução de estados e exemplo de minimização com seis estados
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
Exemplo resolvido da apostila, conferido por código. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Pré-requisitos:** o autômato tem de ser AFD, sem estados inacessíveis e com $\delta$ total (complete com estado morto se faltar transição).

**Algoritmo da tabela de pares:**
1. Monte a tabela com cada par de estados uma vez.
2. Marque todo par {final, não final}.
3. Para cada par $\{p, q\}$ não marcado e cada símbolo $a$, olhe $\{\delta(p,a), \delta(q,a)\}$. Se esse par já está marcado, marque $\{p,q\}$ e propague para os pares que dependiam dele. Repita até não mudar.
4. Pares não marcados são equivalentes: una-os (a equivalência é transitiva).
5. Retire estados inúteis.

**Exemplo:** $M = (\{q_0,\dots,q_5\}, \{a,b\}, \delta, q_0, \{q_0, q_4, q_5\})$.

| $\delta$ | a | b |
|---|---|---|
| → $q_0$ (final) | $q_2$ | $q_1$ |
| $q_1$ | $q_1$ | $q_0$ |
| $q_2$ | $q_4$ | $q_5$ |
| $q_3$ | $q_5$ | $q_4$ |
| $q_4$ (final) | $q_3$ | $q_2$ |
| $q_5$ (final) | $q_2$ | $q_3$ |

- Passo 2 marca os 9 pares final × não final.
- Sobram $\{q_0,q_4\}$, $\{q_0,q_5\}$, $\{q_4,q_5\}$, $\{q_1,q_2\}$, $\{q_1,q_3\}$, $\{q_2,q_3\}$.
- $\{q_1,q_2\}$ com a vai a $\{q_1,q_4\}$, marcado, então é marcado; $\{q_1,q_3\}$ com a vai a $\{q_1,q_5\}$, marcado.
- $\{q_0,q_4\}$ com b vai a $\{q_1,q_2\}$, marcado; $\{q_0,q_5\}$ com b vai a $\{q_1,q_3\}$, marcado.
- $\{q_2,q_3\}$ vai a $\{q_4,q_5\}$ com a e com b, e $\{q_4,q_5\}$ vai a $\{q_2,q_3\}$: os dois ficam sem marca.

**Resultado:** $q_{23} = \{q_2,q_3\}$ e $q_{45} = \{q_4,q_5\}$; o mínimo tem **4 estados**.

| $\delta_{min}$ | a | b |
|---|---|---|
| → $q_0$ (final) | $q_{23}$ | $q_1$ |
| $q_1$ | $q_1$ | $q_0$ |
| $q_{23}$ | $q_{45}$ | $q_{45}$ |
| $q_{45}$ (final) | $q_{23}$ | $q_{23}$ |

**Verificação:** o refinamento de partições de `AFD.classes()` dá as classes $\{q_0\}, \{q_1\}, \{q_2,q_3\}, \{q_4,q_5\}$, e a busca de contraexemplo no produto não acha cadeia em que o original e o mínimo discordem.
