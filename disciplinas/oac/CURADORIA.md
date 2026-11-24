# Organização e Arquitetura de Computadores — curadoria do acervo

Situação: **em validação** desde 27/10/2026. A disciplina está cadastrada, com acervo e índice próprios, e passa pelo mesmo fluxo da IA. Enquanto a validação não acontecer, o servidor recusa perguntas de OAC no atendimento normal (403, a mesma barreira usada por SD antes do beta). Para testes autorizados, use `TUTORON_LIBERAR_EM_VALIDACAO=oac` (veja [`docs/DISCIPLINAS.md`](../../docs/DISCIPLINAS.md)).

| Item | Estado em 27/10/2026 |
|---|---|
| Cadastro, acervo (41 blocos desde 23/11/2026; eram 37) e índice híbrido (`bge-m3`) | **Feitos** |
| Contas, codificações e código RISC-V das resoluções | **Conferidos por código** (`tests_acervo/test_disciplina_oac.py`) |
| Revisão humana interna dos 28 blocos | **Pendente** (`revisao_humana: pendente` em todos) |
| Autorização para publicar transcrições literais da prova e da lista | **Não dada**: os blocos trazem enunciados parafraseados e os dados, não a transcrição |
| Aprovação do professor | **Não declarada**; nenhum bloco tem `revisao_professor: sim` |
| Plano de ensino atual | **Não localizado**; só a ementa de 2011 (seção 1) |
| Página do Notion da turma | **Inventariada** em 02/11/2026: 7 blocos `s*` (seção 4.1) |
| Validação das respostas da IA | **Parcial**: 4 perguntas com o Gemini, todas corretas (seção 5.1); modelo local não testado |

- Catálogo legível por máquina (fonte da verdade): [`fontes.json`](fontes.json)
- Blocos do acervo (um arquivo por bloco): [`materiais/`](materiais/). `t*` são materiais da turma; `s*` são anotações da turma no Notion; `n*` são notas da equipe
- Gerados a partir dos blocos (não editar à mão): [`acervo/itens.json`](acervo/itens.json) e [`acervo/indice.json`](acervo/indice.json)
- Regras de rigor que o tutor segue em OAC: [`rigor.md`](rigor.md)

## 1. Ementa: o que foi encontrado

Encontramos a ementa oficial de **ECOM025 Organização e Arquitetura de Computadores** (60 h, 4º semestre) no Projeto Pedagógico de Engenharia de Computação da UFAL de 2011 (`ufal-ppc-ecomp-2011-oac`, p. 28):

> Organização básica de computadores: processador, memória, entrada-saída. Organização interna do processador. Hierarquia de memória. Dispositivos de E/S. Barramentos. Microarquiteturas e microprogramação. Arquitetura do conjunto de instruções. Linguagem de máquina e de montagem. Arquiteturas não convencionais.

A bibliografia de 2011 (Tanenbaum, Stallings, Weber, Murdocca, Hennessy) **não** inclui o livro usado hoje. Os slides da aula têm rodapé "Chapter N — …" e o logo da Morgan Kaufmann, ou seja, o livro em uso é Patterson & Hennessy, *Computer Organization and Design, RISC-V Edition*. O **plano de ensino atual não foi localizado**. Por isso, esta curadoria **não está validada pelo professor**. Os tópicos abaixo seguem o sumário do livro e foram classificados pela evidência encontrada.

### Tópicos, evidência e seção do livro-texto

