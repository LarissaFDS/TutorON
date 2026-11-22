---
id: calc1-retas-tangentes-problemas
titulo: Problemas de reta tangente: tangentes a y = ±√(x + 4) onde |y| = 3, tangente a 1/∛x, tangentes a y = x³ + 1 pelo ponto (1, 1)
assunto: calc1-04-derivada-definicao-tangente
tipo: prova
questao: vários
semestre: 2014
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 1ª Avaliação (29.08.2014), Q4a; 1ª Avaliação (30.08.2014), Q4a; 2ª Avaliação (04.10.2014), Q1b
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

**Tangentes a $y = \sqrt{x+4}$ e $y = -\sqrt{x+4}$ onde $|y| = 3$.** $x + 4 = 9$, $x = 5$. Inclinações: $\tfrac{1}{2\sqrt{9}} = \tfrac16$ e $-\tfrac16$. Retas $y = 3 + \tfrac{x-5}{6}$ e $y = -3 - \tfrac{x-5}{6}$. Igualando: $\tfrac{x-5}{3} = -6$, $x = -13$, $y = 0$. As retas se cortam em $(-13, 0)$ (a figura é simétrica em relação ao eixo x).

**$f(x) = x^{-1/3}$ no inteiro p com $[\![p]\!] = 2$.** Como p é inteiro, $p = 2$. $f'(x) = -\tfrac13 x^{-4/3}$, então $f'(2) = -\dfrac{1}{3\cdot 2^{4/3}} = -\dfrac{1}{6\sqrt[3]{2}}$.

**Tangentes a $y = x^3 + 1$ que passam por (1, 1)** (o ponto não está na curva). Ponto de tangência $(a, a^3+1)$, inclinação $3a^2$. A reta passa por (1, 1): $1 - (a^3+1) = 3a^2(1 - a)$, ou seja, $2a^3 - 3a^2 = 0$, $a = 0$ ou $a = \tfrac32$. Pontos de tangência $(0, 1)$ e $(\tfrac32, \tfrac{35}{8})$; retas $y = 1$ e $y = \tfrac{27}{4}x - \tfrac{23}{4}$.

Roteiro: quando o ponto dado **não** está na curva, a incógnita é o ponto de tangência.

**Verificação:** $y = \tfrac{27}{4}x - \tfrac{23}{4}$ passa por (1, 1) e por $(\tfrac32, \tfrac{35}{8})$; $(-13, 0)$ satisfaz as duas retas.
