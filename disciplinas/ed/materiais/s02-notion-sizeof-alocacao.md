---
id: ed-notion-sizeof-alocacao
titulo: Anotações da turma (Notion) — aritmética de ponteiros, sizeof e alocação dinâmica
assunto: ed-01-ponteiros-memoria
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Aritmética de Ponteiros / sizeof / Alocação de memória"
fontes_catalogo: ufal-ed-notion
autoria: Anotações de alunos da turma de Estrutura de Dados (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código revisado; o original não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
Aritmética de ponteiros: se `int *p = v;`, então `p + i` aponta para `v[i]` e `*(p + i)` é `v[i]`. Somar 1 avança `sizeof(int)` bytes, não 1 byte. Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

`sizeof` dá o tamanho em bytes do tipo ou objeto, com tipo `size_t`; imprima com `%zu` (C99). Tamanho de vetor: `sizeof v / sizeof v[0]`, que só funciona com o vetor de verdade, não com um ponteiro recebido como parâmetro.

Alocação: variáveis locais são automáticas (criadas na pilha quando a função roda e destruídas ao sair); globais e `static` têm duração estática; `malloc` reserva memória no heap, que dura até o `free`. Sempre teste o retorno: `int *v = malloc(n * sizeof *v); if (v == NULL) ...`. Para cada `malloc`, um `free`, uma única vez.

Correções da equipe
- Divergência: a anotação usava `%lu` para `size_t`; o certo é `%zu`.
- Dizia que int "pode ter 8 bytes" em 64 bits: nas plataformas comuns (Linux, Windows, macOS em 64 bits) int tem 4 bytes; o padrão só exige ao menos 16 bits. O que costuma ter 8 bytes é o ponteiro, e mesmo isso depende da plataforma.
- Dizia que sizeof é calculado na compilação "salvo alocação dinâmica": sizeof nunca mede o bloco de um malloc (`sizeof p` dá o tamanho do ponteiro). A exceção real é o vetor de tamanho variável (VLA), medido em tempo de execução.
- Chamava a alocação local de "estática (ou automática)": são coisas diferentes, como acima.
- Removidos restos de cópia ("CopiarEditar").