| Assunto (`assunto` nos blocos) | Classificação | Evidência | Patterson & Hennessy | Blocos |
|---|---|---|---|---|
| `oac-01-abstracoes-hierarquia`: arquitetura × organização, compilador, montador | Confirmado pela turma | Prova 1 Q1 | 1.1–1.4, 2.12 | t06 |
| `oac-02-desempenho`: tempo de CPU, CPI, CPI médio, speedup, MIPS, Amdahl | Confirmado pela turma | Lista cap. 1; Prova 1 Q1–Q3; resumo de fórmulas | 1.6, 1.7, 1.10 | t01–t05, t07, n01 |
| `oac-03-custo-ci`: die, wafer, yield | Confirmado pela turma | Slide do cap. 1 | 1.5 | n02 |
| `oac-04-risc-cisc` | Confirmado pela turma | Prova 1 Q1c (duas versões) | 2.17, 2.19 | t06, t07 |
| `oac-05-isa-registradores-memoria`: registradores, convenção, memória por byte, endianness | Confirmado pela turma | Slides; foto de aula | 2.2, 2.3 | t11, n03 |
| `oac-06-representacao-numeros`: com e sem sinal, extensão de sinal | Confirmado pela turma | Slide "Signed vs. Unsigned" | 2.4 | n05, n10 |
| `oac-07-formatos-codificacao`: R, I, S (B, U, J) | Parcial: R, I e S confirmados | Slides de formatos | 2.5, 2.10 | n04 |
| `oac-08-logicas-deslocamentos` | Confirmado pela turma (`slli` nas questões) | Prova 1 Q4 e Q5 | 2.6 | t08–t10 |
| `oac-09-desvios-lacos-vetores` | Confirmado pela turma | Slides if/while; Prova 1 Q5 | 2.7, 2.14 | t09, t10, n05 |
| `oac-10-procedimentos`: jal/jalr, pilha, registradores salvos | Confirmado pela turma | Prova 1 Q4 (swap) | 2.8, 2.13 | t08, n06 |
| `oac-11-constantes-enderecamento-traducao`: lui, modos de endereçamento, ligação | Fundamental no livro, não confirmado | — | 2.10, 2.12 | n10 (lui) |
| `oac-12-aritmetica`: overflow, multiplicação, IEEE 754 | Fundamental no livro, não confirmado | — | 3.2–3.5 | n10 |
| `oac-13-datapath-controle`: monociclo, unidade de controle | Confirmado pela turma | Slide do cap. 4; ementa ("organização interna do processador") | 4.3, 4.4 | n07, s04, u01 |
| `oac-14-pipeline-hazards` | Fundamental no livro, não confirmado | Ementa ("microarquiteturas") | 4.5–4.9 | n08, s05, u02 |
| `oac-15-hierarquia-memoria`: cache, memória virtual, TLB | Fundamental; está na ementa | Ementa ("hierarquia de memória") | 5.1–5.8 | n09, s06, u03–u05 |
| `oac-16-paralelismo` | Complementar ou dependente da ementa | Ementa ("arquiteturas não convencionais") | 6 | s07, u06 |

Lacunas da ementa sem bloco: dispositivos de E/S, barramentos e microprogramação. O livro RISC-V trata pouco desses temas. Fica para depois de confirmar o plano de ensino.

## 2. Fronteira com Sistemas Digitais

OAC e SD têm vocabulário em comum. A regra é que **a disciplina escolhida pelo aluno define o acervo**: cada uma tem índice próprio, e não há filtro por palavra-chave. Os testes `test_vocabulario_comum_fica_na_disciplina_escolhida` (acervo) e `test_vocabulario_comum_so_recupera_a_disciplina_escolhida` (backend) confirmam que "somador", "registradores" e "overflow" recuperam só blocos da disciplina escolhida.

| Tópico de fronteira | Fica em SD | Fica em OAC (pelo ângulo da arquitetura) |
|---|---|---|
| Complemento de 2, overflow | Representação, soma coluna a coluna, detecção por carries (`sd-nota-numeracao`, `sd-nota-aritmeticos`) | Comparação com e sem sinal em desvios, extensão de sinal de imediatos, overflow sem exceção no RISC-V (n05, n10) |
| Somador, ALU | Projeto do somador completo, ripple-carry, ULA (`sd-somadores-monitoria`) | A ALU como bloco do datapath e o ALU control (n07) |
| Multiplexador | Projeto e expressão do MUX | MUX ALUSrc, MemtoReg e do PC no datapath (n07) |
| Registradores, flip-flops | Flip-flops, registradores de carga e deslocamento | Banco de registradores x0–x31 e convenção de uso (n03) |
| Memórias | ROM/RAM como componentes | Memória endereçada por byte, caches, hierarquia (t11, n09) |
| Máquinas de estados | FSM, Moore × Mealy | Unidade de controle monociclo como lógica combinacional do opcode (n07) |

Nenhum bloco de OAC repete o conteúdo de projeto de circuitos de SD.

## 3. Critérios e matriz de curadoria

Mesma escala de SD: notas de 1 a 5 em **autoridade**, **cobertura**, **profundidade**, **didática**, **aderência** (RISC-V e compatível com o livro e a turma), **acessibilidade**, **reutilização** (licença) e **utilidade para tutoria**. Em OAC, a tutoria precisa de material **procedimental**: conta de desempenho passo a passo, tradução de C para RISC-V, codificação em binário, sinais no datapath e diagrama de pipeline. Por isso, slides teóricos ficam abaixo de exercícios resolvidos.

