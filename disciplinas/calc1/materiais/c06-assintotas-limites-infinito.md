---
id: calc1-assintotas-limites-infinito
titulo: Quais são as assíntotas de uma função racional (vertical, horizontal, oblíqua) e limites no infinito: (x² + x − 2)/(x³ + 2x² − 3x), x/√(x² + 1), √(3x² + 8x + 6) − √(3x² + 3x + 1)
assunto: calc1-03-limites-infinito-assintotas
tipo: prova
questao: vários
semestre: 2014–2017
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 1ª Avaliação (30.08.2014), Q1b e Q4b; 1ª Avaliação (05.04.2014), Q4a; Exercícios resolvidos (aula de 17.02.2017), Q4
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-calc1-aula-distancia-2017
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

Quais são as assíntotas de $y = \dfrac{x^2}{x-1}$? Domínio $x \ne 1$; vertical $x = 1$; como $x^2 = (x-1)(x+1) + 1$, a assíntota oblíqua é $y = x + 1$ e não há horizontal.

**Roteiro.** Domínio primeiro. Vertical: $x = a$ é assíntota se algum limite lateral em a for $\pm\infty$ (candidatos: zeros do denominador que **não** cancelam). Horizontal: $y = L$ se $\lim_{x\to\pm\infty} f(x) = L$ (calcule os **dois** lados). Oblíqua: $y = mx + b$ com $m = \lim f(x)/x$ e $b = \lim (f(x) - mx)$.

- $y = \dfrac{x^2+x-2}{x^3+2x^2-3x} = \dfrac{(x+2)(x-1)}{x(x+3)(x-1)}$. Domínio: $x \ne 0, -3, 1$. Verticais $x = 0$ e $x = -3$; em $x = 1$ o fator cancela (limite $\tfrac34$, buraco, não assíntota). Horizontal $y = 0$.
- $f(x) = \dfrac{x}{\sqrt{x^2+1}}$: sem vertical (domínio todo $\mathbb R$). Como $\sqrt{x^2} = |x|$: $x \to +\infty$ dá 1 e $x \to -\infty$ dá −1, duas horizontais, $y = 1$ e $y = -1$.
- $\lim_{x\to\infty}\left(\sqrt{3x^2+8x+6}-\sqrt{3x^2+3x+1}\right)$ ($\infty - \infty$): multiplique pelo conjugado, $\dfrac{5x+5}{\sqrt{3x^2+8x+6}+\sqrt{3x^2+3x+1}} \to \dfrac{5}{2\sqrt3}$.
- $\lim_{x\to\infty}\left(\sqrt{x^2+x}-\sqrt{x^2-x}\right) = 1$ (resolução da aula conferida).
- $\lim_{x\to-\infty}\dfrac{\sqrt{9x^2+2}}{4x+3} = -\dfrac34$: para $x < 0$, $\sqrt{x^2} = -x$.

Erro comum: usar $\sqrt{x^2} = x$ quando $x \to -\infty$.

**Verificação:** $f(-1000) \approx -0{,}9999995$; a diferença de raízes em $x = 10^6$ vale $\approx 1{,}4434 \approx 5/(2\sqrt3)$.
