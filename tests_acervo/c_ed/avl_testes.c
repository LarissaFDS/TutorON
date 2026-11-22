/* Como testar AVL e heap (bloco ed-testes-avl-heap): sequências de inserção e remoção
   com a pré-ordem esperada, verificador de balanceamento e build-heap mínimo.
   As pré-ordens esperadas foram conferidas com uma implementação independente em Python. */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct avl {
    int chave, altura;
    struct avl *esq, *dir;
} Avl;

static int alt(const Avl *a)
{
    return a == NULL ? 0 : a->altura;
}

static void atualizar(Avl *a)
{
    int e = alt(a->esq), d = alt(a->dir);
    a->altura = 1 + (e > d ? e : d);
}

static Avl *rot_dir(Avl *y)
{
    Avl *x = y->esq;
    y->esq = x->dir;
    x->dir = y;
    atualizar(y);
    atualizar(x);
    return x;
}

static Avl *rot_esq(Avl *x)
{
    Avl *y = x->dir;
    x->dir = y->esq;
    y->esq = x;
    atualizar(x);
    atualizar(y);
    return y;
}

/* Rebalanceia olhando as alturas dos filhos: serve para inserção e remoção. */
static Avl *balancear(Avl *a)
{
    int fb;
    atualizar(a);
    fb = alt(a->esq) - alt(a->dir);
    if (fb > 1) {
        if (alt(a->esq->esq) < alt(a->esq->dir)) a->esq = rot_esq(a->esq);
        return rot_dir(a);
    }
    if (fb < -1) {
        if (alt(a->dir->dir) < alt(a->dir->esq)) a->dir = rot_dir(a->dir);
        return rot_esq(a);
    }
    return a;
}

static Avl *inserir(Avl *a, int k)
{
    if (a == NULL) {
        a = malloc(sizeof *a);
        if (a == NULL) exit(1);
        a->chave = k;
        a->altura = 1;
        a->esq = a->dir = NULL;
        return a;
    }
    if (k < a->chave) a->esq = inserir(a->esq, k);
    else if (k > a->chave) a->dir = inserir(a->dir, k);
    else return a;
    return balancear(a);
}

/* Nó com dois filhos troca de chave com o sucessor (menor da direita). */
static Avl *remover(Avl *a, int k)
{
    if (a == NULL) return NULL; /* remover de árvore vazia não quebra */
    if (k < a->chave) a->esq = remover(a->esq, k);
    else if (k > a->chave) a->dir = remover(a->dir, k);
    else if (a->esq == NULL || a->dir == NULL) {
        Avl *f = a->esq != NULL ? a->esq : a->dir;
        free(a);
        return f;
    } else {
        Avl *s = a->dir;
        while (s->esq != NULL) s = s->esq;
        a->chave = s->chave;
        a->dir = remover(a->dir, s->chave);
    }
    return balancear(a);
}

/* O teste: recalcula a altura de baixo para cima, sem confiar no campo guardado.
   Devolve a altura real, ou -1 se a ordem, a altura guardada ou o fator falhar. */
int eh_avl(const Avl *a, long min, long max)
{
    int he, hd;
    if (a == NULL) return 0;
    if (a->chave <= min || a->chave >= max) return -1;
    he = eh_avl(a->esq, min, a->chave);
    hd = eh_avl(a->dir, a->chave, max);
    if (he < 0 || hd < 0 || abs(he - hd) > 1) return -1;
    if (a->altura != 1 + (he > hd ? he : hd)) return -1;
    return a->altura;
}

static int pre_ordem(const Avl *a, int v[], int n)
{
    if (a == NULL) return n;
    v[n++] = a->chave;
    n = pre_ordem(a->esq, v, n);
    return pre_ordem(a->dir, v, n);
}

static int confere(const Avl *a, const int *esperado, int n)
{
    int v[64];
    return pre_ordem(a, v, 0) == n && memcmp(v, esperado, n * sizeof *v) == 0;
}

static void liberar(Avl *a)
{
    if (a == NULL) return;
    liberar(a->esq);
    liberar(a->dir);
    free(a);
}

/* Heap mínimo: desce o elemento i até os filhos serem maiores ou iguais. */
static void descer_min(int v[], int n, int i)
{
    for (;;) {
        int m = i, e = 2 * i + 1, d = e + 1, t;
        if (e < n && v[e] < v[m]) m = e;
        if (d < n && v[d] < v[m]) m = d;
        if (m == i) return;
        t = v[i];
        v[i] = v[m];
        v[m] = t;
        i = m;
    }
}

void build_heap_min(int v[], int n)
{
    int i;
    for (i = n / 2 - 1; i >= 0; i--) descer_min(v, n, i);
}

int eh_heap_min(const int v[], int n)
{
    int i;
    for (i = 1; i < n; i++)
        if (v[(i - 1) / 2] > v[i]) return 0;
    return 1;
}

int main(void)
{
    static const int seq[] = {1, 4, 7, 10, 13, 2, 5, 8, 11, 14, 3, 15, 6, 12, 9};
    static const int p0[] = {10, 4, 2, 1, 3, 7, 5, 6, 8, 9, 13, 11, 12, 14, 15};
    static const int p6[] = {10, 4, 2, 1, 3, 7, 5, 8, 9, 13, 11, 12, 14, 15};
    static const int p11[] = {10, 4, 2, 1, 3, 7, 5, 8, 9, 13, 12, 14, 15};
    static const int p10[] = {7, 4, 2, 1, 3, 5, 12, 8, 9, 14, 13, 15};
    static const int t3[] = {20, 18, 22};
    int b[] = {15, 14, 13, 10, 11, 12, 9, 8, 7};
    static const int b_esp[] = {7, 8, 9, 10, 11, 12, 13, 14, 15};
    Avl *r = NULL;
    int i, v[64];
    assert(pre_ordem(r, v, 0) == 0 && eh_avl(r, -1L, 100L) == 0); /* vazia */
    r = remover(r, 12);
    assert(r == NULL);
    for (i = 0; i < 15; i++) {
        r = inserir(r, seq[i]);
        assert(eh_avl(r, -1L, 100L) >= 0); /* confere depois de cada operação */
    }
    assert(confere(r, p0, 15) && eh_avl(r, -1L, 100L) == 5);
    /* teorema da altura: h < 1,44 lg(n + 2); com n = 15, h <= 5 */
    r = remover(r, 6);
    assert(confere(r, p6, 14) && eh_avl(r, -1L, 100L) >= 0);
    r = remover(r, 11);
    assert(confere(r, p11, 13) && eh_avl(r, -1L, 100L) >= 0);
    r = remover(r, 10);
    assert(confere(r, p10, 12) && eh_avl(r, -1L, 100L) >= 0);
    liberar(r);
    r = NULL;
    r = inserir(inserir(inserir(r, 22), 18), 20); /* zigue-zague: rotação dupla */
    assert(confere(r, t3, 3));
    r->esq->altura = 7; /* altura guardada errada: o teste precisa pegar */
    assert(eh_avl(r, -1L, 100L) == -1);
    r->esq->altura = 1;
    liberar(r);
    build_heap_min(b, 9);
    assert(memcmp(b, b_esp, sizeof b) == 0 && eh_heap_min(b, 9));
    b[4] = 1; /* estraga o heap: o verificador precisa pegar */
    assert(!eh_heap_min(b, 9));
    puts("OK");
    return 0;
}
