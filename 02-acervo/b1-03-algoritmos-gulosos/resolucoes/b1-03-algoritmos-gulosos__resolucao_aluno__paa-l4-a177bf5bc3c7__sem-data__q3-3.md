# a177bf5bc3c7-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 3

Versão derivada corrigida por agente; original SHA-256: aa1f6df1dc46221deb51a57b9ac91703dbfd15141a819c16026fbb38f302de62. Não é aprovação do professor.

Agendamento do maior número de intervalos compatíveis.
Para intervalos semiabertos [s_i,f_i), ordene por término crescente. Comece com ultimo_fim=-infinito. Para cada atividade nessa ordem, aceite-a se s_i>=ultimo_fim e atualize ultimo_fim=f_i. A convenção semiaberta permite uma atividade começar quando outra termina.
A escolha do menor término pode substituir a primeira atividade de uma solução ótima sem reduzir o espaço para as seguintes; repetindo o argumento, o algoritmo é ótimo. Custo O(n log n) para ordenar e O(n) para selecionar. Este pseudocódigo derivado substitui OCR de imagem; não é transcrição literal.
