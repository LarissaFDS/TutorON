---
id: ga-esfera-plano-tangente
titulo: Plano tangente a uma esfera num ponto e circunferência de interseção entre esfera e plano (centro e raio)
assunto: ga-06-circunferencia-esfera
tipo: prova
questao: vários
semestre: 2016.2 e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | P2 (15.10.2016), Q1; Final (14.11.2016), Q5; Reavaliação AB2 (24.05.2017), Q3a; P2 Adventistas, Q4; Reposição 2, Q2a
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

**Plano tangente em P.** O raio $\overrightarrow{CP}$ é o vetor normal do plano: $\overrightarrow{CP}\cdot(X - P) = 0$. Antes, confira que P está na esfera.
- **P2 2016:** $x^2 + y^2 + z^2 + 4y = 3x$, centro $(\tfrac32, -2, 0)$, raio $\tfrac52$. P(1, 0, √2) está na esfera (1 + 2 = 3). Normal $(-\tfrac12, 2, \sqrt2)$; plano $-x + 4y + 2\sqrt2\,z = 3$.
- **Final 2016:** $x^2 + y^2 + z^2 - 2x = 3z$, centro $(1, 0, \tfrac32)$, raio $\tfrac{\sqrt{13}}{2}$. P(0, √2, 1) está na esfera. Normal $(-1, \sqrt2, -\tfrac12)$; plano $-2x + 2\sqrt2\,y - z = 3$.
- **Reavaliação AB2:** $(x-1)^2 + (y-2)^2 + (z+1)^2 = 4$, tangente em (1, 0, −1): normal (0, −2, 0), plano $y = 0$. O plano paralelo pelo centro é $y = 2$.

**Interseção com um plano.** Esfera de centro C e raio R, plano a distância $d < R$ de C: a circunferência tem raio $\sqrt{R^2 - d^2}$ e centro na projeção de C no plano.
- $(x-1)^2 + (y-2)^2 + (z+1)^2 = 4$ e $2x + y + 2z = 5$: $d = \dfrac{|2 + 2 - 2 - 5|}{3} = 1$; raio $\sqrt3$; centro $C - \dfrac{2 + 2 - 2 - 5}{9}(2, 1, 2) = (\tfrac53, \tfrac73, -\tfrac13)$.

**Verificação:** $(\tfrac53, \tfrac73, -\tfrac13)$ satisfaz $2x + y + 2z = 5$ e está a 1 de C; P(1, 0, √2) satisfaz $-1 + 0 + 4 = 3$; P(0, √2, 1) satisfaz $0 + 4 - 1 = 3$.
