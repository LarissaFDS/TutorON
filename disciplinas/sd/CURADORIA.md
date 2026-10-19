# Sistemas Digitais — curadoria do acervo

Situação: **em validação**. A curadoria inicial (19/10/2026) **não foi validada pelo professor**. Toda a seleção abaixo é uma proposta da equipe para revisão.

- Catálogo legível por máquina (fonte da verdade): [`fontes.json`](fontes.json)
- Blocos do acervo (um arquivo por bloco): [`materiais/`](materiais/)
- Gerados a partir dos blocos (não editar à mão): [`acervo/itens.json`](acervo/itens.json) e [`acervo/indice.json`](acervo/indice.json)
- Regras de rigor que o tutor segue em SD: [`rigor.md`](rigor.md)
- Como o TutorON usa o acervo e como cadastrar outra disciplina: [`docs/DISCIPLINAS.md`](../../docs/DISCIPLINAS.md)

## 1. Ementa: o que foi encontrado e o que não foi

Não localizamos o **plano de ensino atual** da disciplina de Sistemas Digitais da UFAL. Encontramos duas ementas oficiais de 2011, nos projetos pedagógicos publicados pela UFAL:

| Curso | Disciplina | Ementa (resumo fiel) |
|---|---|---|
| Ciência da Computação (matriz 2011), `ufal-ppc-cc-2011` | CCOM019 Circuitos Digitais, 30 h | Sistemas numéricos e códigos; portas lógicas e álgebra booleana; circuitos combinacionais e sequenciais; aritmética binária (operações e circuitos); conversão D/A e A/D. |
| Engenharia de Computação (2011), `ufal-ppc-ecomp-2011` | ECOM019 Sistemas Digitais, 60 h | Metodologias de desenvolvimento; análise e síntese de circuitos sequenciais (síncronos e assíncronos); diagramas e tabelas de estados; lógica programável; conversores e teorema da amostragem; máquinas de estados finitos; linguagem de descrição de hardware; hardware reconfigurável; controladores. |

As listas e provas recebidas (AV1, AV2, Prova 1, Prova 2 e REAV) cobrem a união das duas ementas e usam o vocabulário do livro de Vahid ("FSM de alto nível", "bloco operacional", "bloco de controle", projeto RTL). Por isso, tratamos os materiais da disciplina como a melhor evidência do conteúdo cobrado hoje. **Limitação:** as ementas de 2011 podem estar desatualizadas, e o livro adotado não foi confirmado com o professor.

### Tópicos e classificação

| Assunto (`assunto` nos blocos) | Classificação | Evidência |
|---|---|---|
| `sd-01-numeracao-aritmetica` — bases, complemento de 2, aritmética binária, códigos | Fundamental | Ementa CCOM019; AV1 Q1–Q4 |
| `sd-02-algebra-booleana-portas` — álgebra booleana, De Morgan, portas | Fundamental | Ementa CCOM019; AV1 Q5–Q6 |
| `sd-03-simplificacao-karnaugh` — mapas de Karnaugh, irrelevâncias | Fundamental | AV1 Q7; monitoria de somadores |
| `sd-04-blocos-combinacionais` — MUX, decodificador, display, deslocador | Fundamental | AV1 Q8–Q13 e Q18; REAV Q1 |
| `sd-05-circuitos-aritmeticos` — somadores, subtratores, comparadores, overflow | Fundamental | AV1 Q14–Q17; Provas 1 e REAV |
| `sd-06-analise-temporal` — atraso de propagação, formas de onda | Fundamental | AV1 Q21–Q23; Prova 1 Q2 |
| `sd-07-latches-flip-flops` | Fundamental | Ementas; AV2 Q1; Prova 2 Q1 |
| `sd-08-registradores-contadores` | Fundamental | AV2 Q3 e Q7; Prova 2 Q3 |
| `sd-09-maquinas-de-estados` | Fundamental | Ementa ECOM019; AV2 Q2; Prova 2 Q2 |
| `sd-10-projeto-rtl` — FSM de alto nível, bloco operacional e de controle | Fundamental para a AV2 | AV2 Q4, Q5 e Q8; Prova 2 Q4; REAV Q2 e Q4 |
| `sd-11-hdl-vhdl` | Dependente da ementa | Ementa ECOM019; arquivo VHDL do Fibonacci; sem questão de prova recebida |
| `sd-12-conversores-memorias` — D/A, A/D, amostragem, ROM/RAM | Complementar / dependente da ementa | Ementas; Prova 1 Q1 (D/A); memórias só aparecem dentro do RTL (REAV Q2) |

