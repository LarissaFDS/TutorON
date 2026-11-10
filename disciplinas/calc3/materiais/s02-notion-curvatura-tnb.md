---
id: calc3-notion-curvatura-tnb
titulo: Anotações da turma (Notion) — curvatura, vetores tangente, normal e binormal (T, N, B)
assunto: calc3-06-curvatura-movimento
tipo: material_estudo
resolucao: nao
fonte: Notion da turma, páginas "Integrais/comprimento de arco", "Curvatura e movimento" e "Vetor unitário e planos" (texto; imagens não lidas)
autoria: Alunos da turma de Cálculo 3 (UFAL); revisão da equipe TutorON
licenca: Não declarada (anotações de alunos no Notion da turma); imagens não estão no repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações
fontes_catalogo: ufal-calc3-notion-anotacoes
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
Anotações dos alunos sobre curvatura e triedro T, N, B, resumidas. Status da resolução: corrigida (três fórmulas reescritas; ver "Correções").

Para uma curva lisa ($\mathbf{r}'(t) \neq \mathbf{0}$):
- Vetor tangente unitário: $\mathbf{T}(t) = \dfrac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$.
- Curvatura (quão rápido T muda de direção por unidade de comprimento): $\kappa = \left\|\dfrac{d\mathbf{T}}{ds}\right\| = \dfrac{\|\mathbf{T}'(t)\|}{\|\mathbf{r}'(t)\|} = \dfrac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}$.
- Curva plana $y = f(x)$: $\kappa(x) = \dfrac{|f''(x)|}{[1 + f'(x)^2]^{3/2}}$.
- Vetor normal unitário: $\mathbf{N}(t) = \dfrac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}$ (aponta para o lado em que a curva se dobra).
- Vetor binormal: $\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)$, perpendicular a T e N.
- Plano normal (contém N e B, normal T) e plano osculador (contém T e N, normal B) passam pelo ponto; a equação de um plano por $P_0 = (x_0, y_0, z_0)$ com vetor normal $\langle a, b, c \rangle$ é $a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$.

Correções:
1. As anotações escreviam $\kappa(t) = \left\|\mathbf{T}'(t)/\mathbf{r}'(t)\right\|$, dividindo por um vetor; o certo é o quociente das **normas**, $\|\mathbf{T}'(t)\| / \|\mathbf{r}'(t)\|$.
2. A fórmula para a curva plana estava sem o módulo em $f''$; sem ele, a curvatura sairia negativa onde a concavidade é para baixo. Curvatura é sempre $\ge 0$.
3. "$\mathbf{T}(t) = \|\mathbf{T}'\|\mathbf{N}$" deveria ser $\mathbf{T}'(t) = \|\mathbf{T}'(t)\|\,\mathbf{N}(t)$ (é a derivada de T que aponta na direção de N).

**Verificação:** a circunferência de raio a, $\langle a\cos t, a\operatorname{sen} t \rangle$, tem $\|\mathbf{T}'\| = 1$ e $\|\mathbf{r}'\| = a$, então $\kappa = 1/a$ (constante, maior para círculos menores).
