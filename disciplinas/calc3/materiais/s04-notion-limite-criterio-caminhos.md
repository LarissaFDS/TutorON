---
id: calc3-notion-limite-criterio-caminhos
titulo: Anotações da turma (Notion) — limite em duas variáveis: definição e critério dos dois caminhos
assunto: calc3-08-limites-derivadas-parciais
tipo: material_estudo
resolucao: nao
fonte: Notion da turma, página "Limite e derivadas parciais" (texto; as seções de continuidade e de derivadas parciais estão vazias)
autoria: Alunos da turma de Cálculo 3 (UFAL); revisão da equipe TutorON
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações
fontes_catalogo: ufal-calc3-notion-anotacoes
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Anotações dos alunos sobre limites de funções de duas variáveis, resumidas. Status da resolução: validada. As seções de continuidade e de derivadas parciais da página estão vazias.

Definição: $\lim_{(x,y)\to(a,b)} f(x, y) = L$ significa que $f(x, y)$ fica tão perto de L quanto se queira para todo (x, y) do domínio suficientemente perto de (a, b), **por qualquer direção ou caminho** (formalmente: para todo ε > 0 existe δ > 0 tal que $0 < \sqrt{(x-a)^2 + (y-b)^2} < \delta$ implica $|f(x,y) - L| < \varepsilon$).

Critério dos dois caminhos: se $f \to L_1$ ao longo de um caminho $C_1$ e $f \to L_2$ ao longo de $C_2$, com $L_1 \neq L_2$, o limite **não existe**.

Exemplo: $f = \dfrac{x^2 - y^2}{x^2 + y^2}$ em (0, 0): no eixo x vale 1, no eixo y vale −1, então não há limite.

Cuidado: caminhos iguais não provam existência. Para provar que existe, use continuidade (polinômios e quocientes com denominador não nulo são contínuos), o Teorema do Confronto ou coordenadas polares com uma cota que não dependa do ângulo. Exemplos resolvidos: AB2 Q1 e reavaliação Q1 de 2024.1 e a lista de limites da turma.

**Verificação:** no exemplo, ao longo de y = x a função vale 0, um terceiro valor, coerente com a não existência.
