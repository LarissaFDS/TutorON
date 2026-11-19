---
id: prob-nota-hipergeometrica
titulo: Nota — distribuição hipergeométrica: sorteio sem reposição, fórmula, média e comparação com a binomial
assunto: prob-05-distribuicoes-discretas
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor nem das anotações)
fontes_catalogo: openstax-introductory-statistics-2e,grinstead-snell
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Nota da equipe (revisão humana pendente). Conferida com `scipy.stats.hypergeom`.

População de N itens com K "sucessos"; sorteiam-se n **sem reposição**; X = sucessos na amostra.
$$P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}, \qquad E(X) = n\frac{K}{N}, \qquad \operatorname{Var}(X) = n\frac{K}{N}\frac{N-K}{N}\frac{N-n}{N-1}.$$
O fator $(N-n)/(N-1)$ é a correção de população finita; com N muito maior que n, a hipergeométrica se aproxima da binomial com $p = K/N$.

Ex.: N = 35, K = 14 mulheres, n = 3: $E(X) = 1{,}2$; $P(X \ge 2) \approx 0{,}3476$. No R: `phyper(1, 14, 21, 3, lower.tail = FALSE)`.

**Verificação:** as probabilidades para k = 0..3 somam 1; `hypergeom(35, 14, 3).mean()` = 1,2.
