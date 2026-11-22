# Curadoria — Matemática Discreta (`discreta`, ECOM003)

Situação: **MVP** desde 20/11/2026, sem aviso, por decisão da equipe, aceitando a falha de busca registrada em `docs/DISCIPLINAS.md`.

## Disciplina

- Código ECOM003, 1º período, 60 h, Engenharia de Computação da UFAL. Professor do plano de curso: Lucas Benevides Viana de Amorim (IC/UFAL).
- Ementa, do plano de curso: "Noções Básicas, Conjuntos e Funções. Construção Axiomática do Conjunto dos Números Naturais: Postulados de Peano. Estruturas Algébricas, Construção Axiomática do Conjunto dos Números Inteiros. Representação dos Números Inteiros: Sistemas de Numeração. Fatoração de Números Inteiros: Máximo Divisor Comum, Números Primos. Aritmética Modular: Congruências, Anéis Zn, Criptografia RSA. Noções da Teoria dos Grafos, Combinatória Elementar, Aplicações."

## Fontes (`fontes.json`)

| id | Uso | Observação |
|---|---|---|
| `ufal-discreta-plano` | citada | Ementa, tópicos e bibliografia |
| `ufal-discreta-slides-lucas` | acervo | Slides 2017.2. Licença não declarada; parafraseados. E-mails do professor e da lista da turma ficaram de fora |
| `ufal-discreta-lista01` | acervo | Lista 01 (conjuntos), sem gabarito; resoluções da equipe conferidas por código. Questões em imagem não usadas |
| `ufrpe-discreta-pablo` | acervo | Notas, listas e respostas do Prof. Pablo Sampaio (UFRPE); parafraseadas; nomes de monitores fora |
| `ufcg-discreta-leandro` | acervo | Slides e listas do Prof. Leandro Balby Marinho (UFCG), sem gabarito |
| `ufal-evaristo-algebra` | acervo | Livro de Evaristo e Perdigão (EDUFAL), sem licença aberta; parafraseado; números recalculados |
| `albertson-hutchinson` | acervo | Livro protegido, escaneado: só paráfrase por seção, com exemplos próprios; nada transcrito, nenhuma imagem versionada |
| `albertson-hutchinson-solucoes` | referência | Manual de soluções: não transcrito |
| `ila-capitulos-5-6` | referência | Livro de pseudocódigo (ILA), fora da disciplina; excluído |
| `respostas-introducao-algebra` | referência | .zip com .doc de autoria desconhecida; não aberto |
| `levin-dmoi` | referência | CC BY-NC-SA 4.0; só consulta |
| `mit-mcs` | referência | CC BY-SA 3.0; só consulta |
| `ufal-ppc-cc-2011` | citada | PPC de Ciência da Computação (matriz 2011), ementa de CCOM010 |
| `ufal-cc-discreta-provas-bruno` | acervo | 8 provas do Prof. Bruno Pimentel (2020.1 a 2021.1), sem gabarito; enunciados parafraseados, resolução da equipe conferida por código |
| `ufal-cc-discreta-prova-lucas-2017` | acervo | 4 fotos da Prova 01 de 2017 (Prof. Lucas Amorim) respondida por aluno: só os enunciados foram usados; fotos, nome e respostas do aluno fora |
| `ufal-cc-discreta-monitoria` | acervo | Revisões da monitoria (2020.2); nomes dos monitores omitidos |
| `cc-discreta-rsa-python` | referência | RSA em Python de aluno (GPL-3.0), com chave privada de exemplo: não versionado |

Arquivos marcados "não incluído" no pacote da equipe não foram buscados nem baixados.

## Blocos (22, todos `material_da_disciplina`, todos na busca)

Nenhum bloco é `nota_da_equipe_ia`. Todos têm `revisao_humana: pendente`, e nenhum tem revisão do professor. As contas estão conferidas em `tests_acervo/test_disciplina_discreta.py`.

