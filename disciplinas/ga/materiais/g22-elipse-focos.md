---
id: ga-elipse-focos
titulo: Elipse pelos focos e eixo maior: focos (1, 1) e (1, −1) com eixo 4√2, focos (0, a) e (0, b) com vértice na origem, focos (−3, 0) e (0, 4) com eixo maior 7 (elipse inclinada)
assunto: ga-08-elipse
tipo: prova
questao: 3a, 3b; 3b
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 2ª Avaliação (10.03.2017), Q3; Reavaliação AB1 (24.05.2017), Q3b
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

**Definição:** $d(P, F_1) + d(P, F_2) = 2a$ (eixo maior). Centro = ponto médio dos focos; $2c$ = distância entre os focos; $b^2 = a^2 - c^2$. Exige $2a > 2c$.

**Focos (1, 1) e (1, −1), eixo maior $4\sqrt2$.** Centro (1, 0), $c = 1$, $a = 2\sqrt2$, $b^2 = 8 - 1 = 7$. Eixo focal vertical: $\dfrac{(x-1)^2}{7} + \dfrac{y^2}{8} = 1$.

**Focos F(0, a) e F₁(0, b), b > a > 0, um vértice na origem.** Eixo focal: o eixo y. Centro $(0, \tfrac{a+b}{2})$, $c = \tfrac{b-a}{2}$. A origem está no eixo focal, a $\tfrac{a+b}{2}$ do centro: esse é o semieixo maior. Semieixo menor ao quadrado: $\left(\tfrac{a+b}{2}\right)^2 - \left(\tfrac{b-a}{2}\right)^2 = ab$. Equação: $\dfrac{x^2}{ab} + \dfrac{\left(y - \frac{a+b}{2}\right)^2}{\left(\frac{a+b}{2}\right)^2} = 1$.

**Focos (−3, 0) e (0, 4), eixo maior 7.** $2c = 5 < 7$; $a = \tfrac72$, $b^2 = \tfrac{49 - 25}{4} = 6$. O eixo focal é inclinado, então partimos da definição: $\sqrt{(x+3)^2 + y^2} + \sqrt{x^2 + (y-4)^2} = 7$. Isolando uma raiz e elevando ao quadrado duas vezes: $40x^2 - 24xy + 33y^2 + 168x - 168y = 0$.

**Verificação:** a origem está na última elipse (3 + 4 = 7), coerente com o termo independente 0; no vértice (1, 2√2) da primeira, as distâncias aos focos são $2\sqrt2 - 1$ e $2\sqrt2 + 1$, que somam $4\sqrt2$.