| Fonte | ISA | Aut. | Cob. | Prof. | Did. | Ader. | Acess. | Reut. | Tut. | Prioridade | Uso |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ufal-oac-prova1-2025-1` Prova 1 com gabarito | RISC-V | 5 | 3 | 4 | 3 | 5 | 4 | 2 | 5 | alta | no acervo (parafraseada) |
| `ufal-oac-lista-cap1` Lista cap. 1 | genérica | 4 | 2 | 3 | 3 | 5 | 5 | 2 | 5 | alta | no acervo (parafraseada) |
| `ufal-oac-aula-foto` Quadro "Memory Operand Example" | RISC-V | 4 | 1 | 3 | 4 | 5 | 3 | 1 | 5 | alta | no acervo (só o conteúdo) |
| `ufal-oac-resumo-formulas` Resumo de fórmulas | genérica | 2 | 1 | 2 | 3 | 4 | 3 | 2 | 4 | média | citada (n01) |
| `ufal-oac-anotacoes-manuscritas` Anotações | genérica | 2 | 1 | 2 | 3 | 4 | 3 | 2 | 3 | média | citada (n01) |
| `riscv-isa-manual` Manual oficial do RISC-V | RISC-V | 5 | 3 | 5 | 2 | 5 | 5 | 5 | 3 | alta | citada |
| `riscv-card-jameslzhu` Cartão de referência | RISC-V | 3 | 2 | 3 | 3 | 5 | 5 | 5 | 4 | alta | citada |
| `unicamp-mc404-rodolfo` MC404 Unicamp (slides) | RISC-V | 5 | 2 | 3 | 4 | 5 | 5 | 4 | 3 | média | citada |
| `cs61c-berkeley` CS 61C Berkeley | RISC-V | 5 | 5 | 4 | 5 | 5 | 5 | 1 | 5 | média | citada (sem licença) |
| `ripes` Ripes (simulador visual) | RISC-V | — | — | — | — | — | — | — | — | média | citada (ferramenta) |
| `rars` RARS (simulador) | RISC-V | — | — | — | — | — | — | — | — | média | citada (ferramenta) |
| `venus-cs61c` Venus (simulador web) | RISC-V | — | — | — | — | — | — | — | — | referência | ferramenta |
| `mit-ocw-6004-2017` MIT 6.004 (2017) | **Beta** | 5 | 4 | 5 | 4 | 2 | 4 | 3 | 3 | referência | comparação |
| `borin-riscv-book` Borin, Unicamp | RISC-V | 5 | 3 | 4 | 5 | 5 | 4 | 1 | 4 | referência | sem licença aberta |
| `pattersonhennessy-cod-riscv` Livro-texto | RISC-V | 5 | 5 | 5 | 5 | 5 | 2 | 1 | 5 | referência | protegido |
| `ufal-oac-slides-editora` Slides do livro | RISC-V | 5 | 3 | 4 | 4 | 5 | 3 | 1 | 4 | referência | protegido |
| `ufal-ppc-ecomp-2011-oac` Ementa ECOM025 | — | 5 | 3 | 1 | 1 | 3 | 5 | 3 | 1 | referência | ementa |
| `ufal-oac-notion` Notion da turma | RISC-V | 4 | 3 | 3 | 3 | 4 | 4 | 1 | 2 | referência | resumida (s01–s07) |
| `ufal-oac-anotacoes-otavio-2025-2` Anotações manuscritas de aluno (2025.2) | RISC-V | 2 | 3 | 3 | 4 | 5 | 3 | 1 | 4 | média | resumida (u01–u06) |
| `ufal-oac-prova-2016-2` Prova do módulo 3 (2016.2) com gabarito | genérica | 5 | 3 | 3 | 4 | 4 | 4 | 2 | 5 | alta | no acervo (t12, t13) |
| `ufal-oac-lista-cap2` Lista RISC-V do cap. 2 | RISC-V | 4 | 3 | 3 | 3 | 5 | 5 | 2 | 5 | alta | no acervo (t14, t15) |
| `ufal-oac-listas-cap5-cap6` Listas dos cap. 5 e 6 | genérica | 4 | 3 | 3 | 3 | 5 | 5 | 2 | 4 | média | referência (já resolvidas em u04, u05, s06, s07) |

### Por que esta seleção

- **Materiais da turma primeiro**, como em PAA e SD: mostram como o professor cobra. Cada gabarito foi refeito (seção 4).
- **Notas da equipe preenchem o procedimento** (n01–n10): fórmulas com exemplos, codificação passo a passo, tabela de sinais do datapath, diagrama de pipeline. Foram escritas com auxílio de IA e com texto próprio. Os exemplos numéricos e de código têm teste. **Não são material do professor.**
- **Fontes abertas citadas, não copiadas.** O manual do RISC-V e o cartão de referência (CC BY 4.0) e os slides de MC404 (CC BY-SA 4.0, a única fonte universitária aberta em português que encontramos) são os primeiros candidatos a ingestão com atribuição. Nesta entrega ficam só citados, para evitar cópia em massa sem revisão.
- **CS 61C** é o melhor material procedimental em RISC-V, mas o site não declara licença: fica como leitura indicada.
- **MIT 6.004 de 2017 usa a ISA Beta**, não RISC-V. Serve para conceitos de pipeline e cache, nunca como exemplo de código. A versão RISC-V do 6.004 não foi conferida no OCW.
- **Livro-texto e slides da editora:** só referência. O PDF de 1665 páginas foi usado **apenas para ler o sumário** e mapear seções; nada dele foi copiado, fragmentado ou indexado.
- **Duplicações evitadas:** os Exercícios 3 e 4 da lista são a Prova 1 Q3 e a Q2 da versão A; cada questão tem um único bloco, que cita as duas fontes.

## 4. Materiais da turma: inventário e validação dos gabaritos

Origem de todos: **material de turma**, compartilhado pelos alunos. Os originais (PDFs e imagens) **não estão no repositório**. Como a publicação ainda não foi autorizada pela equipe, os blocos `t*` trazem **enunciados parafraseados** e os dados numéricos (`publicacao_transcricao` no cabeçalho), não a transcrição literal. A foto de aula mostra uma pessoa: só o conteúdo do quadro foi descrito.

Cada bloco tem `status_resolucao` no cabeçalho, e o texto também diz o status, porque é o texto que a IA lê. As regras de rigor proíbem apresentar resolução corrigida ou pendente como gabarito oficial.

| Arquivo | id | Questão | Gabarito original | Resolução revisada | Status |
|---|---|---|---|---|---|
| t01 | `oac-lista-ex1` | Lista Ex. 1 (P1, P2, P3) | não há | P2 maior IPS; frequência × 1,714 (5,14 / 4,29 / 6,86 GHz) | validada |
| t02 | `oac-lista-ex2` | Lista Ex. 2 (4 classes) | não há | CPI 2,4 × 2,0; P2 ≈ 1,44× mais rápido | validada |
| t03 | `oac-compiladores` | Prova Q3 (A e B) = Lista Ex. 3 | CPI 1,1 e 1,25; f_B/f_A = 1,37; speedups 1,67 e 2,27 | 1,5/1,1 = **1,36**; a pergunta pede A em relação a B: o clock de A é ≈ 0,73 do de B | **corrigida** |
| t04 | `oac-prova1-a-q2-enade` | Versão A, Q2 (M2 a 500 MHz) = Lista Ex. 4 | (E), com CPIs arredondados para 6 e 3 e "3/5×10⁻⁸" | 5,1 ns × 5,2 ns → (E); CPI médio não se arredonda; frequência ≠ período | **corrigida** |
| t05 | `oac-prova1-b-q2-enade` | Versão B, Q2 (M2 a 250 MHz) | (A), com CPIs arredondados (6 ns × 12 ns) | 5,1 ns × 10,4 ns → (A), razão 2,04 | **corrigida** |
| t06 | `oac-prova1-a-q1` | Versão A, Q1 V/F | F, V, F, V | a–c conferem; d (compilador "direto para código de máquina") contradiz o modelo da seção 2.12 | **pendente de confirmação do professor** |
| t07 | `oac-prova1-b-q1` | Versão B, Q1 V/F | F, V, V, F, F (com correções riscadas) | Confere. Riscado lido na imagem: "diminuir" o tempo de resposta e "aumentar" o throughput; "Não é possível" usar MIPS | **pendente de confirmação do professor** (leitura do riscado) |
| t08 | `oac-prova1-q4-swap` | Q4 swap (duas versões) | código certo; comentários "$t1"/"$t0"/"$t2" | código simulado; comentários corrigidos para x5 = t0, x6 = t1, x7 = t2 | **corrigida** (comentários) |
| t09 | `oac-prova1-a-q5` | Versão A, Q5 (bne) | "quantidade de números iguais" | número de **pares (i, j)** iguais (com repetição, {1,1} × {1} dá 2) | **corrigida** |
| t10 | `oac-prova1-b-q5` | Versão B, Q5 (beq; impressa como "4") | pares diferentes | confere por simulação | validada |
| t11 | `oac-aula-operando-memoria` | Quadro da aula | x22 = 4 → endereço 36 | confere; sw em 52 = 4 + 12 × 4 | validada |

Correspondência MIPS × RISC-V nos comentários: no gabarito da Q5, "t0" e "t1" são x5 e x6, o que confere com a convenção do RISC-V. Na Q4, os nomes vêm do exemplo MIPS do livro e estavam trocados.

## 4.1 Notion da turma (lido em 02/11/2026)

A página `ufal-oac-notion` (Engenharia de Computação / Quarto Período) foi lida pela integração do Notion: a raiz e as subpáginas Capítulo 1, Capítulo 2, Capítulo 5, Capítulo 6, Projeto 1 e Projeto 2. São anotações de alunos; as dos caps. 5 e 6 e parte do Projeto 2 foram feitas com assistente de IA. Os blocos `s*` resumem esse conteúdo **com texto próprio**, e cada um tem `status_resolucao`.

| Arquivo | id | Página | O que foi corrigido | Status |
|---|---|---|---|---|
| s01 | `oac-notion-cap1-desempenho` | Capítulo 1 | "aumento proporcional do clock": o certo é × 1,714 (+71,4%) | **corrigida** |
| s02 | `oac-notion-cap2-instrucoes` | Capítulo 2 | `sw` anotado ao contrário; imediato do `beq` de 12 bits, não 16; `lli` não existe; sintaxe MIPS `$s1`; `srli` só divide sem sinal | **corrigida** |
| s03 | `oac-notion-cap2-procedimentos` | Capítulo 2 | nada: fatorial e laço simulados | validada |
| s04 | `oac-notion-projeto1-monociclo` | Projeto 1 + anexos `.sv` e `.s` | extend recebe 25 bits (Instr[31:7]); WE da memória vem de MemWrite. ALUOp = 11 no addi conferido no `.sv`: está certo | **corrigida** |
| s05 | `oac-notion-projeto2-pipeline` | Projeto 2 + subpágina Code | hazards e forwarding não testam x0; saídas do hazard_unit com nomes trocados (lógica certa) | **corrigida** |
| s06 | `oac-notion-cap5-memoria` | Capítulo 5 | nada: exemplo de tag/índice/offset e CPI com L2 conferidos | validada |
| s07 | `oac-notion-cap6-paralelismo` | Capítulo 6 + subpágina Perplexity | Ex. 1 contava 9 somas escalares (o livro conta 10; speedups 5,5 e 10); a lista de princípios de DSA da página principal não é a do livro (a da Perplexity é) | **corrigida** |

Em 02/11/2026 também foram lidos, com autorização da responsável, os anexos `riscvsingle_p1.sv` (original e modificado) e `riscvtest.s` do Projeto 1 e as subpáginas "Code" (Projeto 2) e "Perplexity" (caps. 5 e 6). Os arquivos ficaram fora do repositório: o código-base e o programa de teste são de Harris & Harris. A Perplexity do cap. 5 não acrescenta nada aos blocos. O projeto não foi simulado (não há Icarus Verilog nesta máquina). Não incorporados: o PDF do livro e as imagens de slides (protegidos); o PDF de exercícios e o gabarito da Prova 1 (já resumidos nos blocos `t*`); a animação do Projeto 2; e o curso da Softex incorporado na página, cuja licença não foi avaliada. Com os blocos s05–s07, pipeline, cache e paralelismo deixam de ser só notas da equipe.

## 4.2 Anotações manuscritas de aluno, 2025.2 (lidas em 18/11/2026)

`ufal-oac-anotacoes-otavio-2025-2`: quatro PDFs de anotações manuscritas de Otávio Joshua Costa Brandão Menezes (turma 2025.2 do Prof. Erick de Andrade Barboza). Os arquivos são: Projeto 1 SingleCycle (5 págs.), Projeto 2 Pipeline (11), Hierarquia de Memória (3) e Revisão AB2 (7). Os PDFs não têm texto extraível; foram lidos página a página como imagem. Ficaram **fora do repositório**, assim como as figuras, que são slides da editora (protegidos) e foram descritas em texto. São anotações de um aluno, não gabarito, e o autor, integrante da equipe TutorON, autorizou a publicação em 18/11/2026 (`autorizacao_transcricao` em `fontes.json`). Os blocos `u*` parafraseiam com texto próprio, e a autorização não cobre os slides da editora. Os Projetos 1 e 2 são avaliados, então os blocos explicam conceitos e não trazem implementação (regra acrescentada ao `rigor.md`).

| Arquivo | id | Origem | Erros encontrados | Status |
|---|---|---|---|---|
| u01 | `oac-otavio-projeto1-monociclo` | Projeto 1 | MemtoReg = 00 no beq (é X, porque RegWrite = 0); "extend sem ImmSrc para B e I" não confirmado no código | **corrigida** |
| u02 | `oac-otavio-projeto2-hazards` | Projeto 2 | forwarding e hazard sem teste de x0; valor do banco (00) chamado de "mais recente"; nomes Reg_ControlWB_E/M para RegWrite de M e W; `sd` é RV64 | **corrigida** |
| u03 | `oac-otavio-hierarquia-memoria` | Hierarquia de Memória | "DRAM síncrona transfere na subida e na descida" é a DDR, não toda SDRAM; QDR é de SRAM | **corrigida** |
| u04 | `oac-otavio-ab2-q1-cache` | Revisão AB2, Q1 | nada: 13, 12 e 12 misses conferidos por simulador (LRU) | validada |
| u05 | `oac-otavio-ab2-q2-q7` | Revisão AB2, Q2–Q7 | Q5a: endereço virtual dividido em 4 + 36 bits (o certo é offset de 14, página virtual de 26 e física de 22 bits; tabela de 2^26 entradas); Q7b: CPI 3,3 e ganho 2,73 (o certo é 3,4 e ≈ 2,6, porque toda falta da L1 paga a L2) | **corrigida** |
| u06 | `oac-otavio-ab2-cpu-gpu` | Revisão AB2, cap. 6 | nada | validada |

Conferências em `tests_acervo/test_disciplina_oac.py`: simulador de cache (mapeamento direto, associativa por conjunto, LRU, índice pelo endereço do bloco, falta compulsória × conflito) e diagrama de pipeline ciclo a ciclo (enchimento, bolha de load-use mesmo com forwarding, sequência sub/and/or/add/sw com e sem forwarding). O enunciado original da Q5b (tamanho da PTE) não está nas anotações; o bloco avisa que o tamanho depende dele. As questões 1–3 do cap. 6 que a anotação marca como foco não estão resolvidas no PDF.

## 4.3 Complemento de Ciência da Computação (22/11/2026)

As provas do Prof. Erick de Andrade Barboza são comuns às turmas de Engenharia e Ciência da Computação; o PPC de CC (`ufal-ppc-cc-2011`) traz os mesmos tópicos. Não há disciplina separada. As provas de 2017 usam MIPS, e o acervo usa RISC-V: os blocos dizem isso no status.

Entraram 3 blocos de `ufal-cc-oac-provas-erick-2017`, todos `validada` e com `curso:` no cabeçalho: `oac-cc-desempenho-compiladores`, `oac-cc-cache-tres-mapeamentos`, `oac-cc-pipeline-reordenar-ciclo`. O item b da Q2 da prova 1 foi anulado no gabarito; o bloco mostra a conta (clock de A cerca de 27% mais lento). Fora do repositório: as provas de 2016.2 e a reavaliação de 2017.1 (mesmos tópicos) e os arquivos do MARS.

## 4.4 Complemento do 4º período de Engenharia de Computação (23/11/2026)

Material bruto do 4º período de EC, comparado arquivo a arquivo com este catálogo e com os blocos.

- **Novo no acervo:** prova do módulo 3 de 2016.2 com gabarito (t12: cache de 8 blocos, 15/15/14 faltas conferidas por simulador; t13: V/F de cache, memória virtual e RAID; a Q5 depende de um diagrama que não está no arquivo) e a lista RISC-V do cap. 2 (t14: Ex. 1 e 2; t15: Ex. 4 e 5, código da equipe simulado no teste). Os Ex. 3 e 6 ficaram sem resolução.
- **Já coberto:** a lista do cap. 1 e a Prova 1 de 2025.1 (mesmo arquivo, `ufal-oac-prova1-2025-1` e `ufal-oac-lista-cap1`); as listas dos cap. 5 e 6 (`ufal-oac-listas-cap5-cap6`), que u04, u05, s06 e s07 já resolvem. A lista oficial do cap. 5 traz o endereço 56 onde u04 tem 58; refeita a simulação, as faltas são as mesmas (13, 12, 12), então u04 não foi mudado.
- **Só evidência, fora do repositório:** `OAC - Cap 5.pdf` e `Exercícios Cap 1 - Resposta.pdf` (anotações manuscritas de aluno sobre as mesmas listas); `riscv_entrega1` (`.sv`, `.s`, trabalho de aluno: confirma o datapath single-cycle já tratado em u01 e s04; nenhum bloco a partir da solução); `animated_pipeline.html` (parece gerado por IA).
- **Protegido:** `Computer Organization and D_ .pdf` (Patterson & Hennessy), não versionado (`pattersonhennessy-cod-riscv`, só referência).

## 5. Blocos do acervo

Todos com `curadoria: aprovado` e confiabilidade **média**, como em SD. Nenhum bloco tem confiabilidade alta.

| Arquivo | id | Natureza | Verificação |
|---|---|---|---|
| t01–t05, t08–t11 | `oac-lista-ex1`, `oac-lista-ex2`, `oac-compiladores`, `oac-prova1-a-q2-enade`, `oac-prova1-b-q2-enade`, `oac-prova1-q4-swap`, `oac-prova1-a-q5`, `oac-prova1-b-q5`, `oac-aula-operando-memoria` | material da disciplina | conferida por código |
| t06, t07 | `oac-prova1-a-q1`, `oac-prova1-b-q1` | material da disciplina | não verificada (V/F conceitual) |
| n01 | `oac-nota-desempenho` | nota da equipe (IA) | exemplos conferidos |
| n02 | `oac-nota-custo-ci` | nota da equipe (IA) | exemplos conferidos |
| n03 | `oac-nota-registradores-memoria` | nota da equipe (IA) | não verificada |
| n04 | `oac-nota-formatos-codificacao` | nota da equipe (IA) | exemplos conferidos (5 codificações) |
| n05 | `oac-nota-desvios-lacos` | nota da equipe (IA) | exemplos conferidos (if/else e while simulados) |
| n06 | `oac-nota-procedimentos` | nota da equipe (IA) | não verificada (fatorial não simulado: usa pilha, jal e mul) |
| n07 | `oac-nota-datapath-controle` | nota da equipe (IA) | não verificada (tabela de sinais conferida com o livro, não por código) |
| n08 | `oac-nota-pipeline-hazards` | nota da equipe (IA) | não verificada |
| n09 | `oac-nota-hierarquia-memoria` | nota da equipe (IA) | exemplos conferidos |
| n10 | `oac-nota-aritmetica-constantes` | nota da equipe (IA) | exemplos conferidos |
| s01, s02, s04–s07 | anotações do Notion (seção 4.1) | material da disciplina | exemplos conferidos (contas e afirmações) |
| s03 | `oac-notion-cap2-procedimentos` | material da disciplina | conferida por código (fatorial e laço simulados) |
| u01–u06 | anotações manuscritas de aluno, 2025.2 (seção 4.2) | material da disciplina | u04 e u05 conferidos por simulador e contas; u02 por diagrama ciclo a ciclo; u01, u03 e u06 conceituais |
| t12, t13 | `oac-prova2016-2-q1-cache`, `oac-prova2016-2-q2-q4-vf` | material da disciplina | t12 conferida por simulador; t13 não verificada (V/F conceitual, gabarito do professor) |
| t14, t15 | `oac-lista-cap2-ex1-ex2`, `oac-lista-cap2-ex4-ex5` | material da disciplina | conferida por código (simulados) |

**Código assembly e fórmulas.** Cada bloco cabe inteiro num trecho (menos de 2.000 caracteres; `backend/rag.py` corta acima de 2.200), então nenhum bloco de código é partido na indexação. O teste confere que os blocos ```` ``` ```` estão fechados. Fórmulas estão em texto legível (o tutor responde em Markdown com LaTeX). O datapath do cap. 4 foi transcrito em texto: componentes, campos da instrução usados e tabela de sinais (n07).

