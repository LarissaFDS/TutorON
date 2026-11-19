---
id: prob-nota-covariancia-regressao
titulo: Nota — covariância, correlação e reta de regressão por mínimos quadrados
assunto: prob-13-conjuntas-regressao
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor nem das anotações)
fontes_catalogo: openstax-introductory-statistics-2e,openintro-statistics
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Nota da equipe (revisão humana pendente). Conferida com `numpy`.

**Covariância:** $\operatorname{Cov}(X, Y) = E(XY) - E(X)E(Y)$. Independentes ⇒ covariância 0 (a volta não vale). **Correlação:** $\rho = \dfrac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$, entre −1 e 1, mede só relação **linear**.

**Regressão linear simples** $\hat y = b_0 + b_1 x$ (mínimos quadrados):
$$b_1 = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^2}, \qquad b_0 = \bar y - b_1\bar x.$$
Ex.: x = 1, 2, 3, 4, 5 e y = 2, 4, 5, 4, 5: $\bar x = 3$, $\bar y = 4$, $S_{xy} = 6$, $S_{xx} = 10$; $b_1 = 0{,}6$, $b_0 = 2{,}2$; $r \approx 0{,}7746$, $r^2 = 0{,}6$.

Correlação não é causalidade; não extrapole fora da faixa de x observada. Integrais duplas de densidades conjuntas são técnica de Cálculo 3.

**Verificação:** `numpy.polyfit(x, y, 1)` = (0,6; 2,2) e `numpy.corrcoef` = 0,7746; os resíduos somam 0.
