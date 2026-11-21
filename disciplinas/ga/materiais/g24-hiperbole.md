---
id: ga-hiperbole
titulo: Hipérbole: equação pelos focos e vértices na reta y = x, focos, vértices e assíntotas por completar quadrados, reta normal à hipérbole num ponto
assunto: ga-09-hiperbole
tipo: prova
questao: 4a, 4b; 4a; 3a
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 2ª Avaliação (10.03.2017), Q4; 2ª Avaliação (11.03.2017), Q4a; Reavaliação AB1 (24.05.2017), Q3a
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

**Como achar focos, vértices e assíntotas de uma hipérbole.** Definição: $|d(P, F_1) - d(P, F_2)| = 2a$; $c^2 = a^2 + b^2$. Forma reduzida com eixo horizontal: $\tfrac{(x-h)^2}{a^2} - \tfrac{(y-k)^2}{b^2} = 1$, assíntotas $y - k = \pm\tfrac ba(x - h)$.

**$x^2 - 9y^2 = 14 - 4x - 18y$.** $(x+2)^2 - 4 - 9(y-1)^2 + 9 = 14$, ou $\dfrac{(x+2)^2}{9} - (y-1)^2 = 1$. Centro (−2, 1), $a = 3$, $b = 1$, $c = \sqrt{10}$; vértices (1, 1) e (−5, 1); focos $(-2 \pm \sqrt{10}, 1)$; assíntotas $y - 1 = \pm\tfrac13(x + 2)$.

**$4x^2 - y^2 - 16x - 6y = -3$.** $4(x-2)^2 - 16 - (y+3)^2 + 9 = -3$, ou $(x-2)^2 - \dfrac{(y+3)^2}{4} = 1$. Centro (2, −3), $a = 1$, $b = 2$, $c = \sqrt5$; vértices (3, −3) e (1, −3); focos $(2 \pm \sqrt5, -3)$; assíntotas $y + 3 = \pm2(x - 2)$.

**Focos (2, 2) e (−2, −2), vértices (1, 1) e (−1, −1).** Centro na origem, eixo focal $y = x$, $c = 2\sqrt2$, $a = \sqrt2$, $b^2 = 6$. Nas coordenadas giradas de 45° ($u = \tfrac{x+y}{\sqrt2}$, $w = \tfrac{y-x}{\sqrt2}$): $\tfrac{u^2}{2} - \tfrac{w^2}{6} = 1$; de volta em x e y: $x^2 + 4xy + y^2 = 6$.

**Reta normal em $(x_0, y_0)$.** A tangente $\tfrac{x_0x}{a^2} - \tfrac{y_0y}{b^2} = 1$ tem normal $\left(\tfrac{x_0}{a^2}, -\tfrac{y_0}{b^2}\right)$, que é o **diretor** da reta normal. Forma geral: $\tfrac{y_0}{b^2}(x - x_0) + \tfrac{x_0}{a^2}(y - y_0) = 0$; se $x_0y_0 \neq 0$, equivale a $\tfrac{a^2x}{x_0} + \tfrac{b^2y}{y_0} = a^2 + b^2$.

**Verificação:** (1, 1) satisfaz $1 + 4 + 1 = 6$, e o foco (2, 2) dá $|d(P, F_1) - d(P, F_2)| = 2\sqrt2$ no vértice; o diretor da normal é ortogonal ao da tangente.
