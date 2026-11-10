---
id: calc3-nota-gradiente-derivada-direcional
titulo: Nota — derivada direcional e vetor gradiente: f = x²y em (1, 2) na direção (3, 4), taxa máxima
assunto: calc3-09-derivada-direcional-gradiente
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: ufal-calc3-ppc,openstax-calculus-vol3,mit-ocw-1802sc
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Derivada direcional e gradiente (Stewart, Clegg e Watson, *Cálculo*, vol. 2, 9ª ed., seção 14.6). A página "Derivadas direcionais e vetor gradiente" do Notion da turma está vazia; esta nota não tem material de aula como base. Conferida com SymPy.

Definições: o gradiente de f é o vetor das derivadas parciais, $\nabla f(x, y) = \langle f_x, f_y \rangle$. A derivada direcional na direção do vetor **unitário** $\mathbf{u}$ é o produto escalar $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$ (um número: a taxa de variação de f andando na direção u).

Exemplo: f(x, y) = x²y (ou $f = x^2 y$), no ponto (1, 2), na direção do vetor (3, 4).
1. Parciais: $f_x = 2xy$, $f_y = x^2$. No ponto: $\nabla f(1, 2) = \langle 4, 1 \rangle$.
2. Normalizar a direção: $\|\langle 3, 4 \rangle\| = 5$, então $\mathbf{u} = \langle 3/5, 4/5 \rangle$. Usar (3, 4) sem normalizar daria 16, cinco vezes maior: erro comum.
3. $D_{\mathbf{u}} f(1, 2) = 4 \cdot \tfrac35 + 1 \cdot \tfrac45 = \tfrac{16}{5} = 3{,}2$.

Taxa máxima: $D_{\mathbf{u}} f = \|\nabla f\|\cos\theta$, máxima quando u aponta como o gradiente. Em (1, 2), a taxa máxima é $\|\nabla f(1,2)\| = \sqrt{17} \approx 4{,}12$, na direção $\langle 4, 1 \rangle / \sqrt{17}$; a mínima é $-\sqrt{17}$, na direção oposta; é zero nas direções perpendiculares ao gradiente (tangentes à curva de nível $x^2y = 2$).

**Verificação:** pela definição, $\frac{d}{dh} f(1 + \tfrac35 h,\ 2 + \tfrac45 h)\big|_{h=0} = \frac{d}{dh}\left[(1 + 0{,}6h)^2 (2 + 0{,}8h)\right]_{h=0} = 2\cdot0{,}6\cdot2 + 0{,}8 = 3{,}2$.