## 2. Critérios e matriz de curadoria

Cada fonte recebeu notas de 1 a 5 (campo `notas` em `fontes.json`) em: **autoridade** (universidade, autor reconhecido), **cobertura** (tópicos da tabela acima), **profundidade** (nível universitário), **didática** (explicações, exemplos e exercícios), **aderência** (ao conteúdo cobrado na UFAL), **acessibilidade** (dá para ler e processar?), **reutilização** (licença conhecida permite incluir?) e **utilidade para tutoria** (ajuda a responder dúvidas concretas?).

Prioridades: **alta** compõe o acervo inicial; **média** complementa ou preenche lacunas; **referência** é para consulta e comparação, sem ingestão.

| Fonte | Aut. | Cob. | Prof. | Did. | Ader. | Acess. | Reut. | Tut. | Prioridade | Uso |
|---|---|---|---|---|---|---|---|---|---|---|
| `ufal-sd-lista-av1` Lista AV1 | 5 | 4 | 4 | 4 | 5 | 4 | 2 | 5 | alta | no acervo |
| `ufal-sd-lista-av2` Lista AV2 | 5 | 4 | 4 | 3 | 5 | 3 | 2 | 5 | alta | no acervo |
| `ufal-sd-prova1` Prova 1 | 5 | 3 | 4 | 3 | 5 | 4 | 2 | 5 | alta | no acervo |
| `ufal-sd-prova2` Prova 2 | 5 | 3 | 4 | 3 | 5 | 3 | 2 | 5 | alta | no acervo |
| `ufal-sd-reav` Reavaliação | 5 | 3 | 4 | 3 | 5 | 2 | 2 | 5 | alta | no acervo |
| `ufal-sd-somadores` Somadores (monitoria) | 4 | 2 | 3 | 4 | 5 | 4 | 2 | 4 | alta | no acervo |
| `ufal-sd-fibonacci-vhdl` VHDL do Fibonacci | 2 | 2 | 3 | 3 | 5 | 5 | 2 | 4 | média | no acervo, com ressalvas |
| `ufal-sd-resolucao-prova2` Resolução manuscrita da Prova 2 | 4 | 2 | 3 | 3 | 5 | 1 | 2 | 4 | média | candidato |
| `ufal-sd-monitorias-video` Gravações de monitoria | 4 | 3 | 3 | 4 | 5 | 1 | 1 | 4 | média | candidato |
| `kuphaldt-lec-vol4` Lessons in Electric Circuits, vol. IV | 4 | 5 | 3 | 5 | 4 | 5 | 4 | 4 | alta | citada |
| `free-range-vhdl` Free Range VHDL | 4 | 2 | 4 | 5 | 4 | 5 | 5 | 4 | alta | citada |
| `wikibooks-digital-circuits` Digital Circuits (Wikibooks) | 3 | 4 | 3 | 3 | 4 | 5 | 5 | 3 | média | citada |
| `wikilivros-eletronica-digital` Eletrônica Digital (Wikilivros) | 2 | 4 | 2 | 3 | 4 | 5 | 5 | 3 | média | citada |
| `mit-ocw-6004` MIT 6.004 | 5 | 4 | 5 | 4 | 3 | 4 | 3 | 3 | média | citada |
| `sim-digital-hneemann` Simulador Digital | — | — | — | — | — | — | — | — | média | citada (ferramenta) |
| `vahid-sistemas-digitais` Vahid, *Sistemas Digitais* | 5 | 5 | 5 | 5 | 5 | 2 | 1 | 5 | referência | protegido |
| `tocci-sistemas-digitais` Tocci, *Sistemas Digitais* | — | — | — | — | — | — | — | — | referência | protegido |
| `uff-apostila-circuitos-digitais` Apostila UFF | 4 | 5 | 4 | 4 | 4 | 5 | 1 | 4 | referência | sem licença |
| `ufrgs-circuitos-digitais` Apostila UFRGS | 4 | 3 | 3 | 4 | 4 | 5 | 1 | 3 | referência | sem licença |
| `nand2tetris` Nand2Tetris | 4 | 2 | 3 | 5 | 2 | 4 | 1 | 2 | referência | licença não determinada |
| `ufal-ppc-cc-2011` Ementa CCOM019 | 5 | 3 | 1 | 1 | 4 | 5 | 3 | 1 | referência | ementa |
| `ufal-ppc-ecomp-2011` Ementa ECOM019 | 5 | 3 | 1 | 1 | 4 | 5 | 3 | 1 | referência | ementa |
| `ufpr-ci1068` Ficha UFPR CI1068 | — | — | — | — | — | — | — | — | referência | comparação de ementa |
| `sim-logisim-evolution` Logisim-evolution | — | — | — | — | — | — | — | — | referência | ferramenta |
| `sim-circuitverse` CircuitVerse | — | — | — | — | — | — | — | — | referência | ferramenta |
| `ufal-sd-lista4-projetos` Lista 4 — projetos (.docx) | — | — | — | — | — | — | — | — | referência | indisponível |

