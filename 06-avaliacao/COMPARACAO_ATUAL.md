# Comparação local atual

Mesmos pesos Qwen2.5 3B, temperatura 0,2, seed 42, contexto de 4096 tokens. Todos recebem a mesma orientação de até 220 palavras. TutorON adiciona contexto acadêmico curado. O controle usa as mesmas instruções sem dados. Nenhum fine-tuning foi executado.

| Condição | Respostas | Checklist comum | Tempo médio (s) | Com citação de ID válida | IDs inválidos |
|---|---:|---:|---:|---:|---:|---:|
| generico | 12 | 17/46 | 40.8 | 0 | 0 |
| controle_prompt | 12 | 16/46 | 46.9 | 0 | 0 |
| rag_manual | 12 | 30/46 | 66.0 | 0 | 0 |
| rag_automatica | 12 | 29/46 | 109.9 | 0 | 0 |

A métrica de citações verifica somente IDs explícitos do acervo. Marcadores como [1] não são fontes verificadas. Ausência de IDs inválidos não demonstra fundamentação.

## Comparação por questão (mesmos critérios aplicáveis)

| Questão | Genérico | Controle | Manual | Automática | Total |
|---|---:|---:|---:|---:|---:|
| Q1 | 0 | 1 | 2 | 2 | 7 |
| Q2 | 0 | 0 | 3 | 4 | 6 |
| Q3 | 0 | 0 | 2 | 2 | 4 |
| Q4 | 3 | 3 | 4 | 5 | 5 |
| Q5 | 1 | 1 | 2 | 1 | 3 |
| Q6 | 2 | 2 | 2 | 3 | 4 |
| Q7 | 2 | 2 | 3 | 1 | 3 |
| Q8 | 4 | 3 | 4 | 4 | 4 |
| Q9 | 1 | 0 | 3 | 1 | 3 |
| Q10 | 0 | 0 | 0 | 1 | 2 |
| Q11 | 2 | 2 | 3 | 3 | 3 |
| Q12 | 2 | 2 | 2 | 2 | 2 |

## Revisão matemática por agente

Somente pareceres vinculados ao hash exato da resposta são contabilizados. Não são votos humanos nem avaliação independente.

| Condição | Adequadas | Parciais | Erro material | Pendentes |
|---|---:|---:|---:|---:|
| generico | 1 | 1 | 10 | 0 |
| controle_prompt | 0 | 0 | 12 | 0 |
| rag_manual | 0 | 2 | 10 | 0 |
| rag_automatica | 2 | 1 | 9 | 0 |

## Limites da conclusão

- Cobertura lexical não é acurácia.
- Questões incluem variantes da mesma família.
- Uma semente na rodada principal; sem inferência estatística de superioridade.
- Material no RAG é permitido no protocolo aberto; não é teste de conhecimento memorizado.
- Revisão técnica por agente e validação cega com alunos/professor são evidências separadas.

Respostas integrais, fontes, hashes e latência: resultados.json. Avaliação por agente: revisao-tecnica.json. Votos humanos reais são coletados em http://127.0.0.1:8765; nenhum voto é fabricado.
