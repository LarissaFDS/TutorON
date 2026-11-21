---
id: ga-circunferencias
titulo: Circunferência por três pontos, circunferência tangente a duas retas com centro numa reta, ponto da circunferência mais próximo de uma reta e rotação de uma circunferência
assunto: ga-06-circunferencia-esfera
tipo: prova
questao: 1a, 1b
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 2ª Avaliação (10.03.2017), Q1; 2ª Avaliação (11.03.2017), Q1
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

Forma reduzida: $(x - x_c)^2 + (y - y_c)^2 = r^2$, centro $(x_c, y_c)$ e raio r.

**Por A(8, 6), B(6, 4), C(4, 6).** O centro equidista dos três: a mediatriz de AC é $x = 6$; a de AB passa por (7, 5) com normal (1, 1): $x + y = 12$. Centro (6, 6), raio 2: $(x-6)^2 + (y-6)^2 = 4$.

**Tangente a $y = 2x$ e $x = 2y$, centro em $x + y = 6$.** Centro (a, b) equidistante das retas: $|2a - b| = |a - 2b|$ (o $\sqrt5$ cancela). Ou $a = b$, ou $a = -b$; com $a + b = 6$, só $a = b = 3$. Raio $\dfrac{|6 - 3|}{\sqrt5} = \dfrac{3}{\sqrt5}$: $(x-3)^2 + (y-3)^2 = \tfrac95$.

**Ponto de $(x-1)^2 + (y-2)^2 = 9$ mais próximo de $x = -3 + t,\ y = 1 - 2t$.** Forma geral da reta: $2x + y + 5 = 0$, normal $(2, 1)$. Distância do centro: $9/\sqrt5 \approx 4{,}02 > 3$, então não se cortam. O ponto está na perpendicular à reta pelo centro, a 3 unidades do centro, do lado da reta: $(1, 2) - \tfrac{3}{\sqrt5}(2, 1) = (1 - \tfrac{6}{\sqrt5},\ 2 - \tfrac{3}{\sqrt5})$.

**Rotação de $x^2 - 8x + y^2 + 6y = 0$ por π/2 em torno da origem.** Completando quadrados: $(x-4)^2 + (y+3)^2 = 25$. A rotação anti-horária leva (x, y) em (−y, x): o centro (4, −3) vai para (3, 4), e o raio se mantém: $(x-3)^2 + (y-4)^2 = 25$. As duas passam pela origem.

**Verificação:** A, B e C estão a distância 2 de (6, 6); o ponto mais próximo satisfaz a equação da circunferência e está a $9/\sqrt5 - 3$ da reta.
