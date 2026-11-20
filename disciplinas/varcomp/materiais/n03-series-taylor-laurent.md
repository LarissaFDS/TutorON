---
id: varcomp-nota-ia-taylor-laurent
titulo: Nota — séries de Taylor e de Laurent: 1/(1 − z), raio de convergência, Laurent de 1/(z(z − 1)) em 0 < |z| < 1
assunto: varcomp-07-series-taylor-laurent
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON escrita com IA (não é material do professor)
autoria: Equipe TutorON (rascunho gerado por IA); revisão humana pendente
licenca: Texto próprio da equipe
publicacao_transcricao: não se aplica
fontes_catalogo: beck-first-course-complex-analysis,mit-ocw-1804-2018
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Rascunho escrito por IA, aguardando revisão humana; fora da busca. Contas conferidas com SymPy em `tests_acervo/test_disciplina_varcomp.py`.

**Taylor:** se f é analítica no disco $|z - z_0| < R$, então $f(z) = \sum_{n\ge0} a_n (z - z_0)^n$ com $a_n = f^{(n)}(z_0)/n!$, e a série converge em todo o disco. O raio de convergência vai até a singularidade mais próxima de $z_0$.

Exemplo: $\frac{1}{1 - z} = \sum_{n\ge0} z^n$ para $|z| < 1$ (singularidade em z = 1, raio 1).

**Laurent:** numa coroa $r < |z - z_0| < R$ onde f é analítica, $f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n$. O coeficiente $a_{-1}$ é o resíduo.

Exemplo: $f(z) = \frac{1}{z(z - 1)}$ em $0 < |z| < 1$: $\frac{1}{z(z - 1)} = -\frac1z\cdot\frac{1}{1 - z} = -\frac1z - 1 - z - z^2 - \dots$. A parte principal é $-1/z$; o resíduo em 0 é $-1$.

Em $|z| > 1$ a série é outra: $\frac{1}{z(z - 1)} = \frac{1}{z^2}\cdot\frac{1}{1 - 1/z} = \frac{1}{z^2} + \frac{1}{z^3} + \dots$. A mesma função tem séries diferentes em coroas diferentes.

**Verificação:** SymPy `series(1/(z*(z-1)), z, 0, 3)` dá $-1/z - 1 - z - z^2 + O(z^3)$.
