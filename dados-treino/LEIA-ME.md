# dados-treino — entrada de dados novos para treinar o TutorON

Pasta só de organização. Nada aqui é usado pelo servidor nem pelo `3-Treinar.bat` ainda.

| Pasta | O que vai nela |
|---|---|
| `novos/` | Tudo que chegar, do jeito que chegou (PDF, JSONL, planilhas, conversas exportadas). Uma subpasta por disciplina ajuda (`novos/paa/`, `novos/calculo/`, `novos/geral/`). |
| `curados/` | O que passou pela curadoria (revisado, sem dado pessoal, formato JSONL de conversa). |
| `divisao/` | Saída da separação: `treino.jsonl` (70%) e `validacao.jsonl` (30%), separados por disciplina para cada uma ter a mesma proporção. |

Regras:
- Não colocar aqui os arquivos de `dados/` (votos e perguntas reais dos alunos): copie só as linhas escolhidas.
- Dados pessoais (nome, matrícula, e-mail) saem na curadoria antes de ir para `curados/`.
- O conteúdo das pastas não vai para o Git (só esta explicação).
