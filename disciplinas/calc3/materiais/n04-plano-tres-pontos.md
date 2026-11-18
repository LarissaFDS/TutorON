---
id: calc3-nota-plano-tres-pontos
titulo: Nota — equação do plano por três pontos com o produto vetorial: (1,0,0), (0,2,0), (0,0,3)
assunto: calc3-03-vetores-retas-planos
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: ufal-calc3-notion-anotacoes,openstax-calculus-vol3,mit-ocw-1802sc
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Plano por três pontos não colineares (Stewart, Clegg e Watson, *Cálculo*, vol. 2, 9ª ed., seções 12.4 e 12.5). Pré-requisito de Cálculo 3 (vetores e geometria analítica no espaço). Conferido com SymPy.

Método: dois vetores no plano, $\overrightarrow{PQ}$ e $\overrightarrow{PR}$; o vetor normal é o produto vetorial $\mathbf{n} = \overrightarrow{PQ} \times \overrightarrow{PR}$; a equação é $a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$ com $\mathbf{n} = \langle a, b, c \rangle$ e $P = (x_0, y_0, z_0)$.

Exemplo: P = (1, 0, 0), Q = (0, 2, 0), R = (0, 0, 3).
1. $\overrightarrow{PQ} = \langle -1, 2, 0 \rangle$, $\overrightarrow{PR} = \langle -1, 0, 3 \rangle$.
2. Produto vetorial (determinante com i, j, k):
$\mathbf{n} = \langle 2\cdot3 - 0\cdot0,\ -[(-1)\cdot3 - 0\cdot(-1)],\ (-1)\cdot0 - 2\cdot(-1) \rangle = \langle 6, 3, 2 \rangle$.
3. Plano: $6(x - 1) + 3y + 2z = 0$, ou seja, $6x + 3y + 2z = 6$ (forma segmentária: $\tfrac{x}{1} + \tfrac{y}{2} + \tfrac{z}{3} = 1$, cortando os eixos nos três pontos dados).

Se o produto vetorial der o vetor nulo, os três pontos são colineares e não determinam um único plano.

**Verificação:** Q dá $0 + 6 + 0 = 6$ ✔ e R dá $0 + 0 + 6 = 6$ ✔; e $\mathbf{n} \cdot \overrightarrow{PQ} = -6 + 6 + 0 = 0$, $\mathbf{n} \cdot \overrightarrow{PR} = -6 + 0 + 6 = 0$.
