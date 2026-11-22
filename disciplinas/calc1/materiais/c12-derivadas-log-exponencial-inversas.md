---
id: calc1-derivadas-log-inversas
titulo: Derivadas de logaritmo, exponencial e inversas: (f⁻¹)'(1) de x + e^(2x), x^(ln x), (1 + 1/x)^x, log_x 2, ln[cos(arcsec x)], arcsen x/√(1 − x²)
assunto: calc1-05-regras-derivacao
tipo: prova
questao: vários
semestre: 2014–2015
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 2ª Avaliação (10.05.2014), Q2b e Q4a; 2ª Avaliação (04.10.2014), Q2a; Avaliação Final (03.12.2015), Q4a, Q4b e Q6a
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-im-calc1-provas-pdf
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

- **Derivada da inversa.** $f(x) = x + e^{2x}$: $f(0) = 1$, logo $f^{-1}(1) = 0$; $(f^{-1})'(1) = \dfrac{1}{f'(0)} = \dfrac{1}{1 + 2e^0} = \dfrac13$. Hipótese: $f'(0) \ne 0$.
- **Expoente variável: logaritme.** $y = x^{\ln x}$ ($x > 0$): $\ln y = (\ln x)^2$, $y' = x^{\ln x}\cdot\dfrac{2\ln x}{x}$. $y = (1 + \tfrac1x)^x$: $y' = (1+\tfrac1x)^x\left[\ln(1+\tfrac1x) - \dfrac{1}{x+1}\right]$.
- **Mudança de base.** $f(x) = \log_x 2 = \dfrac{\ln2}{\ln x}$; ordenada 1 em $x = 2$; $f'(x) = -\dfrac{\ln2}{x\ln^2x}$, $f'(2) = -\dfrac{1}{2\ln2}$. Normal: $y = 1 + 2\ln2\,(x - 2)$.
- **Simplifique antes.** $\cos(\operatorname{arcsec} x) = \tfrac1x$, então para $x \ge 1$, $f(x) = \ln[\cos(\operatorname{arcsec}x)] = -\ln x$ e $f'(2) = -\tfrac12$.
- **Quociente com inversa trigonométrica.** $f(x) = \dfrac{\operatorname{arcsen}x}{\sqrt{1-x^2}}$: $f'(x) = \dfrac{1}{1-x^2} + \dfrac{x\operatorname{arcsen}x}{(1-x^2)^{3/2}}$; em $\tfrac{\sqrt2}{2}$, $f' = 2 + \tfrac{\pi}{2}$.

Domínio antes de derivar: $\log_x 2$ exige $x > 0$, $x \ne 1$; $\operatorname{arcsen}$ exige $|x| \le 1$.

**Verificação:** com SymPy, `diff(log(2)/log(x), x).subs(x, 2)` dá $-1/(2\ln2)$; numericamente $(f^{-1})'(1) \approx 0{,}3333$.
