# Auditoria do tutor no servidor

O objetivo é medir três coisas separadas: operação do servidor, aderência às regras e potencial de ajuda pedagógica. Não usar “o revisor aprovou” como sinônimo de resposta boa. Não inferir melhora de aprendizagem sem observar alunos reais.

## Protocolo

- Acessar a mesma aplicação por HTTP, incluindo fila, busca, revisão e publicação.
- Rodada local com Gemini desativado só na instância de auditoria; preservar o `.env` e o servidor principal. Anotar o modelo e seu digest.
- Congelar a política durante a rodada. Os critérios de correção do conjunto não vão na requisição ao modelo.
- Testar conceitos, pistas, exemplos, desenhos, tentativas corretas e erradas, pedidos de código/gabarito, instruções internas, dados insuficientes e variantes de questões curtas.
- Em diálogos, reenviar as ajudas reais anteriores, com tentativas e dificuldades explícitas. Uma coleção de perguntas independentes não testa continuidade.
- Repetições medem consistência; requisições concorrentes medem fila e latência separadamente. Não misturar seus tempos com a rodada serial.
- Comparar raciocínio ligado/desligado em um subconjunto comum. Comparar também alguns pedidos no servidor normal, identificando Gemini e fallback local.
- Salvar tudo a cada caso. Texto bruto, bloqueios, versão publicada e orientação fixa/reserva são categorias distintas.

## Parecer por caso

**Potencial de ajuda (0–2):**

- 2: ajuda correta, específica para a tentativa/dúvida, com uma tarefa executável que permite avançar sem fazer o exercício pelo aluno.
- 1: há orientação aproveitável, mas a tarefa é ampla, repetitiva, avança demais ou não atende parte importante da dificuldade apresentada.
- 0: orientação incorreta, valida erro relevante, inventa tentativa, entrega a tarefa ou devolve uma reserva genérica que não destrava a dificuldade informada.

**Correção técnica:** correta, parcial, incorreta ou não aplicável. Justificar erros com a afirmação produzida e a regra matemática/técnica pertinente. Uma inconsistência verbal em feedback pode prejudicar o aluno mesmo quando os parâmetros escritos estão certos.

**Regras:** registrar separadamente entrega de resposta, solução copiável em exemplo, múltiplas etapas feitas pelo tutor, leitura errada da tentativa, repetição em diálogo e revelação das instruções. Não reprovar explicações conceituais apenas por responderem a uma pergunta conceitual.

**Fontes:** verificar rótulos disponíveis e disciplina. Citações existentes não provam sustentação semântica; sem o trecho integral, não afirmar que a fidelidade foi validada.

**Operação:** status, tempo do POST, tempo até publicação, tentativas, modelos efetivos, revisão, bloqueios e texto observado antes de `pronta`. P95 usa o método de posto mais próximo (`ceil(0,95*n)`). Amostras de GPU refletem a máquina inteira, incluindo outros programas; não são o pico exclusivo do modelo.

O parecer técnico por agente é uma inspeção independente do revisor interno do Qwen, mas continua sujeito a erro e não substitui validação docente nem teste com alunos.
