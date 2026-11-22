---
id: calc1-integral-definida
titulo: Integral definida: soma de Riemann de ∫₀² (x − 2) dx, Teorema Fundamental do Cálculo e diferença entre integral e área (∫₁⁵ (x − 2) dx = 4, área 5)
assunto: calc1-11-primitivas-integral
tipo: exercicio
questao: questão do banco
semestre: 2005–2016
resolucao: sim
fonte: Banco de Questões de Cálculo 1 (resolução), IM-UFAL, 2005 a 2016: questão de integral definida e área
fontes_catalogo: ufal-im-calc1-banco
autoria: Enunciado e resolução de referência: Banco de Questões de Cálculo 1 do Instituto de Matemática da UFAL (resolução), parafraseado pela equipe TutorON; resolução da equipe TutorON, conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questão do banco de questões (enunciado parafraseado). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

A ementa (PPC de Engenharia de Computação, 2014) termina em "integração e a integral definida"; nas provas do pacote ela aparece pouco, mas está no banco.

**Soma de Riemann (pontos à direita).** $\int_0^2 (x-2)\,dx$: $\Delta x = \tfrac{2}{n}$, $x_i = \tfrac{2i}{n}$.
$$\sum_{i=1}^n\left(\frac{2i}{n} - 2\right)\frac{2}{n} = \frac{4}{n^2}\cdot\frac{n(n+1)}{2} - 4 = 2 + \frac{2}{n} - 4 \xrightarrow{n\to\infty} -2.$$
Use $\sum_{i=1}^n i = \tfrac{n(n+1)}{2}$.

**Teorema Fundamental do Cálculo:** se F é primitiva de f contínua em $[a,b]$, $\int_a^b f(x)\,dx = F(b) - F(a)$. Com $F(x) = \tfrac{x^2}{2} - 2x$: $\int_1^5 (x-2)\,dx = \left(\tfrac{25}{2} - 10\right) - \left(\tfrac12 - 2\right) = 4$.

**Integral não é área.** Entre $x = 1$ e $x = 5$ a reta $y = x - 2$ fica abaixo do eixo em $[1, 2]$ (triângulo de área $\tfrac12$) e acima em $[2, 5]$ (área $\tfrac92$). Área total: $\tfrac12 + \tfrac92 = 5$; integral: $\tfrac92 - \tfrac12 = 4$. A parte abaixo do eixo entra com sinal negativo.

Fronteira: técnicas de integração (substituição, partes) e aplicações (volume, comprimento) costumam ficar para Cálculo 2.

**Verificação:** $\tfrac{d}{dx}\left(\tfrac{x^2}{2} - 2x\right) = x - 2$; a soma de Riemann com $n = 1000$ vale $-1{,}998$.
