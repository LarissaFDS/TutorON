---
id: sinais-anot-numeros-complexos
titulo: Números complexos para sinais: forma retangular, polar, fórmula de Euler, ângulo quando a parte real é negativa
assunto: sinais-01-complexos
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Revisão números complexos" (8 mar. 2026)
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

**Formas:** $z = a + jb$ (retangular, $j^2 = -1$), $z = r(\cos\theta + j\,\mathrm{sen}\,\theta)$ (trigonométrica) e $z = re^{j\theta}$ (polar), com $r = |z| = \sqrt{a^2+b^2}$ (módulo) e $\theta = \angle z$ (ângulo).

**Fórmula de Euler:** trocando $x$ por $j\theta$ na série de $e^x$ e separando os termos pares e ímpares: $e^{j\theta} = \cos\theta + j\,\mathrm{sen}\,\theta$, com $|e^{j\theta}| = 1$. Em palavras: e elevado a j teta é cosseno mais j seno. Identidades úteis: $1 = e^{j2\pi n}$, $-1 = e^{j\pi}$, $j = e^{j\pi/2}$, $-j = e^{-j\pi/2}$.

**Ângulo (correção):** as anotações escrevem $\theta = \tan^{-1}(b/a)$ também para $a < 0$. O certo é
$$\theta = \tan^{-1}\!\left(\frac{b}{a}\right)\ (a > 0),\qquad \theta = \tan^{-1}\!\left(\frac{b}{a}\right) \pm \pi\ (a < 0),$$
porque o arco tangente só devolve ângulos do 1º e 4º quadrantes. Ex.: $-6 + j8$ tem ângulo $126{,}87^\circ$, não $-53{,}13^\circ$. Na calculadora ou em Python use `atan2(b, a)`.

**Recíproco e conjugado (correções):** $1/z = \frac{1}{r}e^{-j\theta}$ (as anotações escreveram $e^{-jz}$); $z^* = a - jb = re^{-j\theta}$, que **não** é igual a $re^{j\theta}$ (a não ser que $b = 0$).

**Exemplo:** $z = 2 + j3$: $|z| = \sqrt{13} \approx 3{,}606$, $\theta = \tan^{-1}(3/2) = 56{,}3^\circ = 0{,}983$ rad; $z = \sqrt{13}\,e^{j56{,}3^\circ}$.

**Verificação:** `cmath.polar(2+3j)` dá $(3{,}606;\ 0{,}983)$; `cmath.phase(-6+8j)` dá $2{,}214$ rad $= 126{,}87^\circ$; $z\cdot(1/z) = 1$ e $z z^* = |z|^2$.
