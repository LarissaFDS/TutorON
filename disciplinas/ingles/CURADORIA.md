# Inglês Instrumental — curadoria do acervo

Situação: **MVP** desde 20/11/2026, sem aviso: liberada no atendimento normal depois do critério da seção 6. A disciplina usa o mesmo fluxo e a mesma IA das outras: só acrescenta acervo, `rigor.md` e exemplos.

| Item | Estado em 20/11/2026 |
|---|---|
| Cadastro, acervo (12 blocos) e índice híbrido (`bge-m3`) | **Feitos**; os 12 blocos estão na busca; nenhuma nota de IA |
| Respostas dos exercícios | **Conferidas no próprio texto** (`tests_acervo/test_disciplina_ingles.py`) |
| Gabarito do professor | **Não existe**: a prova só tem o texto, sem questões |
| Autoria e licença do texto da prova | **Conferidas**: Pavela (2016), CC BY-NC 4.0; no repositório, só trechos curtos |
| Professor da turma | **Não identificado** |
| Revisão humana interna | **Pendente** em todos os blocos |
| Aprovação do professor | **Não declarada**; nenhum bloco tem `revisao_professor: sim` |
| Ementa oficial | **Conferida** no PPC de 2014 (seção 1) |

- Catálogo legível por máquina: [`fontes.json`](fontes.json)
- Blocos: [`materiais/`](materiais/), um exercício por arquivo
- Gerados a partir dos blocos (não editar à mão): [`acervo/itens.json`](acervo/itens.json) e [`acervo/indice.json`](acervo/indice.json)
- Regras de rigor do tutor: [`rigor.md`](rigor.md)
- Trechos em inglês citados (para os testes): [`tests_acervo/ingles_trechos.json`](../../tests_acervo/ingles_trechos.json)

## 1. Disciplina, ementa e material

O PPC de Engenharia de Computação de 2014 (`ufal-ppc-ecomp-2014`, p. 19 e 22 do PDF) lista **ECOM001 Inglês Instrumental**, 1º semestre, 60 h (40 teóricas e 20 práticas). Ementa, literal: "Estudo de textos específicos da área de computação visando compreensão. Aspectos gramaticais e morfológicos pertinentes à compreensão. Desenvolvimento e ampliação das estratégias de leitura. Conscientização do processo de leitura. Exploração de informações não-lineares, cognatos e contexto. Seletividade do tipo de leitura (Skimming/Scanning). Levantamento de hipótese sobre texto (título e subtítulos). Abordagem de pontos gramaticais problemáticos para leitura. Uso do dicionário como estratégia-suporte de leitura: tipos, recursos, prática." Bibliografia básica: Pinto (*Grasping the Meaning*), Dubin (*Reading by All Means*) e Ediger (*Reading for Meaning*); complementar: dicionários Michaelis, Houaiss e Oxford Escolar.

Material da turma: um só arquivo, `Cópia de Texto - Prova de Proficiência.docx` (`ufal-ingles-texto-prova`), com o título e seis parágrafos de um artigo em inglês, sem questões. O texto é o começo do artigo de revisão de **Roman Pavela**, *Plant Protection Science* 52(4): 229–241, 2016 (`pavela-2016-pps`), publicado em acesso aberto com **CC BY-NC 4.0** (licença conferida na página do artigo). O arquivo não diz o professor, o semestre nem a turma. Os metadados do .docx trazem o nome de uma pessoa, que não foi registrado; um teste confere que ele não está no repositório.

Observação: a ementa fala de "textos específicos da área de computação", mas o texto da prova é de agricultura e saúde. O texto de computação vem de **Wilson et al., *Best Practices for Scientific Computing*** (PLOS Biology, 2014, **CC BY 4.0**, `wilson-2014-best-practices`).

### Tópicos, evidência e blocos

**Ementa** = está no texto literal da ementa; **interpretação** = é a leitura da equipe para "aspectos gramaticais e morfológicos" e "pontos gramaticais problemáticos", a confirmar com o professor.

| Assunto | Evidência | Blocos na busca |
|---|---|---|
| `ingles-01-estrategias-leitura` | Ementa (skimming, scanning, hipótese pelo título) | `ingles-prova-skimming-hipotese`, `ingles-prova-scanning` |
| `ingles-02-cognatos-falsos-cognatos` | Ementa (cognatos e contexto) | `ingles-cognatos-falsos-cognatos` |
| `ingles-03-grupos-nominais` | Interpretação (aspectos gramaticais) | `ingles-grupos-nominais` |
| `ingles-04-afixos-formacao-palavras` | Ementa (aspectos morfológicos) | `ingles-afixos` |
| `ingles-05-referencia-pronominal` | Interpretação | `ingles-referencia-pronominal` |
| `ingles-06-marcadores-discurso` | Interpretação | `ingles-marcadores-discurso` |
| `ingles-07-tempos-verbais-voz-passiva` | Interpretação (pontos gramaticais problemáticos) | `ingles-voz-passiva`, `ingles-tempos-verbais` |
| `ingles-08-dicionario-contexto` | Ementa (uso do dicionário: tipos, recursos, prática) | `ingles-dicionario-contexto` |
| `ingles-09-leitura-artigos-cientificos` | Ementa (textos da área, informações não lineares) e texto da prova | `ingles-estrutura-artigo-cientifico`, `ingles-compreensao-texto-computacao` |

