# Curadoria — Lógica Aplicada à Computação (`logica`, ECOM007)

Situação: **MVP** desde 21/11/2026, sem aviso, depois dos critérios de liberação: suíte e relevância verdes, nenhuma nota de IA na busca, bateria com o Gemini real lida e conferida, todo assunto com material com bloco. Falhas da IA registradas em `docs/DISCIPLINAS.md`.

## Disciplina e ementa

- ECOM007, 2º semestre, 60 h (40 teóricas e 20 práticas), Engenharia de Computação da UFAL.
- **Ementa conferida** no PPC de 2014 (`ufal-ppc-ecomp-2014`, p. 19 e 26 do PDF): histórico evolutivo; fundamentos de lógica; lógica proposicional; lógica de primeira ordem; prova automática de teoremas; seminários em temas complementares. Bibliografia básica: Polya (*A arte de resolver problemas*), Souza (*Lógica para Ciência da Computação*), Casanova, Giorno e Furtado (*Programação em Lógica e a Linguagem PROLOG*).
- Material da turma: Profs. **Evandro Costa** e **Baldoino Fonseca** (IC-UFAL), slides, Prova 1 de 2013 e listas. Material complementar: slides de Lógica Matemática do Prof. **Tiago Massoni** (UFCG), com a parte de Alloy feita com o Prof. **Rohit Gheyi**.
- "Prova automática de teoremas" está coberta por resolução (proposicional e de primeira ordem), Horn/Prolog e SAT. "Seminários em temas complementares" ficou com model checking (LTL) e Alloy, os temas dos slides da UFCG.
- Os 14 assuntos de `disciplinas.json` (`logica-01-historico-fundamentos` a `logica-14-programacao-logica-prolog`) têm todos pelo menos um bloco.

## Fronteiras

| Tópico | Aqui (Lógica) | Aprofundado em |
|---|---|---|
| Conjuntos, relações, indução, contagem | só como pano de fundo da semântica | Matemática Discreta (`discreta`) |
| Álgebra de Boole, portas, Karnaugh | equivalências e CNF como fórmulas, sem circuito | Sistemas Digitais (`sd`) e IEC (`iec`) |
| SAT | o que é, Horn polinomial, solver linear | PAA (`paa`): NP-completude |

O rigor diz isso ao tutor, e `tests_acervo/test_disciplina_logica.py` testa o isolamento nos dois sentidos com essas quatro disciplinas.

## Material protegido e dados pessoais

- O livro **Huth e Ryan, *Logic in Computer Science*** (`huth-ryan-lics`) é protegido: não foi versionado, ingerido nem transcrito; os blocos e o rigor citam só capítulo e seção. Os slides log04 e log08 da UFCG contêm páginas copiadas desse livro; essas páginas não foram transcritas (os blocos de dedução natural e LTL usam exemplos próprios ou os dos slides do professor).
- Nenhum PDF ou imagem está no repositório. Os slides têm o e-mail institucional de um professor: **não foi copiado**. A Prova 1 tem nome e matrícula em branco; nenhum aluno aparece.
- Nenhum material tem licença aberta declarada: todos os blocos são paráfrases com resolução da equipe, sem figuras. **Confirmar com a equipe** se os slides da UFAL e da UFCG podem continuar como base de paráfrase.


## Complemento: material de Ciência da Computação (22/11/2026)

