# Curadoria — Geometria Analítica (`ga`, ECOM005)

Situação: **MVP** desde 20/11/2026, sem aviso, por decisão da equipe, aceitando a dica errada da IA sobre cônicas registrada em `docs/DISCIPLINAS.md`.

## Disciplina

- Código ECOM005, 1º período, Engenharia de Computação da UFAL; disciplina do Instituto de Matemática.
- **Ementa não confirmada:** o plano de curso não foi encontrado online nem veio no pacote da equipe (`ufal-ga-ementa`, uso `indisponivel`). Os 13 assuntos foram tirados das próprias provas, que são a evidência dos tópicos. Pedir o plano de curso ao professor.
- Professor: só as provas de 2016.2 trazem nome impresso no cabeçalho (Prof. Adelailson Peixoto). As de 2017.1 não trazem professor, e duas fotos não têm cabeçalho.

## Fotos de provas e dados pessoais

- 14 fotos de provas (2016.2, 2017.1 e duas sem cabeçalho) foram lidas e parafraseadas; **nenhuma imagem está no repositório**.
- Uma foto traz nome, curso e e-mail manuscritos de um aluno: esses dados **não** foram registrados em lugar nenhum. Outra mostra a mão de quem fotografou. Nenhum bloco tem e-mail, nome de aluno ou link de grupo (há teste para isso).
- Publicação da transcrição não autorizada: os blocos trazem o enunciado parafraseado com os dados, não a transcrição literal.
- Não usada: 1ª Avaliação de 10/02/2017, Q1b (depende de figura ilegível).

## Fontes (`fontes.json`)

| id | Uso | Licença |
|---|---|---|
| `ufal-ga-ementa` | indisponivel | Não se aplica (documento não obtido) |
| `ufal-ga-provas-2016` | acervo | Não declarada (prova da disciplina) |
| `ufal-ga-provas-2017` | acervo | Não declarada (prova da disciplina) |
| `ufal-ga-provas-sem-cabecalho` | acervo | Não declarada |
| `ufabc-miranda-gav` | referencia | Conflito: o texto diz CC BY 4.0 e o link aponta para CC BY-NC 4.0; não confirmada |
| `ufms-carvalho-vga` | candidato | CC BY-SA indicada só no nome do arquivo; não confirmada no texto |
| `ufmg-reginaldo-santos` | referencia | Não confirmada (livros irmãos dizem direitos reservados) |
| `geogebra-3d` | citada | Termos de uso do GeoGebra (não é material) |
| `steinbruch-winterle` | referencia | Protegido (direitos reservados) |
| `reis-silva` | referencia | Protegido (direitos reservados) |
| `boulos-camargo` | referencia | Protegido (direitos reservados) |

Os livros protegidos (Steinbruch e Winterle, Reis e Silva, Boulos e Camargo) ficaram "não incluído": não foram buscados, baixados, transcritos nem ingeridos.

## Blocos (29, todos `material_da_disciplina`, todos na busca)

Nenhum bloco é `nota_da_equipe_ia`. Todos têm `revisao_humana: pendente`, e nenhum tem revisão do professor. As resoluções são da equipe TutorON, não gabarito do professor, e as contas estão conferidas com SymPy em `tests_acervo/test_disciplina_ga.py`.

