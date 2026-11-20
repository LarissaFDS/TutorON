---
id: varcomp-nota-ia-residuos
titulo: Nota — singularidades, resíduos e teorema dos resíduos: polo simples, polo de ordem m, ∫ dx/(1 + x²) = π
assunto: varcomp-08-residuos-singularidades
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

**Singularidades isoladas:** removível (Laurent sem potências negativas), polo de ordem m (a menor potência é $(z - z_0)^{-m}$), essencial (infinitas potências negativas, como $e^{1/z}$ em 0).

**Resíduo** = coeficiente $a_{-1}$ da série de Laurent. Cálculo:
- polo simples: $\operatorname{Res}_{z_0} f = \lim_{z\to z_0}(z - z_0)f(z)$; se $f = p/q$ com $q(z_0) = 0$, $q'(z_0) \ne 0$: $p(z_0)/q'(z_0)$;
- polo de ordem m: $\frac{1}{(m-1)!}\lim_{z\to z_0}\frac{d^{m-1}}{dz^{m-1}}[(z - z_0)^m f(z)]$.

**Teorema dos resíduos:** se f é analítica dentro e sobre a curva fechada simples $\gamma$, anti-horária, exceto num número finito de singularidades $z_k$ **dentro** dela, então $\oint_\gamma f\,dz = 2\pi i\sum_k \operatorname{Res}_{z_k} f$.

Exemplo de integral real: $\int_{-\infty}^{\infty}\frac{dx}{1 + x^2}$. Feche com um semicírculo no semiplano superior; só o polo $z = i$ fica dentro; $\operatorname{Res}_i \frac{1}{1 + z^2} = \frac{1}{2i}$; o arco tende a zero (o integrando decai como $1/R^2$). Resultado: $2\pi i\cdot\frac{1}{2i} = \pi$.

**Verificação:** $\int_{-\infty}^{\infty}\frac{dx}{1 + x^2} = [\arctan x]_{-\infty}^{\infty} = \pi$.
