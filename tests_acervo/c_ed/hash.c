/* Tabela hash: endereçamento aberto com marca de removido e encadeamento
   (versões revisadas do bloco ed-09). Testa colisões de propósito. */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define M 7

static int h(int chave)
{
    int r = chave % M;
    return r < 0 ? r + M : r; /* em C, -3 % 7 == -3 */
}

enum estado { LIVRE, OCUPADO, REMOVIDO };

typedef struct {
    enum estado estado[M];
    int chave[M], valor[M];
} Aberta;

/* Posição da chave, ou -1. Passa por REMOVIDO e só para no LIVRE. */
static int procurar(const Aberta *t, int chave)
{
    int i, pos;
    for (i = 0; i < M; i++) {
        pos = (h(chave) + i) % M;
        if (t->estado[pos] == LIVRE) {
            return -1;
        }
        if (t->estado[pos] == OCUPADO && t->chave[pos] == chave) {
            return pos;
        }
    }
    return -1;
}

int put_aberta(Aberta *t, int chave, int valor)
{
    int i, pos, livre = -1;
    pos = procurar(t, chave);
    if (pos >= 0) {
        t->valor[pos] = valor; /* chave já existe: atualiza */
        return 1;
    }
    for (i = 0; i < M && livre < 0; i++) {
        pos = (h(chave) + i) % M;
        if (t->estado[pos] != OCUPADO) {
            livre = pos; /* reaproveita REMOVIDO */
        }
    }
    if (livre < 0) {
        return 0; /* cheia: o chamador fica sabendo */
    }
    t->estado[livre] = OCUPADO;
    t->chave[livre] = chave;
    t->valor[livre] = valor;
    return 1;
}

int get_aberta(const Aberta *t, int chave, int *valor)
{
    int pos = procurar(t, chave);
    if (pos < 0) {
        return 0;
    }
    *valor = t->valor[pos];
    return 1;
}

void remove_aberta(Aberta *t, int chave)
{
    int pos = procurar(t, chave);
    if (pos >= 0) {
        t->estado[pos] = REMOVIDO; /* LIVRE quebraria a sondagem das chaves seguintes */
    }
}

typedef struct no {
    int chave, valor;
    struct no *prox;
} No;

int put_encadeada(No *tabela[], int chave, int valor)
{
    No *p;
    for (p = tabela[h(chave)]; p != NULL; p = p->prox) {
        if (p->chave == chave) {
            p->valor = valor;
            return 1;
        }
    }
    p = malloc(sizeof *p);
    if (p == NULL) {
        return 0;
    }
    p->chave = chave;
    p->valor = valor;
    p->prox = tabela[h(chave)];
    tabela[h(chave)] = p;
    return 1;
}

int get_encadeada(No *tabela[], int chave, int *valor)
{
    No *p;
    for (p = tabela[h(chave)]; p != NULL; p = p->prox) {
        if (p->chave == chave) {
            *valor = p->valor;
            return 1;
        }
    }
    return 0;
}

void liberar_encadeada(No *tabela[])
{
    int i;
    for (i = 0; i < M; i++) {
        while (tabela[i] != NULL) {
            No *prox = tabela[i]->prox;
            free(tabela[i]);
            tabela[i] = prox;
        }
    }
}

int main(void)
{
    Aberta t = {{LIVRE}, {0}, {0}};
    No *tab[M] = {NULL};
    int v, i, n = 0;
    assert(!get_aberta(&t, 3, &v)); /* vazia */
    /* 3, 10 e 17 colidem (h = 3); -4 também cai em 3 */
    assert(put_aberta(&t, 3, 30) && put_aberta(&t, 10, 100) && put_aberta(&t, 17, 170));
    assert(put_aberta(&t, -4, -40) && get_aberta(&t, -4, &v) && v == -40);
    remove_aberta(&t, 10);
    assert(get_aberta(&t, 17, &v) && v == 170); /* achado depois do removido */
    assert(put_aberta(&t, 17, 171)); /* não duplica a chave */
    for (i = 0; i < M; i++) {
        n += t.estado[i] == OCUPADO && t.chave[i] == 17;
    }
    assert(n == 1 && get_aberta(&t, 17, &v) && v == 171);
    assert(put_aberta(&t, -1, 1) && get_aberta(&t, -1, &v) && v == 1); /* -1 é chave comum */
    for (i = 100; put_aberta(&t, i, i); i++) {
    }
    assert(!put_aberta(&t, 999, 0)); /* cheia */

    assert(!get_encadeada(tab, 3, &v));
    assert(put_encadeada(tab, 3, 1) && put_encadeada(tab, 10, 2) && put_encadeada(tab, -4, 3));
    assert(put_encadeada(tab, 10, 20)); /* atualiza */
    assert(get_encadeada(tab, 10, &v) && v == 20 && get_encadeada(tab, -4, &v) && v == 3);
    liberar_encadeada(tab);
    puts("OK");
    return 0;
}
