---
id: sinais-anot-serie-fourier-formulas
titulo: Série de Fourier de sinal periódico: forma exponencial c_k, forma trigonométrica A_k e B_k, simetria par e ímpar, ω₀ = 2π/T₀
assunto: sinais-07-serie-fourier
tipo: resumo
resolucao: nao
fonte: Anotações manuscritas "Represen em Série de Fourier de Sinais Periódicos" (13 maio 2026) e versão passada a limpo (3 jun. 2026)
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

Convenção: frequência angular em rad/s, $\omega_0 = 2\pi/T_0$ ($T_0$ = período fundamental). Erro típico: usar $T_0$ onde vai $\omega_0$.

**Forma exponencial:**
$$x(t) = \sum_{k=-\infty}^{\infty}c_ke^{jk\omega_0t},\qquad c_k = \frac{1}{T_0}\int_{T_0}x(t)\,e^{-jk\omega_0t}\,dt.$$
Em palavras: c k é a média, num período, de x vezes e elevado a menos j k ômega zero t. $c_0$ é o valor médio. Os $c_k$ saem da **ortogonalidade**: $\int_{T_0}e^{j(k-m)\omega_0t}dt = T_0$ se $k = m$ e 0 caso contrário.

**Forma trigonométrica:** $x(t) = A_0 + \sum_{k\ge1}[A_k\cos(k\omega_0t) + B_k\,\mathrm{sen}(k\omega_0t)]$, com $A_0 = c_0$, $A_k = 2\,\mathrm{Re}\,c_k$, $B_k = -2\,\mathrm{Im}\,c_k$, ou seja $c_k = (A_k - jB_k)/2$; para $x$ real, $c_{-k} = c_k^*$ e $x(t) = c_0 + \sum_{k\ge1}2|c_k|\cos(k\omega_0t + \angle c_k)$.

**Simetrias:** $x$ par $\Rightarrow B_k = 0$ (só cossenos), $A_k = \frac{4}{T_0}\int_0^{T_0/2}x\cos(k\omega_0t)dt$; $x$ ímpar $\Rightarrow A_k = 0$ (só senos), $B_k = \frac{4}{T_0}\int_0^{T_0/2}x\,\mathrm{sen}(k\omega_0t)dt$.

**Espectro de linhas:** gráficos de $|c_k|$ e $\angle c_k$ em função de $k\omega_0$ (só nas harmônicas).

**Verificação:** para $x = \cos(\omega_0t)$ a fórmula dá $c_{\pm1} = \tfrac12$ e os demais zero, pois $\cos = (e^{j\omega_0t} + e^{-j\omega_0t})/2$; conferido por integração numérica nos testes.
