# Curadoria — Programação 1 (`prog1`, ECOM002)

Situação: **em validação**. A barreira continua ligada; `TUTORON_LIBERAR_EM_VALIDACAO` não deve ser ligado no servidor público.

## Disciplina

- Código ECOM002, 1º período, 60 h, Engenharia de Computação da UFAL. A linguagem é C.
- Ementa, do PPC de 2014 (p. 23): "Resolução de problemas e desenvolvimento de algoritmos. Análise do problema. Estratégias de solução. Representação e documentação. Programação de algoritmos usando uma linguagem de programação. Estruturação de programas. Noções de tipos e estrutura elementares de dados. Conceito de recursão e sua aplicação."
- Professor dos slides: Rodrigo de Barros Paes (IC/UFAL). Não sabemos se ele é o professor atual da turma.

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

## Blocos (18, todos `material_da_disciplina`, todos na busca)

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
| `prog1-huxley-juiz-online` | como o juiz corrige; números e temas | sem resolução |

"corrigida" é correção da equipe TutorON e **não é gabarito do professor**. Cada bloco corrigido diz qual foi a divergência.

## Erros encontrados nos originais (corrigidos nos blocos)

- Slides: `int` com 2 bytes e faixa do `float` errada; exemplo do salário sem `;` e com `%d` para valor real; `imprimir_varios` declarada `int` sem `return`; aspas curvas no código; `gets`; `--n` e `parede(h-2)` sem `;`; `^` usado como "ou exclusivo" lógico.
- Livro: `main()` sem tipo; `scanf("%c")` logo depois de ler um número; `fflush(stdin)`.

## Código

Os trechos de C dos blocos são cópias exatas de `tests_acervo/c_prog1/*.c` (conferido por teste). Os programas compilam com `gcc -std=c99 -Wall -Wextra -pedantic -Werror` e conferem as saídas com casos de teste.

**Os sanitizers (`-fsanitize=address,undefined`) não rodaram nesta máquina.** O gcc local é MinGW 6.3, que não tem sanitizers, e o Docker Desktop não subiu. O teste tenta primeiro o gcc local, depois o Docker, e senão é pulado com o motivo. Ele precisa rodar em Linux antes da revisão final.

Inversão de string, palíndromo, MDC e primos não têm código no acervo, porque são questões do Huxley. O bloco de strings explica a inversão só em palavras.

## Tópicos e evidência

- Os slides cobrem as aulas 1 a 16: algoritmos, compilação, variáveis e E/S, decisão, repetição, funções, vetores, matrizes, strings, ponteiros, structs e recursão. Todos esses tópicos têm bloco na busca.
- Alocação dinâmica e arquivos não aparecem nos slides. A alocação dinâmica fica com Estrutura de Dados (`ed`), e o `rigor.md` marca essa fronteira. Arquivos não têm material.

## Dados pessoais excluídos

Ficaram de fora o e-mail do professor, os links do grupo, do Google Sites e do Dropbox e as credenciais da VM, que estavam nos slides. Um teste procura e-mails, senhas e links desse tipo nos blocos.

## Pendências

- Revisão humana dos 18 blocos e revisão do professor.
- Rodar os sanitizers em Linux.
- Confirmar quem é o professor atual e se os slides podem ser usados.
