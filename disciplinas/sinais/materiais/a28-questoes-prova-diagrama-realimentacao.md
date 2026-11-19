---
id: sinais-anot-questoes-prova
titulo: Questões de prova: malha fechada 2K/(s² + 3s + 2K) com polos iguais (K = 9/8); da resposta ao degrau à função de transferência e realimentação de estados; y = Me^{−4t}
assunto: sinais-10-funcao-transferencia
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Revisão Prova 2" (30 jun. 2026), questões de prova coladas, parafraseadas
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

**Q1 (paráfrase):** diagrama: o erro $r - y$ passa pelos ganhos $K$ e 2, soma-se a $-3\dot y$ e dá $\ddot y$; dois integradores levam a $\dot y$ e $y$. EDO: $\ddot y + 3\dot y + 2Ky = 2Kr$ e
$$G_{mf}(s) = \frac{2K}{s^2 + 3s + 2K}.$$
Polos iguais: $(s - b)^2 = s^2 - 2bs + b^2$: $b = -\tfrac32$ e $2K = \tfrac94$, **$K = \tfrac98$**. Degrau: $Y = \frac{9/4}{s(s + 3/2)^2} = \frac1s - \frac{1}{s + 3/2} - \frac{3/2}{(s + 3/2)^2}$, logo $y(t) = 1 - e^{-1{,}5t} - 1{,}5te^{-1{,}5t}$.

**Q2 (paráfrase):** resposta ao degrau (CI nulas) $y = 1 - 2e^{t} + e^{2t}$. Resposta ao impulso $h = \dot y = -2e^t + 2e^{2t}$; $G = \frac{-2}{s - 1} + \frac{2}{s - 2} = \frac{2}{s^2 - 3s + 2}$ (instável, polos 1 e 2); EDO $\ddot y - 3\dot y + 2y = 2u$. Com $u = -k_1y - k_2\dot y + r$: $G_{mf} = \frac{2}{s^2 + (2k_2 - 3)s + 2(1 + k_1)}$; para polos $-1$ e $-2$ ($s^2 + 3s + 2$): $k_2 = 3$, $k_1 = 0$.

**Q3 (paráfrase):** $\ddot y + 2\dot y + 0{,}5y = 0{,}5u$, $u = e^{-4t}$: achar $y(0)$ e $\dot y(0)$ para que $y = Me^{-4t}$. As anotações param em "acha M e resolve"; a equipe completou: substituindo, $M(16 - 8 + 0{,}5) = 0{,}5 \Rightarrow M = \tfrac{1}{17}$, logo $y(0) = \tfrac{1}{17}$ e $\dot y(0) = -\tfrac{4}{17}$ (as CI anulam a resposta natural).

**Verificação:** `dsolve` de Q1 com $K = 9/8$ e de Q3 com essas CI confirma; em Q2, $G(s)/s$ invertida devolve $1 - 2e^t + e^{2t}$.