O material da turma de Ciência da Computação (COMP360, IC-UFAL) entrou como **complemento** de `logica`, sem cópia da disciplina e sem mudar a situação (continua MVP).
- **Ementa:** o código COMP360 vem do nome da pasta e não aparece nos PPCs encontrados. O PPC de CC de 2011 (`ufal-ppc-cc-2011`, CCOM014, 60 h) e o de 2006 (COMP014, 80 h) trazem **o mesmo texto de ementa de ECOM007**. A diferença está na bibliografia: o PPC de CC lista Chang e Lee, van Dalen, Souza e Enderton, sem livro de Prolog (o de Engenharia lista Casanova et al.). Por isso não há motivo para separar disciplinas.
- **Diferença de conteúdo:** a turma de CC dedicou uma unidade a **Prolog e sistemas especialistas** (fichas práticas, arquivos .pl, projeto ExpertSystem-GUI, prova de grafos). Isso cabe em "prova automática de teoremas" e "temas complementares" e virou o assunto novo `logica-14-programacao-logica-prolog`.
- **Professora:** Profa. **Roberta Lopes** (IC-UFAL): 1ª avaliação (22/01/2019), 2ª avaliação (19/03/2019) e prova de Prolog (21/03/2019). Semestre letivo não informado nas fotos.
- **Curso e turma** estão no campo `curso:` de cada bloco novo e na linha `fonte`.
- **Dados pessoais:** as fotos das provas mostram o nome e as respostas manuscritas de um aluno. Nenhuma foto foi versionada e nenhum nome entrou. As respostas do aluno não foram usadas (têm erros, como chamar de tautologia uma fórmula verdadeira em um único modelo). Os enunciados foram parafraseados com fórmulas e grafo próprios. Na 1ª prova, cada aluno montava a fórmula a partir do próprio nome, e esse esquema não foi reproduzido.
- **Material protegido:** `Logic In Computer Science.pdf` (já em `huth-ryan-lics`), `Introduction to Algorithms 3rdEd.pdf`, `prolog.pdf` e as apostilas de terceiros da pasta Prolog (`cc-prolog-livros-protegidos`) ficaram fora, só como referência. As fichas práticas são de outra instituição, com autoria não identificada: foram parafraseadas por tópico, sem transcrição.
- **Sistema especialista:** o projeto da turma diagnostica doenças. O bloco descreve só a arquitetura, com exemplo neutro, e o tutor não dá diagnóstico.
- **Execução:** todo código Prolog dos blocos roda no SWI-Prolog 11.0.0 em `test_codigo_prolog_dos_blocos_roda_no_swipl`. O teste é pulado se o `swipl` não estiver instalado (o CI não tem).
- **Correções** nos arquivos da turma:
  - `first.pl` usa `;` no lugar de `.`;
  - as soluções anotadas de `questoes_prolog.txt` trazem `remove([X],X,[])` e somam com `=` em vez de `is`.
- **Pendência:** na 1ª prova, "grau de complexidade" não está definido no enunciado; o bloco `logica-roberta-prova1-complexidade-negacao` fica `pendente_professor`.
- **Fronteiras novas:** listas e recursão também aparecem em Estrutura de Dados (`ed`) e Programação 1 (`prog1`); o isolamento com elas é testado.

## Fontes (`fontes.json`)

| id | Uso | Licença |
|---|---|---|
| `ufal-ppc-ecomp-2014` | citada (ementa) | Documento institucional público |
| `ufal-baldoino-slides-proposicional` | acervo | Não declarada |
| `ufal-baldoino-slides-primeira-ordem` | acervo | Não declarada |
| `ufal-baldoino-prova1-2013` | acervo | Não declarada (prova) |
| `ufal-baldoino-lista-proposicional` | acervo | Não declarada (lista) |
| `ufal-baldoino-lista-primeira-ordem` | acervo | Não declarada (lista) |
| `ufcg-massoni-slides` | acervo | Não declarada |
| `huth-ryan-lics` | referencia | Protegido; não incluído |
| `souza-logica-computacao` | referencia | Protegido; não obtido |
| `ufal-ppc-cc-2011` | citada | Documento institucional público |
| `roberta-provas-2019` | acervo | Não declarada |
| `cc-prolog-turma` | acervo | Não declarada |
| `fichas-praticas-prolog` | acervo | Não declarada |
| `cc-expertsystem-gui` | acervo | Não declarada |
| `swi-prolog-manual` | citada | Sistema sob licença BSD-2 |
| `cc-prolog-livros-protegidos` | referencia | Protegidos ou sem licença declarada |
| `casanova-prolog` | referencia | Protegido; não obtido |
| `forallx` | citada | CC BY 4.0 |
| `open-logic-project` | citada | CC BY |
| `openlogic-proof-checker` | citada | ferramenta |
| `stanford-truth-table-tool` | citada | ferramenta |
| `alloy-tools` | citada | ferramenta |

Os links das fontes citadas foram testados em 20/11/2026 (HTTP 200); nenhuma foi baixada para o acervo.

