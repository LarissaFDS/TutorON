---
id: calc3-ab1-2024-q3-cardioide
titulo: AB1 2024.1, Q3 — cardioide r = 1 + sen θ: inclinação da tangente em θ = π/3 e pontos de tangente horizontal
assunto: calc3-02-coordenadas-polares
tipo: prova
questao: 3
semestre: 2024.1
resolucao: sim
fonte: Prova.jpg (página do Notion "Cálculo 3", seção Provas antigas) | AB1 de 23/08/2024
autoria: Enunciado: Prof. Tiago Alves de Almeida (ECOM017 Cálculo 3, IC/UFAL, AB1 2024.1), parafraseado pela equipe TutorON; resolução da equipe TutorON
licenca: Não declarada (material de turma); a foto não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
fontes_catalogo: ufal-calc3-provas-2024-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
AB1 de Cálculo 3 (2024.1), Questão 3. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (sem gabarito no material; resolução da equipe TutorON, conferida com SymPy). A prova traz a figura da cardioide (simétrica em relação ao eixo y, ponta na origem, topo em (0, 2)) e um apêndice com $1 - \operatorname{sen}\theta - 2\operatorname{sen}^2\theta = (1 + \operatorname{sen}\theta)(1 - 2\operatorname{sen}\theta)$.

Método (tangente em polares): com $x = r\cos\theta$, $y = r\operatorname{sen}\theta$,
$$\frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta} = \frac{r'\operatorname{sen}\theta + r\cos\theta}{r'\cos\theta - r\operatorname{sen}\theta}.$$
Para $r = 1 + \operatorname{sen}\theta$, $r' = \cos\theta$:
- $dy/d\theta = \cos\theta(1 + 2\operatorname{sen}\theta)$
- $dx/d\theta = \cos^2\theta - \operatorname{sen}\theta - \operatorname{sen}^2\theta = (1 + \operatorname{sen}\theta)(1 - 2\operatorname{sen}\theta)$

a) Em $\theta = \pi/3$: $dy/d\theta = \tfrac12(1 + \sqrt3)$ e $dx/d\theta = (1 + \tfrac{\sqrt3}{2})(1 - \sqrt3) = -\tfrac12(1 + \sqrt3)$. Coeficiente angular: $dy/dx = -1$.

b) Tangente horizontal: $dy/d\theta = 0$ com $dx/d\theta \neq 0$, para $0 \le \theta \le 2\pi$.
- $\cos\theta = 0$: $\theta = \pi/2$ dá $r = 2$, ponto (0, 2), com $dx/d\theta = -2 \ne 0$ ✔. $\theta = 3\pi/2$ dá $r = 0$ (origem), mas ali $dx/d\theta = 0$ também: é a ponta (cúspide) da cardioide, onde a tangente é vertical, não horizontal.
- $\operatorname{sen}\theta = -\tfrac12$: $\theta = 7\pi/6$ e $11\pi/6$, $r = \tfrac12$, pontos $(-\tfrac{\sqrt3}{4}, -\tfrac14)$ e $(\tfrac{\sqrt3}{4}, -\tfrac14)$, com $dx/d\theta = 1 \ne 0$ ✔.

Resposta: (0, 2), $(\pm\tfrac{\sqrt3}{4}, -\tfrac14)$.

**Verificação:** os dois pontos com $y = -1/4$ são simétricos, como a figura; e $(\sqrt3/4)^2 + (1/4)^2 = 1/4 = r^2$.
