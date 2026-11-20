---
id: controle-anot-bibo-polos
titulo: Estabilidade BIBO de SLIT contínuo: estável se e só se todos os polos têm Re < 0; exemplos 2/(s(s+2)), 1/(s²+4), (s−2)/(s²+3s+2) e entrada limitada que gera saída ilimitada
assunto: controle-04-estabilidade-routh
tipo: resolucao
resolucao: sim
fonte: Anotações "Estabilidade de SLIT contínuo" (9 set. 2026), p. 1–5
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Definição:** BIBO estável se toda entrada limitada ($|u(t)| \le M < \infty$) produz saída limitada.

**Por quê:** $Y = GU$ separa em parcela da entrada e parcela dos polos de $G$, combinação de $e^{p_it}$, $t^ke^{p_it}$ e $e^{\alpha t}\cos(\beta t + \phi)$. Se a entrada tem raiz igual a um polo de $G$, surgem termos com $t^k$ (ressonância).

**Critério:** $G = B/A$ racional e própria (depois de cancelar fatores comuns) é BIBO estável **se e só se todos os polos têm $\mathrm{Re}\{p_i\} < 0$**. Zeros não importam.

- (a) $G = \frac{2}{s(s + 2)}$: polo em $0$, **não** é BIBO. Degrau: $Y = \frac{2}{s^2(s + 2)}$, $y = -\frac12 + t + \frac12e^{-2t}$ cresce com $t$.
- (b) $G = \frac{1}{s^2 + 4}$: polos $\pm j2$, **não** é BIBO. $u = \mathrm{sen}\,2t$: $Y = \frac{2}{(s^2 + 4)^2}$, $y = \frac18\mathrm{sen}\,2t - \frac14t\cos 2t$, ilimitada.
- (c) $G = \frac{s - 2}{s^2 + 3s + 2}$: polos $-1$ e $-2$, **é** BIBO (o zero em $+2$ não muda nada).
- (d) $\frac{s + 3}{s^5 + 7s^4 - 8s^3 + 4s^2 + 5s + 1}$: coeficientes com sinais diferentes, **instável** (veja Routh-Hurwitz).

**Verificação:** `roots` dos denominadores e `inverse_laplace_transform` das respostas de (a) e (b).
