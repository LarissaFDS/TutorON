---
id: calc3-nota-curvatura-exemplo
titulo: Nota — curvatura de r(t) = (t, t², t³) em t = 0 pela fórmula do produto vetorial; T, N e B no ponto
assunto: calc3-06-curvatura-movimento
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: ufal-calc3-notion-anotacoes,openstax-calculus-vol3
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Exemplo resolvido de curvatura de uma curva no espaço (Stewart, Clegg e Watson, *Cálculo*, vol. 2, 9ª ed., seção 13.3). Conferido com SymPy.

Curva: a cúbica torcida $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ (ou, em texto, r(t) = (t, t^2, t^3)). Fórmula da curvatura, a norma do produto vetorial de r' e r'' sobre a norma de r' ao cubo:
$$\kappa(t) = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}.$$

1. Derivadas: $\mathbf{r}'(t) = \langle 1, 2t, 3t^2 \rangle$, $\mathbf{r}''(t) = \langle 0, 2, 6t \rangle$.
2. Produto vetorial (atenção ao sinal da componente j):
$\mathbf{r}' \times \mathbf{r}'' = \langle 2t\cdot 6t - 3t^2 \cdot 2,\ -(1\cdot 6t - 3t^2\cdot 0),\ 1\cdot 2 - 2t \cdot 0 \rangle = \langle 6t^2, -6t, 2 \rangle$.
3. Normas: $\|\mathbf{r}' \times \mathbf{r}''\| = \sqrt{36t^4 + 36t^2 + 4}$; $\|\mathbf{r}'\| = \sqrt{1 + 4t^2 + 9t^4}$.
4. Fórmula geral: $\kappa(t) = \dfrac{2\sqrt{9t^4 + 9t^2 + 1}}{(1 + 4t^2 + 9t^4)^{3/2}}$.
5. Em t = 0: $\mathbf{r}'(0) = \langle 1, 0, 0 \rangle$, $\mathbf{r}''(0) = \langle 0, 2, 0 \rangle$, produto $\langle 0, 0, 2 \rangle$, então $\kappa(0) = 2/1^3 = 2$ (raio de curvatura 1/2).

Triedro na origem: $\mathbf{T}(0) = \langle 1, 0, 0 \rangle$; como $\mathbf{r}''(0)$ é perpendicular a $\mathbf{r}'(0)$, $\mathbf{N}(0) = \langle 0, 1, 0 \rangle$; $\mathbf{B}(0) = \mathbf{T} \times \mathbf{N} = \langle 0, 0, 1 \rangle$. O plano osculador em t = 0 é z = 0.

**Verificação:** perto de t = 0 a curva é quase a parábola $y = x^2$ no plano z = 0, cuja curvatura no vértice é $|f''|/(1 + 0)^{3/2} = 2$, o mesmo valor.