## 5.1 Teste com a busca e a IA reais (27/10/2026)

**Busca híbrida (`bge-m3`), com OAC e SD.** "lw x9, 32(x22)", "CPI médio 50/30/20", "blt × bltu" e "sinais do sw" trazem em 1º lugar o bloco certo (t11, n01, n05 e n07). Em SD, as três primeiras não trazem nada. "Somador completo" traz a nota de OAC em OAC e o material de somadores em SD. "Quanto é 2+2?" não recupera nada em nenhuma das duas.

**Respostas com o modelo real.** Mesmo caminho do site (`rag.recuperar` → `prompts.sistema_tutor` → `LLM.complete`). Os primeiros Gemini da lista deram 503, e a corrida passou para os seguintes:

| Pergunta | Modelo que respondeu | Resultado (leitura da equipe) |
|---|---|---|
| Por que `lw x9, 32(x22)` acessa `A[8]`? | gemini-3.1-flash-lite | Correta: byte × palavra de 4 bytes, 8 × 4 = 32, citou [P1] |
| CPI médio 50% A, 30% B, 20% C | gemini-3.6-flash | Correta: deu a fórmula, avisou que faltam os CPIs e usou o exemplo do ENADE (5,1) sem arredondar |
| `blt` × `bltu` | gemini-3.6-flash | Correta: exemplo 0xFFFFFFFF × 1 e teste de limite com bltu |
| Sinais de controle do `sw` | gemini-3.5-flash | Correta: ALUSrc = 1, MemWrite = 1, RegWrite = 0, MemRead = 0, Branch = 0, MemtoReg = X, ALUOp = 00 |

