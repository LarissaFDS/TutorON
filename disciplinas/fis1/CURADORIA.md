# Curadoria — Física 1 (`fis1`, ECOM009)

Situação: **em validação** até os critérios de liberação serem cumpridos (veja `docs/DISCIPLINAS.md`).

## Disciplina e ementa

- ECOM009, 2º semestre, 60 h (40 teóricas e 20 práticas), Engenharia de Computação da UFAL.
- **Ementa conferida** no PPC de 2014 (`ufal-ppc-ecomp-2014`, p. 19 e 27 do PDF): grandezas físicas; vetores; cinemática e dinâmica da partícula; trabalho e energia; dinâmica de um sistema de partículas; cinemática e dinâmica da rotação. Bibliografia básica: Alonso e Finn (*Física*), Halliday, Resnick e Walker (*Fundamentos de Física 1*), Tipler (*Física 1*).
- Material da turma: provas de 2017 do Prof. **Osvaldo A. Rosso** (UFAL), turmas COMP216-M e ECOMP01-M, e um arquivo de texto de aluno que liga cada questão a um problema do Halliday (10ª ed.) e lista os problemas das listas.

| Assunto (`disciplinas.json`) | Ementa | Halliday | Blocos da turma na busca |
|---|---|---|---|
| `fis1-01-grandezas-cinematica` | grandezas; cinemática | cap. 1, 2, 4.1–4.3 | AB1 Q1, mapa das provas |
| `fis1-02-vetores-projeteis` | vetores; cinemática | cap. 3, 4 | AB1 Q2, reavaliação AB1 Q1 |
| `fis1-03-leis-newton-atrito` | dinâmica da partícula | cap. 5, 6 | AB1 Q3 e Q4, reavaliação AB1 Q3 e Q4 |
| `fis1-04-trabalho-energia` | trabalho e energia | cap. 7, 8 | AB2 Q1 |
| `fis1-05-sistemas-particulas-colisoes` | sistema de partículas | cap. 9 | AB2 Q2, reavaliação AB2 Q1 |
| `fis1-06-rotacao` | cinemática e dinâmica da rotação | cap. 10 | AB2 Q3, reavaliação AB2 Q2 |
| `fis1-07-rolamento-momento-angular` | dinâmica da rotação | cap. 11 | AB2 Q4, reavaliação AB2 Q3 e Q4 |

A hipótese inicial de seis tópicos se confirmou pelas provas: a AB1 cobre os capítulos 2 a 6 e a AB2, os capítulos 7 a 11. Medição (cap. 1) e vetores (cap. 3) não têm questão própria nem lista; aparecem como ferramenta (unidades, componentes) nas questões. Movimento retilíneo (cap. 2), leis de Newton sem atrito (cap. 5) e trabalho (cap. 7) só aparecem nos números das listas, sem enunciado disponível. Para vetores, movimento circular e trabalho há notas da equipe, **fora da busca** até revisão humana.

## Fronteiras

| Tópico | Aqui (Física 1) | Aprofundado em |
|---|---|---|
| Equilíbrio estático, gravitação, fluidos, oscilações, ondas, termodinâmica | não | Física 2 (`fis2`) |
| Derivadas e integrais como técnica | usadas em v = dx/dt e a = dv/dt | Cálculo (Cálculo 3, `calc3`, é a única de cálculo cadastrada) |
| Vetores como objeto geométrico (produto vetorial, retas, planos) | componentes, soma e produto escalar como ferramenta | Geometria Analítica (`ga`) |

Energia aparece nas duas físicas: em Física 1, conservação da energia mecânica e trabalho do atrito; em Física 2, energia de oscilações e a primeira lei da termodinâmica. O rigor diz isso ao tutor, e `tests_acervo/test_disciplina_fis1.py` testa o isolamento com Física 2, Cálculo 3 e GA nos dois sentidos.

## Material protegido e dados pessoais

- O livro **Halliday, Resnick e Walker, *Fundamentos de Física*, vol. 1** (`halliday-fundamentos-vol1`), as **resoluções do Halliday** (`halliday-resolucoes-10ed`) e o **manual de soluções de Alonso e Finn** (`alonso-finn-solucoes`) não foram incluídos no material entregue, nem procurados, versionados ou ingeridos. Os blocos citam só capítulo e número de problema.
- As fotos da AB2 incluem quatro páginas de exemplos resolvidos do Halliday. Elas não foram transcritas: os blocos têm enunciado parafraseado e resolução própria, e os resultados impressos serviram só para conferir números.
- Nenhuma imagem nem o arquivo de texto está no repositório. Três fotos de prova mostram o nome de um aluno (e uma mostra a nota e a resolução manuscrita); **nenhum nome foi copiado**. O teste guarda só hashes de pares de palavras desses nomes para garantir que eles não entrem no acervo.
- Nenhum material da turma tem licença aberta declarada: todos os blocos são paráfrases com resolução da equipe, sem figuras (as figuras são descritas em texto). **Confirmar com a equipe** se as provas do Prof. Rosso podem continuar como base de paráfrase e se o professor autoriza a transcrição.

