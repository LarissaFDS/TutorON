---
id: sinais-anot-tf-pares-senoidal
titulo: Pares de Fourier com impulso (δ, constante, e^{jω₀t}, cosseno, seno) e resposta de SLIT a senoide por G(jω): exemplo 5cos(2t + 40°)
assunto: sinais-08-transformada-fourier
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Transformada de Fourier" (28 maio 2026)
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

**Pares (ω em rad/s):** $\delta(t - t_0) \leftrightarrow e^{-j\omega t_0}$; $1 \leftrightarrow 2\pi\delta(\omega)$; $e^{j\omega_0t} \leftrightarrow 2\pi\delta(\omega - \omega_0)$; $B\cos(\omega_0t) \leftrightarrow \pi B[\delta(\omega + \omega_0) + \delta(\omega - \omega_0)]$; $A\,\mathrm{sen}(\omega_0t) \leftrightarrow j\pi A[\delta(\omega + \omega_0) - \delta(\omega - \omega_0)]$.

**Resposta a exponencial e a senoide:** num SLIT estável, $e^{st}$ gera $G(s)e^{st}$ ($G$ = função de transferência). Para $u = A\cos(\omega t + \phi)$, a resposta em regime é
$$y_{ss}(t) = A\,|G(j\omega)|\cos\big(\omega t + \phi + \angle G(j\omega)\big).$$

**Exemplo:** $\ddot y + 3\dot y + 2y = 10u$, $u = 5\cos(2t + 40^\circ)$. $G(s) = \frac{10}{s^2 + 3s + 2}$ e
$$G(j2) = \frac{10}{-4 + j6 + 2} = \frac{10}{-2 + j6},\quad |G| = \frac{10}{\sqrt{40}} = 1{,}581,\quad \angle G = -(180^\circ - 71{,}57^\circ) = -108{,}43^\circ.$$
$$y_{ss}(t) = 7{,}906\cos(2t - 68{,}43^\circ).$$
O ângulo de $-2 + j6$ está no 2º quadrante ($108{,}43^\circ$, não $-71{,}57^\circ$).

**Verificação:** `scipy.signal.freqresp` em $\omega = 2$ dá $|G| = 1{,}5811$ e fase $-108{,}43^\circ$; a simulação com `lsim` por 20 s coincide com $y_{ss}$ no fim (polos −1 e −2, transitório extinto); conferido nos testes.
