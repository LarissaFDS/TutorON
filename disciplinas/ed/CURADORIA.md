# Estrutura de Dados — curadoria do acervo

Situação: **em validação** desde 03/11/2026. A disciplina tem cadastro, acervo e índice próprios e passa pelo mesmo fluxo da IA que PAA, SD, OAC, Cálculo 3 e Física 2: mesmo modelo, mesmo backend e mesmo prompt de sistema, com as regras de [`rigor.md`](rigor.md) anexadas. Enquanto a validação não acontecer, o servidor recusa perguntas de ED no atendimento normal (403). Para testes autorizados, use `TUTORON_LIBERAR_EM_VALIDACAO=ed` (veja [`docs/DISCIPLINAS.md`](../../docs/DISCIPLINAS.md)).

| Item | Estado em 03/11/2026 |
|---|---|
| Cadastro, acervo (20 blocos, 18 na busca) e índice híbrido (`bge-m3`) | **Feitos** |
| Código C dos blocos | **Compilado e testado**: `tests_acervo/c_ed/*.c` com `gcc -std=c99 -Wall -Wextra -pedantic -Werror`, e com `-fsanitize=address,undefined` no gcc 14 do Docker (o MinGW local não tem sanitizadores) |
| Revisão humana interna | **Pendente** (`revisao_humana: pendente` em todos os blocos) |
| Autorização para publicar transcrições (anotações e PDFs do professor) | **Não dada**: os blocos reescrevem e parafraseiam |
| Aprovação do professor | **Não declarada**; nenhum bloco tem `revisao_professor: sim` |
| Respostas da IA com o modelo real | **Conferidas em 5 casos** em 03/11/2026 com o Gemini 3.6 Flash (seção 7); não substitui a validação com alunos |

- Catálogo legível por máquina: [`fontes.json`](fontes.json)
- Blocos (um arquivo por bloco): [`materiais/`](materiais/). `s01`–`s15` = anotações da turma no Notion, reescritas e corrigidas; `s16`–`s18` = material do professor, parafraseado; `n*` = notas da equipe (candidatas, fora da busca)
- Os trechos de código dos blocos são cópias exatas de funções dos programas de teste; `tests_acervo/test_disciplina_ed.py` confere isso.
- Gerados (não editar à mão): [`acervo/itens.json`](acervo/itens.json) e [`acervo/indice.json`](acervo/indice.json)

## 1. Ementa e professor

Os PDFs anexados no Notion trazem "Estruturas de Dados - ECOM008" e "Márcio Ribeiro, UFAL, Instituto de Computação" (`ufal-ed-prof-preparatorio`, `ufal-ed-prof-sat`). O PPC de Engenharia de Computação da UFAL (2014, `ufal-ppc-ecomp-2014`) dá para ECOM008 60 h (40 teóricas, 20 práticas), no 2º semestre da grade de 2014. A ementa diz, em resumo: introdução à orientação a objetos; containers (arrays, arrays ordenados, listas e variantes com alocação dinâmica); TADs pilha, fila, fila de prioridade, árvore e grafo; notação de complexidade; busca e ordenação. A bibliografia básica cita Lafore (Java), Ascencio & Campos e Forbellone & Eberspacher. A turma estuda no 3º período e programa em **C**, não em Java; hash, AVL, heap, Huffman e SAT aparecem no Notion e nos projetos, não na ementa de 2014. Não foi localizado um plano de ensino mais recente. A curadoria **não está validada pelo professor**.

## 2. Tópicos, evidência e blocos

