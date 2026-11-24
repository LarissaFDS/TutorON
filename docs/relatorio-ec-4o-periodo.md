# Relatório: Engenharia de Computação, 4º período (23/11/2026)

Material bruto `4__periodo.zip`, extraído fora do repositório. Decisão da equipe para este lote: disciplina criada entra
como `MVP`, sem aviso. Liberar não é revisar: nenhum bloco está marcado com `revisao_humana: feita` nem
`revisao_professor: sim`, e nenhuma nota escrita por IA entrou na busca.

Não lidos nem versionados: `historico_23211102.pdf`, a tela do SIGAA e `cola.pdf` (documentos pessoais); Halliday,
Boyce & DiPrima e Patterson & Hennessy (protegidos); `.git`, `__pycache__`, `.vscode`, `.pyc`, executáveis,
`breast_cancer_tratado.xlsx`, imagens geradas por IA e fotos de WhatsApp.

| # | Item | PR | Merge dev / main | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|
| 1 | OAC (`oac`) | [#170](https://github.com/LarissaFDS/TutorON/pull/170) | dev: sim; main: sim ([#172](https://github.com/LarissaFDS/TutorON/pull/172)) | 4 (`oac-prova2016-2-*`, `oac-lista-cap2-*`) | pytest 2290 ok, ruff ok; relevância 677/677 | revisão humana e do professor dos 4 blocos; Ex. 3 e 6 da lista do cap. 2 sem resolução |
| 2 | Probabilidade e Estatística (`prob`) | [#171](https://github.com/LarissaFDS/TutorON/pull/171) | dev: sim; main: sim ([#172](https://github.com/LarissaFDS/TutorON/pull/172)) | 6 (`prob-petrucio-*`, `prob-ec4-lista2-basica`) | pytest 2272 ok (30 pulados sem Docker local), ruff ok; relevância 682/682 | revisão humana e do professor dos 6 blocos |
| 3 | Variáveis Complexas (`varcomp`) | [#173](https://github.com/LarissaFDS/TutorON/pull/173) | dev: sim; main: sim ([#175](https://github.com/LarissaFDS/TutorON/pull/175)) | 3 (`varcomp-lista1-*`) | pytest 2275 ok (30 pulados: Docker), ruff ok; relevância 685/685 | revisão humana e do professor; Q5c do arquivo sem o $i$ |
| 4 | Teoria dos Grafos (`grafos`) | [#174](https://github.com/LarissaFDS/TutorON/pull/174) | dev: sim; main: sim ([#175](https://github.com/LarissaFDS/TutorON/pull/175)) | 3 (`grafos-pratica1-*`) | pytest 2278 ok (30 pulados: Docker), ruff ok; relevância 688/688 | revisão humana e do professor dos 3 blocos |
| 5 | Projeto de Software (`projsw`) | [#176](https://github.com/LarissaFDS/TutorON/pull/176) | dev: sim; main: pendente | 3 (`projsw-padrao-observer-*`, `-command-*`, `-criacao-*`) | pytest 2282 ok (30 pulados: Docker), ruff ok; relevância 691/691 | revisão humana e do professor; confirmar a ligação com Engenharia de Software (ECOM021) |
| 6 | Cálculo 4 (`calc4`, nova) e complemento de Cálculo 3 (`calc3`) | PR deste item | — | calc4: 5 (`calc4-p2-*`, `calc4-impulso-*`); calc3: 2 (`calc3-lista-gleydson-*`) | pytest 2298 ok (30 pulados: Docker), ruff ok; relevância 701/701 | revisão humana e do professor; ementa de ECOM023 não conferida |

## Item 1: OAC (`oac`, complemento)

- **Novo:** prova do módulo 3 de 2016.2 com gabarito (Prof. Erick Barboza): Q1 de cache de 8 blocos (15, 15 e 14
  faltas, conferidas por simulador, com estados finais) e Q2 a Q4 de V/F (políticas de escrita, coerência, memória
  virtual, TLB, RAID). A Q5 depende de um diagrama que não está no arquivo. Lista RISC-V do cap. 2: Ex. 1, 2, 4 e 5
  resolvidos pela equipe e simulados no interpretador do teste.
- **Já coberto:** lista do cap. 1 e Prova 1 de 2025.1 (mesmos arquivos do catálogo); listas dos cap. 5 e 6, já
  resolvidas em u04, u05, s06 e s07. A lista oficial do cap. 5 tem o endereço 56 onde u04 tem 58; as faltas são as
  mesmas (13, 12, 12), então u04 não mudou.
- **Só evidência:** `riscv_entrega1` (trabalho de aluno: datapath single-cycle, já tratado em u01 e s04), as
  anotações manuscritas `OAC - Cap 5.pdf` e `Exercícios Cap 1 - Resposta.pdf`, `animated_pipeline.html`.
- **Teste estendido:** a contagem de blocos da turma em `test_resolucoes_da_turma_tem_status_e_dizem_no_texto`
  passou de 27 para 31, sem afrouxar nenhuma condição.

## Item 2: Probabilidade e Estatística (`prob`, complemento)

- **Novo:** listas do Prof. Petrucio de VA discretas e de distribuições contínuas (só enunciados e dicas de R):
  5 blocos com os valores refeitos com `scipy.stats` (binomial, Poisson, normal, exponencial, soma e média de
  normais). Lista 2 de probabilidade básica, com respostas: um bloco `corrigida` (bilhetes: o arquivo só dá a chance
  de perder; vacina chinesa: 28,57%, não 28,75%; cartas "maiores que 7" dependem de convenção).
- **Só referência:** AB1.1, AB2.1 (2024.2) e AB2.2 (2025.2): dependem da matrícula ou da base de dados de cada
  aluno, sem resposta única.
- **Fora:** arquivos com nome de aluno (`AB2_*`, `02_PE_*`, a AB2.1 entregue), trabalhos, scripts `.R` (preparação
  de dados e estudo, sem procedimento que falte), a lista 1 (mesmos assuntos de a01 a a04) e a pasta `Monitoria`
  (Sistemas Digitais; não usada, para não sobrepor a PR #104). A cópia de `C4` dentro de `ab2.1` vai com Cálculo 4.
- **Busca:** a pergunta de exemplo "P(X > 2) numa Poisson com média 3" passou a trazer o bloco novo antes de
  `prob-anot-poisson`; ajustei a redação do bloco novo (sem mexer no teste nem nos limiares).
- **Teste estendido:** a contagem de blocos da turma passou de 23 para 29 e o conjunto de corrigidas ganhou o novo
  bloco; nenhuma condição foi afrouxada.

## Item 3: Variáveis Complexas (`varcomp`, complemento)

- **Novo:** Lista nº 1 (sem gabarito oficial): Q2 (partes real e imaginária), Q3 (limites 0/0) e Q6 e Q7 (exponencial
  complexa), em 3 blocos conferidos com SymPy e com status `pendente_professor`. Os tópicos 02 e 03 passam a ter bloco
  na busca; o teste de tópicos ganhou esses dois, sem tirar nenhum, e a contagem de blocos passou de 13 para 16.
- **Sem bloco:** Q1 (pede desenho), Q4 e Q5 (Cauchy-Riemann segue só com a nota de IA fora da busca), Q8 a Q10.
  A Q5c do arquivo dá uma função real (parece faltar um $i$) e a Q7b perde a raiz de $\sqrt3$ na extração.
- **Fora:** a resolução manuscrita (de aluno, com nome; os resultados da Q2 conferem com os da equipe) e
  `stirling_complex.html` (evidência).
- **Busca:** a primeira redação de uma pergunta nova trouxe um bloco da prova; reescrevi a pergunta nova (684 → 685).

## Item 4: Teoria dos Grafos (`grafos`, complemento)

- **Novo:** Prática 1 de ECOM033 (caminho mínimo), três cenários com os arquivos de entrada da prática: estação
  central de metrô por Floyd-Warshall (vértice 9, soma 219), carro elétrico com pesos negativos por Bellman-Ford
  (0 → 3 → 5 → 6, custo 8) e robô em grid 10 × 15 por Dijkstra (custo 26, 22 movimentos). Os números foram
  recalculados com NetworkX e com implementações próprias no teste; ao conferir, corrigi o texto do bloco do grid,
  que dizia três células `~` em vez de duas.
- **Só evidência:** slides ECOM033 (assuntos já cobertos por g01 a g10); o repositório
  `Minimum-path-algoritms-scenarios` (sem arquivo de licença, não versionado nem copiado); `.html` soltos.
- O enunciado diz `=` para célula livre, mas o arquivo de exemplo usa `.`; o bloco registra a diferença.

## Item 5: Projeto de Software (`projsw`, complemento; ligado a Engenharia de Software de EC)

- **Ligação:** "Engenharia de Software" entrou em `nomes_nos_cursos` de `projsw`: o material do 4º período (lista de
  projetos OO e repositórios com padrões de projeto) cobre os mesmos assuntos. Decisão registrada no `CURADORIA.md`
  de `projsw`; o teste novo confere `projsw` em `preferidas("ecom", 4)`. Processos de software não têm material.
- **Novo:** 3 blocos de padrões (Observer, Command, padrões de criação) com contexto da lista de projetos
  (`Software_Projects.pdf`, lista da disciplina: não versionada) e código Java da equipe compilado e executado no teste.
- **Só evidência:** `crm-tool-PS-OO` (MIT), `design-patterns-python` (Apache 2.0) e `Biblioteca` (sem licença), todos
  de alunos ou de terceiros; nada copiado.

## Item 6: Cálculo 4 (`calc4`, disciplina nova) e complemento de Cálculo 3

- **Cálculo 4, nova:** `situacao: MVP`, sem aviso, `cursos: {"ecom": 4}`; entrou em `preferidas("ecom", 4)`.
  Quatro blocos da prova 2 do Prof. Gleydson Santos da Silva (campo conservativo e potencial, área da esfera por
  integral de superfície, Stokes no plano $x + y + z = 1$, divergência na caixa), status `pendente_professor`, e um
  bloco das anotações da aula de função impulso (peneiração, $\mathcal L\{\delta(t-a)\} = e^{-as}$, EDO
  $y'' + 4y = \delta(t-\pi) - \delta(t-2\pi)$), todos conferidos com SymPy.
- **Ementa de ECOM023 não conferida:** os assuntos saíram da prova e da aula. A prova confirma que integrais de
  linha, Stokes e Gauss são de Cálculo 4, como o `CURADORIA.md` de Cálculo 3 supunha.
- **Só referência:** o resumo de função impulso (material de apresentação, autoria incerta), `impulse_function.html`,
  Stewart e Boyce & DiPrima (protegidos, só catálogo).
- **Cálculo 3 (complemento no mesmo PR):** a lista P3C3 do Prof. Gleydson virou 2 blocos (jacobiana e taxa ao longo
  de vetor unitário; pontos críticos e posto). A correção manuscrita da prova 3 é de aluno (só evidência).
  `C3.docx` é uma lista de frequência com notas e matrículas: fora, sem citação.
- **Busca:** uma pergunta antiga de Cálculo 3 marcada "fora" (derivada direcional de $x^2y$) passou a trazer o bloco
  novo; reescrevi o bloco novo (sem mexer na pergunta nem nos limiares) e a bateria voltou a 701/701.
- **Teste estendido:** a contagem de blocos da turma de Cálculo 3 passou de 16 para 18; nenhuma condição afrouxada.
- IA real: não rodada.

## Aguardando decisão

- Revisão humana e do professor dos blocos novos (nenhum marcado como revisado).
- Confirmar que Engenharia de Software (ECOM021) deve mesmo abrir o acervo de Projeto de Software (`nomes_nos_cursos`).
- Conferir a ementa oficial de Cálculo 4 (ECOM023); os assuntos vieram só da prova 2 e da aula de impulso.