### Por que esta seleção

- **Materiais da própria disciplina vêm primeiro.** Como em PAA, eles mostram como o conteúdo é cobrado. Transcrevemos os enunciados e, onde foi possível conferir, escrevemos resoluções. Cada resolução com resultado afirmado é conferida por código em `tests_acervo/test_disciplinas.py`: Karnaugh, equações da FSM da Prova 2, catracas da REAV, display de 7 segmentos, contas do D/A e subtrator.
- **Lacunas preenchidas por notas da equipe** (`n01` a `n12`). Slides e enunciados não bastam para tutoria: faltava o *procedimento* (como agrupar no Karnaugh, como montar a tabela de estados, como passar da FSM de alto nível ao bloco operacional). As notas foram escritas pela equipe com auxílio de IA, com texto próprio, e citam fontes abertas como leitura complementar. Não são material do professor.
- **Fontes abertas citadas, não copiadas.** Kuphaldt (Creative Commons) e Free Range VHDL (CC BY-SA 3.0) permitem reutilização com atribuição e são as primeiras candidatas a ingestão de capítulos. Nesta entrega elas ficam só citadas, para evitar uma cópia em massa sem revisão.
- **Livros protegidos ficam só como referência.** O livro de Vahid parece ser o texto-base de fato, mas é protegido. A cópia digitalizada local não foi versionada nem ingerida. Se a equipe tiver autorização, ela pode ir para o Supabase privado, como o livro de PAA. Para isso, a tabela `chunks` precisa de uma coluna de disciplina antes (veja docs/DISCIPLINAS.md).
- **Apostilas universitárias sem licença** (UFF, UFRGS) são de ótima qualidade em português, mas ficam como referência para a equipe consultar.
- **Duplicações evitadas:** REAV Q3 e Prova 1 Q5 são a mesma questão (o bloco da REAV remete à Prova 1), e AV2 Q1–Q4 repetem a Prova 2 (o bloco da AV2 remete ao da Prova 2).

## 3. Inventário do acervo (blocos)

Situação da curadoria: `aprovado` entra na busca com confiabilidade **média** (como as correções derivadas de PAA); `candidato` e `rejeitado` ficam fora. Nenhum bloco está com `revisao_professor: sim`, então nenhum tem confiabilidade alta.