| Assunto | Evidência da turma | Blocos |
|---|---|---|
| `ed-01-ponteiros-memoria` | Notion (Ponteiros, Aritmética de ponteiros em imagem, sizeof, Alocação) | `ed-notion-ponteiros-lista`, `ed-notion-sizeof-alocacao` |
| `ed-02-structs-funcoes` | Notion (Structs, Ponteiros para Funções, Map e Filter, Integral) | `ed-notion-structs`, `ed-notion-ponteiros-funcao` |
| `ed-03-busca` | Notion (Busca, Análise da busca) | `ed-notion-busca` |
| `ed-04-complexidade-recorrencias` | Notion (Big-O, Equações de recorrência em imagem) | `ed-notion-big-o`, `ed-notion-recorrencias` |
| `ed-05-ordenacao` | Notion (Ordenação) | `ed-notion-ordenacao-simples`, `ed-notion-quick-merge` |
| `ed-06-listas` | Notion (Listas, Apêndice, Chamada de Funções) | `ed-notion-listas-genericas` |
| `ed-07-pilhas-filas` | Notion (Pilha estática/dinâmica, Fila) | `ed-notion-pilha-fila` |
| `ed-08-heap-fila-prioridade` | Notion (Priority Queue, Heap no Apêndice; página Heaps vazia) | `ed-notion-heap` |
| `ed-09-hash` | Notion (Hash aberto e encadeado) | `ed-notion-hash` |
| `ed-10-arvores` | Notion (ABB; página AVL vazia) | `ed-notion-abb`, `ed-nota-avl` (candidata) |
| `ed-11-grafos` | Notion (DFS/BFS) | `ed-notion-grafos` |
| `ed-12-huffman` | Notion (Exemplo com Árvore Binária) + PDF do professor | `ed-prof-huffman` |
| `ed-13-sat` | PDF da aula 21 + Casos teste do Notion | `ed-prof-sat` |
| `ed-14-projetos-depuracao` | PDF do professor (AB2) | `ed-prof-projetos-ab2`, `ed-nota-depuracao-memoria` (candidata) |

### Fronteira com PAA

Os resultados são os mesmos nas duas disciplinas; o ângulo muda. Os blocos de ED não copiam blocos de PAA, e a busca de cada disciplina usa só o próprio acervo, sem filtro por palavra-chave (`tests_acervo/test_disciplina_ed.py`).

| Assunto | ED (este acervo) | PAA (`02-acervo`) |
|---|---|---|
| Merge sort, Quick sort | implementação em C, índices, memória auxiliar, testes; O(n log n), Quick O(n²) no pior caso | recorrência e prova (Teorema Mestre, divisão e conquista) |
| Big-O e recorrências | contar laços, expansão até o caso-base | definição formal, provas, Teorema Mestre |
| Heap | vetor com raiz em 1, limites, heapsort | análise de construção O(n), uso em algoritmos gulosos |
| BFS, DFS | lista de adjacência, fila, marcação | corretude, aplicações em grafos |
| SAT | leitor DIMACS e backtracking do projeto | NP-completude, redução |
| Huffman | árvore, fila de prioridade, arquivo binário | prova da escolha gulosa |

Uma pergunta como "prove pelo Teorema Mestre que o Merge sort é O(n log n)" com ED selecionada recebe o material de ED (recorrência e expansão) e a indicação de que a prova formal é de PAA (regra em `rigor.md`).

## 3. Inventário do Notion e dos anexos

Página "Engenharia de Computação / Terceiro Período / Estrutura de Dados" (linguagem C), lida pelo conector do Notion em 02/11/2026.

- **Lidas e usadas**: Ponteiros, Structs, sizeof, Alocação de memória, Ponteiros para Funções, Map e Filter, Integral, Busca, Análise da busca, Big-O, Ordenação, Listas, Apêndice, Chamada de Funções, Pilha, Fila, Priority Queue, Hash, Árvore Binária de Busca, DFS/BFS, Huffman (Exemplo com Árvore Binária), Casos teste do SAT.
- **Só imagem** (lidas e conferidas; não versionadas): Aritmética de Ponteiros e Equações de recorrência (quadro dos métodos de ordenação e expansões do Quick sort, do Merge sort e da busca binária).
- **Vazias**: Método da árvore, Método da expansão, AVL, Heaps (página principal), Compactação, Descompactação.
- **Ilegíveis**: embed do Miro; objeto externo do Huffman.
- **Seminário**: código de exemplo só para Windows (`windows.h`), pilha de estados de jogo; não entrou no acervo (não é C padrão).
- **PDFs do professor** (anexos, fora do repositório; sha256 em `fontes.json`): "Preparatório para os Projetos – AB 2" e "Aula 21 – SAT Solver".

Nenhum código de projeto avaliativo de aluno foi lido ou versionado. O exemplo de Huffman do Notion monta a árvore e os códigos, sem leitura de arquivo; ele não é uma implementação do projeto.

## 4. Erros encontrados nas anotações e como foram tratados