Todos os exercícios usam trechos do texto da prova (o único material da turma), menos `ingles-compreensao-texto-computacao`, que usa só Wilson et al. Por isso todos os tópicos têm bloco na busca. Os exercícios são da equipe, escritos com IA e com cada resposta verificável refeita por código; seguem a mesma regra das resoluções de Variáveis Complexas (`material_da_disciplina`, `curadoria: aprovado`, revisão humana pendente).

## 2. Fronteiras

| Tema | Tratamento |
|---|---|
| Metodologia da Pesquisa (ECOM018: estrutura e escrita de trabalho científico) | Não está cadastrada. Aqui só a **leitura** do artigo em inglês (IMRaD, *abstract*, citações autor-data como pistas de compreensão), não a escrita nem as normas |
| Conteúdo técnico dos textos (boas práticas de software, inseticidas) | Fora: o tutor explica a leitura, não ensina a área. Perguntas de programação vão para ED ou PAA |

O teste `test_isolamento_com_disciplinas_de_computacao` confere os dois sentidos com ED, BD e PAA. Os índices não têm blocos em comum com nenhuma disciplina.

## 3. Status dos exercícios e verificação

A prova não tem questões nem gabarito, então nenhum exercício está como `corrigida`.

- `validada` (a resposta é um fato do texto, conferido por código): skimming (as seis primeiras frases abrem os seis parágrafos, em ordem), scanning (cada número está no texto), grupos nominais (o núcleo é a última palavra do grupo), voz passiva (cada trecho tem *to be* + particípio; os contraexemplos não têm), tempos verbais, estrutura do artigo (o Box 1 de Wilson et al. tem 8 práticas) e o texto de computação (30% e 90%).
- `pendente_professor` (a resposta depende de interpretação ou de uma análise da equipe): falsos cognatos, afixos, referência pronominal (o teste confere que o referente vem antes do pronome no mesmo parágrafo, mas não o sentido), marcadores de discurso e dicionário.

Cada trecho em inglês citado nos blocos (entre aspas curvas) está em `tests_acervo/ingles_trechos.json`. Com `TUTORON_INGLES_ORIGINAIS` apontando para a pasta com `prova.docx` e `wilson.xml` (fora do repositório), os testes também conferem os trechos nos originais e o SHA-256 do texto da prova normalizado. Sem a pasta, esses testes são pulados com o motivo.

Tamanho das citações: só trechos curtos (no máximo 35 palavras cada, conferido por teste). O texto integral da prova não é versionado nem traduzido; o tutor é instruído (`rigor.md`) a trabalhar com trechos curtos.

## 4. Fontes

Matriz de critérios igual à das outras disciplinas (`fontes.json`, notas de 1 a 5).

| id | Fonte | Licença | Prioridade | Uso |
|---|---|---|---|---|
| `ufal-ingles-texto-prova` | Texto da prova de proficiência (arquivo da turma) | texto de Pavela, CC BY-NC 4.0 | alta | acervo (trechos) |
| `pavela-2016-pps` | Pavela, *Plant Protection Science*, 2016 | CC BY-NC 4.0 | alta | acervo (trechos) |
| `wilson-2014-best-practices` | Wilson et al., *Best Practices for Scientific Computing*, PLOS Biology, 2014 | CC BY 4.0 | alta | acervo (trechos) |
| `ufal-ppc-ecomp-2014` | PPC de Engenharia de Computação, ECOM001 | documento público | alta | referência (ementa) |
| `fromm-ufu-leitura-instrumental` | Fromm, *Língua Inglesa: Leitura Instrumental*, UFU, 2022 | CC BY-NC-SA 3.0 US | média | referência |
| `pinto-grasping-the-meaning` | Pinto, *Grasping the Meaning* | protegida | referência | só catálogo |
| `dubin-reading-by-all-means` | Dubin, *Reading by All Means*; Ediger, *Reading for Meaning* | protegida | referência | só catálogo |

Material aberto de inglês instrumental de universidade brasileira: o livro de Fromm (UFU) tem licença aberta declarada no repositório, mas o PDF não foi aberto, então os capítulos não foram conferidos; ele fica só no catálogo. A cláusula ShareAlike também exigiria a mesma licença nos blocos derivados. Nenhum texto dele foi usado.

