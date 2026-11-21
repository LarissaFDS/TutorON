---
id: ga-vetores-angulo-norma
titulo: Ângulo entre combinações de vetores com normas e ângulo dados (u − 2v e u + v; 2u + v e u − 3v), norma de w = a₁u + b₁v e |u| = |v| quando u + v ⊥ u − v
assunto: ga-01-vetores-operacoes
tipo: prova
questao: 3; 4; 2
semestre: nao_informado
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Provas sem cabeçalho (fotos), Q4 e Q3; Final (14.11.2016), Q2
fontes_catalogo: ufal-ga-provas-sem-cabecalho,ufal-ga-provas-2016
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

Ferramentas: $\mathbf{u}\cdot\mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$ e $\|\mathbf{a}\|^2 = \mathbf{a}\cdot\mathbf{a}$. Expanda o produto escalar como um produto de binômios.

**Ângulo entre u − 2v e u + v**, com $\|\mathbf{u}\| = 1$, $\|\mathbf{v}\| = 3$ e ângulo de 60° entre eles: $\mathbf{u}\cdot\mathbf{v} = \tfrac32$.
- $(\mathbf{u}-2\mathbf{v})\cdot(\mathbf{u}+\mathbf{v}) = 1 - \tfrac32 - 18 = -\tfrac{37}{2}$.
- $\|\mathbf{u}-2\mathbf{v}\|^2 = 1 - 6 + 36 = 31$ e $\|\mathbf{u}+\mathbf{v}\|^2 = 1 + 3 + 9 = 13$.
- $\cos\theta = \dfrac{-37/2}{\sqrt{403}} \approx -0{,}9216$, então $\theta \approx 157{,}2°$.

**Ângulo entre 2u + v e u − 3v**, com $\|\mathbf{u}\| = 2$, $\|\mathbf{v}\| = 1$, 45°: $\mathbf{u}\cdot\mathbf{v} = \sqrt2$. Produto $8 - 5\sqrt2 - 3 = 5 - 5\sqrt2$; normas ao quadrado $17 + 4\sqrt2$ e $13 - 6\sqrt2$; $\cos\theta \approx -0{,}2048$, $\theta \approx 101{,}8°$.

**Final 2016, Q2.** u e v unitários e perpendiculares, $\mathbf{w} = a_1\mathbf{u} + b_1\mathbf{v}$, $\mathbf{z} = a_2\mathbf{u} + b_2\mathbf{v}$: $\|\mathbf{w}\| = \sqrt{a_1^2 + b_1^2}$, $\|\mathbf{z}\| = \sqrt{a_2^2 + b_2^2}$ e $\mathbf{w}\cdot\mathbf{z} = a_1a_2 + b_1b_2$, porque $\mathbf{u}\cdot\mathbf{u} = \mathbf{v}\cdot\mathbf{v} = 1$ e $\mathbf{u}\cdot\mathbf{v} = 0$.

**Se u + v é perpendicular a u − v, então |u| = |v|:** $0 = (\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v}) = \|\mathbf{u}\|^2 - \|\mathbf{v}\|^2$. As diagonais de um paralelogramo são perpendiculares só no losango.

**Verificação:** com u = (1, 0) e v = 3(cos 60°, sen 60°), o ângulo entre (1, 0) − 2v e (1, 0) + v calculado direto dá 157,2°; o mesmo teste dá 101,8° no segundo caso.
