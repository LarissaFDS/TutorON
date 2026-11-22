---
id: calc1-esboco-grafico
titulo: Esboço de gráfico completo: x/(x² − 4) e (4x² + 8)/(−2x − 1) com assíntota oblíqua, crescimento, concavidade e inflexão
assunto: calc1-08-esboco-graficos
tipo: prova
questao: vários
semestre: 2015
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª prova (foto), Q5b; Avaliação Final (03.12.2015), Q8
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

**Roteiro:** domínio; interceptos; simetria; assíntotas (vertical, horizontal, oblíqua); f' e quadro de sinais (crescimento, máximos e mínimos); f'' e quadro de sinais (concavidade, inflexão); esboço.

**$f(x) = \dfrac{x}{x^2-4}$.** Domínio $x \ne \pm2$; corta os eixos só na origem; ímpar. Verticais $x = \pm2$; horizontal $y = 0$. $f'(x) = -\dfrac{x^2+4}{(x^2-4)^2} < 0$: decrescente em cada intervalo do domínio, sem extremos. $f''(x) = \dfrac{2x(x^2+12)}{(x^2-4)^3}$: côncava para cima em $(-2, 0)$ e $(2, \infty)$, para baixo em $(-\infty, -2)$ e $(0, 2)$; inflexão em (0, 0) (em ±2 a concavidade muda, mas f não está definida).

**$f(x) = \dfrac{4x^2+8}{-2x-1}$** (a prova dá f' e f''). Domínio $x \ne -\tfrac12$. Divisão: $4x^2 + 8 = (-2x-1)(-2x+1) + 9$, então $f(x) = -2x + 1 + \dfrac{9}{-2x-1}$: assíntota **oblíqua** $y = -2x + 1$ e vertical $x = -\tfrac12$; sem horizontal. $f'(x) = -\dfrac{8(x^2+x-2)}{(2x+1)^2}$: zeros em $x = -2$ e $x = 1$; decrescente em $(-\infty,-2)$ e $(1,\infty)$, crescente em $(-2,-\tfrac12)$ e $(-\tfrac12, 1)$. Mínimo local $f(-2) = 8$, máximo local $f(1) = -4$. $f''(x) = -\dfrac{72}{(2x+1)^3}$: côncava para cima à esquerda de $-\tfrac12$, para baixo à direita; sem inflexão.

Erro comum: ignorar a assíntota oblíqua quando o grau do numerador é um a mais.

**Verificação:** $f(-2) = \tfrac{24}{3} = 8$; $f(1) = \tfrac{12}{-3} = -4$; $f(100) - (-199) \approx -0{,}045 \to 0$.
