/* Heap máximo com índice a partir de 1 (versão revisada do bloco ed-08). */
#include <assert.h>
#include <stdio.h>

#define MAX_HEAP_SIZE 100

typedef struct {
    int size;
    int data[MAX_HEAP_SIZE + 1]; /* data[0] fica sem uso */
} Heap;

static void troca(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int enqueue(Heap *h, int item)
{
    int i;
    if (h->size >= MAX_HEAP_SIZE) {
        return 0;
    }
    i = ++h->size;
    h->data[i] = item;
    while (i > 1 && h->data[i / 2] < h->data[i]) {
        troca(&h->data[i], &h->data[i / 2]);
        i /= 2;
    }
    return 1;
}

void max_heapify(int data[], int size, int i)
{
    for (;;) {
        int maior = i, esq = 2 * i, dir = 2 * i + 1;
        if (esq <= size && data[esq] > data[maior]) {
            maior = esq;
        }
        if (dir <= size && data[dir] > data[maior]) {
            maior = dir;
        }
        if (maior == i) {
            return;
        }
        troca(&data[i], &data[maior]);
        i = maior;
    }
}

int dequeue(Heap *h, int *item)
{
    if (h->size == 0) {
        return 0;
    }
    *item = h->data[1];
    h->data[1] = h->data[h->size--];
    max_heapify(h->data, h->size, 1);
    return 1;
}

/* data[1..size] em qualquer ordem: primeiro constrói o heap, depois ordena. */
void heapsort(int data[], int size)
{
    int i;
    for (i = size / 2; i >= 1; i--) {
        max_heapify(data, size, i);
    }
    for (i = size; i >= 2; i--) {
        troca(&data[1], &data[i]);
        max_heapify(data, i - 1, 1);
    }
}

int main(void)
{
    Heap h = {0, {0}};
    int v[] = {0, 5, 1, 9, 3, 9, 7, -2}; /* v[0] sem uso */
    int i, x, anterior;
    assert(!dequeue(&h, &x)); /* vazio */
    assert(enqueue(&h, 42) && dequeue(&h, &x) && x == 42); /* um elemento */
    for (i = 0; i < MAX_HEAP_SIZE; i++) {
        assert(enqueue(&h, (i * 37) % 101));
    }
    assert(!enqueue(&h, 1)); /* cheio: não escreve fora do vetor */
    anterior = 1000;
    while (dequeue(&h, &x)) {
        assert(x <= anterior);
        anterior = x;
    }
    heapsort(v, 7);
    for (i = 1; i < 7; i++) {
        assert(v[i] <= v[i + 1]);
    }
    puts("OK");
    return 0;
}
