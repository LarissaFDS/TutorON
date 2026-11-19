---
id: sinais-anot-tf-pulso
titulo: Transformada de Fourier: definição em rad/s, e^{−at}u(t) → 1/(a + jω) e pulso retangular → T·sinc(ωT/2)
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

Convenção: $\omega$ em rad/s.
$$X(\omega) = \int_{-\infty}^{\infty}x(t)e^{-j\omega t}dt,\qquad x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty}X(\omega)e^{j\omega t}d\omega.$$
A transformada aparece como limite da série de Fourier quando $T_0 \to \infty$ ($k\omega_0 \to \omega$, $T_0c_k \to X(\omega)$). Para $x$ real vale a simetria conjugada $X(-\omega) = X^*(\omega)$.

**Exponencial causal** ($a > 0$): $e^{-at}u(t) \leftrightarrow \frac{1}{a + j\omega}$, $|X| = \frac{1}{\sqrt{a^2 + \omega^2}}$, $\angle X = -\tan^{-1}(\omega/a)$. (Com $a \le 0$ a integral não converge.)

**Pulso retangular** de amplitude $V$ e largura $T$, centrado em zero ($V\,\mathrm{rect}(t/T)$):
$$X(\omega) = \int_{-T/2}^{T/2}Ve^{-j\omega t}dt = \frac{2V}{\omega}\mathrm{sen}\frac{\omega T}{2} = VT\,\mathrm{sinc}\!\left(\frac{\omega T}{2}\right),\quad \mathrm{sinc}(x) = \frac{\mathrm{sen}\,x}{x}.$$
Em palavras: a transformada do pulso retangular é amplitude vezes largura vezes sinc de ômega T sobre 2. $X(0) = VT$ (área do pulso); zeros em $\omega = 2\pi n/T$, $n \ne 0$. Pulso mais estreito $\Rightarrow$ espectro mais largo.

Atenção à convenção: com $\mathrm{sinc}(x) = \mathrm{sen}(\pi x)/(\pi x)$ (normalizada, como em `numpy.sinc`) e frequência $f$ em Hz, o mesmo par fica $VT\,\mathrm{sinc}(fT)$.

**Verificação:** SymPy integra o pulso e devolve $2V\mathrm{sen}(\omega T/2)/\omega$; integração numérica em $\omega = 1$ com $V = 1$, $T = 2$ dá $2\,\mathrm{sen}\,1 = 1{,}683$; conferido nos testes.
