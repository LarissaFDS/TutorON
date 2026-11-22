# Relatório da fila: Ciência da Computação, parte 2 (22/11/2026)

| # | Disciplina | id | PR | Merge dev / main | Situação final | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|---|---|
| 1 | Sistemas Operacionais | `so` | #124 | dev: sim; main: não (ver abaixo) | complemento (MVP, sem mudança) | 0: material idêntico ao de Engenharia | pytest 1672 ok, 8 pulados; relevância 489/489; ruff ok | nenhuma nova |
| 2 | Teoria da Computação | `lfa` | #125 | dev: sim; main: não (ver abaixo) | complemento (MVP, sem mudança) | 3 (`t01`–`t03`) | pytest 1680 ok, 8 pulados; relevância 493/493; ruff ok | ementa de CC (CCOM015, 30 h) é só a parte de computabilidade; problema de Post sem bloco |
| 3 | Metodologia | `metodologia` | sem PR | — | complemento (sem mudança) | 0: os três arquivos da pasta de CC já estão no catálogo | — | nenhuma |
| 4 | Teoria dos Grafos | `grafos` | #128 | dev: sim; main: não (ver abaixo) | **em validação** (disciplina nova) | 14 (`g01`–`g14`) | pytest 1714 ok, 8 pulados; relevância 500/500; ruff ok; bateria real 5 perguntas | resposta de planaridade caiu na ajuda de reserva (não conferida); hipergrafos e matróides sem material; questão 4.4 (mapa do Brasil) sem resolução; POSCOMP não conferido |
| 5 | Projeto de Software (Programação 2) | `projsw` | #129 | dev: sim; main: não (ver abaixo) | **em validação** (disciplina nova) | 12 (`p01`–`p12`), 1 corrigida | pytest 1725 ok, 30 pulados (Docker desligado nesta rodada); relevância 507/507; ruff ok; bateria real 5 perguntas | recursividade sem bloco; sobrecarga de operadores e templates (C++) sem material; resposta fora do assunto não indicou a outra disciplina; sem ligação em `cursos.json` (ver abaixo); ECOM015 (Engenharia) não ligada |
| 6 | Redes de Computadores | `redes` | (esta PR) | — | **em validação** (disciplina nova) | 12 (`r01`–`r12`) | pytest 1759 ok, 30 pulados (Docker desligado); relevância 520/520; ruff ok; bateria real 5 perguntas (Gemini principal em 429, respondeu o flash-lite) | revisão humana pendente; questões do projeto de implementação sem bloco; Redes 2 (CCOM039) sem material; resposta fora do assunto citou Cálculo 2 em vez de Cálculo 3; ECOM029 (Engenharia) não ligada |

## Aguardando decisão
- **PR dev → main não aberta:** o comando `gh pr create --base main --head dev` foi recusado pela permissão automática desta sessão. `dev` tem as PRs da fila; abra a PR para `main` ou libere o comando.
- Projeto de Software: ligar `"acervo": "projsw"` à Programação 2 de CC em `disciplinas/cursos.json` exige pôr `projsw` nas preferidas do 4º período de CC em `backend/tests/test_versao_final.py` (hoje `{paa, lfa}`). Não mexi nesse teste; a decisão é sua.
- Grafos: ECOM033 (Teoria dos Grafos de Engenharia) não foi ligada ao acervo `grafos`, porque a ementa de Engenharia não foi conferida.
- Grafos: promover a MVP depende de rodar de novo a pergunta de planaridade e de decidir sobre hipergrafos e matróides (sem material da turma).
- O site não foi atualizado: não há acesso ao PC do servidor.

- Redes: ECOM029 (Engenharia) não ligada.
