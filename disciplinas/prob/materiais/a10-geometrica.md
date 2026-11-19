---
id: prob-anot-geometrica
titulo: Distribuição geométrica: número da tentativa do primeiro sucesso; acumulada e dgeom/pgeom no R
assunto: prob-05-distribuicoes-discretas
tipo: material_estudo
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Principais Distribuições Discretas_251011_130200.pdf" (2025.2), pág. 3
autoria: Otávio Joshua Costa Brandão Menezes (aluno, equipe TutorON), anotações de estudo; paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações pessoais do aluno); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia as anotações e não reproduz imagens
fontes_catalogo: ufal-prob-anotacoes-2025-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Anotações de aluno (2025.2), parafraseadas. Status da resolução: validada (com o aviso sobre a convenção do R). Conferido com `scipy.stats.geom`.

**Geométrica:** X = número da tentativa em que ocorre o **primeiro sucesso**, em ensaios de Bernoulli independentes e com a mesma probabilidade de sucesso p (ex.: persistência até alcançar um resultado).
$$P(X = k) = (1-p)^{k-1}\,p,\quad k = 1, 2, \dots; \qquad P(X \le k) = 1 - (1-p)^k.$$
Média $E(X) = 1/p$ e variância $(1-p)/p^2$ (nesta convenção).

**Convenção do R:** `dgeom` conta os **fracassos antes** do primeiro sucesso (começa em 0). Por isso, para a tentativa k, use `dgeom(k - 1, p)`; a acumulada $P(X \le k)$ é `pgeom(k - 1, p)`. A scipy usa a mesma convenção das anotações (`geom.pmf(k, p)` começa em 1).

Ex.: p = 0,2; primeiro sucesso na 3ª tentativa: $0{,}8^2 \cdot 0{,}2 = 0{,}128$; até a 3ª: $1 - 0{,}8^3 = 0{,}488$.

**Hipergeométrica** (as anotações só citam): sorteio **sem reposição** em população finita e pequena; o exemplo da comissão (35 pessoas, 3 sorteadas) é desse tipo.

**Verificação:** $0{,}2 + 0{,}16 + 0{,}128 = 0{,}488$ (soma das três primeiras = acumulada); `geom.cdf(3, 0.2)` = 0,488.
