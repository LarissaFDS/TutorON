/* Pilha dinâmica e fila circular (versões revisadas do bloco ed-07). */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct elem {
    int item;
    struct elem *prox;
} Elem;

typedef struct {
    Elem *topo;
} Pilha;

int push(Pilha *s, int item)
{
    Elem *novo = malloc(sizeof *novo);
    if (novo == NULL) {
        return 0;
    }
    novo->item = item;
    novo->prox = s->topo;
    s->topo = novo;
    return 1;
}

/* Devolve 1 e grava em *item, ou 0 se a pilha está vazia (sem valor sentinela). */
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

#define CAP 4

typedef struct {
    int itens[CAP];
    int inicio, tamanho;
} Fila;

int enqueue(Fila *f, int item)
{
    if (f->tamanho == CAP) {
        return 0; /* cheia */
    }
    f->itens[(f->inicio + f->tamanho) % CAP] = item;
    f->tamanho++;
    return 1;
}

int dequeue(Fila *f, int *item)
{
    if (f->tamanho == 0) {
        return 0; /* vazia */
    }
    *item = f->itens[f->inicio];
    f->inicio = (f->inicio + 1) % CAP;
    f->tamanho--;
    return 1;
}

int main(void)
{
    Pilha s = {NULL};
    Fila f = {{0}, 0, 0};
    int x, i;
    assert(!pop(&s, &x)); /* vazia */
    assert(push(&s, -1)); /* -1 é um valor válido, não sentinela */
    assert(pop(&s, &x) && x == -1 && s.topo == NULL);
    for (i = 0; i < 5; i++) {
        assert(push(&s, i));
    }
    for (i = 4; i >= 0; i--) {
        assert(pop(&s, &x) && x == i); /* LIFO */
    }
    assert(!dequeue(&f, &x));
    for (i = 0; i < CAP; i++) {
        assert(enqueue(&f, i));
    }
    assert(!enqueue(&f, 99)); /* cheia: recusa */
    assert(dequeue(&f, &x) && x == 0);
    assert(enqueue(&f, 4)); /* dá a volta no vetor */
    for (i = 1; i <= 4; i++) {
        assert(dequeue(&f, &x) && x == i); /* FIFO */
    }
    assert(f.tamanho == 0);
    puts("OK");
    return 0;
}
