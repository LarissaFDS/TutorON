---
id: sinais-anot-serie-fourier-quadrada
titulo: Coeficientes da série de Fourier de uma onda quadrada (V e −V): c_k = −j2V/(kπ) para k ímpar, x(t) = Σ 4V/(kπ) sen(kω₀t)
assunto: sinais-07-serie-fourier
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Represen em Série de Fourier de Sinais Periódicos" (13 maio 2026)
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

**Sinal:** onda quadrada de período $T_0$: $x(t) = V$ em $(0, T_0/2)$ e $x(t) = -V$ em $(T_0/2, T_0)$; valor médio zero; sinal ímpar.

**Cálculo:** com $\omega_0T_0 = 2\pi$,
$$c_k = \frac{1}{T_0}\left[\int_0^{T_0/2}Ve^{-jk\omega_0t}dt - \int_{T_0/2}^{T_0}Ve^{-jk\omega_0t}dt\right] = \frac{V}{jk2\pi}\big(1 - e^{-jk\pi}\big)^2 .$$
Como $e^{-jk\pi} = (-1)^k$: para $k$ par, $c_k = 0$; para $k$ ímpar, $(1 - (-1))^2 = 4$ e
$$c_k = \frac{4V}{j2\pi k} = -j\frac{2V}{k\pi}\quad(k\ \text{ímpar}),\qquad c_0 = 0.$$

**Forma trigonométrica:** $A_k = 2\,\mathrm{Re}\,c_k = 0$ e $B_k = -2\,\mathrm{Im}\,c_k = \frac{4V}{k\pi}$:
$$x(t) = \frac{4V}{\pi}\left[\mathrm{sen}(\omega_0t) + \frac13\mathrm{sen}(3\omega_0t) + \frac15\mathrm{sen}(5\omega_0t) + \dots\right].$$
Em palavras: só harmônicas ímpares de seno, com amplitude 4V sobre k pi. Espectro: $|c_k| = 2V/(k\pi)$ e fase $-90^\circ$ para $k > 0$ ímpar.

**Verificação:** integração numérica de $c_k$ (k = 1…7) coincide com $-j2V/(k\pi)$; a soma até $k = 199$ reconstrói o sinal (erro pequeno longe dos saltos; perto deles aparece o fenômeno de Gibbs, cerca de 9% de sobressinal); conferido nos testes.
