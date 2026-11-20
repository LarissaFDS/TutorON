# Avaliação de PAA

Checklists ainda dependem do professor. Percentuais são cobertura lexical, não acurácia.

| Condição | Respostas concluídas | Critérios encontrados | Critérios aplicáveis |
|---|---:|---:|---:|
| generico | 12 | 17 | 46 |
| controle_prompt | 12 | 16 | 47 |
| rag_manual | 12 | 30 | 47 |
| rag_automatica | 12 | 29 | 47 |

RAG manual usa os contextos previstos, inclusive material de baixa confiabilidade nos casos adversariais. RAG automática os exclui. Esses casos avaliam também abstenção/filtragem, não só top-k.

| Questão | Top-k automático | Fontes excluídas por baixa confiança | Segundos de busca |
|---|---|---|---:|
| Q1 | True |  | 3.569 |
| Q2 | True | c04 | 3.419 |
| Q3 | True |  | 3.199 |
| Q4 | True |  | 2.921 |
| Q5 | True |  | 3.134 |
| Q6 | True |  | 3.332 |
| Q7 | True |  | 3.087 |
| Q8 | True |  | 3.346 |
| Q9 | True |  | 3.085 |
| Q10 | True | c04 | 3.119 |
| Q11 | True |  | 3.152 |
| Q12 | None |  | 2.968 |