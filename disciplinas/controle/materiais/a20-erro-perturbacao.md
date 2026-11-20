---
id: controle-anot-erro-perturbacao
titulo: Erro em regime devido a perturbação: Y = Gmf·R + Gwmf·W; ewss = −lim s·Gwmf·W; exemplo C = 1/(s+1), G = 1/s, Gw = 0,1/(s+10): ewss = −0,01 ao degrau
assunto: controle-06-erro-regime
tipo: resolucao
resolucao: sim
fonte: Anotações "Resposta em Regime permanente" (20 out. 2026), p. 6–9
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

**Estrutura:** controlador $C$, planta $G$, perturbação $W$ entrando via $G_w$ antes da planta; realimentação unitária negativa.
$$Y = G_{mf}R + G_{wmf}W,\quad G_{mf} = \frac{CG}{1 + CG},\quad G_{wmf} = \frac{G_wG}{1 + CG}.$$
$E = [1 - G_{mf}]R - G_{wmf}W$; se ambas são BIBO estáveis: $e_{ss} = e_{Rss} + e_{Wss}$, com $e_{Wss} = -\lim_{s\to0}sG_{wmf}W$. Para perturbação em degrau: $e_{Wss} = -\lim_{s\to0}\frac{G_w}{1/G + C}$. **$C(0)$ grande reduz o efeito; polo na origem em $C$ zera** o erro ao degrau de perturbação.

**Exemplo:** $C = \frac{1}{s + 1}$, $G = \frac1s$, $G_w = \frac{0{,}1}{s + 10}$.
- $G_{mf} = \frac{1}{s^2 + s + 1}$ (estável). Degrau: $e_{Rss} = 0$ (tipo 1: polo na origem em $CG$). Rampa: $K_v = \lim s\frac{1}{s(s + 1)} = 1$, $e_{Rss} = 1$.
- $G_{wmf} = \frac{0{,}1(s + 1)}{(s + 10)(s^2 + s + 1)}$ (estável). Degrau: $e_{Wss} = -G_{wmf}(0) = -0{,}01$ (tipo 0 para a perturbação). Rampa: $e_{Wss} \to -\infty$.

**Verificação:** `sympy.limit` dá $0{,}01$; o polo na origem está em $G$, não em $C$, por isso não rejeita a perturbação.
