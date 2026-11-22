---
id: calc1-regra-lhospital
titulo: Regra de L'Hospital: quando pode usar, formas 0/0, ∞/∞, ∞ − ∞, 1^∞ e 0·∞; tg x − x sobre x³, x/cotg x − π/(2 cos x), ((eˣ + e)/eˣ)^(eˣ), área do segmento sobre área do triângulo
assunto: calc1-09-lhospital
tipo: prova
questao: vários
semestre: 2013–2016
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª Avaliação (16.03.2013), Q2a e Q2b; 4ª prova (foto), Q4b e Q5b; Quarto Simulado (04.05.2016), Q1a
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-calc1-listas-simulados
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

**Quando posso usar a regra de L'Hospital?** Só quando o quociente $\tfrac{f(x)}{g(x)}$ é forma indeterminada $\tfrac00$ ou $\tfrac{\infty}{\infty}$, f e g deriváveis perto do ponto, $g'(x) \ne 0$ ali, e o limite de $\tfrac{f'}{g'}$ existe (ou é ±∞). Deriva-se numerador e denominador **separadamente** (não é a regra do quociente). Outras formas viram quociente antes: $0\cdot\infty$ (passe um fator para o denominador), $\infty - \infty$ (denominador comum), $1^\infty$, $0^0$, $\infty^0$ (tome o logaritmo).

- $\lim_{x\to0}\dfrac{\operatorname{tg}x - x}{x^3}$ (0/0): $\dfrac{\sec^2x - 1}{3x^2} = \dfrac{\operatorname{tg}^2x}{3x^2} \to \dfrac13$.
- $\lim_{x\to\pi/2}\left[\dfrac{x}{\operatorname{cotg}x} - \dfrac{\pi}{2\cos x}\right]$ ($\infty-\infty$): $= \dfrac{x\operatorname{sen}x - \pi/2}{\cos x}$ (0/0), L'Hospital: $\dfrac{\operatorname{sen}x + x\cos x}{-\operatorname{sen}x} \to -1$.
- $\lim_{x\to+\infty}\left(\dfrac{e^x+e}{e^x}\right)^{e^x}$ ($1^\infty$): $\ln y = e^x\ln(1 + e^{1-x}) \to e$, então o limite é $e^e$.
- $(1+x)^{1/x^2}$: $\ln y = \tfrac{\ln(1+x)}{x^2} \approx \tfrac{1}{x}$; para $x \to 0^+$ o limite é $+\infty$ e para $x \to 0^-$ é 0.
- Setor de raio 1 e ângulo θ: segmento $A = \tfrac{\theta - \operatorname{sen}\theta}{2}$, triângulo PQR $B = \tfrac12\operatorname{sen}\theta(1-\cos\theta)$. $\lim_{\theta\to0^+}\tfrac{A}{B} = \tfrac13$ (L'Hospital ou Taylor: $\tfrac{\theta^3/6}{\theta^3/2}$).

Erro comum: aplicar a regra em $\tfrac{\operatorname{sen}x}{x+1}$ com $x \to 0$, que não é indeterminado (o limite é 0, não 1).

**Verificação:** em $x = 0{,}01$, $\tfrac{\operatorname{tg}x - x}{x^3} \approx 0{,}33335$; em $\theta = 0{,}01$, $A/B \approx 0{,}33334$.
