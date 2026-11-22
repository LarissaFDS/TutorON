---
id: calc1-continuidade-por-partes
titulo: Continuidade de função definida por partes: achar constantes (c e k; m e n) e classificar descontinuidades
assunto: calc1-02-limites-continuidade
tipo: prova
questao: vários
semestre: 2014–2017
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 1ª Avaliação (05.04.2014), Q1b; 1ª Avaliação (11.04.2015), Q4; 1ª Avaliação (30.08.2014), Q3a; Três exercícios com soluções (aula de 17.02.2017), Q1 e Q2
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

**Definição:** f é contínua em a se (i) $f(a)$ existe, (ii) $\lim_{x\to a} f(x)$ existe (laterais iguais) e (iii) os dois são iguais. Em função por partes, cada pedaço polinomial ou trigonométrico é contínuo; só os pontos de emenda precisam de conta.

- $f(x) = x$ ($x \le 1$), $cx + k$ ($1 < x < 4$), $-2x$ ($x \ge 4$). Em 1: $c + k = 1$. Em 4: $4c + k = -8$. Logo $c = -3$, $k = 4$.
- $f(x) = \cos(\pi x)$ ($x < 1$), $mx^2 + 3x + n$ ($1 \le x < 2$), $mx + n$ ($x \ge 2$). Em 1: $m + 3 + n = \cos\pi = -1$. Em 2: $4m + 6 + n = 2m + n$, logo $m = -3$ e $n = -1$.
- $g(x) = \dfrac{x^2-16}{x^2-3x-4} = \dfrac{(x-4)(x+4)}{(x-4)(x+1)}$: definir $g(4) = \tfrac{8}{5}$ remove a descontinuidade (removível); em $x = -1$ ela é infinita.
- Aula de 2017: $\cos x$ ($x<0$), $\sqrt{1-x^2}$ ($0\le x\le1$), $x^2-2$ ($x>1$) é contínua em 0 (tudo vale 1) e descontínua em 1 (pela esquerda 0, pela direita −1). A solução da aula escreve "$\lim_{x\to1^-}\sqrt{1-x^2} = 1$"; o valor certo é 0, mas a conclusão (descontínua em 1) não muda.
- $\dfrac{2x^2+5x-3}{x^2-2x-15}$: removível em −3 (limite $\tfrac{7}{8}$), infinita em 5.

**Verificação:** substitua as constantes: $-3\cdot1+4 = 1$ e $-3\cdot4+4 = -8$; $-3+3-1 = -1$ e $-12+6-1 = -6+(-1)$.
