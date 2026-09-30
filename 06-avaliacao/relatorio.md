# Avaliação de PAA

Checklists ainda dependem do professor. Percentuais são cobertura lexical, não acurácia.

| Condição | Respostas concluídas | Critérios encontrados | Critérios aplicáveis |
|---|---:|---:|---:|
| generico | 12 | 23 | 46 |
| rag_manual | 12 | 33 | 47 |
| rag_automatica | 12 | 31 | 47 |

RAG manual usa os contextos previstos, inclusive material de baixa confiabilidade nos casos adversariais. RAG automática os exclui. Esses casos avaliam também abstenção/filtragem, não só top-k.

| Questão | Top-k automático | Fontes excluídas por baixa confiança | Segundos de busca |
|---|---|---|---:|
| Q1 | True |  | 3.547 |
| Q2 | True | c04, c06 | 3.047 |
| Q3 | True |  | 2.953 |
| Q4 | True | c09 | 3.157 |
| Q5 | False | a177bf5bc3c7-q1-1 | 3.000 |
| Q6 | False | 1a81ca283132-q4-4 | 2.969 |
| Q7 | False | 97254bb4a1b8-q1-1 | 2.718 |
| Q8 | False | 70d6475b28bf-q1-1 | 2.625 |
| Q9 | False | d455baef2cdf-q1-1 | 3.250 |
| Q10 | True | c04 | 3.125 |
| Q11 | True |  | 2.015 |
| Q12 | None |  | 0.156 |