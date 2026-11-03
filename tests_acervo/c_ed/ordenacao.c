/* Ordenações da aula (versões revisadas do bloco ed-05), conferidas contra qsort. */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void troca(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

void selection_sort(int v[], int n)
{
    int i, j;
    for (i = 0; i < n - 1; i++) {
        int menor = i;
        for (j = i + 1; j < n; j++) {
            if (v[j] < v[menor]) {
                menor = j;
            }
        }
        troca(&v[i], &v[menor]);
    }
}

void bubble_sort(int v[], int n)
{
    int i, j, trocou = 1;
    for (i = 0; i < n - 1 && trocou; i++) {
        trocou = 0; /* passada sem troca: já está ordenado */
        for (j = 0; j < n - 1 - i; j++) {
            if (v[j] > v[j + 1]) {
                troca(&v[j], &v[j + 1]);
                trocou = 1;
            }
        }
    }
}

void insertion_sort(int v[], int n)
{
    int i, j;
    for (i = 1; i < n; i++) {
        int chave = v[i];
        for (j = i - 1; j >= 0 && v[j] > chave; j--) {
            v[j + 1] = v[j];
        }
        v[j + 1] = chave;
    }
}

/* Quick sort da aula: pivô do meio, partição com dois índices. */
void quick_sort(int v[], int size)
{
    int a = 0, b = size - 1;
    int pivo;
    if (size <= 1) {
        return;
    }
    pivo = v[size / 2];
    while (a < b) {
        while (v[a] < pivo) {
            a++;
        }
        while (v[b] > pivo) {
            b--;
        }
        if (a <= b) {
            troca(&v[a], &v[b]);
            a++;
            b--;
        }
    }
    quick_sort(v, b + 1);
    quick_sort(v + a, size - a);
}

static void merge(int v[], int ini, int meio, int fim, int aux[])
{
    int i = ini, j = meio, k = ini;
    while (i < meio && j < fim) {
        aux[k++] = (v[i] <= v[j]) ? v[i++] : v[j++]; /* <= mantém estável */
    }
    while (i < meio) {
        aux[k++] = v[i++];
    }
    while (j < fim) {
        aux[k++] = v[j++];
    }
    memcpy(v + ini, aux + ini, (size_t)(fim - ini) * sizeof v[0]);
}

static void merge_rec(int v[], int ini, int fim, int aux[])
{
    int meio;
    if (fim - ini < 2) {
        return;
    }
    meio = ini + (fim - ini) / 2;
    merge_rec(v, ini, meio, aux);
    merge_rec(v, meio, fim, aux);
    merge(v, ini, meio, fim, aux);
}

int merge_sort(int v[], int n)
{
    int *aux;
    if (n < 2) {
        return 1;
    }
    aux = malloc((size_t)n * sizeof *aux);
    if (aux == NULL) {
        return 0;
    }
    merge_rec(v, 0, n, aux);
    free(aux);
    return 1;
}

static int cmp(const void *a, const void *b)
{
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

typedef void (*Ordena)(int[], int);

static void merge_void(int v[], int n)
{
    assert(merge_sort(v, n));
}

int main(void)
{
    Ordena metodos[] = {selection_sort, bubble_sort, insertion_sort, quick_sort, merge_void};
    int v[64], esperado[64];
    int m, rodada, n, i;
    srand(2025);
    for (m = 0; m < 5; m++) {
        for (rodada = 0; rodada < 2000; rodada++) {
            n = rand() % 65; /* inclui 0 e 1 elemento */
            for (i = 0; i < n; i++) {
                v[i] = rand() % 10 - 5; /* muitos repetidos */
            }
            if (rodada % 7 == 0) {
                for (i = 0; i < n; i++) {
                    v[i] = i; /* já ordenado */
                }
            }
            memcpy(esperado, v, sizeof v);
            qsort(esperado, (size_t)n, sizeof esperado[0], cmp);
            metodos[m](v, n);
            assert(n == 0 || memcmp(v, esperado, (size_t)n * sizeof v[0]) == 0);
        }
    }
    puts("OK");
    return 0;
}
