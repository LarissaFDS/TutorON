---
id: ga-parabola
titulo: Parábola: equação pela definição (foco e diretriz), parábola com diretriz inclinada y = −x, elementos de y = ax² + bx + c e de y² − 2y = 4x, parábola por vértice e ponto
assunto: ga-07-parabola
tipo: prova
questao: vários
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 2ª Avaliação (10.03.2017), Q2; 2ª Avaliação (11.03.2017), Q2b; Reavaliação AB1 (24.05.2017), Q4a
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

**Definição:** pontos equidistantes do foco F e da reta diretriz. Com eixo vertical: $(x - h)^2 = 4p(y - k)$, vértice (h, k), foco $(h, k + p)$, diretriz $y = k - p$.

**Foco F(2, 2), diretriz $x + y = 0$.** $\sqrt{(x-2)^2 + (y-2)^2} = \dfrac{|x + y|}{\sqrt2}$. Elevando ao quadrado e multiplicando por 2: $x^2 - 2xy + y^2 - 8x - 8y + 16 = 0$. O termo $xy$ aparece porque o eixo (a reta y = x) é inclinado.

**Elementos de $y = ax^2 + bx + c$, $a \neq 0$.** Completando quadrado: $\left(x + \tfrac{b}{2a}\right)^2 = \tfrac1a\left(y + \tfrac{\Delta}{4a}\right)$, com $\Delta = b^2 - 4ac$. Vértice $\left(-\tfrac{b}{2a}, -\tfrac{\Delta}{4a}\right)$, $p = \tfrac{1}{4a}$, foco $\left(-\tfrac{b}{2a}, \tfrac{1 - \Delta}{4a}\right)$, diretriz $y = -\tfrac{1 + \Delta}{4a}$.

**$y^2 - 2y = 4x$.** $(y - 1)^2 = 4\left(x + \tfrac14\right)$: eixo horizontal $y = 1$, vértice $(-\tfrac14, 1)$, $p = 1$, foco $(\tfrac34, 1)$, diretriz $x = -\tfrac54$.

**Eixo paralelo ao eixo y, vértice (2, 3), passa por (1, 4).** $y - 3 = a(x - 2)^2$; com (1, 4), $a = 1$: $y = (x-2)^2 + 3$.

**Verificação:** o vértice (1, 1) da primeira parábola satisfaz $1 - 2 + 1 - 8 - 8 + 16 = 0$; o ponto $(\tfrac34, 3)$ de $(y-1)^2 = 4(x + \tfrac14)$ está a 2 do foco e a 2 da diretriz.