## Resoluções e correções

Todas as resoluções são da equipe TutorON, **não gabarito do professor**, e o texto de cada bloco diz isso. Cada refutação, prova em dedução natural, consequência e contramodelo é recalculado em `tests_acervo/test_disciplina_logica.py` com o verificador `tests_acervo/logica_verif.py` (tabela-verdade, resolvente, unificação, caixas da dedução natural e busca de contramodelo em universos finitos).

Correções em relação ao material original (status `corrigida`):
- `logica-sintaxe-proposicional`: um slide de Baldoino lista outra precedência; o bloco usa a dos slides da UFCG e manda pôr parênteses;
- `logica-semantica-tabela-verdade`: o slide repete a interpretação $I_2$ no lugar de $I_4=\{\neg P,\neg Q\}$;
- `logica-lista-q3-consequencias`: a Q3d pede para provar uma consequência que **não vale**; o bloco dá o contraexemplo;
- `logica-deducao-natural-regras`: os slides citam $\land e_2$ onde a regra é $\land e_1$;
- `logica-primeira-ordem-sintaxe`: a desigualdade do seno e o enunciado da transitividade de "ancestral";
- `logica-gabarito-formalizacao-correcoes`: três erros do gabarito (Q1b, Q3 S3, Q6d);
- `logica-primeira-ordem-semantica`: a cláusula da negação ("¬P é V se ¬P é F" → "se P é F");
- `logica-unificacao-mgu`: um parêntese não fechado em $x/h(a,g(b))$.

**Pendente com o professor:** Prova 1, Q2 (greve), `pendente_professor`. Com as premissas dadas, nem S3 nem ¬S3 seguem; só com a premissa implícita "terminou em menos de 1 ano → não durou mais de 1 ano" segue ¬S3. A resposta esperada não está no material.

Não conferido por código: os exemplos de LTL (semáforo) e de Alloy, conferidos à mão (`verificacao: exemplos_conferidos`).

## Blocos (42, todos `material_da_disciplina`, todos na busca)

Nenhum bloco é `nota_da_equipe_ia`. Todos têm `revisao_humana: pendente` e nenhum tem revisão do professor.

