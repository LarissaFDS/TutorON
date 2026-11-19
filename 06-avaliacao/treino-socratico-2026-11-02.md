# Tutor socrático e preparação do treino — 02/11/2026

O [PR #29](https://github.com/LarissaFDS/TutorON/pull/29), com tutor socrático, foto e Manim, foi mesclado em `dev`. Esta entrega troca o treinamento antigo de soluções completas por exemplos de orientação em PAA e Sistemas Digitais e reforça a publicação das ajudas. O treino completo ainda não foi executado nem ativado.

## O que já funciona

- Política socrática própria, com rigor por disciplina, sem herdar ordens para resolver todas as contas. Pede uma tarefa curta ao aluno, considera o histórico e restringe exemplos copiáveis e desenhos já preenchidos.
- A ajuda fica no servidor até ser revisada. Uma reprovação permite reformular; uma segunda reprovação ou falha de revisão devolve uma orientação de reserva. Isso vale também para o lado TutorON do A/B e para roteiros Manim antes do render.
- Perguntas de um bit sobre portas lógicas com entradas literais recebem uma orientação fixa, sem calcular a saída; as rodadas seguintes mudam a tarefa. Essa regra cobre a regressão encontrada, não todo exercício curto possível.
- Reserva de GPU entre processos durante treino e mescla, para o servidor não recarregar o modelo local. A trava é liberada pelo sistema operacional se o treino cair.

## Verificações

| Verificação | Resultado |
|---|---|
| Suíte do projeto | 343 testes passaram; 1 teste de treino é separado porque o ambiente do servidor não tem PyTorch. |
| Loss e gradientes | Teste com um Qwen3 pequeno confirmou equivalência entre a projeção só das respostas e o cálculo denso, inclusive padding e normalização. Passou no ambiente de treino. |
| Atalho Windows | `-Acao Treinar --so-dados` e `--verificar` executados com sucesso. |
| Dataset | 112 treino, 28 validação, 28 teste; 24 famílias, sem cruzar famílias entre splits e com PAA/SD equilibrados. Sem conversas de alunos. |
| Tokenização real | Todos os 168 exemplos cabem em 2048 tokens; máximo 1975. Não há corte silencioso das respostas. |
| GPU real | Um passo de otimização com os dois exemplos longos (um de cada disciplina), acumulação 2, learning rate 5e-5; grad norm 4,514; loss de validação 2,276. Pico de memória alocada: 7,08 GB na RTX 4060. Adapter de teste salvo, sem importar/ativar. |

A otimização da projeção reduziu o pico medido de 9,65 para 7,08 GB. Isso verifica viabilidade do processo, não melhora pedagógica. O treino padrão usa 60 passos e acumulação 4. [Métricas e configuração da execução](execucoes/treino-socratico-2026-11-02/resultado-treino.json).

## Respostas reais e falhas encontradas

A [bateria completa de 32 casos](../eval/results/socratico-completo-20261102.md) usou `tutoron-paa` com o RAG local real, sem Gemini nem Supabase. Incluiu quatro famílias reservadas, sete formas de ajuda, histórico real das ajudas anteriores e quatro pedidos adversariais. Não é avaliação de um modelo novo com pesos adaptados.

Nessa rodada, houve 32 respostas publicadas, 10 primeiras versões reprovadas e 8 orientações de reserva. O revisor aprovou 24 publicações, mas **aprovação não significa correção**: uma delas revelou o bit pedido numa questão de AND, sob a forma de regra geral. A inspeção por agente encontrou também feedback errado ao aluno que trocou os parâmetros do Mestre, exemplo com recorrência de troco copiável e inconsistências em índices da árvore. O revisor não detectou todos esses problemas.

Depois dessa rodada:

- A pergunta de um bit foi tratada por regra de código e ganhou testes para AND, OR, XOR, NAND, NOR, XNOR e NOT e para o A/B.
- Exemplos passaram a pedir apenas um passo parcial e desenhos passaram a pedir campos em branco. O revisor recebeu os critérios de copiabilidade e de questões cuja explicação já determina o resultado.
- A [rodada de regressão de quatro casos](../eval/results/socratico-regressoes-20261102.md) publicou duas ajudas aprovadas, uma reserva e uma orientação fixa. A questão AND não chamou modelo nem revelou a saída. O exemplo de troco deixou a fórmula para o aluno; a subtração deixou os resultados em branco. A árvore que avançou demais foi bloqueada.

A revisão técnica acima foi feita por agente, não por docente. Ainda há imprecisões técnicas em respostas aprovadas: por exemplo, a convenção dos índices de carry na ajuda de subtração não foi definida. O revisor é o próprio modelo e pode errar, rejeitar uma ajuda válida ou aceitar conteúdo indevido. Portanto, esta entrega estabelece a versão inicial e o processo de melhoria; não comprova ausência de vazamento nem ganho de aprendizagem.

## Treinar quando quiser

Dê duplo clique em **`3-Treinar.bat`**. Ele prepara os dados, treina, mescla, converte e instala o candidato como `tutoron-socratico-ft`, depois avalia atual e candidato pelo fluxo do site. Mescla e conversão reaproveitam o pipeline anterior; não foram repetidas com o adapter de teste desta entrega. Nada troca o modelo ativo automaticamente.

Veja [COMO_TREINAR.md](../05-modelo/COMO_TREINAR.md). Os dados são sintéticos e pequenos, com revisão docente pendente. O relatório deve ser lido antes de ativar o candidato. O teste direto no Ollama usa somente o prompt; a barreira de revisão pertence ao servidor.
