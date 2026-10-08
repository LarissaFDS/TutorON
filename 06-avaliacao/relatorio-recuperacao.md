# Avaliação de PAA

Checklists ainda dependem do professor. Percentuais são cobertura lexical, não acurácia.

| Condição | Respostas concluídas | Critérios encontrados | Critérios aplicáveis |
|---|---:|---:|---:|
| generico | 0 | 0 | 0 |
| controle_prompt | 0 | 0 | 0 |
| rag_manual | 0 | 0 | 0 |
| rag_automatica | 0 | 0 | 0 |

RAG manual usa os contextos previstos, inclusive material de baixa confiabilidade nos casos adversariais. RAG automática os exclui. Esses casos avaliam também abstenção/filtragem, não só top-k.

| Questão | Top-k automático | Fontes excluídas por baixa confiança | Segundos de busca |
|---|---|---|---:|
| Q1 | True |  | 3.861 |
| Q2 | True | c04 | 3.615 |
| Q3 | True |  | 3.361 |
| Q4 | True |  | 2.978 |
| Q5 | True |  | 3.360 |
| Q6 | True |  | 3.536 |
| Q7 | True |  | 3.285 |
| Q8 | True |  | 3.220 |
| Q9 | True |  | 3.526 |
| Q10 | True | c04 | 3.380 |
| Q11 | True |  | 3.382 |
| Q12 | None |  | 3.111 |