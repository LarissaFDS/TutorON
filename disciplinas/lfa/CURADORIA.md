# Curadoria — Linguagens Formais, Autômatos e Computabilidade (`lfa`, ECOM014)

Situação: **MVP** desde 21/11/2026, sem aviso, depois de cumprido o critério de liberação (veja `docs/DISCIPLINAS.md`).

## Disciplina e ementa

- ECOM014, 3º semestre, 60 h (40 teóricas e 20 práticas), Engenharia de Computação da UFAL; corresponde a Teoria da Computação em Ciência da Computação.
- **Ementa conferida** no PPC de 2014, p. 30 (`ufal-ppc-ecomp-2014`): alfabeto; linguagens e operações; gramáticas formais e autômatos; tipos de linguagens e hierarquia de Chomsky; autômatos finitos e de pilha; contagem e enumerabilidade; tese de Church-Turing; modelos de computação; teoria das funções recursivas; máquinas de Turing; decidibilidade; problema da parada; redutibilidade; complexidade computacional. Bibliografia básica: Menezes, Hopcroft, Sipser; complementar: Diverio e Menezes, Lewis e Papadimitriou, Carrol e Long, Vieira, Hein.
- **Autoria (correção):** a lista de 2014.1 cujo arquivo tem o nome de um aluno é da **Profa. Eliana (UFAL)**; o aluno só a resolveu à mão. A Prova 2 de 2017.1 também é da Profa. Eliana. A atividade de 2015.1 é do Prof. Thyago Tenório Martins de Oliveira. A lista de decidibilidade de 2016.2 não identifica o professor.

| Assunto | Ementa | Blocos na busca |
|---|---|---|
| `lfa-01-linguagens-chomsky` | alfabeto, linguagens, hierarquia de Chomsky | s01–s02 |
| `lfa-02-automatos-finitos` | autômatos finitos | s03–s07 |
| `lfa-03-expressoes-gramaticas-regulares` | gramáticas formais e autômatos | s08–s10 |
| `lfa-04-nao-regularidade` | autômatos finitos (limites) | s11–s13 |
| `lfa-05-livres-de-contexto` | autômatos de pilha, gramáticas | s14–s18 |
| `lfa-06-maquinas-de-turing` | máquinas de Turing, Church-Turing, modelos | s19–s22 |
| `lfa-07-funcoes-recursivas-programas` | funções recursivas, modelos de computação | s23–s26 |
| `lfa-08-decidibilidade-parada` | decidibilidade, contagem e enumerabilidade, parada | s27–s30 |
| `lfa-09-reducao-complexidade` | redutibilidade, complexidade | s31 |

## Fronteiras

| Tópico | Aqui | Aprofundado em |
|---|---|---|
| P, NP, NP-completude, análise de algoritmos | definição das classes | Projeto e Análise de Algoritmos (`paa`) |
| Lógica proposicional e de predicados | uso em provas | Lógica Aplicada à Computação |
| Conjuntos, relações, indução, contagem | como ferramenta | Matemática Discreta |

`tests_acervo/test_disciplina_lfa.py` testa o isolamento com PAA, Lógica e Discreta nos dois sentidos.

## Material protegido e dados pessoais

- **A lista de 2014.1 traz nome, matrícula e resolução manuscrita de um aluno.** Não foi versionada; nenhum dado pessoal entrou no acervo. O teste guarda só hash do nome e procura a matrícula.
- As apostilas da Profa. Simone Prado trazem o e-mail da autora: não copiado. Não declaram licença: só paráfrase.
- Sipser, Menezes, Hopcroft e Diverio e Menezes não foram incluídos nem transcritos; o JFLAP não foi baixado. O trecho de Turing (1950) fica só no catálogo.
- PDFs, .doc, .docx e imagens não estão no repositório.
- Listas e provas não têm licença declarada: os blocos são paráfrases com resolução própria. **Confirmar com a equipe** se os professores autorizam a transcrição.

## Fontes (`fontes.json`)

`ufal-ppc-ecomp-2014`, `ufal-eliana-lista-2014-1`, `ufal-eliana-prova2-2017-1`, `ufal-lista-decidibilidade-2016-2`, `ufal-thyago-atividade-2015-1`, `unesp-prado-apostilas-tc`, `lee-sipser-notas-2012`, `mit-ocw-18-404j`, `openlogic-slc`, `jflap`, `turing-1950-imitation-game`, `sipser-livro`, `menezes-livro`, `hopcroft`, `diverio-menezes`.

