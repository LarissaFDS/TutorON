# Comparação do modelo treinado — decisão de implantação

**Decisão: manter `tutoron-paa` no servidor. O candidato `tutoron-socratico-ft` não demonstrou melhora.**

Foram geradas 24 ajudas novas: 12 situações para cada modelo, no mesmo fluxo local de busca, revisão e publicação. Raciocínio desligado, temperatura 0,2, antes das alterações de limite de saída desta entrega. Os critérios foram definidos antes da geração em [CRITERIOS_PROMOCAO.md](../eval/CRITERIOS_PROMOCAO.md).

| Medida na rodada nova | Atual | Treinado |
|---|---:|---:|
| Tarefas concluídas | 12/12 | 12/12 |
| Erros técnicos claros nas publicadas | 3 | 5 |
| Ajuda adequada para um próximo passo (nota 2) | 2 | 1 |
| Orientações genéricas de reserva | 2 | 2 |
| Mediana | 9.1 s | 5.7 s |

O candidato teve 0 pares com potencial de ajuda maior e 5 menor. Não foram observadas entregas do resultado solicitado nas 24 ajudas desta rodada; isso não demonstra cumprimento universal das regras.

**O atual também erra.** Manter o atual evita promover uma regressão; não o torna validado para aprendizagem. Os pareceres foram escritos pelo agente em inspeção técnica, sem cegamento, docente ou alunos. A nota 0–2 descreve potencial de ajuda neste caso, não ganho medido de aprendizagem.

A rodada anterior tinha 32 respostas por modelo. O atual precisou de 8 reservas e chegou a 21,7 s; o treinado precisou de 13 reservas e chegou a 430,8 s num caso repetitivo. [Relatório dessa execução](diagnostico-treino-2026-11-02.md).

## Exemplos que impedem a promoção

- Mestre: o candidato confirma parâmetros trocados e usa a base errada no logaritmo.
- Reduções: aceita a direção que não prova a dificuldade do problema novo.
- Karnaugh: confirma 01 e 10 como vizinhos e confunde zero obrigatório com irrelevância.
- NP-dificuldade: transfere dificuldade na direção errada de uma redução.

## Evidências e próxima avaliação

[Respostas completas](../eval/results/promocao-20261102/comparacao.md), [textos e tempos exatos](../eval/results/promocao-20261102/comparacao.json), [pareceres por caso](../eval/results/promocao-20261102/pareceres.json), [decisão calculada a partir dos pareceres](../eval/results/promocao-20261102/decisao.json).

Para uma revisão docente independente, estão prontos [12 pares com lados embaralhados](../eval/results/promocao-20261102/pares-cegos.md). A chave está em arquivo separado. O docente pode marcar correção, entrega indevida e utilidade, sem saber qual modelo produziu cada lado. Depois, testar tarefas equivalentes com alunos e medir se conseguem dar o próximo passo; preferência por texto mais curto não basta.

Esta bateria permanece fora do treino. Nenhum novo fine-tuning ou troca do `.env` ocorreu nesta comparação. As novas proteções limitam a saída sem raciocínio e recusam candidatas extensas para revisão, sem aprovar só um prefixo. Um novo ensaio do caso visual terminou em 6,6 s sem repetir o problema, mas uma repetição isolada não demonstra causalmente a eliminação de repetições.
