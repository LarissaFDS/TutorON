---
id: ga-identificar-conicas
titulo: Como identificar uma cônica pela equação: completar quadrados (translação de eixos), sinais dos coeficientes e discriminante B² − 4AC; 4(y−2)² − x² + 2x − 4 = 0 e 2x² + y² − x + 4y + 1 = 0
assunto: ga-10-identificacao-conicas
tipo: prova
questao: 6; 4
semestre: 2016.2
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Final (14.11.2016), Q6; Reposição 2 (03.11.2016), Q4
fontes_catalogo: ufal-ga-provas-2016
autoria: Enunciado: Prof. Adelailson Peixoto (Instituto de Matemática, UFAL), nome impresso no cabeçalho da prova, parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

**Como identificar uma cônica pela equação.** Roteiro para identificar a cônica $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$:
1. Se $B \neq 0$, há rotação (veja o bloco de rotação). O sinal de $B^2 - 4AC$ indica o tipo: negativo, elipse; zero, parábola; positivo, hipérbole (ou casos degenerados).
2. Se $B = 0$, complete quadrados. É uma **translação**: com $X = x - h$ e $Y = y - k$, a equação fica na forma reduzida.
3. Mesmos sinais em $X^2$ e $Y^2$: elipse (ou ponto, ou vazio). Sinais opostos: hipérbole (ou par de retas). Um só quadrado: parábola.

**Final, 6a: $4(y-2)^2 - x^2 + 2x - 4 = 0$.** $-(x^2 - 2x) = -(x-1)^2 + 1$, então $4(y-2)^2 - (x-1)^2 = 3$, ou $\dfrac{(y-2)^2}{3/4} - \dfrac{(x-1)^2}{3} = 1$: **hipérbole** de eixo focal vertical, centro (1, 2), $c^2 = \tfrac{15}{4}$.

**Final, 6b: $2x^2 + y^2 - x + 4y + 1 = 0$.** $2(x - \tfrac14)^2 + (y + 2)^2 = \tfrac{25}{8}$: **elipse**, centro $(\tfrac14, -2)$, eixo maior vertical, $a^2 = \tfrac{25}{8}$, $b^2 = \tfrac{25}{16}$.

**Reposição 2, 4a: $4(y-2)^2 + x^2 + 2x - 4 = 0$.** $\dfrac{(x+1)^2}{5} + \dfrac{(y-2)^2}{5/4} = 1$: elipse de centro (−1, 2), eixo maior horizontal.

**Reposição 2, 4b: $2x^2 - y^2 - x + 4y + 1 = 0$** (o enunciado traz "4y.+1"; lemos 4y + 1). $2(x - \tfrac14)^2 - (y-2)^2 = -\tfrac{39}{8}$, ou $\dfrac{(y-2)^2}{39/8} - \dfrac{(x - 1/4)^2}{39/16} = 1$: hipérbole de eixo focal vertical.

**Verificação:** o vértice $(1, 2 + \tfrac{\sqrt3}{2})$ da 6a satisfaz a equação original ($3 - 1 + 2 - 4 = 0$); o vértice $(\tfrac14, -2 + \tfrac{5}{2\sqrt2})$ da 6b também.
