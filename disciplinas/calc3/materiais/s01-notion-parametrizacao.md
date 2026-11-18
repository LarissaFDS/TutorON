---
id: calc3-notion-parametrizacao
titulo: Anotações da turma (Notion) — parametrização: eliminar o parâmetro, velocidade inicial e altura máxima
assunto: calc3-01-curvas-parametricas
tipo: material_estudo
resolucao: sim
fonte: Notion da turma, página "Parametrização" (texto; imagens não lidas)
autoria: Alunos da turma de Cálculo 3 (UFAL); revisão da equipe TutorON
licenca: Não declarada (anotações de alunos no Notion da turma); imagens não estão no repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações
fontes_catalogo: ufal-calc3-notion-anotacoes
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Anotações dos alunos sobre parametrização, resumidas. Status da resolução: corrigida (um passo de álgebra e duas frases reescritos; ver "Correções").

Ideia central: para achar a equação cartesiana, isole t numa das equações e substitua na outra (ou use uma identidade, como $\operatorname{sen}^2 t + \cos^2 t = 1$). O vetor velocidade é $\langle x'(t), y'(t) \rangle$.

Exemplo das anotações: $x = 2t + 2$, $y = t + 1$. Isolando t: $t = \dfrac{x - 2}{2}$, logo $y = \dfrac{x - 2}{2} + 1 = \dfrac{x}{2}$, uma reta pela origem com inclinação 1/2.

Correções:
1. As anotações isolaram $t = \dfrac{-x + 2}{2}$; o certo é $t = \dfrac{x - 2}{2}$ (de $x = 2t + 2$ vem $2t = x - 2$). Com o sinal errado, a reta sairia com inclinação −1/2.
2. "Velocidade = x′ em t = 0" vale só para a **velocidade inicial**; em geral o vetor velocidade é $\langle x'(t), y'(t) \rangle$ e a velocidade escalar é $\sqrt{x'^2 + y'^2}$.
3. "m = 0 → altura máxima": a inclinação zero ($dy/dx = 0$, ou seja $y' = 0$ com $x' \ne 0$) marca uma tangente horizontal. Ela é altura máxima numa trajetória de projétil (concavidade para baixo), mas pode ser mínimo ou nenhum dos dois em outras curvas; confira com $d^2y/dx^2$ ou com o sinal de y′.

**Verificação:** em t = 0, (x, y) = (2, 1) e 1 = 2/2 ✔; em t = 1, (4, 2) e 2 = 4/2 ✔.
