---
id: calc3-resumo-comprimento-de-arco
titulo: Resumo de aula — comprimento de arco de curvas paramétricas, distância percorrida, velocidade escalar e área de superfície de revolução
assunto: calc3-05-comprimento-de-arco
tipo: material_estudo
resolucao: nao
fonte: "Resumo 2" (página do Notion "Cálculo 3"; manuscrito escaneado)
autoria: Resumo manuscrito anexado ao Notion da turma com o rótulo "Resumo do professor" (autoria não confirmada); paráfrase da equipe TutorON
licenca: Não declarada (material de turma); o arquivo não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco resume com texto próprio
fontes_catalogo: ufal-calc3-notion-resumos
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Resumo de aula sobre comprimento de arco no plano, parafraseado (rótulo "Resumo do professor" no Notion; autoria não confirmada). Status da resolução: validada (fórmulas e exemplos conferidos com SymPy).

Comprimento de arco de uma curva $x = x(t)$, $y = y(t)$, $\alpha \le t \le \beta$, percorrida **uma vez** e com $x'$, $y'$ contínuas:
$$L = \int_\alpha^\beta \sqrt{x'(t)^2 + y'(t)^2}\;dt$$
(a integral da raiz da soma dos quadrados das derivadas).

Distância percorrida × deslocamento: se a partícula passa mais de uma vez pelo mesmo trecho, a mesma integral dá a **distância percorrida**, maior que o comprimento da curva. O deslocamento é só a diferença entre posição final e inicial.

Função comprimento de arco: $s(t) = \int_\alpha^t \sqrt{x'(u)^2 + y'(u)^2}\,du$; a velocidade escalar é $\dfrac{ds}{dt} = \sqrt{x'(t)^2 + y'(t)^2}$.

Área da superfície gerada girando a curva em torno do eixo x ($y \ge 0$):
$$S = 2\pi \int_\alpha^\beta y(t)\,\sqrt{x'(t)^2 + y'(t)^2}\;dt$$
(em torno do eixo y, troque $y(t)$ por $x(t)$).

**Verificação:** para a circunferência $x = \cos t$, $y = \operatorname{sen} t$, $0 \le t \le 2\pi$, $L = \int_0^{2\pi} 1\,dt = 2\pi$; para a semicircunferência ($0 \le t \le \pi$) girada em torno do eixo x, $S = 2\pi\int_0^\pi \operatorname{sen}t\,dt = 4\pi$, a área da esfera de raio 1.