**Limites deste teste:** 4 perguntas, uma execução, avaliadas só pela equipe. O modelo local (`tutoron-paa`) não foi testado em OAC (em SD, ele errou cálculos). Por isso a disciplina continua **em validação**.

## 5.2 Teste com a IA real das anotações de 2025.2 (18/11/2026)

`python eval/bateria_tutor.py --so oac-cache-misses oac-forwarding oac-associativa oac-beq`, pelo fluxo completo do site. A resposta crua está em `eval/results/bateria-oac-2026-11-18.json`. O gemini-3.6-flash e o gemini-flash-latest deram 503; respondeu o gemini-3.1-flash-lite (modo socrático, que não entrega o resultado final).

| Pergunta | Fontes recuperadas | Resultado (leitura da equipe) |
|---|---|---|
| Misses de 1, 4, 8, 5, 20, 17 em 16 blocos | u04, u03, s06, u05 | Correta: índice = bloco mod 16, primeira referência é compulsória; pede a tabela ao aluno, sem dar o 6 |
| Hazard de dados e quando o forwarding não resolve | u02, s05, s07 | Correta: load-use, dado só no fim do MEM; pede o diagrama do lw/add |
| Associativa por conjunto × mapeamento direto | u04, s06, u03, s07 | Correta: um lugar por bloco × qualquer via do conjunto; falta de conflito com cache vazia |
| Datapath monociclo no beq | u01, s04 | Correta: comparação na ULA (Zero), somador de desvio, porta Branch·Zero no mux do PC, nada escrito |

