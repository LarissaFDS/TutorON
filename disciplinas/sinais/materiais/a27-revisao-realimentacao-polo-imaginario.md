---
id: sinais-anot-revisao-realimentacao
titulo: Revisão prova 2, questões 2 e 3: malha fechada G/(1 + KG) com polo duplo (K = 4 ± 2√3) e G = 100/(s² + 100) com entrada e^{−t}
assunto: sinais-10-funcao-transferencia
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Revisão Prova 2" (30 jun. 2026), questões 2 e 3
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sinais e Sistemas 2026.1; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-sinais-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Questão 2:** $G(s) = \frac{s + 2}{s^2 - 1}$ com realimentação negativa de ganho $K$: $Y = G(R - KY)$, logo
$$G_{mf}(s) = \frac{G}{1 + KG} = \frac{s + 2}{s^2 + Ks + (2K - 1)}.$$
(b) Para a resposta ao degrau ter a forma $M_1 + (M_2 + M_3t)e^{\beta t}$, o polo de malha fechada tem de ser **duplo**: $s^2 + Ks + 2K - 1 = (s - \beta)^2$, $K = -2\beta$ e $2K - 1 = \beta^2 = K^2/4$, ou seja $K^2 - 8K + 4 = 0$ e
$$K = 4 \pm 2\sqrt3\ (\approx 0{,}536\ \text{ou}\ 7{,}464),\qquad \beta = -K/2 < 0.$$
Os dois valores são positivos e dão polo estável.

**Questão 3:** $G = \frac{1}{0{,}01s^2 + 1} = \frac{100}{s^2 + 100}$ (polos $\pm j10$, no eixo imaginário), $u = e^{-t}$: $Y = \frac{100}{(s + 1)(s^2 + 100)}$. Resíduos: $A_1 = \frac{100}{101}$; $A_2 = \frac{100}{(1 + j10)(j20)} = \frac{5}{-10 + j} = \frac{5}{\sqrt{101}}e^{-j\theta}$, com $\theta = \angle(-10 + j) = \pi - \tan^{-1}(0{,}1) = 174{,}29^\circ$.
$$y(t) = \frac{100}{101}e^{-t} + \frac{10}{\sqrt{101}}\cos(10t - 174{,}29^\circ) = \frac{100}{101}\big(e^{-t} - \cos 10t + 0{,}1\,\mathrm{sen}\,10t\big).$$
**Correções:** (i) as anotações usam $\theta = \tan^{-1}(1/(-10))$ sem somar $\pi$; $-10 + j$ está no 2º quadrante. (ii) Ao lado aparece $\mathcal{L}\{e^{-at}\cos\omega t\} = \frac{s - a}{(s - a)^2 + \omega^2}$; o certo é $\frac{s + a}{(s + a)^2 + \omega^2}$. Polos simples no eixo imaginário: marginalmente estável, não BIBO estável (entrada $\cos 10t$ ressoa).

**Verificação:** `roots` de $s^2 + Ks + 2K - 1$ com $K = 4 - 2\sqrt3$ dá raiz dupla $-0{,}268$; `inverse_laplace_transform` da questão 3 dá a forma com seno e cosseno; $y(0) = \frac{100}{101}(1 - 1) = 0$.
