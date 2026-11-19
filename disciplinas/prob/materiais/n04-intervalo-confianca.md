---
id: prob-nota-intervalo-confianca
titulo: Nota — estimação pontual e intervalo de confiança para a média (z e t de Student) e para a proporção
assunto: prob-11-estimacao
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
Nota da equipe (revisão humana pendente). Conferida com `scipy.stats`.

**Estimadores pontuais:** $\bar x$ para μ, $s^2$ (com $n-1$, não viesado) para σ², $\hat p$ para p.

**IC para a média, σ conhecido:** $\bar x \pm z_{\alpha/2}\,\sigma/\sqrt n$ ($z_{0,025} = 1{,}96$ para 95%).
**σ desconhecido** (caso usual): $\bar x \pm t_{\alpha/2,\,n-1}\,s/\sqrt n$, t de Student com $n - 1$ graus de liberdade.
Ex.: n = 16, $\bar x = 50$, s = 8, 95%: $t_{0,025;15} \approx 2{,}1314$; margem $2{,}1314 \cdot 2 = 4{,}2629$; IC ≈ (45,74; 54,26).

**IC para proporção** (n grande, $n\hat p$ e $n(1-\hat p)$ ≥ 10): $\hat p \pm z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$. Ex.: 120 de 400, 95%: 0,30 ± 0,0449.

**Interpretação:** 95% dos intervalos construídos assim contêm μ; não é "μ está aqui com 95% de probabilidade" para um intervalo já calculado.

**Verificação:** `t.ppf(0.975, 15)` = 2,1314; em simulação, ≈ 95% dos IC de amostras normais cobrem μ.
