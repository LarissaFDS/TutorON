---
id: sinais-anot-fracoes-parciais-reais
titulo: Resposta por frações parciais com polos reais: G(s) = (7s + 10)/(s² + 3s + 2) com entrada e^{−5t}; EDO com condições iniciais y(0) = 1, y′(0) = −1
assunto: sinais-10-funcao-transferencia
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Representação por função de transferência" (19 jun. 2026)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sinais e Sistemas 2026.1; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-sinais-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Método:** $Y(s) = G(s)U(s) = \frac{\bar B(s)}{\bar A(s)}$; com polos reais distintos $p_i$, $Y = \sum\frac{A_i}{s - p_i}$, resíduos $A_i = Y(s)(s - p_i)\big|_{s=p_i}$, e $y(t) = \sum A_ie^{p_it}$, $t \ge 0$.

**Exemplo 1:** $G(s) = \frac{7s + 10}{s^2 + 3s + 2}$ (polos $-1$ e $-2$), $u = e^{-5t}$, $U = \frac{1}{s + 5}$:
$$A_{-5} = \frac{7(-5) + 10}{(-4)(-3)} = -\frac{25}{12},\quad A_{-1} = \frac{3}{(4)(1)} = \frac34,\quad A_{-2} = \frac{-4}{(3)(-1)} = \frac43,$$
$$y(t) = -\tfrac{25}{12}e^{-5t} + \tfrac34e^{-t} + \tfrac43e^{-2t},\quad t \ge 0.$$
O termo $e^{-5t}$ vem da entrada; $e^{-t}$ e $e^{-2t}$ vêm dos polos de $G$.

**Exemplo 2 (com condições iniciais):** $\ddot y + 4\dot y + 3y = 6u_{-1}(t)$, $y(0^-) = 1$, $\dot y(0^-) = -1$. Laplace: $(s^2 + 4s + 3)Y = (s + 4)y(0) + \dot y(0) + \frac6s$, logo
$$Y = \frac{s + 3}{(s+1)(s+3)} + \frac{6}{s(s+1)(s+3)} = \frac2s - \frac{2}{s+1} + \frac{1}{s+3},\quad y(t) = 2 - 2e^{-t} + e^{-3t}.$$
A função de transferência $\frac{1}{s^2 + 4s + 3}$ só descreve a parte que vem da entrada (CI nulas); as CI somam a resposta de entrada zero.

**Verificação:** $y(0) = 2 - 2 + 1 = 1$ e $\dot y(0) = 2 - 3 = -1$; `dsolve` e `inverse_laplace_transform` dão as mesmas expressões; no exemplo 1, $y(0) = -\tfrac{25}{12} + \tfrac34 + \tfrac43 = 0$ (grau relativo 1).
