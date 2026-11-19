---
id: sinais-anot-serie-fourier-exponencial
titulo: Série de Fourier da exponencial periódica e^{−t/2} de período π: c_k = 2(1 − e^{−π/2})/(π(1 + j4k))
assunto: sinais-07-serie-fourier
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Rep em Série de Fourier de Sinais Periódicos" (3 jun. 2026)
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

**Sinal:** $x(t) = e^{-t/2}$ para $0 \le t < \pi$, repetido com período $T_0 = \pi$; logo $\omega_0 = 2\pi/\pi = 2$ rad/s.

**Cálculo:**
$$c_k = \frac1\pi\int_0^\pi e^{-t/2}e^{-j2kt}dt = \frac1\pi\cdot\frac{1 - e^{-\pi/2}e^{-j2k\pi}}{\tfrac12 + j2k} = \frac{2(1 - e^{-\pi/2})}{\pi(1 + j4k)},$$
pois $e^{-j2k\pi} = 1$. Com $2(1 - e^{-\pi/2})/\pi \approx 0{,}504$:
$$|c_k| = \frac{0{,}504}{\sqrt{1 + 16k^2}},\qquad \angle c_k = -\tan^{-1}(4k).$$
Em palavras: o módulo cai com k e a fase tende a menos 90 graus.

**Série:** $x(t) = 0{,}504\sum_k \frac{1}{1 + j4k}e^{j2kt}$; na forma trigonométrica, $x(t) = 0{,}504 + 0{,}504\sum_{k\ge1}\frac{2}{\sqrt{1+16k^2}}\cos(2kt - \tan^{-1}4k)$.

**Verificação:** $c_0 = 0{,}504$ é a média $\frac1\pi\int_0^\pi e^{-t/2}dt$; integração numérica de $c_1$ dá $0{,}0297 - j0{,}1186$, igual a $0{,}504/(1 + j4) = 0{,}504(1 - j4)/17$; conferido nos testes.
