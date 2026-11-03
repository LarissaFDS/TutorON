---
id: ed-notion-listas-genericas
titulo: Anotações da turma (Notion) — lista genérica com void* e comparação por ponteiro de função
assunto: ed-06-listas
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Listas / Apêndice / Chamada de Funções"
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
Lista genérica: o nó guarda `void *item`, e quem usa a lista passa uma função de comparação. Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

```c
typedef struct gnode {
    void *item;
    struct gnode *prox;
} GNode;

int inteiros_iguais(const void *a, const void *b)
{
    return *(const int *)a == *(const int *)b;
}
```

A busca recebe `const void *alvo` e `int (*iguais)(const void *, const void *)` e chama `iguais(p->item, alvo)`. Não se desreferencia `void *` direto: converta para o tipo certo antes.

Correções da equipe
- Divergência: a anotação declarava `integers_equals(void item1, void item2)`. Um parâmetro não pode ter tipo `void`, então não compila; o certo é `const void *`.
- A busca genérica misturava `void *` com um item `int`.
- Uma função chamada `remove` conflita com `remove` de `<stdio.h>`; use outro nome (ex.: `remover`).
- `add` não testava o `malloc`; `list_to_array` chamava `malloc(0)` com a lista vazia e não testava o retorno; a lista do exemplo "Chamada de Funções" nunca era liberada.

Remoção do primeiro, do meio e do último, com lista vazia e de um elemento, está no bloco de ponteiros e lista (testada com AddressSanitizer).
