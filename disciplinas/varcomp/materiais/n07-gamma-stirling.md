---
id: varcomp-nota-ia-gamma-stirling
titulo: Nota — função Gamma e fórmula de Stirling: Γ(n + 1) = n!, Γ(1/2) = √π, n! ≈ √(2πn)(n/e)^n
assunto: varcomp-11-gamma-stirling
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON escrita com IA (não é material do professor)
autoria: Equipe TutorON (rascunho gerado por IA); revisão humana pendente
licenca: Texto próprio da equipe
publicacao_transcricao: não se aplica
fontes_catalogo: mit-ocw-1804-2018
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Rascunho escrito por IA, aguardando revisão humana; fora da busca. Contas conferidas com SymPy em `tests_acervo/test_disciplina_varcomp.py`.

**Gamma:** para $\operatorname{Re} z > 0$, $\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}\,dt$. Integrando por partes, $\Gamma(z + 1) = z\,\Gamma(z)$, e com $\Gamma(1) = 1$ vem $\Gamma(n + 1) = n!$. A relação estende $\Gamma$ a uma função analítica em todo o plano exceto em $0, -1, -2, \dots$, onde tem polos simples (continuação analítica). Valor notável: $\Gamma(1/2) = \sqrt\pi$.

**Stirling:** $n! \sim \sqrt{2\pi n}\,(n/e)^n$ quando $n \to \infty$ (o quociente tende a 1). Exemplo: para $n = 10$, $\sqrt{20\pi}(10/e)^{10} \approx 3{,}5987\times10^6$, contra $10! = 3\,628\,800$: erro relativo de cerca de 0,83%, próximo de $1/(12n)$.

**Verificação:** SymPy dá `gamma(Rational(1,2)) = sqrt(pi)` e o quociente de Stirling para n = 10 vale ≈ 0,9917.