| Arquivo | id | Assunto | Tipo | Curadoria | Observação |
|---|---|---|---|---|---|
| m01 | `sd-av1-q01-07` | numeração/booleana/Karnaugh | lista | aprovado | figura da Q5 não transcrita |
| m02 | `sd-av1-q08-13` | blocos combinacionais | lista | aprovado | figura da Q9 não transcrita |
| m03 | `sd-av1-q14-18` | aritméticos/display | lista | aprovado | — |
| m04 | `sd-av1-q19-25` | aplicações/temporal | lista | aprovado | Q21–Q25 dependem de figuras; só enunciados |
| m05 | `sd-av2-q01-04-07` | sequenciais | lista | aprovado | figuras não transcritas |
| m06 | `sd-av2-q05-06-08` | RTL | lista | aprovado | posição dos sensores da Q6 suposta (sinalizada) |
| m07 | `sd-prova1` | aritméticos | prova | aprovado | circuito da Q2 em figura |
| m08 | `sd-prova2-q1-2` | FSM | prova | aprovado | transições lidas da figura |
| m09 | `sd-prova2-q3-4` | RTL | prova | aprovado | esboço; Q3 depende da figura |
| m10 | `sd-reav-q1-q3` | combinacionais | prova | aprovado | — |
| m11 | `sd-reav-q2-q4` | RTL | prova | aprovado | divergência 25 × 26 sinalizada |
| m12 | `sd-somadores-monitoria` | aritméticos | material de estudo | aprovado | — |
| m13 | `sd-vhdl-fibonacci-controle` | VHDL | resolução | aprovado | ressalvas sobre saídas registradas |
| n01–n12 | `sd-nota-*` | um por tópico | material de estudo | aprovado | notas da equipe; revisão humana pendente |

## 4. Licenças e restrições

- **Materiais da disciplina (UFAL):** sem licença declarada. O repositório é público, por isso **os PDFs/DOCX/vídeos originais não foram versionados**; só entram as transcrições necessárias para a busca. Assim como no acervo de PAA, a equipe precisa **confirmar com o professor e os monitores** que pode publicar essas transcrições. Se não puder, mova `materiais/m*.md` para fora do Git e gere os índices localmente.
- **Vídeos de monitoria:** contêm voz de pessoas; não publicar sem consentimento.
- **Notas da equipe:** texto original do TutorON.
- **CC BY-SA (Wikibooks, Wikilivros, Free Range VHDL):** ao ingerir trechos, manter atribuição e a mesma licença no trecho derivado.
- **CC BY-NC-SA (MIT OCW):** só uso não comercial.
- **Vahid, Tocci, apostilas UFF/UFRGS, Nand2Tetris:** não copiar para o repositório.

## 5. Pendências

1. Revisão do professor (ou de monitor) dos 25 blocos, sobretudo das resoluções e das notas. Ao revisar, marque `revisao_professor: sim` no cabeçalho para promover o bloco a confiabilidade alta.
2. Descrever as figuras que faltam (AV1 Q5, Q9, Q21–Q25; AV2 Q3, Q4, Q7; Prova 1 Q2; Prova 2 Q1 e Q3).
3. Transcrever a resolução manuscrita da Prova 2 e as gravações de monitoria (candidatos).
4. Confirmar o plano de ensino atual e o livro adotado.
5. Gerar o índice com embeddings (`python -m acervo.disciplinas sd --embeddings`, com o `bge-m3` no Ollama). Hoje o índice é **léxico**, porque o `bge-m3` não estava instalado nesta máquina.
6. Avaliar a ingestão de capítulos de Kuphaldt (vol. IV) e Free Range VHDL, com atribuição.

## 6. Como atualizar

1. Edite ou crie `materiais/<arquivo>.md` com o cabeçalho completo (veja qualquer bloco existente). O texto de cada bloco deve ficar abaixo de ~2.000 caracteres: o tutor corta trechos maiores que 2.200.
2. Se a fonte for nova, cadastre-a em `fontes.json` e na tabela da seção 2 (o teste confere que todo id do catálogo aparece aqui).
3. Rode `python -m acervo.disciplinas sd` (ou com `--embeddings`) e os testes. O teste `test_itens_gerados_estao_atualizados` falha se o índice não foi refeito.
4. Para retirar um bloco da busca sem apagá-lo, mude `curadoria:` para `candidato` ou `rejeitado` e refaça o índice.
