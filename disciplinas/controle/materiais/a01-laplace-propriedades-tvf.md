---
id: controle-anot-laplace-tvf
titulo: Revisão de Laplace: propriedades, entradas de teste e teorema do valor final (quando vale); exemplos 7(s+5)/(2s(s²+2s+3)) e 4/(s(s²−5s+6))
assunto: controle-01-laplace-ft
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão de Laplace e Sistemas mecânicos" (19 ago. 2026), p. 1–4
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

**Definição (unilateral):** $F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty f(t)e^{-st}\,dt$, com $s = \sigma + j\omega$ (a transformada de f de t é a integral de f vezes e elevado a menos s t).

**Propriedades:** linearidade; atraso $\mathcal{L}\{f(t - t_d)\} = e^{-st_d}F(s)$; derivada $\mathcal{L}\{\dot f\} = sF(s) - f(0)$; integral $\mathcal{L}\{\int_0^t f\} = F(s)/s$; $\mathcal{L}\{t f(t)\} = -\frac{dF}{ds}$; deslocamento em $s$: $\mathcal{L}\{e^{-at}f(t)\} = F(s + a)$.

**Entradas de teste:** degrau $A/s$; rampa $A/s^2$ (e $t^n \to n!/s^{n+1}$); $Ae^{-at} \to A/(s + a)$; impulso $\to 1$; $\mathrm{sen}\,\omega t \to \frac{\omega}{s^2 + \omega^2}$; $\cos\omega t \to \frac{s}{s^2 + \omega^2}$.

**Teorema do valor final (TVF):** $\lim_{t\to\infty} f(t) = \lim_{s\to 0} sF(s)$, **só se** todos os polos de $sF(s)$ têm parte real negativa (em $F(s)$: no máximo um polo simples em $s = 0$). Verifique a estabilidade antes de usar.

- $F(s) = \frac{7(s + 5)}{2s(s^2 + 2s + 3)}$: polos $0$ e $-1 \pm j\sqrt2$, o TVF vale: $f(\infty) = \frac{7\cdot5}{2\cdot3} = \frac{35}{6}$.
- $F(s) = \frac{4}{s(s^2 - 5s + 6)}$: polos $0, 2, 3$. O TVF daria $4/6$, mas **não se aplica**: $f(t) = \frac23 - 2e^{2t} + \frac43e^{3t}$ cresce sem limite.

**Verificação:** a inversa por frações parciais (SymPy) confirma $f(t)$ do segundo exemplo e o limite $35/6$ do primeiro.
