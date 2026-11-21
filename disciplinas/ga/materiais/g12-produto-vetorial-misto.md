---
id: ga-produto-vetorial-misto
titulo: Para que servem o produto vetorial e o produto misto: área do paralelogramo, volume do paralelepípedo, pontos coplanares (valor de k), identidade de Lagrange ‖u × v‖² = ‖u‖²‖v‖² − (u·v)²
assunto: ga-02-produto-vetorial-misto
tipo: prova
questao: vários
semestre: 2016.2 e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | P2 Adventistas (14.10.2016), Q2 e Q3; Reposição 2 (03.11.2016), Q1a e Q1b; Reavaliação AB2 (24.05.2017), Q2a
fontes_catalogo: ufal-ga-provas-2016,ufal-ga-provas-2017
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

**Para que serve o produto misto, e o vetorial.** $\|\mathbf{u}\times\mathbf{v}\|$ é a área do paralelogramo de u e v, e $\mathbf{u}\times\mathbf{v}$ é normal aos dois. O **produto misto** $(\mathbf{u}, \mathbf{v}, \mathbf{w}) = (\mathbf{u}\times\mathbf{v})\cdot\mathbf{w}$ (determinante com u, v, w nas linhas) dá, em módulo, o volume do paralelepípedo; é zero quando os três vetores são coplanares.

$\mathbf{u}\times\mathbf{v} = (u_2v_3 - u_3v_2,\ -(u_1v_3 - u_3v_1),\ u_1v_2 - u_2v_1)$. Cuidado com o sinal da componente do meio.

**A(1, 2, 1), B(2, −1, 3), C(−3, 0, 3), D(4, 2, 2).** $\overrightarrow{AB} = (1,-3,2)$, $\overrightarrow{AC} = (-4,-2,2)$, $\overrightarrow{AD} = (3,0,1)$.
- $\overrightarrow{AB}\times\overrightarrow{AC} = (-2, -10, -14)$; área $\sqrt{300} = 10\sqrt3$.
- Produto misto: $(-2)(3) + 0 + (-14)(1) = -20$; volume 20.
(Na Reposição 2, A = (1, 2, 2) e B = (1, −1, 3): normal $(-1, -4, -12)$, área $\sqrt{161}$, volume 3.)

**Coplanares (Reavaliação AB2).** A(1,1,1), B(2,−1,3), C(3,1,k), D(3,2,1): $\det\begin{pmatrix}1 & -2 & 2\\ 2 & 0 & k-1\\ 2 & 1 & 0\end{pmatrix} = 9 - 5k = 0$, então $k = \tfrac95$.

**Identidade de Lagrange.** $\|\mathbf{u}\times\mathbf{v}\|^2 = \|\mathbf{u}\|^2\|\mathbf{v}\|^2\operatorname{sen}^2\theta = \|\mathbf{u}\|^2\|\mathbf{v}\|^2(1 - \cos^2\theta) = \|\mathbf{u}\|^2\|\mathbf{v}\|^2 - (\mathbf{u}\cdot\mathbf{v})^2$.

**Verificação:** $(-2,-10,-14)$ é ortogonal a $\overrightarrow{AB}$ ($-2 + 30 - 28 = 0$) e a $\overrightarrow{AC}$ ($8 + 20 - 28 = 0$); Lagrange: $14\cdot24 - 6^2 = 300$.
