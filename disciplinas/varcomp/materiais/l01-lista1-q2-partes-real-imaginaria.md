---
id: varcomp-lista1-q2-partes-u-v
titulo: Lista 1, Q2 — partes real u(x, y) e imaginária v(x, y) de (z − 4i)/(z + 3i), (z − 3i z̄)/(z − i) e e^z (z − i)
assunto: varcomp-01-numeros-complexos
tipo: lista
questao: 2
resolucao: sim
fonte: Lista nº 1 de Variável Complexa (Instituto de Computação, UFAL; arquivo Lista_1.pdf), questão 2
autoria: Enunciado: lista da disciplina (Instituto de Computação, UFAL; autor não identificado no arquivo), parafraseado pela equipe TutorON; resolução da equipe TutorON, conferida com SymPy
licenca: Não declarada (lista da disciplina); PDFs e imagens fora do repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
fontes_catalogo: ufal-varcomp-lista1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Lista nº 1 de Variável Complexa (IC/UFAL), questão 2. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (a lista não tem gabarito oficial; a resolução é da equipe TutorON, conferida com SymPy em `tests_acervo/test_disciplina_varcomp.py`).

Com $z = x + iy$, o caminho é sempre o mesmo: substituir, e num quociente **multiplicar em cima e embaixo pelo conjugado do denominador**, para que o denominador fique real.

**(a)** $w = \frac{z - 4i}{z + 3i} = \frac{x + i(y - 4)}{x + i(y + 3)}$. Multiplicando por $x - i(y + 3)$, o denominador vira $x^2 + (y + 3)^2$:
$$u = \frac{x^2 + y^2 - y - 12}{x^2 + (y+3)^2}, \qquad v = \frac{-7x}{x^2 + (y+3)^2}.$$

**(b)** $w = \frac{z - 3i\bar z}{z - i}$, com $\bar z = x - iy$: o numerador é $(x - 3y) + i(y - 3x)$ e o denominador $x + i(y - 1)$. Multiplicando por $x - i(y - 1)$:
$$u = \frac{x^2 + y^2 - 6xy + 3x - y}{x^2 + (y-1)^2}, \qquad v = \frac{-3x^2 + x + 3y^2 - 3y}{x^2 + (y-1)^2}.$$

**(c)** $w = e^z(z - i) = e^x(\cos y + i\sin y)\,[x + i(y - 1)]$:
$$u = e^x\,[x\cos y - (y - 1)\sin y], \qquad v = e^x\,[x\sin y + (y - 1)\cos y].$$

Erro comum: esquecer que $\bar z$ troca o sinal de $y$ em (b), ou multiplicar só o denominador pelo conjugado.

**Verificação:** com SymPy (`expand_complex`), $\mathrm{re}$ e $\mathrm{im}$ de cada $w$ coincidem com as expressões acima.
