# Relatório da fila: Ciência da Computação, parte 3 (23/11/2026)

Decisão da equipe para esta parte: cada disciplina nova entra direto como `MVP`, sem aviso. Liberar não é
revisar: nenhum bloco está marcado com `revisao_humana: feita` nem `revisao_professor: sim`, e nenhuma
nota escrita por IA entrou na busca.

| # | Disciplina | id | PR | Merge dev / main | Situação final | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|---|---|
| 1 | Inteligência Artificial | `ia` | #145 | dev: sim; main: ver item 3 | **MVP** (disciplina nova) | 14 (`i01`–`i14`): slides da UFES, aulas de RCR e lógica do Prof. Evandro Costa e enunciados das listas de 2020.2 | pytest 2148 ok, 30 pulados; relevância 631/631; ruff ok; bateria real 5 perguntas (Gemini em 503/429, respondeu o modelo local `tutoron-paa`) | revisão humana e do professor pendentes; ementa de COMP380 não conferida; respostas do aluno nas listas não usadas; Russell e Norvig só como referência; bateria: respostas sem rótulos de fonte citados, e a de fora do assunto foi respondida como Circuitos em vez de recusada |
| 2 | Computação Gráfica | `cg` | #146 | dev: sim; main: ver item 3 | **MVP** (disciplina nova) | 13 (`g01`–`g13`): aulas do Prof. Marcelo Costa Oliveira e enunciados de exercícios e provas (2014, bimestral I.2, 2021.2), contas e algoritmos refeitos em Python | pytest 2187 ok, 30 pulados; relevância 639/639; ruff ok; bateria real 5 perguntas (2 pelo Gemini com rótulos citados, 3 pelo modelo local `tutoron-paa` sem rótulos) | revisão humana e do professor pendentes; ementa de COMP381 não conferida; `g10` e `g11` dependem de gabarito oficial; livros, fotos, apostila e guia não versionados; bateria: a pergunta de fora do assunto (alfa-beta) foi respondida em vez de encaminhada para IA |

## Aguardando decisão
- Inteligência Artificial: revisão humana dos 14 blocos e conferência da ementa de COMP380.
- Computação Gráfica: revisão humana dos 13 blocos, ementa de COMP381 e gabaritos de `g10`/`g11`.
- O site não foi atualizado: não há acesso ao PC do servidor.
