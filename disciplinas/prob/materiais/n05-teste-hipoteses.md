---
id: prob-nota-teste-hipoteses
titulo: Nota — teste de hipóteses para a média: H0 e H1, estatística de teste, valor-p, erros tipo I e II
assunto: prob-12-testes-hipoteses
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor nem das anotações)
fontes_catalogo: openstax-introductory-statistics-2e,openintro-statistics,mit-ocw-18-05
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Nota da equipe (revisão humana pendente). Conferida com `scipy.stats`.

Passos: (1) hipóteses $H_0: \mu = \mu_0$ e $H_1$ ($\ne$, $<$ ou $>$); (2) nível α; (3) estatística de teste, $t = \dfrac{\bar x - \mu_0}{s/\sqrt n}$ com $n-1$ graus (ou z, se σ é conhecido); (4) valor-p ou região crítica; (5) conclusão no contexto.

Ex.: $H_0: \mu = 50$ x $H_1: \mu \ne 50$, n = 25, $\bar x = 53$, s = 6, α = 0,05. $t = 3/1{,}2 = 2{,}5$; valor-p bilateral $= 2P(T_{24} > 2{,}5) \approx 0{,}0197 < 0{,}05$: rejeita $H_0$.

- **Valor-p:** probabilidade, supondo $H_0$ verdadeira, de uma estatística tão ou mais extrema que a observada. Não é a probabilidade de $H_0$ ser verdadeira.
- **Erro tipo I:** rejeitar $H_0$ verdadeira (probabilidade α). **Tipo II:** não rejeitar $H_0$ falsa (β); poder = 1 − β.
- "Não rejeitar" não prova $H_0$.

**Verificação:** `2*t.sf(2.5, 24)` = 0,0197; o IC de 95% (50,52; 55,48) não contém 50, coerente com a rejeição.