## Blocos

| Bloco | Status | Verificação |
|---|---|---|
| `lfa-alfabetos-cadeias-operacoes` | validada | conferida_por_codigo |
| `lfa-hierarquia-de-chomsky` | — | exemplos_conferidos |
| `lfa-afd-numero-par-de-zeros` | — | conferida_por_codigo |
| `lfa-afd-subcadeia-aa-bb-simulacao` | — | conferida_por_codigo |
| `lfa-afn-para-afd-subconjuntos` | — | conferida_por_codigo |
| `lfa-afn-para-afd-exemplos-corrigidos` | corrigida | conferida_por_codigo |
| `lfa-minimizacao-afd-tabela-de-pares` | validada | conferida_por_codigo |
| `lfa-expressoes-regulares-sem-aa-cada-a-com-b` | validada | conferida_por_codigo |
| `lfa-gramatica-regular-e-conversoes` | — | conferida_por_codigo |
| `lfa-fechamento-uniao-intersecao-complemento` | — | conferida_por_codigo |
| `lfa-lema-do-bombeamento-anbn` | — | conferida_por_codigo |
| `lfa-bombeamento-mesmo-numero-a-b-corrigido` | corrigida | conferida_por_codigo |
| `lfa-linguagem-regular-vazia-finita-infinita` | validada | conferida_por_codigo |
| `lfa-glc-derivacao-arvore-corrigido` | corrigida | conferida_por_codigo |
| `lfa-ambiguidade-gramatica-linguagem-inerente` | corrigida | conferida_por_codigo |
| `lfa-simplificacao-glc-producoes-vazias-unitarias` | validada | conferida_por_codigo |
| `lfa-forma-normal-de-chomsky` | validada | conferida_por_codigo |
| `lfa-automato-com-pilha-anbn` | validada | conferida_por_codigo |
| `lfa-maquina-de-turing-definicao-perguntas` | pendente_professor | exemplos_conferidos |
| `lfa-mt-mesmo-numero-de-0-e-1` | validada | conferida_por_codigo |
| `lfa-mt-inserir-separador-entre-0-e-1` | validada | conferida_por_codigo |
| `lfa-tese-de-church-turing-modelos` | — | parcial |
| `lfa-lpm-divisao-inteira-loop-sem-goto` | corrigida | conferida_por_codigo |
| `lfa-lpm-para-passo-2-e-while-com-goto` | validada | conferida_por_codigo |
| `lfa-funcoes-recursivas-primitivas-composicao` | validada | conferida_por_codigo |
| `lfa-prova2-funcao-f-quatro-componentes` | pendente_professor | conferida_por_codigo |
| `lfa-decidivel-vs-reconhecivel-diagonalizacao` | validada | parcial |
| `lfa-decidiveis-a-er-afd-todas-equivalencia` | validada | conferida_por_codigo |
| `lfa-lista-decidibilidade-afd-m-figura` | pendente_professor | sem_resolucao |
| `lfa-problema-da-parada-indecidivel` | — | parcial |
| `lfa-reducao-por-mapeamento-e-complexidade` | — | parcial |

Fora da busca (`nota_da_equipe_ia`, `candidato`): `lfa-nota-bombeamento-livres-de-contexto`.

## Erros encontrados no material

- Apostila TC02, ex. 09: conjunto de finais sem o estado que reúne q1 e qf, e o vazio escrito como lambda. Ex. 11: conjunto de finais copiado do exemplo anterior.
- TC02, ex. 17: bombeamento com n = 4 e w = aabb, e casos escolhidos em vez de toda decomposição.
- TC03, ex. 04: conclui ambiguidade a partir de derivação à esquerda e à direita da mesma árvore. Ex. 09: uma gramática ambígua apresentada como prova de ambiguidade inerente.
- Lista 2014.1, Q1 (resolução do aluno): o programa calcula o teto de X/Y, não a divisão inteira.

## Resoluções e conferência

Todas as resoluções são da equipe TutorON, **não gabarito do professor**. `tests_acervo/lfa_verif.py` simula AFD, AFN (subconjuntos), minimização, ER (Thompson), gramáticas (Earley e contagem de derivações), autômato com pilha, máquina de Turing, programas LPM e funções recursivas primitivas.

Revisão humana e do professor: **pendentes** em todos os blocos.