Cada correção foi conferida por um programa em `tests_acervo/c_ed/`. As falhas de memória do original foram reproduzidas com AddressSanitizer num programa mínimo fora do repositório.

| Bloco | Original | Revisado | Justificativa / evidência |
|---|---|---|---|
| `ed-notion-ponteiros-lista` | `typedef ... Noe;` usado como `Node`; `#include` colados; `int *p = &` cortado; sem teste do malloc; lista nunca liberada | um só nome; malloc testado; `liberar` | não compila; a versão revisada passa no LeakSanitizer (`lista.c`) |
| `ed-notion-sizeof-alocacao` | `%lu` para size_t; "int pode ter 8 bytes em 64 bits"; sizeof "salvo alocação dinâmica"; "estática (ou automática)" | `%zu`; int costuma ter 4 bytes; a exceção é o VLA; local é automática | padrão C99 (cppreference para conferência) |
| `ed-notion-structs` | `int n; struct personagem p[n];` antes do scanf; `scanf("%s")` | malloc depois de ler n; `%49s` | n não inicializado (comportamento indefinido); estouro de buffer |
| `ed-notion-ponteiros-funcao` | map/filter devolvem só o último valor; `result` não inicializado; exemplo em Haskell; `volume_circulo` | vetor de saída e contagem; versão em C; `volume_esfera` | o código não fazia o que o texto dizia |
| `ed-notion-busca` | "not found" dentro do laço; melhor caso = primeiro elemento; `sizeof(v)/4.0` | retorno −1 depois do laço; melhor caso = meio | `busca.c` |
| `ed-notion-big-o` | O "levando em consideração o pior caso"; regra 3 truncada | O é um limite; cada caso tem o seu; regra da soma completa | definição |
| `ed-notion-recorrencias` | T(0) = 0 e T(1) = 1 como "elementos neutros"; quadro sem o pior caso do Quick | o caso-base vem do algoritmo (custo constante da entrada mínima); Quick O(n²) no pior caso | `pendente_professor`: se for convenção do professor, vale como convenção |
| `ed-notion-quick-merge` | merge imprime `L[n1]` e `R[n2]` | sem leitura fora; auxiliar alocado uma vez | heap-buffer-overflow no ASan; `ordenacao.c` compara com qsort. O Quick sort da aula passou em 200 000 vetores aleatórios |
| `ed-notion-listas-genericas` | `integers_equals(void, void)`; void* misturado com int; `remove` conflita com stdio; malloc(0) | `const void *`; `remover` | não compila; conflito de nome |
| `ed-notion-pilha-fila` | pop devolve −1 como sentinela; sem malloc testado; sem free | pop devolve 0/1 e grava por ponteiro | −1 é um item válido (`pilha_fila.c`) |
| `ed-notion-heap` | `data[100]` com raiz em 1 e `data[++size]` | `data[MAX_HEAP_SIZE + 1]`; heapsort constrói o heap | stack-buffer-overflow no ASan; `heap.c` |
| `ed-notion-hash` | índice negativo; para no removido e duplica; −1 reservado; malloc no remove; cheia em silêncio | `h` não negativa; estado separado; atualiza chave existente | `hash.c` com colisões 3, 10, 17, −4 |
| `ed-notion-abb` | sem teste do malloc; sem liberar | `liberar` em pós-ordem | lógica da aula **validada** (`arvores.c`) |
| `ed-notion-grafos` | laço de criação começa em 1 | começa em 0 | `vertices[0]` com lixo; `grafos.c` |
| `ed-prof-huffman` | códigos f 0, c 100, d 101, a 1100, b 1101, e 111 | iguais | conferidos com heapq (224 bits) no teste |
| `ed-prof-sat` | exemplo `p cnf 3 3` SAT com 1 = 1, 2 = 0, 3 = 0 | igual | conferido por força bruta no teste |

## 5. Resoluções: status

| Status | Blocos |
|---|---|
| `validada` | `ed-notion-ordenacao-simples`, `ed-notion-abb`, `ed-prof-huffman`, `ed-prof-sat` |
| `corrigida` | `ed-notion-ponteiros-lista`, `ed-notion-sizeof-alocacao`, `ed-notion-structs`, `ed-notion-ponteiros-funcao`, `ed-notion-busca`, `ed-notion-big-o`, `ed-notion-quick-merge`, `ed-notion-listas-genericas`, `ed-notion-pilha-fila`, `ed-notion-heap`, `ed-notion-hash`, `ed-notion-grafos` |
| `pendente_professor` | `ed-notion-recorrencias` (convenção dos casos-base) |

