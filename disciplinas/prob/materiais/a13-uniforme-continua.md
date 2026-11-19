---
id: prob-anot-uniforme-continua
titulo: Distribuição uniforme contínua em [a, b]: densidade, média, variância e punif/qunif no R
assunto: prob-06-uniforme-normal
tipo: material_estudo
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Distribuições Normais e Uniformes_251011_135256.pdf" (2025.2), págs. 2–3
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
Anotações de aluno (2025.2), parafraseadas. Status da resolução: validada. Conferido com `scipy.stats.uniform`.

**Uniforme contínua** $X \sim U(a, b)$: todos os subintervalos de mesmo comprimento dentro de $[a, b]$ têm a mesma probabilidade.
$$f(x) = \frac{1}{b - a}\ \text{para}\ a \le x \le b; \qquad \mu = \frac{a + b}{2}; \qquad \sigma^2 = \frac{(b - a)^2}{12}.$$
Probabilidade de um subintervalo: $P(c < X < d) = \dfrac{d - c}{b - a}$ (base × altura do retângulo).

**No R:** $P(X \le x)$ = `punif(x, min = a, max = b)`; $P(c < X < d)$ = `punif(d, a, b) - punif(c, a, b)`; o x de uma probabilidade p = `qunif(p, a, b)`; valores aleatórios = `runif(n, a, b)`.

Ex.: $X \sim U(0, 10)$: $P(2 < X < 5) = 3/10 = 0{,}3000$; média 5; variância $100/12 \approx 8{,}3333$.

**Verificação:** `uniform(0, 10).cdf(5) - uniform(0, 10).cdf(2)` = 0,3; a área total é $(b-a)\cdot\frac{1}{b-a} = 1$.
