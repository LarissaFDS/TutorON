/* Árvore rubro-negra: inserção com os casos de conserto (blocos ed-ufcg-rubro-negra) e verificação das invariantes. */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef enum { PRETO, VERMELHO } Cor;

typedef struct rb {
    int chave;
    Cor cor;
    struct rb *esq, *dir, *pai;
} RB;

/* NULL faz o papel da folha NIL, que é sempre preta. */
static Cor cor(const RB *n)
{
    return n == NULL ? PRETO : n->cor;
}

static void rotacao_esq(RB **raiz, RB *x)
{
    RB *y = x->dir;
    x->dir = y->esq;
    if (y->esq != NULL) y->esq->pai = x;
    y->pai = x->pai;
    if (x->pai == NULL) *raiz = y;
    else if (x == x->pai->esq) x->pai->esq = y;
    else x->pai->dir = y;
    y->esq = x;
    x->pai = y;
}

static void rotacao_dir(RB **raiz, RB *x)
{
    RB *y = x->esq;
    x->esq = y->dir;
    if (y->dir != NULL) y->dir->pai = x;
    y->pai = x->pai;
    if (x->pai == NULL) *raiz = y;
    else if (x == x->pai->dir) x->pai->dir = y;
    else x->pai->esq = y;
    y->dir = x;
    x->pai = y;
}

/* n acabou de entrar vermelho; enquanto o pai for vermelho, olhe o tio. */
void consertar_insercao(RB **raiz, RB *n)
{
    while (n->pai != NULL && n->pai->cor == VERMELHO) {
        RB *p = n->pai, *g = p->pai; /* p vermelho não é raiz: g existe */
        RB *tio = (p == g->esq) ? g->dir : g->esq;
        if (cor(tio) == VERMELHO) { /* tio vermelho: recolorir e subir */
            p->cor = PRETO;
            tio->cor = PRETO;
            g->cor = VERMELHO;
            n = g;
            continue;
        }
        if (p == g->esq && n == p->dir) { /* zigue-zague: vira linha reta */
            rotacao_esq(raiz, p);
            n = p;
            p = n->pai;
        } else if (p == g->dir && n == p->esq) {
            rotacao_dir(raiz, p);
            n = p;
            p = n->pai;
        }
        p->cor = PRETO; /* linha reta: pai preto, avô vermelho, gira o avô */
        g->cor = VERMELHO;
        if (n == p->esq) rotacao_dir(raiz, g);
        else rotacao_esq(raiz, g);
    }
    (*raiz)->cor = PRETO;
}

/* Devolve 0 se a chave já existe ou se faltou memória. */
int inserir_rb(RB **raiz, int chave)
{
    RB *pai = NULL, *a = *raiz, *n;
    while (a != NULL) {
        if (chave == a->chave) return 0;
        pai = a;
        a = chave < a->chave ? a->esq : a->dir;
    }
    n = malloc(sizeof *n);
    if (n == NULL) return 0;
    n->chave = chave;
    n->cor = VERMELHO;
    n->esq = n->dir = NULL;
    n->pai = pai;
    if (pai == NULL) *raiz = n;
    else if (chave < pai->chave) pai->esq = n;
    else pai->dir = n;
    consertar_insercao(raiz, n);
    return 1;
}

/* Altura negra se a subárvore respeita ordem, cor e altura negra; -1 se não. */
static int verificar(const RB *n, long min, long max)
{
    int he, hd;
    if (n == NULL) return 1;
    if (n->chave <= min || n->chave >= max) return -1;
    if (n->cor == VERMELHO && (cor(n->esq) == VERMELHO || cor(n->dir) == VERMELHO)) return -1;
    if ((n->esq && n->esq->pai != n) || (n->dir && n->dir->pai != n)) return -1;
    he = verificar(n->esq, min, n->chave);
    hd = verificar(n->dir, n->chave, max);
    if (he < 0 || he != hd) return -1;
    return he + (n->cor == PRETO);
}

static int altura(const RB *n)
{
    int e, d;
    if (n == NULL) return 0;
    e = altura(n->esq);
    d = altura(n->dir);
    return 1 + (e > d ? e : d);
}

static void liberar(RB *n)
{
    if (n == NULL) return;
    liberar(n->esq);
    liberar(n->dir);
    free(n);
}

int main(void)
{
    RB *r = NULL;
    int i, n = 0;
    assert(verificar(r, -1000000L, 1000000L) == 1); /* vazia */
    /* Exemplo da aula: 8, 4, 2 -> raiz 4 preta, 2 e 8 vermelhos. */
    assert(inserir_rb(&r, 8) && inserir_rb(&r, 4) && inserir_rb(&r, 2));
    assert(r->chave == 4 && r->cor == PRETO && r->esq->chave == 2 && r->dir->chave == 8);
    assert(r->esq->cor == VERMELHO && r->dir->cor == VERMELHO);
    assert(!inserir_rb(&r, 4)); /* repetida não entra */
    liberar(r);
    r = NULL;
    srand(7);
    for (i = 0; i < 3000; i++) { /* crescente: sem conserto viraria lista */
        n += inserir_rb(&r, i);
        assert(cor(r) == PRETO && verificar(r, -1L, 1000000L) > 0);
    }
    for (i = 0; i < 3000; i++) n += inserir_rb(&r, 3000 + rand() % 30000);
    assert(verificar(r, -1L, 1000000L) > 0);
    /* h <= 2 lg(n + 1): 2^(h/2) <= n + 1 */
    assert((1L << ((altura(r) + 1) / 2)) <= 2L * (n + 1));
    liberar(r);
    puts("OK");
    return 0;
}
