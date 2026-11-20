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
