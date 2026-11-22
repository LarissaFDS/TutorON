---
id: ga-cc-conicas-provas-cc
titulo: Cônicas das provas de CC: parábola por foco e diretriz inclinada, elipse por focos e eixo maior, hipérbole completando quadrados, xy = 1 por rotação
assunto: ga-10-identificacao-conicas
tipo: prova
questao: Reavaliações AB1 (22 e 29.11.2017), Q4 e Q5; Provas finais (06.12.2017), Q3
semestre: 2017.1
resolucao: sim
fonte: Provas de Geometria Analítica 2017.1, IM-UFAL (turmas de Ciência da Computação) | Reavaliações AB1 (22 e 29.11.2017), Q4 e Q5; Provas finais (06.12.2017), Q3
curso: Ciência da Computação (UFAL), provas de 2017.1 aplicadas em novembro e dezembro de 2017
fontes_catalogo: ufal-cc-ga-provas-2017-2
autoria: Enunciados: provas de Geometria Analítica do Instituto de Matemática da UFAL, parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

**Parábola com foco F(1, 1) e diretriz pela reta por (0, −2) e (−2, 0).** A diretriz é $x+y+2=0$. Distância ao foco igual à distância à diretriz: $(x-1)^2+(y-1)^2=\dfrac{(x+y+2)^2}{2}$, que simplifica para $x^2-2xy+y^2-8x-8y=0$. O termo $xy$ aparece porque o eixo é inclinado.

**Elipse com focos (1, 1) e (1, −1) e eixo maior $4\sqrt2$:** centro (1, 0), eixo maior vertical, $a=2\sqrt2$, $c=1$, $b^2=a^2-c^2=7$: $\dfrac{(x-1)^2}{7}+\dfrac{y^2}{8}=1$. Com focos $(0,\pm1)$ e eixo maior 4: $a=2$, $b^2=3$, $\dfrac{x^2}{3}+\dfrac{y^2}{4}=1$.

**Hipérbole $x^2-9y^2=14-4x-18y$.** Complete quadrados: $(x+2)^2-9(y-1)^2=9$, isto é, $\dfrac{(x+2)^2}{9}-(y-1)^2=1$. Centro (−2, 1), $a=3$, $b=1$, $c=\sqrt{10}$. Vértices (1, 1) e (−5, 1); focos $(-2\pm\sqrt{10},\,1)$; assíntotas $y-1=\pm\tfrac13(x+2)$.

**xy = 1 sem termo misto.** Gire os eixos de 45°: $x=\tfrac{x_1-y_1}{\sqrt2}$, $y=\tfrac{x_1+y_1}{\sqrt2}$. Então $xy=\tfrac{x_1^2-y_1^2}{2}=1$: hipérbole equilátera com $a=b=\sqrt2$ no sistema novo, e assíntotas nos eixos x e y do sistema antigo.

Erro comum: na elipse, usar o eixo maior inteiro como a (a é a metade).

**Verificação:** as equações foram expandidas e comparadas com SymPy, e a soma das distâncias aos focos foi testada num vértice.
