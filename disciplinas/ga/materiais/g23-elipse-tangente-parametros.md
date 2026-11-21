---
id: ga-elipse-tangente-parametros
titulo: Elipse: valor de k para a reta 2x/9 + ky/4 = 1 ser tangente a x²/9 + y²/4 = 1; focos, vértices e eixo maior de 9x² − 18x + 4y² + 8y − 23 = 0
assunto: ga-08-elipse
tipo: prova
questao: 3a, 3b
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 2ª Avaliação (11.03.2017), Q3
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

**a) Tangente.** A reta tangente a $\tfrac{x^2}{9} + \tfrac{y^2}{4} = 1$ no ponto $(x_0, y_0)$ é $\tfrac{x_0 x}{9} + \tfrac{y_0 y}{4} = 1$. Comparando com $\tfrac{2x}{9} + \tfrac{ky}{4} = 1$: $x_0 = 2$ e $y_0 = k$. O ponto precisa estar na elipse: $\tfrac49 + \tfrac{k^2}{4} = 1$, $k^2 = \tfrac{20}{9}$, $k = \pm\tfrac{2\sqrt5}{3}$.
Outro caminho: substituir a reta na elipse e exigir discriminante zero (um só ponto comum).

**b) $9x^2 - 18x + 4y^2 + 8y - 23 = 0$.** Completando quadrados: $9(x-1)^2 - 9 + 4(y+1)^2 - 4 = 23$, ou seja, $9(x-1)^2 + 4(y+1)^2 = 36$, e na forma reduzida $\dfrac{(x-1)^2}{4} + \dfrac{(y+1)^2}{9} = 1$.
- Centro (1, −1). O maior denominador está em y: eixo maior vertical, $a = 3$, $b = 2$, $c = \sqrt{9 - 4} = \sqrt5$.
- Vértices do eixo maior (1, 2) e (1, −4); do menor (3, −1) e (−1, −1).
- Focos $(1, -1 \pm \sqrt5)$; eixo maior $2a = 6$.

**Verificação:** com $k = \tfrac{2\sqrt5}{3}$, substituir a reta na elipse dá discriminante 0; o vértice (1, 2) satisfaz $9 - 18 + 16 + 16 - 23 = 0$; a soma das distâncias de (3, −1) aos focos é $2\sqrt{4 + 5} = 6$.
