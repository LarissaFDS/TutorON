---
id: lfa-automato-com-pilha-anbn
titulo: Autômato com pilha (AP) — sêxtupla/sétupla (Q, Σ, Γ, δ, q0, z, F), leitura de δ(q1, a, b) = {(q2, cd)}, AP para aⁿbⁿ, aceitação por estado final e equivalência GLC ↔ AP
assunto: lfa-05-livres-de-contexto
tipo: exercicio_resolvido
questao: exemplos 18 e 19
resolucao: sim
fonte: Apostila 03 (Profa. Simone Prado, UNESP), seção 7 e exemplos 18 e 19; aulas 4 e 5 das notas de Sipser (MIT)
fontes_catalogo: unesp-prado-apostilas-tc,lee-sipser-notas-2012
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exemplos 18 e 19 da apostila, conferidos por simulação. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**AP não determinístico:** $M = (Q, \Sigma, \Gamma, \delta, q_0, z, F)$, com $\Gamma$ o alfabeto da pilha, $z$ o símbolo inicial da pilha e $\delta: Q \times (\Sigma \cup \{\varepsilon\}) \times (\Gamma \cup \{\varepsilon\}) \to$ subconjuntos finitos de $Q \times \Gamma^*$.

$\delta(q_1, a, b) \ni (q_2, cd)$ se lê assim: em $q_1$, lendo a com b no topo, desempilha b, empilha cd ($c$ fica no topo) e vai para $q_2$.

**Exemplo 19:** $\Sigma = \{a,b\}$, $\Gamma = \{0, 1\}$, $z = 0$, $F = \{q_3\}$.

| Transição | Ação |
|---|---|
| $\delta(q_0, a, 0)$ | $\{(q_1, 10), (q_3, \varepsilon)\}$ |
| $\delta(q_0, \varepsilon, 0)$ | $\{(q_3, \varepsilon)\}$ |
| $\delta(q_1, a, 1)$ | $\{(q_1, 11)\}$ |
| $\delta(q_1, b, 1)$ | $\{(q_2, \varepsilon)\}$ |
| $\delta(q_2, b, 1)$ | $\{(q_2, \varepsilon)\}$ |
| $\delta(q_2, \varepsilon, 0)$ | $\{(q_3, \varepsilon)\}$ |

Em palavras: cada a empilha um 1; cada b desempilha um 1; quando aparece o 0 do fundo, vai para $q_3$. Aceitação por **estado final** com a entrada toda lida.
- Linguagem: $L = \{a^nb^n \mid n \ge 1\} \cup \{\varepsilon, a\}$.
- $\varepsilon$ e $a$ entram pelas transições que vão de $q_0$ direto a $q_3$.

Traço de $aabb$: $(q_0, aabb, 0) \vdash (q_1, abb, 10) \vdash (q_1, bb, 110) \vdash (q_2, b, 10) \vdash (q_2, \varepsilon, 0) \vdash (q_3, \varepsilon, \varepsilon)$, aceita.

**GLC ↔ AP:** toda GLC tem um AP equivalente (o AP simula derivações mais à esquerda na pilha), e vice-versa. AP **determinísticos** reconhecem menos: $ww^R$ precisa de não determinismo para adivinhar o meio.

**Verificação:** a simulação em largura de `ap_aceita` aceita, entre as palavras até comprimento 6, exatamente $\varepsilon$, a, ab, aabb e aaabbb.
