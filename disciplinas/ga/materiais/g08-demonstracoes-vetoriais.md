---
id: ga-demonstracoes-vetoriais
titulo: Demonstrações com vetores: diagonais do paralelogramo se cortam ao meio, base média do trapézio, triângulo inscrito na semicircunferência é retângulo, diagonais do quadrado são perpendiculares
assunto: ga-13-demonstracoes-vetoriais
tipo: prova
questao: 1a, 2a
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 1ª Avaliação (10.02.2017), Q1a e Q2a; 1ª Avaliação (11.02.2017), Q1a e Q2a
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
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; identidades conferidas com SymPy). Técnica: escreva tudo com dois vetores independentes e compare coeficientes.

**Diagonais do paralelogramo ABCD se cortam ao meio.** $\mathbf{a} = \overrightarrow{AB}$, $\mathbf{b} = \overrightarrow{AD}$. Um ponto de AC é $A + s(\mathbf{a}+\mathbf{b})$; um de BD é $A + \mathbf{a} + t(\mathbf{b} - \mathbf{a})$. Igualando e comparando coeficientes: $s = 1 - t$ (de a) e $s = t$ (de b), logo $s = t = \tfrac12$: o encontro é o ponto médio das duas.

**Base média do trapézio.** ABCD com $\overrightarrow{DC} = \lambda\overrightarrow{AB}$, λ > 0. M e N, pontos médios de AD e BC: $\overrightarrow{MN} = \tfrac12(\overrightarrow{AB} + \overrightarrow{DC}) = \tfrac{1+\lambda}{2}\overrightarrow{AB}$. É paralelo às bases e mede $\tfrac{|AB| + |DC|}{2}$.

**Triângulo inscrito na semicircunferência.** Centro O, diâmetro AB, P na circunferência: $\overrightarrow{OA} = -\overrightarrow{OB}$ e $\|\overrightarrow{OP}\| = \|\overrightarrow{OB}\|$. $\overrightarrow{PA}\cdot\overrightarrow{PB} = (-\overrightarrow{OB} - \overrightarrow{OP})\cdot(\overrightarrow{OB} - \overrightarrow{OP}) = \|\overrightarrow{OP}\|^2 - \|\overrightarrow{OB}\|^2 = 0$: ângulo reto em P.

**Diagonais do quadrado.** $\|\mathbf{a}\| = \|\mathbf{b}\|$: $(\mathbf{a}+\mathbf{b})\cdot(\mathbf{b}-\mathbf{a}) = \|\mathbf{b}\|^2 - \|\mathbf{a}\|^2 = 0$. Basta lados iguais (losango).

Exemplos numéricos ilustram, mas não provam: a prova usa vetores genéricos.

**Verificação:** com A(0,0), B(4,0), D(1,3), C(5,3), os pontos médios de AC e de BD são ambos (2,5; 1,5); no quadrado de lado 1, (1, 1)·(−1, 1) = 0.
