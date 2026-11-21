# Curadoria — Lógica Aplicada à Computação (`logica`, ECOM007)

Situação: **MVP** desde 21/11/2026, sem aviso, depois dos critérios de liberação: suíte e relevância verdes, nenhuma nota de IA na busca, bateria com o Gemini real lida e conferida, todo assunto com material com bloco. Falhas da IA registradas em `docs/DISCIPLINAS.md`.

## Disciplina e ementa

- ECOM007, 2º semestre, 60 h (40 teóricas e 20 práticas), Engenharia de Computação da UFAL.
- **Ementa conferida** no PPC de 2014 (`ufal-ppc-ecomp-2014`, p. 19 e 26 do PDF): histórico evolutivo; fundamentos de lógica; lógica proposicional; lógica de primeira ordem; prova automática de teoremas; seminários em temas complementares. Bibliografia básica: Polya (*A arte de resolver problemas*), Souza (*Lógica para Ciência da Computação*), Casanova, Giorno e Furtado (*Programação em Lógica e a Linguagem PROLOG*).
- Material da turma: Profs. **Evandro Costa** e **Baldoino Fonseca** (IC-UFAL), slides, Prova 1 de 2013 e listas. Material complementar: slides de Lógica Matemática do Prof. **Tiago Massoni** (UFCG), com a parte de Alloy feita com o Prof. **Rohit Gheyi**.
- "Prova automática de teoremas" está coberta por resolução (proposicional e de primeira ordem), Horn/Prolog e SAT. "Seminários em temas complementares" ficou com model checking (LTL) e Alloy, os temas dos slides da UFCG.
- Os 13 assuntos de `disciplinas.json` (`logica-01-historico-fundamentos` a `logica-13-model-checking-alloy`) têm todos pelo menos um bloco.

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

## Blocos (33, todos `material_da_disciplina`, todos na busca)

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
