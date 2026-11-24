# Relatório: Engenharia de Computação, 4º período (23/11/2026)

Material bruto `4__periodo.zip`, extraído fora do repositório. Decisão da equipe para este lote: disciplina criada entra
como `MVP`, sem aviso. Liberar não é revisar: nenhum bloco está marcado com `revisao_humana: feita` nem
`revisao_professor: sim`, e nenhuma nota escrita por IA entrou na busca.

Não lidos nem versionados: `historico_23211102.pdf`, a tela do SIGAA e `cola.pdf` (documentos pessoais); Halliday,
Boyce & DiPrima e Patterson & Hennessy (protegidos); `.git`, `__pycache__`, `.vscode`, `.pyc`, executáveis,
`breast_cancer_tratado.xlsx`, imagens geradas por IA e fotos de WhatsApp.

| # | Item | PR | Merge dev / main | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|
| 1 | OAC (`oac`) | [#170](https://github.com/LarissaFDS/TutorON/pull/170) | dev: sim; main: PR dev→main dos itens 1 e 2 | 4 (`oac-prova2016-2-*`, `oac-lista-cap2-*`) | pytest 2290 ok, ruff ok; relevância 677/677 | revisão humana e do professor dos 4 blocos; Ex. 3 e 6 da lista do cap. 2 sem resolução |
| 2 | Probabilidade e Estatística (`prob`) | PR deste item | — | 6 (`prob-petrucio-*`, `prob-ec4-lista2-basica`) | pytest 2272 ok (30 pulados sem Docker local), ruff ok; relevância 682/682 | revisão humana e do professor dos 6 blocos |

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

## Aguardando decisão

- Revisão humana e do professor dos blocos novos (nenhum marcado como revisado).
