/* Árvore binária de busca e AVL (blocos ed-10 e ed-11).
   Testa as quatro rotações: simples (LL, RR) e duplas (LR, RL). */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct arv {
    int chave, altura;
    struct arv *esq, *dir;
} Arv;

static int altura(const Arv *a)
{
    return a == NULL ? 0 : a->altura;
}

static int maior(int x, int y)
{
    return x > y ? x : y;
}

static void atualizar(Arv *a)
{
    a->altura = 1 + maior(altura(a->esq), altura(a->dir));
}

static Arv *novo(int chave)
{
    Arv *a = malloc(sizeof *a);
    if (a != NULL) {
        a->chave = chave;
        a->altura = 1;
        a->esq = a->dir = NULL;
    }
    return a;
}

/* ABB sem balanceamento; chave repetida não é inserida de novo. */
Arv *inserir_abb(Arv *a, int chave)
{
    if (a == NULL) {
        return novo(chave);
    }
    if (chave < a->chave) {
        a->esq = inserir_abb(a->esq, chave);
    } else if (chave > a->chave) {
        a->dir = inserir_abb(a->dir, chave);
    }
    atualizar(a);
    return a;
}

Arv *buscar(Arv *a, int chave)
{
    while (a != NULL && a->chave != chave) {
        a = chave < a->chave ? a->esq : a->dir;
    }
    return a;
}

static Arv *rot_dir(Arv *y)
{
    Arv *x = y->esq;
    y->esq = x->dir;
    x->dir = y;
    atualizar(y);
    atualizar(x);
    return x;
}

static Arv *rot_esq(Arv *x)
{
    Arv *y = x->dir;
    x->dir = y->esq;
    y->esq = x;
    atualizar(x);
    atualizar(y);
    return y;
}

static int rotacoes;

Arv *inserir_avl(Arv *a, int chave)
{
    int fb;
    if (a == NULL) {
        return novo(chave);
    }
    if (chave < a->chave) {
        a->esq = inserir_avl(a->esq, chave);
    } else if (chave > a->chave) {
        a->dir = inserir_avl(a->dir, chave);
    } else {
        return a;
    }
    atualizar(a);
    fb = altura(a->esq) - altura(a->dir);
    if (fb > 1 && chave < a->esq->chave) { /* LL: simples à direita */
        rotacoes++;
        return rot_dir(a);
    }
    if (fb < -1 && chave > a->dir->chave) { /* RR: simples à esquerda */
        rotacoes++;
        return rot_esq(a);
    }
    if (fb > 1) { /* LR: dupla */
        rotacoes += 2;
        a->esq = rot_esq(a->esq);
        return rot_dir(a);
    }
    if (fb < -1) { /* RL: dupla */
        rotacoes += 2;
        a->dir = rot_dir(a->dir);
        return rot_esq(a);
    }
    return a;
}

/* Confere ordem, altura guardada e fator de balanceamento; devolve a altura. */
static int conferir(const Arv *a, int min, int max, int avl)
{
    int he, hd;
    if (a == NULL) {
        return 0;
    }
    assert(a->chave > min && a->chave < max);
    he = conferir(a->esq, min, a->chave, avl);
    hd = conferir(a->dir, a->chave, max, avl);
    assert(a->altura == 1 + maior(he, hd));
    assert(!avl || abs(he - hd) <= 1);
    return a->altura;
}

void liberar(Arv *a)
{
    if (a != NULL) {
        liberar(a->esq);
        liberar(a->dir);
        free(a);
    }
}

static Arv *tres(int x, int y, int z)
{
    Arv *a = NULL;
    rotacoes = 0;
    a = inserir_avl(a, x);
    a = inserir_avl(a, y);
    return inserir_avl(a, z);
}

int main(void)
{
    Arv *a = NULL;
    int i;
    int casos[4][3] = {{3, 2, 1}, {1, 2, 3}, {3, 1, 2}, {1, 3, 2}};
    int giros[4] = {1, 1, 2, 2};
    assert(buscar(a, 1) == NULL); /* vazia */
    for (i = 1; i <= 7; i++) {
        a = inserir_abb(a, i); /* em ordem: vira uma lista */
    }
    assert(altura(a) == 7 && buscar(a, 5) != NULL && buscar(a, 8) == NULL);
    conferir(a, -1000, 1000, 0);
    liberar(a);
    for (i = 0; i < 4; i++) { /* LL, RR, LR, RL */
        a = tres(casos[i][0], casos[i][1], casos[i][2]);
        assert(a->chave == 2 && altura(a) == 2 && rotacoes == giros[i]);
        conferir(a, -1000, 1000, 1);
        liberar(a);
    }
    a = NULL;
    for (i = 1; i <= 1000; i++) {
        a = inserir_avl(a, (i * 7919) % 1009);
    }
    assert(altura(a) <= 15); /* AVL: altura < 1,44 log2(n + 2) */
    conferir(a, -1, 2000, 1);
    liberar(a);
    puts("OK");
    return 0;
}
