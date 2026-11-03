# Diagnóstico do treino de 02/11/2026

**O treino terminou: 60 de 60 passos, 100%.** A falha aconteceu depois de salvar o ajuste, mesclar os pesos e instalar `tutoron-socratico-ft` no Ollama. Não é necessário repetir o treino para recuperar a avaliação.

## O que foi preservado

| Etapa da execução `20261102-153112-762218` | Evidência |
|---|---|
| Dados | 112 exemplos de treino, 28 de validação e 28 de teste, com cópia na pasta da execução. |
| Treino | Histórico até o passo 60, métricas finais e validação concluída. Duração registrada: 55,9 minutos. |
| Ajuste LoRA | `adapter/adapter_model.safetensors`, 87.360.584 bytes; todos os 504 tensores são finitos, e nenhuma matriz B de atualização permaneceu zerada. |
| Mescla, conversão e instalação | Modelo de aproximadamente 5,03 GB disponível no Ollama, instalado em 02/11/2026 às 16h38 (horário local). |
| Avaliação comparativa | A execução original parou no import. A recuperação concluiu 64/64 respostas, com saída normal do comando. |

O arquivo `resultado-treino.json` foi salvo às 16h27. O percentual de 100% se refere aos passos de otimização, não à qualidade pedagógica nem à conclusão das cinco etapas do atalho. A loss final de validação foi 1,538; esse número sozinho não comprova melhora do tutor.

Identificação do ajuste salvo (SHA-256): `7ca8ed1206f22bb3b6ce44b584f8a897fbc2005e6f713205873e90ef7e73c2e8`.

Identificação do candidato instalado no Ollama: `89bca9cd2ca3c9725ea693da7c917af39c12497775fc33e7e0b3154402ee53f2`.

## Causa e correção

O terminal mostrou `ModuleNotFoundError: No module named 'pydantic'` ao importar `eval.socratico`, por meio de `backend.tarefas` e `backend.animacao`. O ambiente `.venv-treino` também estava sem Pillow, necessário ao import de `backend.foto`. Essas dependências do fluxo de atendimento não estavam na receita de treino.

- Adicionadas Pydantic e Pillow às dependências do ambiente de treino e instaladas nesta máquina.
- O atalho agora verifica o import real da avaliação antes de iniciar um treino completo. O script Python também faz essa checagem quando chamado diretamente.
- Adicionado `--so-avaliar`, que usa o candidato instalado e não prepara dados, treina, mescla ou importa pesos. O atalho usa o ambiente do servidor nessa modalidade.
- As próximas execuções do atalho salvam a saída do terminal em `dados/logs/treino-*.log`, incluindo a saída do script Python.
- Se a avaliação falhar depois de um treino novo, o terminal informa explicitamente que o treino foi preservado e exibe o comando de recuperação.

## Como executar depois

Para recuperar apenas a avaliação de um modelo instalado:

```bat
3-Treinar.bat --so-avaliar
```

Para iniciar um treino novo, dar duplo clique em `3-Treinar.bat`. Isso repete os 60 passos; não é necessário para corrigir a falha de avaliação desta execução.

Nenhuma alteração foi feita no `.env`, no modelo configurado para atendimento ou no ajuste salvo. O candidato continua separado do modelo atual. A ativação depende de revisar as respostas da comparação.

## Verificação da correção

350 testes automatizados aprovados, um teste opcional de treino ignorado no ambiente do servidor. Os testes novos verificam detecção de dependência ausente antes de ocupar a GPU, recuperação sem repetir treino/mescla/importação, rejeição de opções incompatíveis e detecção de candidato ausente antes de gastar a bateria do modelo atual. O import da avaliação foi confirmado no próprio `.venv-treino`; também foi verificada a captura de saída Python no log do atalho.

A recuperação terminou com **64/64 tarefas prontas** e código de saída zero. [Comparação completa, com respostas brutas e publicadas](../05-modelo/socratico/preparado/avaliacao-socratica-20261102-172835.md); [dados exatos em JSON](../05-modelo/socratico/preparado/avaliacao-socratica-20261102-172835.json).

| Modelo | Respostas finais | Orientações de reserva | Mediana | Máximo |
|---|---:|---:|---:|---:|
| Atual (`tutoron-paa`) | 32 | 8 | 10,5 s | 21,7 s |
| Candidato (`tutoron-socratico-ft`) | 32 | 13 | 5,1 s | 430,8 s |

Uma das respostas de cada modelo é orientação fixa do código, sem geração pelo modelo. O fluxo usa o próprio modelo para revisar sua ajuda; os números de aprovação não são avaliação independente. A inspeção pedagógica completa desta nova comparação continua pendente. A mediana menor do candidato não compensa, por si só, a maior frequência de reservas ou a resposta repetitiva. Não há evidência suficiente para ativá-lo como melhoria.

## Limitação observada no candidato

No caso `paa-mestre-reservado/visual`, o candidato enumerou níveis da árvore de recursão de forma repetitiva até o limite de geração, em vez de fornecer um desenho curto. A primeira versão bruta tem 17.117 caracteres. O log do Ollama registrou uma revisão com 9.487 tokens excedendo o contexto disponível de 8.192, retornando HTTP 400. A reformulação também não foi aprovada; a ajuda final foi a reserva genérica após 430,8 segundos (cerca de 7 minutos).

Esse HTTP 400 é uma falha de revisão durante a recuperação, distinta do import ausente que encerrou a execução original. O atendimento contornou a falha com a reserva; isso não torna a resposta do candidato útil. A correção das dependências não valida a qualidade do modelo nem resolve a repetição ou o dimensionamento do contexto de revisão.
