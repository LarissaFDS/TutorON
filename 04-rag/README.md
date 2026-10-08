# Busca local

`python -m acervo indexar --embeddings` constrói o índice a partir do manifesto atual de `02-acervo/itens.json`. Não percorre arquivos antigos de versões anteriores do acervo.

Uma questão e sua resolução ficam no mesmo bloco quando a segmentação encontra a continuidade no documento. Fontes distintas só se juntam se houver vínculo explícito; não inferimos que duas variantes de algoritmo tenham a mesma resposta.

A busca usa BM25 simplificado sobre palavras normalizadas e bônus de correspondência para ASTERISCO, Algoritmo X e COMPOSTO. Com `bge-m3` disponível, combina ranking lexical e similaridade de embeddings por reciprocal rank fusion. Aplica preferência moderada a alta/média confiança. Retorna até quatro fontes relevantes (não preenche o resultado com fontes sem evidência lexical ou semântica mínima).

Para evitar limites de tokenização de OCR ruidoso, representa o texto completo por janelas de até 1.000 caracteres e agrega seus embeddings com média ponderada normalizada. Isso não altera o chunk: a unidade recuperada continua sendo a questão inteira. Nenhum trecho é truncado silenciosamente.

Qualidade baixa, documentos ilegíveis, classificação incerta e segmentação pendente ficam fora. O estado de confiança é conferido de novo na consulta para que um rebaixamento retire imediatamente um item. Fontes parciais e não verificadas permanecem identificadas no contexto; a revisão humana continua necessária.

Contextos que não cabem no orçamento de caracteres são omitidos integralmente, sem cortar fórmulas ou código pela metade. A avaliação registra apenas os IDs efetivamente enviados ao modelo. `indice.json` informa se a construção usou embeddings ou degradou para busca lexical.
