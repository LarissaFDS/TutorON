# Curadoria — Programação 1 (`prog1`; ECOM002 e Ciência da Computação)

Situação: **MVP** desde 20/11/2026, sem aviso. O complemento de Ciência da Computação (21/11/2026) não mudou a situação.

## Disciplina

- Código ECOM002, 1º período, 60 h, Engenharia de Computação da UFAL. A linguagem é C.
- Ementa, do PPC de 2014 (p. 23): "Resolução de problemas e desenvolvimento de algoritmos. Análise do problema. Estratégias de solução. Representação e documentação. Programação de algoritmos usando uma linguagem de programação. Estruturação de programas. Noções de tipos e estrutura elementares de dados. Conceito de recursão e sua aplicação."
- Professor dos slides: Rodrigo de Barros Paes (IC/UFAL). Não sabemos se ele é o professor atual da turma.
- Ciência da Computação: o material veio da pasta "01. COMP359 - Programação 1". O PPC de Ciência da Computação de 2006 (`ufal-ppc-cc-2006`, p. 17 e 20) traz a disciplina como COMP002 Programação 1, com 80 h (60 teóricas e 20 práticas), no 1º período. A ementa é **idêntica, palavra por palavra,** à de ECOM002, e o livro de Jaime Evaristo está na bibliografia básica. Por isso é a mesma disciplina no TutorON, e não foi criada uma cópia. Diferenças: a carga horária (80 h contra 60 h) e, nas listas da turma de CC, alocação dinâmica básica (`malloc`, `calloc`, `realloc`), que os slides de ECOM não têm. O código COMP359 não aparece no PPC de 2006, e não encontramos um PPC mais novo de CC: fica como pendência. Não há professor, semestre nem turma identificados no material de CC.
- Cada bloco diz no cabeçalho (`curso:`) de que curso e de que turma veio.

## Fontes (`fontes.json`)

| id | Uso | Observação |
|---|---|---|
| `ufal-prog1-slides-paes` | acervo | Aulas 1 a 16. Licença não declarada; parafraseados, sem os originais no repositório |
| `ufal-prog1-huxley-lista` | acervo | Lista "Questões Huxley Sugestões": só números e temas. Autoria não identificada |
| `ufal-evaristo-livro` | acervo | Livro de Jaime Evaristo. A capa diz "cópias autorizadas", mas não há licença aberta; parafraseado (seção 4.4, do-while, e erros do `scanf`) |
| `ufal-ppc-ecomp-2014` | citada | Ementa |
| `paes-livro-novatec` | referência | Livro do professor (Novatec, 2016). O repositório `r0drigopaes/livro` não tem licença; nada foi copiado |
| `schildt-c-completo-total` | referência | Marcado "não incluído": não foi buscado, baixado, versionado nem ingerido |
| `ime-usp-feofiloff-algoritmos` | referência | CC BY-SA 4.0; só consulta |
| `wikibooks-programar-em-c` | referência | CC BY-SA 4.0; só consulta |
| `cppreference-c` | referência | Não confirmamos a licença na página; só consulta |
| `the-huxley` | referência | Juiz online; nenhum enunciado nem solução no acervo |

## Blocos (24, todos `material_da_disciplina`, todos na busca)

Nenhum bloco é `nota_da_equipe_ia`. Todos têm `revisao_humana: pendente`, e nenhum tem revisão do professor.

