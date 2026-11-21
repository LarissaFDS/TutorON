---
id: ga-esferas-equacao
titulo: Equação da esfera: centro e raio completando quadrados, esfera com diâmetro AB, esfera concêntrica, esfera tangente a um plano e esfera com centro em x = y = z tangente a uma reta
assunto: ga-06-circunferencia-esfera
tipo: prova
questao: 1
semestre: 2016.2 e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | P2 Adventistas (14.10.2016), Q1; 4ª Avaliação (12.05.2017), Q1
fontes_catalogo: ufal-ga-provas-2016,ufal-ga-provas-2017
autoria: Enunciados: provas de Geometria Analítica do Instituto de Matemática da UFAL (ver fontes_catalogo), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

Forma reduzida: $(x-a)^2 + (y-b)^2 + (z-c)^2 = r^2$. Da forma geral, complete quadrados em cada variável.

**Como achar o centro e o raio de uma esfera:** complete quadrados. Exemplo: $x^2 + y^2 + z^2 - 4x - 6y - 10z + 13 = 0$.** $(x-2)^2 + (y-3)^2 + (z-5)^2 = 4 + 9 + 25 - 13 = 25$: centro (2, 3, 5), raio 5.

**Diâmetro de A(3, −1, 2) a B(1, 4, −3).** Centro no ponto médio $(2, \tfrac32, -\tfrac12)$; $r^2 = \tfrac{\|\overrightarrow{AB}\|^2}{4} = \tfrac{4 + 25 + 25}{4} = \tfrac{27}{2}$.

**Concêntrica com $x^2 + y^2 + z^2 + 4y = 3x$, por (1, 2, 3).** Centro $(\tfrac32, -2, 0)$; $r^2 = \tfrac14 + 16 + 9 = \tfrac{101}{4}$.

**Centro C(1, 0, 3), tangente a $2x + y - 2z + 1 = 0$.** O raio é a distância do centro ao plano: $\dfrac{|2 + 0 - 6 + 1|}{3} = 1$; $(x-1)^2 + y^2 + (z-3)^2 = 1$.

**Centro em $x = y = z$, tangente a $s: \tfrac x2 = \tfrac{y-1}{3} = \tfrac{z+1}{1}$ em P(0, 1, −1).** Centro (c, c, c). Na tangência, $\overrightarrow{PC}$ é perpendicular ao diretor (2, 3, 1) de s: $2c + 3(c - 1) + (c + 1) = 6c - 2 = 0$, $c = \tfrac13$. $r^2 = \tfrac19 + \tfrac49 + \tfrac{16}{9} = \tfrac73$.

**Verificação:** A e B estão a $\sqrt{27/2}$ do centro; (1, 2, 3) está a $\sqrt{101}/2$ de $(\tfrac32, -2, 0)$; $(\tfrac13, -\tfrac23, \tfrac43)\cdot(2, 3, 1) = 0$.