**Limites:** uma execução por pergunta, avaliadas só pela equipe, com o modelo de reserva. O modelo local não foi testado. Nas referências exibidas, a `fonte` dos blocos s04 e s05 aparece partida ("2026"; "2026; a animação anexa não foi aberta"); o problema já existia e não foi corrigido aqui.

## 6. Licenças e restrições

- **Prova, lista, foto e anotações (material de turma):** licença não declarada. Originais fora do repositório; enunciados só parafraseados. Para publicar a transcrição literal, registre a autorização em `fontes.json` (`autorizacao_transcricao`, como em SD) e no campo `publicacao_transcricao` dos blocos.
- **Foto de aula:** mostra uma pessoa. Nunca versionar a imagem.
- **Livro de Patterson & Hennessy e slides da editora:** protegidos. Não copiar, não fragmentar, não indexar, nem no Supabase sem autorização da editora.
- **CC BY 4.0 (manual do RISC-V, cartão de referência):** ao ingerir trechos, manter atribuição.
- **CC BY-SA 4.0 (MC404 Unicamp):** atribuição e mesma licença no trecho derivado.
- **CC BY-NC-SA 4.0 (MIT OCW):** só uso não comercial.
- **CS 61C e livro de Borin:** sem licença aberta; só indicar como leitura.
- **Notas da equipe:** texto original do TutorON.

