---
id: eletronica-anot-polarizacao-emissor
titulo: TBJ com polarização estável no emissor (VCC 20 V, RB 430 kΩ, RC 2 kΩ, RE 1 kΩ): IB = (VCC − VBE)/(RB + (β+1)RE), VCE para β = 50 e 100
assunto: eletronica-07-tbj-polarizacao
tipo: resolucao
resolucao: sim
fonte: Anotações "Circuitos de Polarização de Transistores" (23 out. 2026), item b (exercício de livro, parafraseado)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Circuito:** $V_{CC} = 20$ V; $R_B = 430$ kΩ do $V_{CC}$ à base; $R_C = 2$ kΩ no coletor; $R_E = 1$ kΩ no emissor, com capacitor de desvio (40 μF) em paralelo; capacitores de acoplamento na entrada e na saída. Em CC, todos os capacitores são abertos.

**Malha base-emissor:** $-20 + 430\mathrm{k}\,I_B + 0{,}7 + 1\mathrm{k}\,I_E = 0$, com $I_E = (\beta + 1)I_B$:
$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E}$$
(a resistência do emissor aparece na base multiplicada por beta mais um).

**Malha coletor-emissor:** $V_{CE} = 20 - 2\mathrm{k}\,I_C - 1\mathrm{k}\,I_E$.

| $\beta$ | $I_B$ | $I_C$ | $V_{CE}$ |
|---|---|---|---|
| 50 | 40,12 μA | 2,006 mA | 13,94 V |
| 100 | 36,35 μA | 3,635 mA | 9,06 V |

Ao dobrar $\beta$: $I_C$ +81,2% e $V_{CE}$ −35%. O resistor de emissor reduz a sensibilidade a $\beta$ em relação à polarização fixa (+100%).

**Verificação:** para $\beta = 50$, $V_E = I_E R_E = 2{,}046$ V, $V_B = 2{,}746$ V, $V_C = 15{,}99$ V; $V_C - V_E = 13{,}94$ V confere com a malha, e $V_{BC} = -13{,}24$ V (reversa) confirma a região ativa.
