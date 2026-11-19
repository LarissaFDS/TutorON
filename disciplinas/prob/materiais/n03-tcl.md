---
id: prob-nota-tcl
titulo: Nota — Teorema Central do Limite e distribuição da média amostral
assunto: prob-09-aproximacao-normal-tcl
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor nem das anotações)
fontes_catalogo: openstax-introductory-statistics-2e,mit-ocw-18-05
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Nota da equipe (revisão humana pendente). Conferida com simulação.

Se $X_1, \dots, X_n$ são independentes e com a mesma distribuição (média μ, variância σ² finita), para n grande a média amostral
$$\bar X \approx N\!\left(\mu,\ \frac{\sigma^2}{n}\right), \qquad Z = \frac{\bar X - \mu}{\sigma/\sqrt n} \approx N(0, 1),$$
qualquer que seja a distribuição original. $\sigma/\sqrt n$ é o **erro-padrão**. Regra prática: n ≥ 30, menos se a distribuição original é simétrica. Se os $X_i$ já são normais, o resultado é exato para todo n.

Ex.: tempos exponenciais com média 5 min (σ = 5); média de 36 tempos: $P(\bar X > 6) \approx P(Z > (6 - 5)/(5/6)) = P(Z > 1{,}2) \approx 0{,}1151$. O valor exato (a soma de exponenciais é gama) é ≈ 0,1184: a aproximação erra na terceira casa, porque a exponencial é assimétrica.

**Verificação:** `gamma(36, scale=5/36).sf(6)` ≈ 0,1184; simulação de 100 mil médias concorda.