`ed-prof-projetos-ab2` não tem resolução (regras das entregas). Os casos 1–8 de SAT do Notion não foram transcritos; só se registrou que o caso 6 declara 5 cláusulas no cabeçalho e traz 4.

## 6. Notas da equipe e validação

`ed-nota-avl` e `ed-nota-depuracao-memoria` foram escritas pela equipe com auxílio de IA: `natureza: nota_da_equipe_ia`, `curadoria: candidato` e, portanto, fora da busca. O código da AVL (rotações LL, RR, LR, RL) foi testado em `arvores.c`, mas a nota só entra na busca depois de uma revisão humana registrada. Nenhuma foi marcada como aprovada.

## 7. Projetos avaliativos, IA e limitações

- Huffman e SAT: o acervo explica conceitos, regras e depuração; nenhuma implementação completa foi versionada. `rigor.md` instrui a IA a não escrever o projeto e a usar perguntas (modo socrático).
- O TutorON não compila nem executa código do aluno no servidor. Os programas de `tests_acervo/c_ed/` são da equipe e rodam só na suíte de testes.
- Os sanitizadores não existem no MinGW 6.3 desta máquina. Os testes usam o `gcc` local quando ele aceita `-fsanitize`; senão usam a imagem `gcc:14` do Docker, se ela existir; senão registram o motivo do skip.
- Conferência com o modelo real (03/11/2026). ED foi liberada só no processo de teste; os modelos Gemini 3.8 e 3.7 Flash deram HTTP 503, e respondeu o Gemini 3.6 Flash.
  - A leitura de foto, com uma imagem de código feita pela equipe, transcreveu o código certo. `backend/foto.py` não mudou.
  - Pedido do projeto completo de Huffman: a IA recusou e seguiu no modo socrático.
  - "Prove pelo Teorema Mestre...": a IA indicou PAA para a prova formal e usou o material de ED.
  - Heap cheio e pop com a pilha vazia: as respostas batem com os blocos corrigidos.
  - Sem a liberação, o servidor respondeu 403.
- Manim não está instalado nesta máquina: nenhuma animação foi gerada e nenhum modelo de animação foi criado. O teste de animação da suíte é pulado por isso.
- Lacuna de PAA (fora do escopo desta entrega): com PAA selecionada, perguntas de implementação em C ("Por que meu heap escreve fora do vetor...", "Como liberar com free uma lista encadeada...") trazem blocos de PAA pouco relacionados (pico de vetor unimodal, ordenação de torneio), por coincidência léxica no acervo de OCR. Isso não vaza material de ED, porque os índices são separados. Corrigir exigiria mudar o acervo ou o corte de PAA; essas perguntas não entraram na bateria de `eval/relevancia.py`.

## 8. Fontes externas

As fontes foram abertas e conferidas em 03/11/2026 (título, autoria, URL e licença declarada). A classificação está em `fontes.json`:

- **Alta**: Notion da turma (`ufal-ed-notion`), os dois PDFs do professor (`ufal-ed-prof-preparatorio`, `ufal-ed-prof-sat`) e Feofiloff, em C e com CC BY-SA 4.0 (`feofiloff-algoritmos-c`).
- **Média**: Open Data Structures, CC BY, código em Java/C++ (`ods-morin`); documentação do GCC (`gcc-instrumentacao`), do ASan (`clang-addresssanitizer`) e do Valgrind (`valgrind-memcheck`).
- **Referência**:
  - MIT OCW 6.006, CC BY-NC-SA 4.0, em Python (`mit-ocw-6006`)
  - PPC de 2014 (`ufal-ppc-ecomp-2014`)
  - artigo de Huffman de 1952 (`huffman-1952`)
  - cppreference, licença não confirmada nesta curadoria (`cppreference-c`)
  - visualizações de David Galles (`usf-galles-visualizacao`)
  - VisuAlgo, termos não lidos (`visualgo`)
  - Python Tutor (`python-tutor-c`)

Não se usaram blogs nem sites de soluções.
