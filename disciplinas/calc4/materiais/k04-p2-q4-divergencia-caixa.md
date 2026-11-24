---
id: calc4-p2-q4-divergencia-caixa
titulo: P2 de Cálculo IV, Q4 — fluxo de F = x²yz i + xy²z j + xyz² k pela caixa [0, a] × [0, b] × [0, c]: teorema da divergência dá 3a²b²c²/4
assunto: calc4-03-teoremas-stokes-divergencia
tipo: prova
questao: 4
resolucao: sim
fonte: Prova 2 de Cálculo IV (Instituto de Computação, UFAL; Prof. Gleydson Santos da Silva; arquivo P2C4.pdf), questão 4 | enunciado parafraseado
curso: Engenharia de Computação (UFAL), ECOM023 Cálculo 4, 4º período; semestre não identificado
fontes_catalogo: ufal-calc4-p2-gleydson
autoria: Enunciado: Prof. Gleydson Santos da Silva (IC-UFAL); resolução da equipe TutorON, conferida com SymPy
licenca: Não declarada (prova da disciplina); PDF não versionado
publicacao_transcricao: não autorizada; enunciado parafraseado
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Prova 2 de Cálculo IV (IC-UFAL, Prof. Gleydson Santos da Silva), questão 4, parafraseada. Status da resolução: pendente de confirmação do professor (a prova não traz gabarito; a resolução é da equipe TutorON e não é gabarito do professor). Prova é atividade avaliativa: o tutor guia, não entrega.

**Enunciado.** Calcular $\iint_S \mathbf F\cdot d\mathbf S$ para $\mathbf F = x^2yz\,\mathbf i + xy^2z\,\mathbf j + xyz^2\,\mathbf k$, com $S$ a superfície da caixa limitada por $x = 0$, $x = a$, $y = 0$, $y = b$, $z = 0$ e $z = c$ ($a, b, c > 0$), normal para fora.

**Por que divergência.** São seis faces; o teorema da divergência troca tudo por uma integral tripla: $\iint_S \mathbf F\cdot d\mathbf S = \iiint_E \operatorname{div}\mathbf F\,dV$, com $S$ fechada e orientada para fora.

**Divergência.** $\operatorname{div}\mathbf F = 2xyz + 2xyz + 2xyz = 6xyz$.

**Integral tripla.** A caixa separa as variáveis:
$$\iiint_E 6xyz\,dV = 6\int_0^a x\,dx\int_0^b y\,dy\int_0^c z\,dz = 6\cdot\frac{a^2}{2}\cdot\frac{b^2}{2}\cdot\frac{c^2}{2} = \frac{3a^2b^2c^2}{4}.$$

**Conferência pelas faces.** Nas faces $x = 0$, $y = 0$ e $z = 0$ o fluxo é zero (a componente normal tem o fator nulo). Na face $x = a$: $\iint a^2yz\,dy\,dz = a^2\frac{b^2c^2}{4}$; o mesmo vale nas faces $y = b$ e $z = c$. Somando, $3\cdot\frac{a^2b^2c^2}{4}$, igual.

**Verificação:** `test_p2_q4_divergencia_caixa` faz a integral tripla e a soma das seis faces.
