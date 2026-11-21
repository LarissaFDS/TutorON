---
id: ga-superficies-revolucao
titulo: Superfícies de revolução: girar y = mz em torno de Oz (cone), y = x³ e y = x em torno de Oy, e a curva de interseção com y > 0
assunto: ga-12-quadricas-superficies
tipo: prova
questao: 1b; 2
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Reavaliação AB2 (24.05.2017), Q1b; 4ª Avaliação (12.05.2017), Q2
fontes_catalogo: ufal-ga-provas-2017
autoria: Enunciado: Instituto de Matemática da UFAL (professor não impresso na prova), parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

**Regra.** Girando uma curva em torno de um eixo, cada ponto descreve uma circunferência centrada no eixo: a coordenada do eixo fica, e a distância ao eixo vira o raio. Em torno de Oz, troque $|y|$ (ou $|x|$) por $\sqrt{x^2 + y^2}$; em torno de Oy, troque $|x|$ por $\sqrt{x^2 + z^2}$.

**Reta $y = mz$, $x = 0$, em torno de Oz.** $\sqrt{x^2 + y^2} = |m||z|$, ou $x^2 + y^2 = m^2z^2$: um cone. Em z = 1, o traço é $x^2 + y^2 = m^2$; para ser $x^2 + y^2 = 1$, $m = \pm1$.

**4ª Avaliação, Q2.** $C_1: y = x^3,\ z = 0$ e $C_2: y = x,\ z = 0$, em torno de Oy.
- a) $S_1$: $|y| = (\sqrt{x^2 + z^2})^3$, ou $y^2 = (x^2 + z^2)^3$. A cúbica tem um ramo com $y < 0$ (para $x < 0$), então a superfície tem uma parte acima e outra abaixo do plano xz, que se tocam na origem.
- b) $S_2$: $y^2 = x^2 + z^2$, cone circular de eixo Oy.
- c) Com $\rho^2 = x^2 + z^2$ e $y > 0$: $y = \rho^3$ e $y = \rho$, logo $\rho^3 = \rho$ e $\rho = 1$ (ρ > 0, já que y > 0). A curva é a circunferência $x^2 + z^2 = 1$ no plano $y = 1$.

**Verificação:** (1, 1, 0) está em $C_1$ e em $C_2$; girando-o em torno de Oy obtém-se $(\cos t, 1, \operatorname{sen} t)$, que satisfaz $1 = 1^3$ e $1 = 1$; para m = 1, o ponto (1, 0, 1) está no cone e no plano z = 1.