| Bloco | Tema | Status da resolução |
|---|---|---|
| `prog1-aula02-algoritmos` | algoritmo, estado, binário | sem resolução |
| `prog1-aula03-compilacao` | compilar, `main` | corrigida |
| `prog1-aula04-variaveis-es` | tipos, `printf`/`scanf` | corrigida |
| `prog1-erros-scanf` | `&`, `%c` depois de número, `fflush(stdin)` | corrigida |
| `prog1-aula05-resolucao-problemas` | roteiro, casas decimais, testes | validada |
| `prog1-divisao-inteira-resto` | `/` e `%` entre inteiros | validada |
| `prog1-aula06-07-decisao` | `if`/`else if`, `=` vs `==` | corrigida |
| `prog1-aula07-08-troca-aninhadas` | troca, decisões aninhadas | sem resolução |
| `prog1-aula09-repeticao` | `while`, `for` | corrigida |
| `prog1-livro-do-while` | `do-while` (livro, 4.4) | corrigida |
| `prog1-aula10-funcoes` | funções, `return` | corrigida |
| `prog1-aula11-vetores` | vetores, vetor como parâmetro | validada |
| `prog1-aula12-matrizes` | matrizes | validada |
| `prog1-aula13-strings` | strings, `fgets`, `'\0'` | corrigida |
| `prog1-aula14-ponteiros` | `&`, `*`, troca por ponteiro | validada |
| `prog1-aula15-structs` | `struct` | validada |
| `prog1-aula16-recursao` | recursão | validada |
| `prog1-huxley-juiz-online` | como o juiz corrige; números e temas (ECOM e CC) | sem resolução |
| `prog1-cc-recursao-listas` | CC, lista 8: casos base, ordem da impressão | corrigida |
| `prog1-cc-ponteiros-listas` | CC, lista 9: `*(v + i)`, `%p`, `**`, `void *` | corrigida |
| `prog1-cc-alocacao-dinamica` | CC, lista 10: `malloc`, `calloc`, `realloc`, `free` | corrigida |
| `prog1-cc-strings-listas` | CC, lista 5: Enter do `fgets`, remover caractere, `toupper` | corrigida |
| `prog1-cc-structs-listas` | CC, lista 6: `typedef`, struct aninhada, vetor de structs | corrigida |
| `prog1-cc-terminal-linux` | CC: comandos do terminal e `gcc` | corrigida |
| `prog1-ec2-ordenacao-vetor` | EC, 2º período: ordenação por trocas e bolha | validada |
| `prog1-ec2-recursao-acumulador` | EC, 2º período: recursão com acumulador, `return` esquecido | validada |

"corrigida" é correção da equipe TutorON e **não é gabarito do professor**. Cada bloco corrigido diz qual foi a divergência.

## Erros encontrados nos originais (corrigidos nos blocos)

- Slides: `int` com 2 bytes e faixa do `float` errada; exemplo do salário sem `;` e com `%d` para valor real; `imprimir_varios` declarada `int` sem `return`; aspas curvas no código; `gets`; `--n` e `parede(h-2)` sem `;`; `^` usado como "ou exclusivo" lógico.
- Livro: `main()` sem tipo; `scanf("%c")` logo depois de ler um número; `fflush(stdin)`.

## Material de Ciência da Computação (21/11/2026)

| Arquivo | Uso |
|---|---|
| Livro de Jaime Evaristo (duas cópias, 139 páginas cada) | já catalogado (`ufal-evaristo-livro`); nada novo entrou |
| "Guia funcional para passar em P1" | `ufal-cc-prog1-guia-huxley`: é a mesma lista de questões do Huxley do bloco s17; 697, 686 e 300 aparecem duas vezes |
| `dicas-terminal.pdf` | `ufal-cc-dicas-terminal`: parafraseado no bloco s23 |
| `c_descomplicado/` (92 arquivos) | `ufal-cc-prog1-codigos-c`: códigos de aluno(s) das listas 5 a 10, sem enunciados nem nomes. Serviram de evidência dos tópicos e como fonte de erros reais. As funções dos blocos s18 a s22 foram escritas pela equipe e testadas, e nenhum código foi copiado |

Ficaram de fora:
- os executáveis (`a.out`, `ata`), que são ELF compilados com gcc 5.4 no Ubuntu;
- os códigos de questões do Huxley (pasta `the huxley`, `lider_copa.c`, `somar_num_grande.c`, `adivinhe.c`, `chandu.c`, `quadro_medalhas.c`), que são atividade avaliativa;
- os códigos incompletos ou que não compilam (`cont_par.c`, `fibonacci.c`, `lista06_24.c`, `lista07_24.c`, `lista08_11.c`, `lista08_12.c`, `lista08_14.c`, `lista09_3.c`);
- os nomes de exemplo que estavam nos códigos.