| Bloco | Tema | Status da resolução |
|---|---|---|
| `discreta-nocoes-logica` | conectivos, equivalências, inferência | sem resolução |
| `discreta-predicados-quantificadores` | quantificadores | sem resolução |
| `discreta-demonstracao-direta` | direta, contrapositiva, casos | validada |
| `discreta-absurdo-contraexemplo` | absurdo (√2, primos), contraexemplo | validada |
| `discreta-conjuntos-operacoes` | notação e operações (slides do Prof. Lucas) | corrigida (∅ ⊆ A; faixa de k) |
| `discreta-lista01-conjuntos` | Lista 01 | validada |
| `discreta-conjuntos-provas` | provas de identidades | corrigida (digitação em 6d) |
| `discreta-relacoes-propriedades` | propriedades e fechos | validada |
| `discreta-relacoes-equivalencia` | equivalência, classes, ordem parcial | validada |
| `discreta-funcoes` | injetiva, sobrejetiva, bijetiva | validada |
| `discreta-inducao` | indução (1 + … + n; 6 divide n³ − n) | validada |
| `discreta-peano-recursao` | Peano, recursão, Hanói | validada |
| `discreta-divisao-bases` | div, mod, bases | validada |
| `discreta-mdc-primos` | Euclides, Bézout, primos, TFA | validada |
| `discreta-congruencias-inverso` | congruência, inverso de 7 mod 26 | corrigida (lista 4, Q7b) |
| `discreta-rsa` | RSA (exemplo de Evaristo e Perdigão) | validada |
| `discreta-estruturas-algebricas` | semigrupo, monoide, grupo, anel, Zn | validada |
| `discreta-algebra-booleana` | axiomas e identidades | validada |
| `discreta-principios-contagem` | multiplicação, inclusão-exclusão, pombos | validada |
| `discreta-permutacoes-combinacoes` | arranjos, combinações, ARARA | validada |
| `discreta-grafos` | grau, isomorfismo, árvores | validada |
| `discreta-recorrencias` | expandir-conjecturar-verificar, lineares | validada |

## Pendências

- Revisão humana e do professor de todos os blocos.
- Questões da Lista 01 em imagem (2, 3 e 13) não foram resolvidas.
- Enunciados ambíguos da lista de contagem da UFCG (com ou sem repetição; salas distintas ou não) não estão no acervo; o rigor manda mostrar as duas leituras.

## Complemento de Ciência da Computação (22/11/2026)

O TutorON organiza o acervo por disciplina, não por curso: o material de Matemática Discreta de Ciência da Computação (COMP362; no PPC de 2011, CCOM010) entrou na disciplina `discreta` já existente, sem cópia e sem mudar a situação (MVP).

**Ementas.** A ementa de CCOM010 no PPC de CC (`ufal-ppc-cc-2011`) é a mesma de ECOM003, sem os itens "Noções Básicas" e "Aplicações". As provas de CC de 2020 e 2021 dão mais peso a congruência linear, Teorema Chinês do Resto e Pequeno Teorema de Fermat do que o material de ECOM; a diferença não justifica disciplina separada.

**O que entrou.** 7 blocos (`s24` a `s30`), todos `material_da_disciplina`, na busca, com `curso:` no cabeçalho, `revisao_humana: pendente` e status `validada`; as contas estão em `tests_acervo/test_disciplina_discreta.py` (testes do complemento de CC).

| Bloco | Tema | Status da resolução |
|---|---|---|
| `discreta-cc-conjuntos-extensao-leis` | conjuntos por extensão, Venn, leis da álgebra dos conjuntos | validada |
| `discreta-cc-relacoes-fecho-ordem` | fecho de equivalência, ordem parcial, relação por grafo, composição | validada |
| `discreta-cc-funcoes-bijecao-composta` | função mal definida, bijeção, composta com inversa, termo geral | validada |
| `discreta-cc-provas-paridade-inducao-euclides` | simplificação lógica, paridade, divisibilidade, indução, Euclides | validada |
| `discreta-cc-congruencias-lineares` | resto de negativo, inverso, $ax\equiv b$ com d soluções | validada |
| `discreta-cc-teorema-chines-resto` | Teorema Chinês do Resto | validada |
| `discreta-cc-fermat-potencias-rsa` | potências pelo Pequeno Teorema de Fermat | validada |

**Observações da validação.** A Prova 1 (2020.2 e 2021.1) define f só em a, b e d no conjunto {a, b, c, d}: o bloco diz que não é função. A prova de 2017 pede compostas com $g(x)=1/x$ "de N em N", que não é função de N em N. O exemplo de TCR da monitoria para em 314; o bloco reduz para 104 (mod 105).

**Fora do acervo.** As fotos da prova de 2017 (nome e respostas de aluno), o código RSA de aluno com chave privada, os livros de Evaristo (já catalogados) e os slides da UFCG e do Prof. Lucas (já catalogados) não foram versionados. Os slides das Aulas 03 e 04 do Prof. Lucas Amorim são os mesmos já cobertos por `ufal-discreta-slides-lucas`.
