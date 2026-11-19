---
id: prob-nota-estatistica-descritiva
titulo: Nota — análise exploratória: média, mediana, moda, variância amostral (n − 1), quartis e boxplot
assunto: prob-10-estatistica-descritiva
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
Nota da equipe (revisão humana pendente). Conferida com `statistics` e `numpy`.

Dados: 2, 4, 4, 5, 7, 9 (n = 6).
- **Média amostral** $\bar x = \frac{1}{n}\sum x_i = 31/6 \approx 5{,}1667$.
- **Mediana:** com n par, média dos dois centrais, $(4 + 5)/2 = 4{,}5$. **Moda:** 4.
- **Variância amostral** (divide por $n - 1$): $s^2 = \frac{1}{n-1}\sum (x_i - \bar x)^2 = 30{,}8333/5 \approx 6{,}1667$; desvio $s \approx 2{,}4833$. A variância **populacional** divide por n (≈ 5,1389). No R, `var()` e `sd()` usam $n - 1$.
- **Quartis e boxplot:** a caixa vai de Q1 a Q3, com a mediana dentro; amplitude interquartil $\text{AIQ} = Q_3 - Q_1$; valores fora de $[Q_1 - 1{,}5\,\text{AIQ},\ Q_3 + 1{,}5\,\text{AIQ}]$ são candidatos a outliers. Há várias convenções de quartil (o R tem 9 tipos); diga qual foi usada.
- Média é sensível a valores extremos; a mediana não.

**Verificação:** `statistics.variance([2,4,4,5,7,9])` = 6,1667 e `statistics.median` = 4,5.