| Bloco | Assunto | Questões | Status da resolução |
|---|---|---|---|
| `ga-vetores-decomposicao-projecao` | ga-01-vetores-operacoes | 1a, 1b; 4 — Reavaliação AB1 (24/05/2017), Q1a e Q1b; Final (14/11/2016), Q4 | validada |
| `ga-vetores-angulo-norma` | ga-01-vetores-operacoes | 3; 4; 2 — Provas sem cabeçalho (fotos), Q4 e Q3; Final (14/11/2016), Q2 | validada |
| `ga-forcas-combinacao-linear` | ga-01-vetores-operacoes | 2 — Prova sem cabeçalho (foto), Q2 | validada |
| `ga-questoes-com-figura` | ga-01-vetores-operacoes | 1; 1; 1b — Reavaliação 1 (03/11/2016), Q1; prova sem cabeçalho (foto), Q1; 1ª Avaliação (11/02/2017), | pendente do professor |
| `ga-triangulo-projecao-altura` | ga-01-vetores-operacoes | 3; 4 — Final (14/11/2016), Q3; Reavaliação 1 (03/11/2016), Q4 | validada |
| `ga-paralelogramo-area` | ga-01-vetores-operacoes | 1; 2b — Prova sem cabeçalho (foto), Q1; 1ª Avaliação (11/02/2017), Q2b | validada |
| `ga-triangulo-angulos-area` | ga-01-vetores-operacoes | 2 — Prova sem cabeçalho (foto desfocada), Q2 | pendente do professor |
| `ga-demonstracoes-vetoriais` | ga-13-demonstracoes-vetoriais | 1a, 2a — 1ª Avaliação (10/02/2017), Q1a e Q2a; 1ª Avaliação (11/02/2017), Q1a e Q2a | validada |
| `ga-retas-plano-parametricas` | ga-03-retas-no-plano | vários — Prova sem cabeçalho (foto), Q3; 1ª Avaliação (11/02/2017), Q3; 1ª Avaliação (10/02/2017),  | validada |
| `ga-retas-plano-distancia` | ga-03-retas-no-plano | 4a; 4a; 2b — 1ª Avaliação (10/02/2017), Q4a; 1ª Avaliação (11/02/2017), Q4a; Reavaliação AB1 (24/05/201 | validada |
| `ga-retas-plano-angulo` | ga-03-retas-no-plano | 2a; 4b; 4b — Reavaliação AB1 (24/05/2017), Q2a; 1ª Avaliação (10/02/2017), Q4b; 1ª Avaliação (11/02/201 | validada |
| `ga-produto-vetorial-misto` | ga-02-produto-vetorial-misto | vários — P2 Adventistas (14/10/2016), Q2 e Q3; Reposição 2 (03/11/2016), Q1a e Q1b; Reavaliação AB2 | validada |
| `ga-plano-tres-pontos` | ga-05-distancias-angulos-espaco | vários — Final (14/11/2016), Q7; P2 (15/10/2016), Q3b; Reavaliação AB2 (24/05/2017), Q4a; P2 Advent | validada |
| `ga-distancia-ponto-plano-deducao` | ga-05-distancias-angulos-espaco | 2b; 3a, 3c, 4 — Reavaliação AB2 (24/05/2017), Q2b; P2 (15/10/2016), Q3a, Q3c e Q4 | validada |
| `ga-distancia-retas-reversas` | ga-05-distancias-angulos-espaco | 4b — Reavaliação AB2 (24/05/2017), Q4b | validada |
| `ga-planos-posicoes-intersecoes` | ga-04-planos-retas-espaco | vários — P2 (15/10/2016), Q2; Reposição 2 (03/11/2016), Q2b e Q3; Reavaliação AB2 (24/05/2017), Q3b | validada |
| `ga-circunferencias` | ga-06-circunferencia-esfera | 1a, 1b — 2ª Avaliação (10/03/2017), Q1; 2ª Avaliação (11/03/2017), Q1 | validada |
| `ga-esferas-equacao` | ga-06-circunferencia-esfera | 1 — P2 Adventistas (14/10/2016), Q1; 4ª Avaliação (12/05/2017), Q1 | validada |
| `ga-esfera-plano-tangente` | ga-06-circunferencia-esfera | vários — P2 (15/10/2016), Q1; Final (14/11/2016), Q5; Reavaliação AB2 (24/05/2017), Q3a; P2 Adventi | validada |
| `ga-parabola` | ga-07-parabola | vários — 2ª Avaliação (10/03/2017), Q2; 2ª Avaliação (11/03/2017), Q2b; Reavaliação AB1 (24/05/2017 | validada |
| `ga-parabola-reta-secante` | ga-07-parabola | 2a — 2ª Avaliação (11/03/2017), Q2a | corrigida |
| `ga-elipse-focos` | ga-08-elipse | 3a, 3b; 3b — 2ª Avaliação (10/03/2017), Q3; Reavaliação AB1 (24/05/2017), Q3b | validada |
| `ga-elipse-tangente-parametros` | ga-08-elipse | 3a, 3b — 2ª Avaliação (11/03/2017), Q3 | validada |
| `ga-hiperbole` | ga-09-hiperbole | 4a, 4b; 4a; 3a — 2ª Avaliação (10/03/2017), Q4; 2ª Avaliação (11/03/2017), Q4a; Reavaliação AB1 (24/05/2017 | validada |
| `ga-identificar-conicas` | ga-10-identificacao-conicas | 6; 4 — Final (14/11/2016), Q6; Reposição 2 (03/11/2016), Q4 | validada |
| `ga-rotacao-conicas` | ga-11-rotacao-coordenadas | 4b; 4b — 2ª Avaliação (11/03/2017), Q4b; Reavaliação AB1 (24/05/2017), Q4b | validada |
| `ga-quadricas-identificar` | ga-12-quadricas-superficies | 1a; 3b, 4 — Reavaliação AB2 (24/05/2017), Q1a; 4ª Avaliação (12/05/2017), Q3b e Q4 | validada |
| `ga-superficies-revolucao` | ga-12-quadricas-superficies | 1b; 2 — Reavaliação AB2 (24/05/2017), Q1b; 4ª Avaliação (12/05/2017), Q2 | validada |
| `ga-paraboloide-secao` | ga-12-quadricas-superficies | 3a — 4ª Avaliação (12/05/2017), Q3a | pendente do professor |

## Correções e pendências de confirmação

- `ga-parabola-reta-secante` (**corrigida**): o enunciado da 2ª Avaliação de 11/03/2017, Q2a, diz que toda reta não perpendicular à diretriz corta a parábola em dois pontos; é falso (contraexemplo y = −5). O bloco mostra o que vale e uma leitura possível (retas pelo foco).
- `ga-questoes-com-figura` (**pendente do professor**): resolução depende da nossa leitura das figuras (ângulos das forças; posição de u e v); erro de digitação "‖u = 3‖" lido como ‖u‖ = 3.
- `ga-triangulo-angulos-area` (**pendente do professor**): foto desfocada; lemos C(3, 4).
- `ga-paraboloide-secao` (**pendente do professor**): o enunciado não diz a direção do eixo nem se 5 e 8 são eixos ou semieixos.
- `ga-identificar-conicas`: "4y.+1" na Reposição 2 lido como 4y + 1.

## Fronteiras

- Cálculo 3: retas, planos e vetores aparecem lá como ferramenta (plano tangente a z = f(x, y), gradiente). Os blocos de GA tratam da geometria em si; o teste de isolamento confere que perguntas de Cálculo 3 não trazem blocos de GA e vice-versa.
- Álgebra Linear não está cadastrada; espaços vetoriais, autovalores e diagonalização ficam para ela (regra em `rigor.md`).

## Pendências

- Plano de curso e ementa oficiais.
- Revisão humana e do professor de todos os blocos.
- Licença do livro da UFABC (conflito CC BY × CC BY-NC) e do livro da UFMS antes de ingerir qualquer um.
