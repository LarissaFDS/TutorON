---
id: ga-vetores-decomposicao-projecao
titulo: Como decompor um vetor em parte paralela e parte perpendicular a outro (projeção ortogonal): (7, −1) sobre (1, −1) e (5, −2) sobre (1, −3)
assunto: ga-01-vetores-operacoes
tipo: prova
questao: 1a, 1b; 4
semestre: 2016.2 e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Reavaliação AB1 (24.05.2017), Q1a e Q1b; Final (14.11.2016), Q4
fontes_catalogo: ufal-ga-provas-2017,ufal-ga-provas-2016
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

**Projeção ortogonal** de $\mathbf{w}$ sobre $\mathbf{u} \neq \mathbf{0}$ (a parte de w na direção de u): $P_{\mathbf{u}}\mathbf{w} = \dfrac{\mathbf{w}\cdot\mathbf{u}}{\|\mathbf{u}\|^2}\,\mathbf{u}$. Decomposição: $\mathbf{w} = P_{\mathbf{u}}\mathbf{w} + (\mathbf{w} - P_{\mathbf{u}}\mathbf{w})$; a primeira parcela é paralela a u, a segunda é perpendicular.

**Reavaliação AB1, Q1a.** Escrever (7, −1) como soma de um vetor paralelo e outro perpendicular a (1, −1).
- $\mathbf{w}\cdot\mathbf{u} = 7 + 1 = 8$ e $\|\mathbf{u}\|^2 = 2$: a parte paralela é $4(1,-1) = (4,-4)$.
- A parte perpendicular é $(7,-1) - (4,-4) = (3,3)$.

**Final 2016, Q4.** O mesmo com (5, −2) e (1, −3): $\mathbf{w}\cdot\mathbf{u} = 11$, $\|\mathbf{u}\|^2 = 10$; paralela $(\tfrac{11}{10}, -\tfrac{33}{10})$; perpendicular $(\tfrac{39}{10}, \tfrac{13}{10})$.

**Reavaliação AB1, Q1b (demonstração direta).** Para u e v não nulos, u é perpendicular a $\mathbf{v} - P_{\mathbf{u}}\mathbf{v}$: $\mathbf{u}\cdot(\mathbf{v} - P_{\mathbf{u}}\mathbf{v}) = \mathbf{u}\cdot\mathbf{v} - \dfrac{\mathbf{v}\cdot\mathbf{u}}{\|\mathbf{u}\|^2}(\mathbf{u}\cdot\mathbf{u}) = \mathbf{u}\cdot\mathbf{v} - \mathbf{v}\cdot\mathbf{u} = 0$, usando $\mathbf{u}\cdot\mathbf{u} = \|\mathbf{u}\|^2$.

**Verificação:** (4, −4) + (3, 3) = (7, −1) e (3, 3)·(1, −1) = 0; (11/10, −33/10) + (39/10, 13/10) = (5, −2) e (39/10)(1) + (13/10)(−3) = 0.