## 5. Blocos

| id | Arquivo | Status | Na busca |
|---|---|---|---|
| `ingles-prova-skimming-hipotese` | p01 | validada | sim |
| `ingles-prova-scanning` | p02 | validada | sim |
| `ingles-cognatos-falsos-cognatos` | p03 | pendente_professor | sim |
| `ingles-grupos-nominais` | p04 | validada | sim |
| `ingles-afixos` | p05 | pendente_professor | sim |
| `ingles-referencia-pronominal` | p06 | pendente_professor | sim |
| `ingles-marcadores-discurso` | p07 | pendente_professor | sim |
| `ingles-voz-passiva` | p08 | validada | sim |
| `ingles-tempos-verbais` | p09 | validada | sim |
| `ingles-dicionario-contexto` | p10 | pendente_professor | sim |
| `ingles-estrutura-artigo-cientifico` | p11 | validada | sim |
| `ingles-compreensao-texto-computacao` | p12 | validada | sim |

Busca (`eval/relevancia.py`, com o `bge-m3` real): as 5 perguntas de exemplo, 8 paráfrases e 5 perguntas de outras áreas passam. Na primeira rodada, "eventually quer dizer eventualmente?" não trazia nada (similaridade 0,466 contra uma mediana de 0,435 no acervo); o bloco de falsos cognatos só citava *eventually* numa lista. Com uma linha própria explicando o par, a pergunta passou; o critério de relevância não mudou.

## 6. Liberação e validação com a IA real

Critério de liberação (o mesmo de PAA e Variáveis Complexas): suíte completa e bateria de relevância passando, nenhuma nota de IA na busca, perguntas de exemplo rodadas com a IA real e conferidas, e nenhum tópico com material da turma sem bloco na busca.

As 6 perguntas de `eval/bateria_tutor.py` rodaram em 20/11/2026 pelo fluxo completo. Os maiores modelos do Gemini deram HTTP 429 e as respostas vieram do `gemini-3.1-flash-lite` (degradado). Arquivos: `eval/results/bateria-ingles-2026-11-20.json`, `…-repeticao.json`, `…-nucleo-1.json`, `…-nucleo-2.json` e, só com o modelo local `tutoron-paa`, `…-local.json`. Cada resposta foi lida e comparada com os blocos e com os testes:

- skimming e scanning, actually × atualmente, voz passiva e referente de *they*: corretas e socráticas nas duas rodadas do Gemini e no modelo local. Citaram o bloco certo e não usaram rótulo inexistente. Em *they*, o tutor deu a estratégia (voltar à frase anterior, concordância, substituição) e deixou a conclusão para o aluno;
- núcleo de "plant extract based insecticides": na 1ª rodada, o revisor reprovou duas vezes a pista do Gemini e sobrou a ajuda de reserva genérica. O motivo era o mesmo da QPSK em Comunicação: o bloco trazia a tradução pronta do caso da pergunta. O bloco passou a resolver *mosquito-borne viral diseases* e a deixar o caso da pergunta para o aluno (o teste confere que a tradução não está no bloco). Depois disso, a pergunta saiu correta e socrática nas 3 rodadas do Gemini (em duas, o ajuste `entregou_resposta` atuou, sem entregar a tradução) e no modelo local;
- modelo local, imprecisão: atribuiu ao "texto da prova" o trecho de *actually*, que é de Wilson et al. O sentido explicado estava certo;
- pergunta de fora (mapa de Karnaugh): a busca devolveu vazio, mas nem o Gemini nem o modelo local disseram que o tema é de Sistemas Digitais. O modelo local ainda disse que os grupos podem ter "forma de L", o que está errado (os grupos são retângulos). É o mesmo comportamento já registrado em Circuitos, Sinais, Controle e Eletrônica, e não envolve o acervo de Inglês.

Com o critério cumprido, a disciplina passou a **MVP**, sem `aviso`, no último commit da branch.

## 7. Pendências

- Que o tutor diga, com Inglês selecionada, que uma pergunta é de outra disciplina (comportamento do prompt comum, igual nas outras disciplinas).
- Revisão humana dos 12 blocos e confirmação do professor dos 5 exercícios `pendente_professor`.
- Identificar o professor e confirmar com a equipe se o arquivo da prova pode ser publicado (hoje, só trechos curtos do artigo, que é CC BY-NC).
- Confirmar com o professor os tópicos marcados como "interpretação" (grupos nominais, referência pronominal, marcadores, tempos verbais e voz passiva).
- Abrir o livro de Fromm (UFU) e decidir se entra como complemento.
- Um texto de computação além de Wilson et al. (por exemplo, outro artigo CC BY da PLOS ou da PeerJ Computer Science).
