---
id: ga-triangulo-angulos-area
titulo: Triângulo A(1, 1), B(4, 0), C(3, 4): ângulos internos pelo produto escalar, projeções dos lados AC e BC sobre AB, pé da altura e área
assunto: ga-01-vetores-operacoes
tipo: prova
questao: 2
semestre: nao_informado
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Prova sem cabeçalho (foto desfocada), Q2
fontes_catalogo: ufal-ga-provas-sem-cabecalho
autoria: Enunciado: autoria não identificada (foto de prova sem cabeçalho), parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Questão de prova (enunciado parafraseado). Status da resolução: pendente de confirmação do professor (a foto está desfocada; lemos C(3, 4), e a resolução da equipe TutorON, conferida com SymPy, vale para essa leitura).

Triângulo A(1, 1), B(4, 0), C(3, 4).

**a) Ângulos.** Em cada vértice, use os dois vetores que **saem** dele: $\cos\hat A = \dfrac{\overrightarrow{AB}\cdot\overrightarrow{AC}}{\|\overrightarrow{AB}\|\|\overrightarrow{AC}\|}$.
- A: $\overrightarrow{AB} = (3,-1)$, $\overrightarrow{AC} = (2,3)$, $\cos\hat A = 3/\sqrt{130}$, $\hat A \approx 74{,}7°$.
- B: $\overrightarrow{BA} = (-3,1)$, $\overrightarrow{BC} = (-1,4)$, $\cos\hat B = 7/\sqrt{170}$, $\hat B \approx 57{,}5°$.
- C: $\overrightarrow{CA} = (-2,-3)$, $\overrightarrow{CB} = (1,-4)$, $\cos\hat C = 10/\sqrt{221}$, $\hat C \approx 47{,}7°$.

**b) Projeções sobre AB** ($\|\overrightarrow{AB}\|^2 = 10$): a de $\overrightarrow{AC}$ é $\tfrac{3}{10}(3,-1)$; a de $\overrightarrow{BC}$ é $-\tfrac{7}{10}(3,-1)$ (o sinal negativo diz que aponta de B para A).

**c) Pé da altura relativa a C:** $H = A + \tfrac{3}{10}(3,-1) = (1{,}9;\ 0{,}7)$.

**d) Área:** $\tfrac12|3\cdot3 - (-1)\cdot2| = \tfrac{11}{2}$.

**Verificação:** os ângulos somam 180° (74,74 + 57,53 + 47,73); $\overrightarrow{HC} = (1{,}1;\ 3{,}3)$ é perpendicular a (3, −1); $\tfrac12\|\overrightarrow{AB}\|\,\|\overrightarrow{HC}\| = \tfrac12\sqrt{10}\sqrt{12{,}1} = 5{,}5$.
