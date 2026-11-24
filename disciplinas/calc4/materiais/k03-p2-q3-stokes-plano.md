---
id: calc4-p2-q3-stokes-plano
titulo: P2 de Cálculo IV, Q3 — Stokes: a integral de z dx − 2x dy + 3y dz numa curva fechada do plano x + y + z = 1 só depende da área englobada
assunto: calc4-03-teoremas-stokes-divergencia
tipo: prova
questao: 3
resolucao: sim
fonte: Prova 2 de Cálculo IV (Instituto de Computação, UFAL; Prof. Gleydson Santos da Silva; arquivo P2C4.pdf), questão 3 | enunciado parafraseado
curso: Engenharia de Computação (UFAL), ECOM023 Cálculo 4, 4º período; semestre não identificado
fontes_catalogo: ufal-calc4-p2-gleydson
autoria: Enunciado: Prof. Gleydson Santos da Silva (IC-UFAL); resolução da equipe TutorON, conferida com SymPy
licenca: Não declarada (prova da disciplina); PDF não versionado
publicacao_transcricao: não autorizada; enunciado parafraseado
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Prova 2 de Cálculo IV (IC-UFAL, Prof. Gleydson Santos da Silva), questão 3, parafraseada. Status da resolução: pendente de confirmação do professor (a prova não traz gabarito; a resolução é da equipe TutorON e não é gabarito do professor). Prova é atividade avaliativa: o tutor guia, não entrega.

**Enunciado.** $C$ é uma curva fechada simples e suave no plano $x + y + z = 1$. Mostrar que $\oint_C z\,dx - 2x\,dy + 3y\,dz$ depende só da área da região englobada por $C$, não da forma nem da posição.

**Ideia: Stokes.** $\oint_C \mathbf F\cdot d\mathbf r = \iint_S (\nabla\times\mathbf F)\cdot\mathbf n\,dS$, com $S$ o pedaço do plano dentro de $C$ e $\mathbf F = (z, -2x, 3y)$.

**Rotacional.** $\nabla\times\mathbf F = \left(\frac{\partial(3y)}{\partial y} - \frac{\partial(-2x)}{\partial z},\ \frac{\partial z}{\partial z} - \frac{\partial(3y)}{\partial x},\ \frac{\partial(-2x)}{\partial x} - \frac{\partial z}{\partial y}\right) = (3, 1, -2)$, constante.

**Normal.** O plano tem normal unitária $\mathbf n = \frac{1}{\sqrt3}(1,1,1)$ (para cima, com $C$ no sentido anti-horário visto de cima). Então $(\nabla\times\mathbf F)\cdot\mathbf n = \frac{3 + 1 - 2}{\sqrt3} = \frac{2}{\sqrt3}$, constante, e
$$\oint_C \mathbf F\cdot d\mathbf r = \frac{2}{\sqrt3}\iint_S dS = \frac{2}{\sqrt3}\,A(S).$$
Só a área entra. Medindo pela projeção $D$ no plano $xy$ ($A(S) = \sqrt3\,A(D)$), a integral vale $2A(D)$. No sentido oposto, o sinal troca.

**Verificação:** `test_p2_q3_stokes_plano` confere o rotacional e, para círculos de raios e centros diferentes no plano, calcula a integral de linha direto e compara com $\frac{2}{\sqrt3}\pi\rho^2$.
