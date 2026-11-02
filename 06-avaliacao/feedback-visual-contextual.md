# Ajustes após o teste da interface — 02/11/2026

## O que mudou

- A introdução “Fase MVP” e a aba de temas visuais fixos saíram da interface principal.
- Depois de uma ajuda textual aparece **Quer entender visualmente?**. O vídeo entra na mesma conversa.
- **Só animação** permite começar pelo desenho, sem gerar uma explicação textual antes.
- **Identificar automaticamente** virou o padrão da disciplina. O aluno ainda pode corrigir manualmente.
- Foto conferida e código/tentativa continuam disponíveis e acompanham o pedido visual.

## Como funciona agora

O tutor planeja um desenho a partir da dúvida enviada. Para uma pergunta conceitual sem números, pode montar blocos e relações com uma parte para o aluno completar. Para problemas com dados, os formatos de grafo, grade, tabela e circuito continuam disponíveis. Não há troca automática por um vídeo de catálogo quando o planejamento falha.

A escolha automática usa sinais de vocabulário para distinguir PAA e Sistemas Digitais. Perguntas vagas ou ambíguas pedem esclarecimento ou seleção manual. Isso ainda não reconhece qualquer disciplina ou garante uma animação correta para qualquer assunto.

## O que foi verificado

| Verificação | Resultado |
| --- | --- |
| Testes automatizados completos | 390 passaram; 1 ignorado |
| Três perguntas conceituais no modelo local: robô/DP, recursão/pilha e registrador de estado | 3 vídeos gerados, aproximadamente 10–11 s cada, sem seleção de tema |
| Navegador, servidor principal: robô com obstáculo, **Só animação** | Vídeo na conversa; disciplina PAA identificada automaticamente |
| Navegador, servidor auxiliar com a mesma implementação: clock de flip-flop D | Texto, botão e vídeo na conversa; SD identificada automaticamente |
| Tentativas iniciais rejeitadas | Preservadas; incluem duas falhas de visual após uma ajuda textual de DP com contexto inadequado |
| Cache da interface | JavaScript versionado e revalidação dos arquivos principais para evitar interface antiga após atualização |

Os quadros dos três vídeos conceituais foram inspecionados quanto a legibilidade, relações e lacunas. Essa amostra verifica o funcionamento e revela limitações; não demonstra melhora de aprendizagem nem precisão em todos os assuntos. O modelo textual também pode errar, e a revisão visual não é infalível. Na segunda tentativa, o planejador pode se apoiar novamente no enunciado sem copiar uma ajuda anterior incorreta; a revisão continua vendo o contexto completo.

As evidências estão em `eval/results/visual-contextual-v1/`: execuções iniciais e finais, bloqueios, roteiros, quadros e capturas da interface. Para repetir os três casos locais: `.venv\Scripts\python eval/testar_visual_contextual.py --saida eval/results/visual-contextual-v1/repeticao.json`.

## Modelo e treinamento

Este ajuste não treinou nem promoveu novos pesos. O servidor continua com o modelo atual. A comparação anterior que recusou a promoção do candidato continua válida e separada deste teste de interface e animação.