| Bloco | Assunto | Status | Fontes |
|---|---|---|---|
| `logica-fundamentos-verdade-prova` | 01-historico-fundamentos | validada | ufal-baldoino-slides-proposicional, ufcg-massoni-slides |
| `logica-sintaxe-proposicional` | 02-proposicional-sintaxe-semantica | corrigida | ufal-baldoino-slides-proposicional, ufcg-massoni-slides |
| `logica-semantica-tabela-verdade` | 02-proposicional-sintaxe-semantica | corrigida | ufal-baldoino-slides-proposicional |
| `logica-conectivos-exercicios-concurso` | 03-consequencia-equivalencia | validada | ufal-baldoino-slides-proposicional |
| `logica-consequencia-logica-teoremas` | 03-consequencia-equivalencia | validada | ufal-baldoino-slides-proposicional |
| `logica-equivalencias-e-conectivos` | 03-consequencia-equivalencia | validada | ufal-baldoino-slides-proposicional, ufal-baldoino-lista-proposicional |
| `logica-argumentos-classicos` | 03-consequencia-equivalencia | validada | ufal-baldoino-slides-proposicional |
| `logica-tableaux-proposicional` | 04-tableaux | validada | ufal-baldoino-slides-proposicional |
| `logica-forma-normal-conjuntiva` | 05-formas-normais-horn-sat | validada | ufcg-massoni-slides, ufal-baldoino-slides-proposicional |
| `logica-horn-prolog-sat` | 05-formas-normais-horn-sat | validada | ufcg-massoni-slides |
| `logica-resolucao-proposicional` | 06-resolucao-proposicional | validada | ufal-baldoino-slides-proposicional |
| `logica-prova1-q1-tres-metodos` | 06-resolucao-proposicional | validada | ufal-baldoino-prova1-2013 |
| `logica-prova1-q2-greve` | 06-resolucao-proposicional | pendente_professor | ufal-baldoino-prova1-2013, ufal-baldoino-lista-proposicional |
| `logica-prova1-q3-alice-betty-carol` | 03-consequencia-equivalencia | validada | ufal-baldoino-prova1-2013, ufal-baldoino-lista-proposicional |
| `logica-lista-q3-consequencias` | 03-consequencia-equivalencia | corrigida | ufal-baldoino-lista-proposicional |
| `logica-lista-q5-q6-argumentos` | 03-consequencia-equivalencia | validada | ufal-baldoino-lista-proposicional |
| `logica-deducao-natural-regras` | 07-deducao-natural | corrigida | ufcg-massoni-slides |
| `logica-deducao-natural-exemplos` | 07-deducao-natural | validada | ufcg-massoni-slides |
| `logica-consequencia-vs-derivacao` | 08-corretude-completude | validada | ufcg-massoni-slides |
| `logica-primeira-ordem-sintaxe` | 09-primeira-ordem-formalizacao | corrigida | ufal-baldoino-slides-primeira-ordem, ufcg-massoni-slides |
| `logica-negacao-quantificadores` | 09-primeira-ordem-formalizacao | validada | ufcg-massoni-slides, ufal-baldoino-slides-primeira-ordem |
| `logica-formalizacao-primeira-ordem-exercicios` | 09-primeira-ordem-formalizacao | validada | ufal-baldoino-lista-primeira-ordem |
| `logica-gabarito-formalizacao-correcoes` | 09-primeira-ordem-formalizacao | corrigida | ufal-baldoino-lista-primeira-ordem |
| `logica-primeira-ordem-semantica` | 10-primeira-ordem-semantica | corrigida | ufcg-massoni-slides, ufal-baldoino-slides-primeira-ordem |
| `logica-deducao-natural-primeira-ordem` | 11-deducao-natural-primeira-ordem | validada | ufcg-massoni-slides |
| `logica-forma-clausal-skolem` | 12-forma-clausal-unificacao-resolucao | validada | ufal-baldoino-slides-primeira-ordem, ufal-baldoino-lista-primeira-ordem |
| `logica-unificacao-mgu` | 12-forma-clausal-unificacao-resolucao | corrigida | ufal-baldoino-slides-primeira-ordem |
| `logica-resolucao-primeira-ordem` | 12-forma-clausal-unificacao-resolucao | validada | ufal-baldoino-slides-primeira-ordem |
| `logica-resolucao-cachorros-agua` | 12-forma-clausal-unificacao-resolucao | validada | ufal-baldoino-lista-primeira-ordem |
| `logica-resolucao-dragoes-zoologico` | 12-forma-clausal-unificacao-resolucao | validada | ufal-baldoino-lista-primeira-ordem |
| `logica-resolucao-passageiros-dragoes-felizes` | 12-forma-clausal-unificacao-resolucao | validada | ufal-baldoino-lista-primeira-ordem |
| `logica-model-checking-ltl` | 13-model-checking-alloy | validada | ufcg-massoni-slides |
| `logica-alloy-especificacao` | 13-model-checking-alloy | validada | ufcg-massoni-slides |
| `logica-prolog-fatos-regras-consultas` | 14-programacao-logica-prolog | corrigida | cc-prolog-turma |
| `logica-prolog-listas-recursao` | 14-programacao-logica-prolog | corrigida | cc-prolog-turma, fichas-praticas-prolog |
| `logica-prolog-unificacao-aritmetica` | 14-programacao-logica-prolog | validada | fichas-praticas-prolog |
| `logica-prolog-corte-negacao-falha` | 14-programacao-logica-prolog | validada | fichas-praticas-prolog |
| `logica-prolog-findall-assert` | 14-programacao-logica-prolog | validada | fichas-praticas-prolog |
| `logica-prolog-grafos-prova` | 14-programacao-logica-prolog | validada | roberta-provas-2019 |
| `logica-sistema-especialista-prolog` | 14-programacao-logica-prolog | validada | cc-expertsystem-gui |
| `logica-roberta-prova1-complexidade-negacao` | 02-proposicional-sintaxe-semantica | pendente_professor | roberta-provas-2019 |
| `logica-roberta-prova2-modelo-finito` | 10-primeira-ordem-semantica | validada | roberta-provas-2019 |
