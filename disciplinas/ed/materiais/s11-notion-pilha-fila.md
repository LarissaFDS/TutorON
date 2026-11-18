---
id: ed-notion-pilha-fila
titulo: Anotações da turma (Notion) — pilha (LIFO) e fila circular (FIFO) em C
assunto: ed-07-pilhas-filas
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Pilha / Fila"
fontes_catalogo: ufal-ed-notion
autoria: Anotações de alunos da turma de Estrutura de Dados (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código revisado; o original não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Pilha: push e pop no topo, O(1). Fila circular: insere em `(inicio + tamanho) % CAP`, remove em `inicio`. Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

```c
int pop(Pilha *s, int *item)
{
    Elem *velho = s->topo;
    if (velho == NULL) {
        return 0;
    }
    *item = velho->item;
    s->topo = velho->prox;
    free(velho);
    return 1;
}

int enqueue(Fila *f, int item)
{
    if (f->tamanho == CAP) {
        return 0; /* cheia */
    }
    f->itens[(f->inicio + f->tamanho) % CAP] = item;
    f->tamanho++;
    return 1;
}
```

Guardar o `tamanho` (o `current_size` da aula) resolve a ambiguidade cheia × vazia da fila circular, quando `inicio == fim` nos dois casos. A fila da aula já fazia isso e está correta.

Correções da equipe
- Divergência: pop devolvia −1 com a pilha vazia. Como −1 também pode ser um item, quem chama não distingue os dois casos. Aqui pop devolve 0 ou 1 e grava o item por ponteiro.
- Pilha estática e dinâmica não testavam o `malloc` e nunca liberavam a memória; a fila também não.
