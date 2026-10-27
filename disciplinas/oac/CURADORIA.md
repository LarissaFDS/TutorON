# Organização e Arquitetura de Computadores — curadoria do acervo

Situação: **em validação** desde 27/10/2026. A disciplina está cadastrada, com acervo e índice próprios, e passa pelo mesmo fluxo da IA. Enquanto a validação não acontecer, o servidor recusa perguntas de OAC no atendimento normal (403, a mesma barreira usada por SD antes do beta). Para testes autorizados, use `TUTORON_LIBERAR_EM_VALIDACAO=oac` (veja [`docs/DISCIPLINAS.md`](../../docs/DISCIPLINAS.md)).

| Item | Estado em 27/10/2026 |
|---|---|
| Cadastro, acervo (21 blocos) e índice híbrido (`bge-m3`) | **Feitos** |
| Contas, codificações e código RISC-V das resoluções | **Conferidos por código** (`tests_acervo/test_disciplina_oac.py`) |
| Revisão humana interna dos 21 blocos | **Pendente** (`revisao_humana: pendente` em todos) |
| Autorização para publicar transcrições literais da prova e da lista | **Não dada**: os blocos trazem enunciados parafraseados e os dados, não a transcrição |
| Aprovação do professor | **Não declarada**; nenhum bloco tem `revisao_professor: sim` |
| Plano de ensino atual | **Não localizado**; só a ementa de 2011 (seção 1) |
| Página do Notion da turma | **Inacessível** neste ambiente (seção 4) |
| Validação das respostas da IA | **Parcial**: 4 perguntas com o Gemini, todas corretas (seção 5.1); modelo local não testado |

- Catálogo legível por máquina (fonte da verdade): [`fontes.json`](fontes.json)
- Blocos do acervo (um arquivo por bloco): [`materiais/`](materiais/). `t*` são materiais da turma; `n*` são notas da equipe
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
| `oac-13-datapath-controle`: monociclo, unidade de controle | Confirmado pela turma | Slide do cap. 4; ementa ("organização interna do processador") | 4.3, 4.4 | n07 |
| `oac-14-pipeline-hazards` | Fundamental no livro, não confirmado | Ementa ("microarquiteturas") | 4.5–4.9 | n08 |
| `oac-15-hierarquia-memoria`: cache, memória virtual, TLB | Fundamental; está na ementa | Ementa ("hierarquia de memória") | 5.1–5.8 | n09 |
| `oac-16-paralelismo` | Complementar ou dependente da ementa | Ementa ("arquiteturas não convencionais") | 6 | nenhum |

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
| `ufal-oac-notion` Notion da turma | — | — | — | — | — | — | — | — | — | referência | indisponível |

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

Não inventariados: a **página do Notion da turma** (`ufal-oac-notion`), que respondeu 404 à integração do Notion deste ambiente em 27/10/2026. Para incluí-la, compartilhe a página com a integração ou exporte o conteúdo em Markdown.

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

1. Revisão humana interna dos 21 blocos (`revisao_humana`), começando pelos corrigidos e pendentes (t03–t09) e pela tabela de sinais (n07).
2. Confirmar com o professor o item d da versão A e a leitura do riscado da versão B (t06, t07), e se a disciplina aceita as correções de t03, t04, t05 e t09.
3. Autorização da equipe para publicar transcrições literais da prova e da lista (hoje, parafraseadas).
4. Validar respostas reais com o Gemini e com o modelo local (as quatro perguntas de `backend/tests/test_disciplinas.py` e as de `tests_acervo/test_disciplina_oac.py`). Só depois mudar a `situacao` no cadastro para `beta`.
5. Inventariar a página do Notion da turma (compartilhar com a integração ou exportar).
6. Confirmar o plano de ensino atual: E/S, barramentos, microprogramação e paralelismo estão na ementa de 2011 e não têm bloco.
7. Avaliar a ingestão do cartão de referência e de trechos do manual RISC-V (CC BY 4.0) e dos slides de MC404 (CC BY-SA 4.0), com atribuição.
8. Rodar a bateria de relevância (`eval/relevancia.py`) com perguntas de OAC rotuladas. Hoje ela só tem PAA e SD.

## 8. Como atualizar

1. Edite ou crie `materiais/<arquivo>.md` com o cabeçalho completo (veja qualquer bloco). Para resolução de exercício da turma, preencha `status_resolucao` (`validada`, `corrigida` ou `pendente_professor`) e escreva o status também no texto.
2. Fonte nova: cadastre em `fontes.json` e nas tabelas das seções 3 e 5 (o teste confere que todo id aparece aqui).
3. Rode `.venv\Scripts\python -m acervo.disciplinas oac --embeddings` e os testes. `test_itens_gerados_estao_atualizados` falha se o índice não foi refeito.
4. Para tirar um bloco da busca sem apagá-lo, mude `curadoria:` para `candidato` ou `rejeitado` e refaça o índice.