## Fontes (`fontes.json`)

| id | Uso | Licença |
|---|---|---|
| `ufal-ppc-ecomp-2014` | citada (ementa) | Documento institucional público |
| `ufal-rosso-ab1-2017` | acervo | Não declarada (prova) |
| `ufal-rosso-reav-ab1` | acervo | Páginas de livro protegido; só paráfrase |
| `ufal-rosso-ab2-2017` | acervo | Não declarada (prova); páginas do livro protegidas |
| `ufal-rosso-reav-ab2-2017` | acervo | Não declarada (prova) |
| `ufal-rosso-lista-questoes` | acervo | Não declarada (anotação de aluno) |
| `halliday-fundamentos-vol1` | referencia | Protegido; não incluído |
| `halliday-resolucoes-10ed` | referencia | Manual protegido; não incluído |
| `alonso-finn-solucoes` | referencia | Manual protegido; não incluído |
| `openstax-university-physics-v1` | citada | CC BY-NC-SA 4.0; não ingerida (restrição a IA registrada em Física 2) |
| `mit-ocw-8-01sc` | citada | CC BY-NC-SA 4.0 |
| `hyperphysics` | referencia | Não aberta |

Os links das fontes citadas foram testados em 21/11/2026 (HTTP 200). Matriz de critérios, como nas disciplinas anteriores: **alta** = material da turma ou documento oficial, que define o que cai; **média** = fonte aberta de boa qualidade, indicada para leitura; **referência** = só catálogo (protegida ou de consulta). As fontes abertas são de definição e de procedimento (MIT 8.01SC tem problemas resolvidos), mas nenhuma foi ingerida: o material procedimental do acervo são as resoluções das provas.

## Blocos

Na busca (material da turma, parafraseado, resolução da equipe, `aprovado`):

| Bloco | Status | Observação |
|---|---|---|
| `fis1-ab1-q1-velocidade-vetorial` | validada | |
| `fis1-ab1-q2-projetil-rochedo` | corrigida | a nota da prova dá sen 60 = 0,809 e cos 60 = 0,588 (valores de 54°) |
| `fis1-ab1-q3-atrito-estatico-cinetico` | validada | com g = 10 o item b fica exatamente no limiar do atrito estático |
| `fis1-ab1-q4-tres-blocos` | validada | |
| `fis1-reav-ab1-q1-bola-parede` | validada | traz também alcance e alcance máximo |
| `fis1-reav-ab1-q3-bloco-forca-inclinada` | validada | |
| `fis1-reav-ab1-q4-plano-inclinado-polia` | validada | diagrama de corpo livre no plano inclinado com atrito |
| `fis1-ab2-q1-pacote-mola-atrito` | validada | quando a energia mecânica se conserva |
| `fis1-ab2-q2-colisao-elastica` | validada | |
| `fis1-ab2-q3-disco-bloco` | corrigida | a prova usa a letra M para o disco e para o bloco |
| `fis1-ab2-q4-bola-rampa-rolamento` | pendente_professor | "bola homogênea" com o momento de inércia do disco; as duas leituras |
| `fis1-reav-ab2-q1-pendulo-balistico` | pendente_professor | h = 6,3 m (provavelmente cm) |
| `fis1-reav-ab2-q2-atwood-disco` | pendente_professor | disco de 500 kg (provavelmente g) |
| `fis1-reav-ab2-q3-cilindro-telhado` | validada | |
| `fis1-reav-ab2-q4-barata-disco` | validada | |
| `fis1-mapa-provas-listas` | — | mapa das avaliações e listas, sem enunciados |

Fora da busca (`nota_da_equipe_ia`, `candidato`, revisão humana pendente): `fis1-nota-vetores-componentes`, `fis1-nota-movimento-circular`, `fis1-nota-trabalho-potencia`.

Não cobertos: a questão 1 da final (exemplo 4.04 da 10ª ed.) não foi fotografada; as listas só têm números de problemas do livro, que não foram transcritos.

## Resoluções e conferência

Todas as resoluções são da equipe TutorON, **não gabarito do professor**, e o texto de cada bloco diz isso. "validada" quer dizer que a resolução foi refeita por código e, quando a turma tinha a página do exemplo do livro fotografada (AB2 Q1, Q2 e Q3), coincide com o resultado impresso. `tests_acervo/fis1_verif.py` refaz cada questão a partir dos dados do enunciado parafraseado e confere as expressões finais por análise dimensional com SymPy; `tests_acervo/test_disciplina_fis1.py` compara cada número com o texto do bloco, inclusive as leituras alternativas dos dados pendentes e os erros comuns citados.

Revisão humana e do professor: **pendentes** em todos os blocos.
