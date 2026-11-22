---
id: calc1-tvi-raizes
titulo: Teorema do Valor Intermediário para mostrar que uma equação tem raiz (x² − cos x, 4x² + x + sen x = 12, x³ + 1 e 15x)
assunto: calc1-02-limites-continuidade
tipo: prova
questao: vários
semestre: 2014–2015
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 1ª Avaliação (05.04.2014), Q2b; 1ª Avaliação (11.04.2015), Q2b; 1ª Avaliação (30.08.2014), Q2a; Avaliação Final (03.12.2015), Q2a
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-im-calc1-provas-pdf
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: pendente de confirmação do professor (resolução da equipe TutorON, conferida com SymPy; depende da leitura do enunciado).

**TVI:** se g é contínua em $[a, b]$ e $g(a)$ e $g(b)$ têm sinais opostos, existe $c \in (a, b)$ com $g(c) = 0$. Hipótese a conferir sempre: **continuidade no intervalo fechado**.

- $x^2 - \cos x = 0$: $g(0) = -1 < 0$ e $g(\pi) = \pi^2 + 1 > 0$; g contínua, logo há raiz em $(0, \pi)$.
- $4x^2 + x + \operatorname{sen} x = 12$: $g(x) = 4x^2 + x + \operatorname{sen}x - 12$, $g(0) = -12$, $g(2) = 6 + \operatorname{sen} 2 > 0$.
- Número positivo igual ao dobro do quadrado: $g(x) = 2x^2 - x$, $g(\tfrac14) = -\tfrac18$, $g(1) = 1$; a raiz é $x = \tfrac12$.

**Pendência (30.08.2014, Q2a).** Na foto, o enunciado pede que as curvas $y = x^3 + 1$ e $y = -15x$ se cortem pelo menos **três** vezes em $[-4, 4]$. Como lido, é falso: $g(x) = x^3 + 15x + 1$ tem $g'(x) = 3x^2 + 15 > 0$, é estritamente crescente e tem **uma** raiz só. Com $y = 15x$ (sem o sinal de menos), $g(x) = x^3 - 15x + 1$ vale $-3,\ 1,\ -13,\ 5$ em $x = -4, 0, 1, 4$: três trocas de sinal, três interseções. O sinal precisa ser confirmado no original.

**Verificação:** $g(0{,}5) = 2\cdot0{,}25 - 0{,}5 = 0$; $x^3-15x+1$ tem raízes reais $\approx -3{,}90;\ 0{,}067;\ 3{,}84$, todas em $[-4, 4]$.
