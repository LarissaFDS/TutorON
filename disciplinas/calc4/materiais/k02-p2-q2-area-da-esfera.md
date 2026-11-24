---
id: calc4-p2-q2-area-esfera-superficie
titulo: P2 de Cálculo IV, Q2 — área da esfera de raio r pela integral de superfície: parametrização esférica e |r_φ × r_θ| = r² sen φ; resultado 4πr²
assunto: calc4-02-integrais-de-superficie
tipo: prova
questao: 2
resolucao: sim
fonte: Prova 2 de Cálculo IV (Instituto de Computação, UFAL; Prof. Gleydson Santos da Silva; arquivo P2C4.pdf), questão 2 | enunciado parafraseado
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
Prova 2 de Cálculo IV (IC-UFAL, Prof. Gleydson Santos da Silva), questão 2, parafraseada. Status da resolução: pendente de confirmação do professor (a prova não traz gabarito; a resolução é da equipe TutorON e não é gabarito do professor). Prova é atividade avaliativa: o tutor guia, não entrega.

**Enunciado.** Calcular a área da esfera de raio $r$ centrada na origem com integral de superfície.

**Parametrização.** Em coordenadas esféricas, com $0 \le \varphi \le \pi$ e $0 \le \theta \le 2\pi$:
$$\mathbf R(\varphi,\theta) = (r\,\text{sen}\,\varphi\cos\theta,\; r\,\text{sen}\,\varphi\,\text{sen}\,\theta,\; r\cos\varphi).$$

**Elemento de área.** $A(S) = \iint_D |\mathbf R_\varphi \times \mathbf R_\theta|\,dA$. O produto vetorial é $r^2\,\text{sen}\,\varphi\,(\text{sen}\,\varphi\cos\theta,\ \text{sen}\,\varphi\,\text{sen}\,\theta,\ \cos\varphi)$, e o módulo é $r^2\,\text{sen}\,\varphi$ (como $\text{sen}\,\varphi \ge 0$ em $[0,\pi]$, não precisa de valor absoluto).

**Conta.**
$$A = \int_0^{2\pi}\!\!\int_0^{\pi} r^2\,\text{sen}\,\varphi\,d\varphi\,d\theta = r^2\cdot 2\pi\cdot[-\cos\varphi]_0^{\pi} = 4\pi r^2.$$

Erros comuns: trocar os intervalos de $\varphi$ e $\theta$ (com $\varphi$ até $2\pi$ a área sai zero); esquecer o fator $r^2\,\text{sen}\,\varphi$. Outra saída: metade de cima como gráfico $z = \sqrt{r^2 - x^2 - y^2}$, com integral imprópria na borda.

**Verificação:** `test_p2_q2_area_da_esfera` refaz o produto vetorial e a integral.
