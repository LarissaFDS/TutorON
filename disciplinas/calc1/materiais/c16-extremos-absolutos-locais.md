---
id: calc1-extremos-absolutos
titulo: Pontos críticos e extremos absolutos e locais: x^(1/3) + x^(4/3), 10x(2 − ln x) em [1, e²], cos²x − 2 sen x em [0, 2π], sen⁴x − sen²x, sen(arctg x), x^(1/x)
assunto: calc1-07-extremos-tvm
tipo: prova
questao: vários
semestre: 2013–2015
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª prova (foto), Q4a e Q2b; 2ª prova Verão 2015, Q5a; 4ª Avaliação (16.03.2013), Q1a; 3ª Avaliação (01.11.2014), Q4a e Q4b
fontes_catalogo: ufal-im-calc1-provas-fotos
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

**Método do intervalo fechado.** f contínua em $[a, b]$: (1) números críticos em $(a, b)$ ($f' = 0$ **ou** f' não existe); (2) calcule f neles **e nas extremidades**; (3) o maior valor é o máximo absoluto e o menor, o mínimo. Para extremo **local**, use o sinal de f' (1ª derivada) ou de f'' (2ª).

- $f(x) = x^{1/3} + x^{4/3}$, domínio $\mathbb R$: $f'(x) = \tfrac13x^{-2/3}(1 + 4x)$. Críticos: $x = -\tfrac14$ ($f' = 0$) e $x = 0$ (f' não existe). f' troca de − para + em $-\tfrac14$: mínimo local e absoluto $f(-\tfrac14) = -\dfrac{3}{4\sqrt[3]4}$. Em 0 o sinal não muda: não é extremo. Sem máximo absoluto.
- $f(x) = 10x(2 - \ln x)$ em $[1, e^2]$: $f'(x) = 10(1 - \ln x)$, crítico $x = e$. $f(1) = 20$, $f(e) = 10e$, $f(e^2) = 0$: máximo $10e$, mínimo 0.
- $f(x) = \cos^2x - 2\operatorname{sen}x$ em $[0, 2\pi]$: $f' = -2\cos x(\operatorname{sen}x + 1)$, críticos $\tfrac{\pi}{2}$ e $\tfrac{3\pi}{2}$. Valores: $1, -2, 2, 1$; máximo 2 em $\tfrac{3\pi}{2}$, mínimo −2 em $\tfrac{\pi}{2}$.
- $f(x) = \operatorname{sen}^4x - \operatorname{sen}^2x$ em $]0, \tfrac{\pi}{2}[$: $f' = 2\operatorname{sen}x\cos x(2\operatorname{sen}^2x - 1)$, crítico $\tfrac{\pi}{4}$, mínimo local $-\tfrac14$.
- $\operatorname{sen}(\operatorname{arctg}x)$ em $[\sqrt3, 2\sqrt2]$ é crescente: mínimo $\tfrac{\sqrt3}{2}$, máximo $\tfrac{2\sqrt2}{3}$.
- $x^{1/x}$, $x > 0$: único número crítico $x = e$.

Erro comum: esquecer as extremidades ou os pontos onde f' não existe.

**Verificação:** $f(-0{,}25) \approx -0{,}4725$ e $f(-0{,}3) \approx -0{,}4481$; $10e \approx 27{,}18 > 20$.
