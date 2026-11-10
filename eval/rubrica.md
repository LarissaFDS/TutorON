# Rubrica do juiz (nota de 1 a 5 por critério)

Cada critério nasce de um comentário do aluno de Engenharia de Computação (5º período) que comparou o TutorON com uma IA genérica às cegas. O juiz recebe a pergunta, a resposta de referência (gabarito curto) e UMA resposta, sem saber de que sistema ela veio.

| Critério | Pergunta que o juiz responde | Comentário do aluno que o originou |
|---|---|---|
| **a. Recorrência antes do código** | O subproblema (o que cada posição da tabela/variável guarda) e a recorrência completa, com casos base, aparecem ANTES de qualquer código ou pseudocódigo? | "faltou mostrar a recorrência antes do código"; "recorrência bem montada" |
| **b. Pseudocódigo claro** | Há pseudocódigo legível, independente de linguagem (não Python/C, salvo pedido), que dá para seguir à mão? | "prefere pseudocódigo a linguagem específica"; "faltou código" |
| **c. Significado dos índices** | A resposta diz o que cada índice representa e por que aparecem i-1, j-1, w-w_i etc. (qual vizinho/subproblema cada um é)? | "não entendeu i-1 e j-1" |
| **d. Organização** | A ordem é didática (ideia → definição → recorrência → algoritmo → exemplo → complexidade), sem repetições, seções vazias ou blocos genéricos? | "organização confusa" |
| **e. Correção matemática** | Recorrência, casos base, contas, exemplo e complexidade estão certos, de acordo com a referência? | notas baixas de confiança |
| **f. Obedece pedidos de formato** | Se o aluno pediu um formato ("esqueminha", "passo a passo", "mais fácil", "tabela"), ele foi entregue? | logs: "faça um esqueminha" ignorado |

## Escala

- **5**: exemplar; o aluno estudaria por esta resposta.
- **4**: bom, com um deslize pequeno.
- **3**: aceitável, mas falta uma parte relevante do critério.
- **2**: fraco; a parte existe só de forma vaga ou fora de ordem.
- **1**: ausente ou errado.

## Quando um critério não se aplica

A aplicabilidade é fixa por tema (definida em `matriz.py`, `CRITERIOS_POR_TEMA`), igual para todos os braços da mesma pergunta, para que a comparação seja justa:

| Tema | Critérios |
|---|---|
| PD, divisão e conquista | a, b, c, d, e |
| Recorrências, análise de laços | a, c, d, e |
| Guloso, NP | d, e |
| Qualquer pergunta com pedido de formato | + f |

A nota de uma resposta é a média dos critérios aplicáveis. As três perguntas originais do aluno também são reportadas critério a critério.

## Riscos conhecidos do juiz

- O juiz é um modelo Gemini, da mesma família dos modelos avaliados. Pode favorecer o estilo do próprio modelo. Mitigação: gabarito explícito, temperatura 0, saída em JSON com justificativa curta por critério, e conferência humana das três perguntas originais.
- Uma nota por resposta (sem repetição) tem ruído. A diferença entre braços só é tratada como real quando aparece de forma consistente nas perguntas, não por uma média isolada.
