# Relatório: Ciência da Computação, lote 4 de 4 (23/11/2026)

Decisão da equipe para este lote: disciplina criada entra como `MVP`, sem aviso. As sete deste lote já
existiam como `MVP` no `dev` e continuam assim (nenhuma foi criada). Liberar não é revisar: nenhum bloco
está marcado com `revisao_humana: feita` nem `revisao_professor: sim`, e nenhuma nota escrita por IA
entrou na busca.

| # | Item | PR | Merge dev / main | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|
| 1 | Geometria Analítica (`ga`) | — | — | nada novo | — | as 14 fotos das pastas `Provas/2016.1` e `2016.2` são as mesmas já usadas nos blocos g01–g29 (por exemplo, a 2ª Avaliação de 11/03/2017 e a prova sem cabeçalho com nome e e-mail de aluno, que segue fora); os PDFs de `Provas/2017.1` são a fonte `ufal-cc-ga-provas-2017-2` (blocos `ga-cc-*`, PR #114); fotos de resumos (Cônicas, O Plano, Anotações) seguem sem uso; álgebra linear da ementa de CC sem bloco |
| 2 | Projeto e Análise de Algoritmos (`paa`) | — | — | nada novo | — | o complemento de 22/11/2026 já avaliou provas, fotos, exercícios, material da UFCG, slides da Profa. Alla e resumos da AB2 (blocos `e06` e `e07`, fora da busca até revisão humana); árvores B, TSP e FFT sem bloco; lista de referência do ranking não foi regenerada |
| 3 | Metodologia da Pesquisa (`metodologia`) | — | — | nada novo | — | os três PDFs (Alves e Arruda, Lopez e Silva, Wilkins) já são fontes do acervo; 6 notas da equipe com IA seguem fora da busca |
| 4 | Noções de Direito (`direito`) | — | — | nada novo | — | as duas avaliações de 2020.2 (só enunciados parafraseados; respostas e dados do aluno fora), os slides "Noções Iniciais" e o PDF digitalizado (provável livro, fora) já foram avaliados (d01–d08); ementa de COMP387 não conferida; artigos do Código Civil, CPC e CPP a conferir |
| 5 | Aprendizagem de Máquina (`am`) | — | — | nada novo | — | provas AB1 e AB2 (2021.1 e sem data), slides e resumos de aluno já avaliados (a01–a12); bayesiano e regressão sem bloco; ementa de COMP390 não conferida |
| 6 | Computação Evolucionária (`compevol`) | — | — | nada novo | — | capturas de tela de 2021.1, apostila de Lucas, tutorial de Dianati e livro de Mitchell (protegido, só referência) já avaliados (e01–e14); ementa de COMP397 não conferida |
| 7 | Interação Humano-Computador (`ihc`) | — | — | nada novo | — | slides "Design centrado no usuário" e os dois trabalhos de alunos de 2020.2 (com nomes, fora do acervo) já avaliados (h01–h08); ementa de COMP395 não conferida |

Suíte completa: 2227 passaram, 30 pulados. Bateria de relevância: 647/647. `ruff check --select E9,F63,F7,F82 .`: sem erros.

Itens 1 a 7: comparei cada arquivo da pasta com o `CURADORIA.md`, o `fontes.json` e os blocos da
disciplina, pelo nome, pelo semestre e pela quantidade de arquivos. Em Geometria Analítica, onde os nomes
das fotos não aparecem no repositório, abri as fotos e conferi o conteúdo com os blocos existentes. Todo o
material deste lote já tinha sido curado nas filas anteriores (21 e 22/11/2026). Não houve PR por item,
porque nada novo entraria. Este relatório entra numa PR própria.

## Aguardando decisão
- Revisão humana e do professor dos blocos das sete disciplinas (nenhum está marcado como revisado).
- PAA: revisão humana de `e06` e `e07` (hoje fora da busca) e se árvores B, TSP e FFT ganham bloco.
- GA: se a parte de álgebra linear da ementa de CC (matrizes, determinantes, sistemas) ganha bloco.
- Os `CURADORIA.md` de `am`, `compevol`, `ihc` e `direito` ainda dizem "em validação" no topo, e os de
  `am` e `compevol` dizem "Sem ligação em `cursos.json`", mas o cadastro diz `MVP` e as duas aparecem
  no grupo de eletivas de CC. Não mexi para não abrir PR só de texto.
- Ementas oficiais não conferidas: COMP387 (Direito), COMP390 (AM), COMP397 (CompEvol), COMP395 (IHC).
- PR #104 (Sistemas Digitais) não foi tocada.
- O site não foi atualizado por mim: não há acesso ao Render nem ao PC do servidor.

## Ciência da Computação: todas as disciplinas

Situação lida em `disciplinas/disciplinas.json` e posição na janela de períodos lida em
`backend/cursos.py` (curso `cc`), no `dev` de 23/11/2026.

| Disciplina | `id` | Situação | Janela de períodos (CC) |
|---|---|---|---|
| Programação 1 | `prog1` | MVP | 1º período |
| Lógica Aplicada à Computação | `logica` | MVP | 1º período |
| Computação, Sociedade e Ética | `etica` | MVP | 1º período |
| Matemática Discreta | `discreta` | MVP | 1º período |
| Cálculo Diferencial e Integral | `calc1` | MVP | 1º período |
| Estrutura de Dados | `ed` | MVP | 2º período |
| Banco de Dados | `bd` | MVP | 2º período |
| Organização e Arquitetura de Computadores | `oac` | MVP | 2º período |
| Geometria Analítica | `ga` | MVP | 2º período |
| Redes de Computadores | `redes` | MVP | 3º período |
| Teoria dos Grafos | `grafos` | MVP | 3º período |
| Probabilidade e Estatística | `prob` | MVP | 3º período |
| Programação 2 (Projeto de Software) | `projsw` | MVP | 4º período |
| Projeto e Análise de Algoritmos | `paa` | MVP | 4º período |
| Teoria da Computação | `lfa` | MVP | 4º período |
| Sistemas Operacionais | `so` | MVP | 5º período |
| Compiladores | `compiladores` | MVP | 5º período |
| Inteligência Artificial | `ia` | MVP | 5º período |
| Computação Gráfica | `cg` | MVP | 5º período |
| Sistemas Distribuídos | `sd_dist` | MVP | 7º período |
| Metodologia da Pesquisa | `metodologia` | MVP | 7º período |
| Noções de Direito | `direito` | MVP | 7º período |
| Aprendizagem de Máquina | `am` | MVP | Eletivas, ênfases e outras |
| Ciência de Dados | `cd` | MVP | Eletivas, ênfases e outras |
| Computação Evolucionária | `compevol` | MVP | Eletivas, ênfases e outras |
| Conceitos de Linguagens de Programação | `clp` | MVP | Eletivas, ênfases e outras |
| Processamento de Linguagem Natural | `pln` | MVP | Eletivas, ênfases e outras |
| Segurança de Sistemas Computacionais | `seguranca` | MVP | Eletivas, ênfases e outras |
| Interação Humano-Computador | `ihc` | MVP | Eletivas, ênfases e outras |

Todas as disciplinas de CC estão `MVP` e aparecem na janela de períodos. Nenhuma está marcada como
revisada por pessoa ou professor.