Erros conferidos compilando ou rodando os originais fora do repositório:
- remover vogais de "oaeb ia" dava "ab a";
- remover espaços de "a  b c" dava "a bc";
- `s[i] - 32` em "ab cd" dava "AB", porque o espaço vira `'\0'`;
- ponteiro usado antes de receber endereço ("used uninitialized");
- função usada antes de ser declarada ("implicit declaration");
- função `float` sem `return` em todos os caminhos;
- aritmética com `void *` ("pointer-arith").

As versões mínimas desses erros estão em `test_erros_dos_slides_e_de_iniciante_dao_aviso`.

## Código

Os trechos de C dos blocos são cópias exatas de `tests_acervo/c_prog1/*.c` (conferido por teste). Os programas compilam com `gcc -std=c99 -Wall -Wextra -pedantic -Werror` e conferem as saídas com casos de teste.

Sanitizers (`-fsanitize=address,undefined`): em 20/11/2026 o teste foi pulado, porque o MinGW 6.3 não tem sanitizers e o Docker Desktop não subiu. Em 21/11/2026 o Docker subiu, e **todos os programas de `tests_acervo/c_prog1/` (os de ECOM e os `cc_*.c`) passaram com AddressSanitizer e UBSan** na imagem `gcc` do Docker. O teste continua tentando o gcc local, depois o Docker, e é pulado com o motivo se não houver nenhum dos dois.

Inversão de string, palíndromo, MDC e primos não têm código no acervo, porque são questões do Huxley. O bloco de strings explica a inversão só em palavras.

## Tópicos e evidência

- Os slides cobrem as aulas 1 a 16: algoritmos, compilação, variáveis e E/S, decisão, repetição, funções, vetores, matrizes, strings, ponteiros, structs e recursão. Todos esses tópicos têm bloco na busca.
- Alocação dinâmica e arquivos não aparecem nos slides de ECOM. A alocação dinâmica básica aparece nas listas de CC e tem bloco próprio (`prog1-14-alocacao-dinamica`). Listas encadeadas e outras estruturas ficam com Estrutura de Dados (`ed`), e o `rigor.md` marca essa fronteira. Arquivos não têm material em nenhum dos dois cursos.

## Dados pessoais excluídos

Ficaram de fora o e-mail do professor, os links do grupo, do Google Sites e do Dropbox e as credenciais da VM, que estavam nos slides. Um teste procura e-mails, senhas e links desse tipo nos blocos.

## Pendências

- Revisão humana dos 18 blocos e revisão do professor.
- Confirmar o código atual (COMP359) e a ementa do PPC de Ciência da Computação em vigor.
- Identificar professor, semestre e turma do material de CC.
- Confirmar quem é o professor atual e se os slides podem ser usados.

## Material do 2º período de Engenharia de Computação (23/11/2026)

| Arquivo | Uso |
|---|---|
| 48 arquivos `.c` de exercícios | `ufal-ec2-prog1-codigos-c`: evidência de dois tópicos novos; blocos s24 (ordenação de vetor) e s25 (recursão com acumulador), com código próprio testado em `tests_acervo/c_prog1/ec2_ordenacao_acumulador.c` |
| executáveis `.exe` e pastas `output/` | fora (binários) |
| `MD.c` (primos e coprimos) | fora: é projeto de Matemática Discreta |

O resto (vetores, matrizes, strings, structs, funções, fatorial com estouro de `int`) já estava nos blocos s01 a s23. Questões do Huxley (como "24 fatorial") não entram resolvidas.

Todos os 48 arquivos foram compilados com `gcc -std=c99 -Wall -Wextra` (MinGW) e rodados com AddressSanitizer/UBSan (Docker `gcc:14`) fora do repositório. Achados, com entrada genérica: índice −1 lido num vetor, estouro de `int` no fatorial de 13 (já no bloco s16), `return` esquecido na chamada recursiva (vira o erro do bloco s25), leitura fora do vetor e estouro de pilha numa recursão sem caso base alcançável. O nome de pessoa que aparece no nome de uma pasta não foi usado.