## 7. Pendências

1. Revisão humana interna dos 37 blocos (`revisao_humana`), começando pelos corrigidos e pendentes (t03–t09, s01, s02, s04, s05, s07) e pela tabela de sinais (n07); das anotações de 2025.2, primeiro u01, u02, u03 e u05 (corrigidas).
2. Confirmar com o professor o item d da versão A e a leitura do riscado da versão B (t06, t07), e se a disciplina aceita as correções de t03, t04, t05 e t09.
3. Autorização da equipe para publicar transcrições literais da prova e da lista (hoje, parafraseadas).
4. Validar respostas reais com o Gemini e com o modelo local (as quatro perguntas de `backend/tests/test_disciplinas.py` e as de `tests_acervo/test_disciplina_oac.py`). Só depois mudar a `situacao` no cadastro para `beta`.
5. Simular os Projetos 1 e 2 no Icarus Verilog para confirmar "Simulation succeeded" (s04, s05).
6. Confirmar o plano de ensino atual: E/S, barramentos, microprogramação e paralelismo estão na ementa de 2011 e não têm bloco.
7. Avaliar a ingestão do cartão de referência e de trechos do manual RISC-V (CC BY 4.0) e dos slides de MC404 (CC BY-SA 4.0), com atribuição.
8. Bateria de relevância: desde 18/11/2026 tem 4 perguntas de OAC (cache, hazard, associatividade, beq). Ampliar para os tópicos 02, 05, 09 e 10.

## 8. Como atualizar

1. Edite ou crie `materiais/<arquivo>.md` com o cabeçalho completo (veja qualquer bloco). Para resolução de exercício da turma, preencha `status_resolucao` (`validada`, `corrigida` ou `pendente_professor`) e escreva o status também no texto.
2. Fonte nova: cadastre em `fontes.json` e nas tabelas das seções 3 e 5 (o teste confere que todo id aparece aqui).
3. Rode `.venv\Scripts\python -m acervo.disciplinas oac --embeddings` e os testes. `test_itens_gerados_estao_atualizados` falha se o índice não foi refeito.
4. Para tirar um bloco da busca sem apagá-lo, mude `curadoria:` para `candidato` ou `rejeitado` e refaça o índice.
