# TutorON — resumo para apresentação

## 1. O que treinamos

Partimos de um modelo pronto, **Qwen3 de 8 bilhões de parâmetros**, e fizemos um ajuste para ele orientar o aluno com pistas, conceitos e perguntas, deixando a resolução para o estudante. A RTX 4060 executou **60 de 60 passos**, em aproximadamente **56 minutos**. O ajuste foi salvo e instalado como candidato separado.

## 2. Quais dados entraram

O treino usa **exemplos sintéticos autorais de PAA e Sistemas Digitais**, em `05-modelo/socratico/casos.json`, com auxílio de IA e revisão docente pendente. Os PDFs e gabaritos da curadoria entram na **busca de material durante o atendimento (RAG)**; não foram usados diretamente como respostas-alvo deste ajuste.

| Separação | Exemplos | Papel |
|---|---:|---|
| Treinamento | 112 | Ajustar os pesos para produzir orientação |
| Validação | 28 | Acompanhar a perda durante o ajuste |
| Teste reservado | 28 | Avaliar depois, sem entrar no ajuste dos pesos |

Cada conjunto tem metade PAA e metade SD. São **24 situações-base com sete formas de ajuda**, e não 168 exercícios independentes: 16 situações-base ficam no treino, quatro na validação e quatro no teste. As variações de uma mesma situação ficam juntas, evitando treinar uma versão e testar sua paráfrase. O teste de atendimento acrescenta quatro ataques/perguntas especiais, totalizando 32 casos por modelo.

## 3. Como sabemos se melhorou

Comparamos os dois modelos nas mesmas perguntas, com o mesmo material, e olhamos quatro coisas: **conteúdo correto, respeito à tentativa, próximo passo útil e ausência de resposta pronta**. Tempo e falhas também contam. O próprio modelo aprovar sua resposta não basta.

Na comparação nova, com **12 situações por modelo**, o candidato teve **5 respostas com erros técnicos claros**, contra **3 do atual**, segundo inspeção técnica do agente. A mediana caiu de **9,1 para 5,7 segundos**, mas isso não compensou a qualidade. Na comparação anterior, ele precisou de mais orientações de reserva e teve um caso repetitivo de cerca de sete minutos.

**Decisão: o modelo novo não foi ativado.** O atual também apresenta erros; ainda não houve validação docente nem medição de aprendizagem com alunos. Estão preparados 12 pares com lados embaralhados para uma revisão independente. [Comparação e evidências](comparacao-modelo-2026-11-02.md).

## 4. O que o Manim acrescenta

Uma área funcional, **Aprender com desenhos**, mostra sete exemplos: robô e DP, fluxo residual, Karnaugh, circuito e tabela-verdade, BFS, certificado em grafos e direção de reduções. Os desenhos deixam cálculos, grupos, saídas e decisões para o aluno. Depois do vídeo, ele escreve sua tentativa e a leva ao tutor.

Os exemplos do catálogo são preparados sem depender de cotas de IA. A animação personalizada da dúvida continua experimental; quando falha e existe correspondência de tema, é oferecido um exemplo relacionado, identificado como outro exercício. [Como demonstrar](../docs/VISUAIS.md).

## 5. Precisamos de mais dados?

**Precisamos de mais situações independentes e revisadas, principalmente erros reais de raciocínio e continuidade da conversa.** Repetir mais vezes os mesmos 112 exemplos não garante corrigir os problemas. Como próximo lote de trabalho, proponho 100–200 situações novas revisadas pelo docente; é uma meta prática do projeto, não um número que assegura qualidade.

Prioridades: direção das reduções, NP-difícil versus NP-completo, predecessores e obstáculos em DP, atualização da mochila 0/1, leitura de fluxo/capacidade, ordem Gray e zeros versus irrelevâncias. Incluir aluno sem pré-requisito, tentativa parcialmente correta e progresso depois de uma pista.

Cada exemplo precisa de **enunciado + tentativa do aluno + primeiro erro ou acerto + pista curta correta + tarefa “Sua vez” + referência de origem**. Para desenhos, incluir um roteiro parcial válido. O gabarito pode ajudar o revisor a conferir a pista, mas não deve virar o texto que o tutor aprende a entregar. Guardar versões e fontes e separar as famílias antes de criar variações. Esta bateria de comparação fica fora do treino.

## Onde buscar material

1. **A própria curadoria e o docente:** melhor alinhamento com a forma de cobrar da disciplina. Transformar exercícios e erros comuns em interações de orientação; revisar antes de acrescentar ao dataset.
2. **MIT OpenCourseWare:** [6.006 — algoritmos](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) e [6.004 — sistemas digitais](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/) têm materiais e exercícios para elaborar novas situações. Conferir as condições de reutilização de cada material; não importar soluções como alvos do tutor.
3. **[MathDial, dos autores da ETH Zurich](https://github.com/eth-nlped/mathdial):** diálogos de tutoria matemática para estudar como dar pistas e reagir a tentativas. Exige adaptação de idioma e domínio para PAA/SD, revisão de qualidade e conferência da licença da versão usada. Não é um dataset pronto para estas disciplinas.

## Fala de aproximadamente um minuto

> “O TutorON usa material curado para buscar contexto e foi ajustado com exemplos de como orientar. Separamos 112 exemplos para treino, 28 para validação e 28 para teste, sem misturar variações de um mesmo problema. O treino terminou, mas o candidato ainda errou conceitos importantes; por isso, mantivemos o modelo atual. Agora também temos desenhos animados de programação dinâmica, grafos e circuitos que mostram as relações e deixam uma etapa para o aluno completar. O próximo avanço exige mais exemplos revisados e avaliação com docente e alunos, além de medir velocidade.”
