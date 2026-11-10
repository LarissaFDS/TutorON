---
id: ed-nota-depuracao-memoria
titulo: Nota da equipe — depurar memória em C com -Wall, AddressSanitizer e Valgrind
assunto: ed-14-projetos-depuracao
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: gcc-instrumentacao,clang-addresssanitizer,valgrind-memcheck
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Nota da equipe, aguarda revisão humana.

Compile sempre com avisos: `gcc -std=c99 -Wall -Wextra -pedantic -g prog.c -o prog`. Aviso não é enfeite: variável não usada, comparação de sinal e formato errado no printf costumam ser bugs.

AddressSanitizer e UBSan (Linux/macOS, gcc ou clang): `gcc -g -fsanitize=address,undefined prog.c -o prog`. Ao rodar, o programa para no primeiro acesso inválido e mostra a linha:
- heap-buffer-overflow: leu ou escreveu além de um bloco de malloc (ex.: `L[n1]` no merge);
- stack-buffer-overflow: além de um vetor local (ex.: `data[++size]` no heap cheio);
- heap-use-after-free: usou depois do free (ex.: `free(p); p = p->prox;`);
- detected memory leaks: faltou free.

Valgrind: `valgrind --leak-check=full ./prog` acusa leitura de memória não inicializada, além de vazamentos.

No Windows com MinGW o -fsanitize costuma não estar disponível; use WSL, Docker ou um Linux.

Roteiro: reproduza com a menor entrada (estrutura vazia, um elemento, primeiro e último), leia a primeira mensagem, não a última, e confira cada ponteiro antes de usar.
