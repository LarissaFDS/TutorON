---
id: calc1-derivacao-implicita
titulo: Reta tangente usando derivação implícita: x² + xy + y² = 3 em x = 1, tangentes paralelas de x² + xy + y² = 7 nos eixos, reta normal a x³y³ − 2xy = 6x + y + 1
assunto: calc1-05-regras-derivacao
tipo: prova
questao: vários
semestre: 2013–2015
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | resolução manuscrita da Prova 1 (17.06.2013), Q2a; 2ª Avaliação (04.10.2014), Q4b; Avaliação Final (03.12.2015), Q5b
fontes_catalogo: ufal-calc1-resolucoes-manuscritas,ufal-im-calc1-provas-fotos,ufal-im-calc1-provas-pdf
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

Como achar a reta tangente usando derivação implícita quando a curva não é gráfico de uma função explícita:

**Método.** Derive os dois lados em relação a x, tratando y como função de x: cada termo com y ganha um fator $y'$ (regra da cadeia), e $xy$ pede a regra do produto. Depois isole $y'$.

**$x^2 + xy + y^2 = 3$.** $2x + y + xy' + 2yy' = 0$, logo $y' = -\dfrac{2x+y}{x+2y}$. Em $x = 1$: $y^2 + y - 2 = 0$, $y = 1$ ou $y = -2$.
- (1, 1): $y' = -1$, tangente $y = -x + 2$.
- (1, −2): $y' = 0$, tangente $y = -2$.
A resolução manuscrita chega às mesmas retas.

**$x^2 + xy + y^2 = 7$ nos eixos.** Eixo x ($y = 0$): $x = \pm\sqrt7$, e $y' = -2$ nos dois pontos: tangentes paralelas. Eixo y ($x = 0$): $y = \pm\sqrt7$, $y' = -\tfrac12$ nos dois: também paralelas.

**Normal a $x^3y^3 - 2xy = 6x + y + 1$ em $x = 0$.** Com $x = 0$: $0 = y + 1$, $y = -1$. Derivando: $3x^2y^3 + 3x^3y^2y' - 2y - 2xy' = 6 + y'$. Em (0, −1): $2 = 6 + y'$, $y' = -4$. Normal (inclinação $-1/y' = \tfrac14$): $y = -1 + \tfrac{x}{4}$.

Erro comum: esquecer o $y'$ ao derivar $y^2$ ou $y^3$.

**Verificação:** (1, −2) satisfaz $1 - 2 + 4 = 3$; $\sqrt7^2 = 7$; com SymPy, `idiff` dá as mesmas inclinações.
