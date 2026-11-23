# Relatório: Engenharia de Computação, 2º período (23/11/2026)

Material bruto `2º_periodo.zip`, extraído fora do repositório. Decisão da equipe para este lote: disciplina criada entra
como `MVP`, sem aviso. Liberar não é revisar: nenhum bloco está marcado com `revisao_humana: feita` nem
`revisao_professor: sim`, e nenhuma nota escrita por IA entrou na busca.

| # | Item | PR | Merge dev / main | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|
| 1 | Lógica (`logica`) | [#161](https://github.com/LarissaFDS/TutorON/pull/161) | dev: sim; main: ver PR dev→main | 3 (`logica-evandro-2024-*`) | pytest 2251 ok, ruff ok; relevância 650/650 | revisão humana e do professor dos 3 blocos |
| 2 | Programação 1 (`prog1`) | ver seção | dev: ver seção; main: ver PR dev→main | 2 (`prog1-ec2-*`) | pytest 2255 ok, ruff ok; relevância 653/653 | revisão humana dos 2 blocos |

## Item 1: Lógica (`logica`, complemento)

- **Novo:** Lista 1 (imagens) e questões da prova 1 (fotos) do Prof. Evandro Costa, 2024.1: técnico culpado,
  governo/desemprego/inflação (duas versões com respostas diferentes) e valoração/classificação de fórmulas.
- **Já coberto:** slides "Lógica Proposicional (Parte 1)" de 2024.1 e a tabela de equivalências.
- **Só evidência:** `teste.py`, `logica (1).cv` e o artigo científico em inglês (de terceiros), fora do repositório.
- **Dados pessoais:** as fotos da prova têm respostas manuscritas de um aluno, que não foram usadas.

## Item 2: Programação 1 (`prog1`, complemento)

- **Novo:** ordenação de vetor (trocas e bolha com parada antecipada) e recursão com acumulador, com o `return`
  esquecido na chamada recursiva. Código próprio em `tests_acervo/c_prog1/ec2_ordenacao_acumulador.c`
  (`-Werror`, ASan/UBSan no Docker `gcc:14`); um teste confere o aviso do gcc para o `return` esquecido.
- **Já coberto:** vetores, matrizes, strings, structs, funções e o fatorial com estouro (blocos s01 a s23).
- **Fora:** `.exe`, `output/`, os códigos da turma, `MD.c` (projeto de Matemática Discreta) e o nome de pessoa
  que aparece no nome de uma pasta. Questões do Huxley não entram resolvidas.
- **Compilação:** os 48 `.c` compilaram com MinGW; com sanitizers e entrada genérica, 5 acusaram erro (índice −1,
  estouro de `int`, `return` esquecido, leitura fora do vetor, estouro de pilha). Como a entrada foi genérica,
  alguns podem ser artefato do teste.

## Aguardando decisão

- Revisão humana e do professor dos blocos novos (nenhum marcado como revisado).
- O site não foi atualizado por mim: não há acesso ao Render nem ao PC do servidor.
