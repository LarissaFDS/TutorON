---
id: circ-anot-grandezas-ohm
titulo: Corrente, tensão, resistência, lei de Ohm, resistores em série e em paralelo, curto-circuito
assunto: circ-01-grandezas-potencia
tipo: material_estudo
resolucao: nao
fonte: Anotações manuscritas "Introdução à Circuitos Elétricos" (5 mar. 2026), págs. 1–4
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Circuitos Elétricos 2026.1, Prof. Jobson de Araújo Nascimento, IC/UFAL); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-circ-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Grandezas.** Corrente elétrica $i$ (ampère, A): carga que passa por segundo; o sentido convencional é o das cargas positivas, oposto ao movimento dos elétrons num fio. Tensão ou diferença de potencial (d.d.p.) $v$ (volt, V): trabalho por unidade de carga para levar a carga de um ponto a outro. Resistência $R$ (ohm, Ω): oposição à passagem de corrente. O circuito precisa estar **fechado** para haver corrente.

**Lei de Ohm:** $v = R\,i$ (tensão igual a resistência vezes corrente), com a corrente entrando pelo terminal + do resistor. Curto-circuito: caminho com $R \to 0$; com fonte de tensão ideal, $i \to \infty$ (aquecimento, risco de incêndio).

**Série** (mesma corrente, a tensão se divide): $R_{eq} = R_1 + R_2 + \dots$; a tensão em cada um é $v_k = R_k\, i$ e, pela LKT, $v_{fonte} = v_1 + v_2 + \dots$ (divisor de tensão: $v_k = v\,R_k/R_{eq}$).

**Paralelo** (mesma tensão, a corrente se divide): $\dfrac{1}{R_{eq}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dots$; para dois, $R_{eq} = \dfrac{R_1 R_2}{R_1+R_2}$; corrente em cada ramo $i_k = v/R_k$ e, pela LKC no nó, $i_{total} = i_1 + i_2 + \dots$

Potência num resistor: $p = v i = R i^2 = v^2/R$. Com tensão fixa, aumentar R diminui a potência ($v^2/R$); com corrente fixa, aumenta ($R i^2$).

**Correções:** as anotações chamam $v_i = I R_i$ de "corrente em cada resistor"; é a **tensão** em cada resistor. A corrente é definida nelas como "movimento de elétrons"; nos cálculos usa-se o sentido convencional.

**Verificação:** 6 Ω em paralelo com 3 Ω dá $18/9 = 2$ Ω, menor que o menor dos dois; em série, 9 Ω.
