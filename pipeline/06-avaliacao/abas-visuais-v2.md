# Abas de atendimento e aprendizado visual — 02/11/2026

## Comportamento atual

- **Tirar dúvida:** a seleção inicial é **O tutor escolhe**, inclusive em links antigos com `?visual=1` e ao voltar de um exemplo. O aluno pode mudar manualmente. Depois da resposta textual aparece **Quer entender visualmente?**; a pergunta, o contexto e a explicação acompanham o pedido de desenho na mesma conversa.
- **Aprender com desenhos:** voltou a ser uma aba separada, em `/visuais`. O formulário livre fica primeiro; aceita pergunta e contexto/código/tentativa sem escolher tema. A disciplina é identificada automaticamente quando possível e pode ser corrigida manualmente.
- **Recomendações opcionais:** os sete exemplos anteriores ficam na aba visual. Nenhum é selecionado inicialmente. O aluno pode abrir um exemplo ou copiar sua pergunta com **Usar como ponto de partida**, editar e enviar quando quiser. As recomendações saíram do formulário de Tirar dúvida.

## Verificação

Os testes de backend, acervo e avaliação totalizaram **390 aprovados e 1 ignorado**. Após o ajuste adicional das folhas de estilo, os 23 testes direcionados passaram. O JavaScript dos dois modos passou pela verificação de sintaxe.

No navegador, um link antigo com `?visual=1` abriu **O tutor escolhe**. Uma pergunta livre sobre clock/flip-flop gerou vídeo na aba visual sem selecionar tema recomendado. Abrir Karnaugh e copiar sua pergunta não enviou nada nem alterou as opções do tutor.

Os testes iniciais do convite após texto encontraram recusas do revisor por exigir conteúdo de uma lacuna intencional; uma outra proposta excedeu o tamanho de rótulo. As falhas foram preservadas. O critério de revisão foi esclarecido para não exigir que a lacuna responda à tarefa do aluno, mantendo a recusa de erro técnico e solução completa. Os 47 testes direcionados de revisão e visual passaram após esse ajuste. Evidências de interface e execuções reais ficam em `eval/results/abas-visuais-v2/`.

**Limitação observada:** repetir o convite de flip-flop após esse esclarecimento ainda resultou em recusa por incompletude, além de um rótulo extenso na primeira proposta. Portanto, não se considera resolvida a confiabilidade do revisor: houve sucesso da pergunta livre na aba separada e falhas no convite após texto nesta rodada. A pergunta e a explicação foram encaminhadas corretamente ao planejador, e a interface preservou o texto e permitiu tentar novamente. Não houve liberação forçada de roteiro reprovado.

Este ajuste não treina novos pesos nem garante desenho correto para todo assunto. Propostas que não passam pela validação continuam pedindo reformulação em vez de substituir a dúvida por tema de catálogo.
