/* Árvore B de ordem M: busca, inserção com divisão na mediana (blocos ed-ufcg-arvore-b) e verificação. */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define M 3 /* ordem: no máximo M filhos e M - 1 chaves por nó */

typedef struct no_b {
    int n;            /* chaves em uso */
    int chave[M];     /* uma vaga extra para o estouro antes da divisão */
    struct no_b *filho[M + 1];
} NoB;

static NoB *novo_no(void)
{
    NoB *x = calloc(1, sizeof *x);
    return x;
}

int buscar_b(const NoB *x, int k)
{
    while (x != NULL) {
        int i = 0;
        while (i < x->n && k > x->chave[i]) i++;
        if (i < x->n && k == x->chave[i]) return 1;
        x = x->filho[i]; /* NULL numa folha */
    }
    return 0;
}

/* x estourou (M chaves): fica com a metade esquerda, *dir recebe a direita
   e a mediana é devolvida para subir ao pai. */
static int dividir(NoB *x, NoB **dir)
{
    int meio = x->n / 2, j;
    NoB *d = novo_no();
    if (d == NULL) exit(1);
    d->n = x->n - meio - 1;
    for (j = 0; j < d->n; j++) d->chave[j] = x->chave[meio + 1 + j];
    for (j = 0; j <= d->n; j++) {
        d->filho[j] = x->filho[meio + 1 + j];
        x->filho[meio + 1 + j] = NULL;
    }
    x->n = meio;
    *dir = d;
    return x->chave[meio];
}

/* Insere em x; se x estourar, devolve 1 com a mediana em *sobe e o novo irmão em *dir. */
static int inserir_rec(NoB *x, int k, int *sobe, NoB **dir)
{
    int i = 0, j;
    NoB *novo = NULL;
    while (i < x->n && k > x->chave[i]) i++;
    if (i < x->n && k == x->chave[i]) return 0;
    if (x->filho[0] != NULL) { /* interno: desce e só age se o filho estourou */
        if (!inserir_rec(x->filho[i], k, &k, &novo)) return 0;
    }
    for (j = x->n; j > i; j--) { /* abre espaço na posição i */
        x->chave[j] = x->chave[j - 1];
        x->filho[j + 1] = x->filho[j];
    }
    x->chave[i] = k;
    x->filho[i + 1] = novo;
    x->n++;
    if (x->n < M) return 0;
    *sobe = dividir(x, dir);
    return 1;
}

void inserir_b(NoB **raiz, int k)
{
    int sobe;
    NoB *dir, *r;
    if (*raiz == NULL) {
        *raiz = novo_no();
        if (*raiz == NULL) exit(1);
    }
    if (buscar_b(*raiz, k)) return;
    if (!inserir_rec(*raiz, k, &sobe, &dir)) return;
    r = novo_no(); /* a raiz se dividiu: a árvore cresce para cima */
    if (r == NULL) exit(1);
    r->n = 1;
    r->chave[0] = sobe;
    r->filho[0] = *raiz;
    r->filho[1] = dir;
    *raiz = r;
}

/* Profundidade das folhas se tudo confere; -1 se não. */
static int verificar(const NoB *x, long min, long max, int raiz)
{
    int i, p = -1, q;
    if (x->n > M - 1 || (!raiz && x->n < (M + 1) / 2 - 1) || (raiz && x->n < 1)) return -1;
    for (i = 0; i < x->n; i++) {
        if (x->chave[i] <= min || x->chave[i] >= max) return -1;
        if (i > 0 && x->chave[i - 1] >= x->chave[i]) return -1;
    }
    if (x->filho[0] == NULL) {
        for (i = 0; i <= x->n; i++)
            if (x->filho[i] != NULL) return -1;
        return 0;
    }
    for (i = 0; i <= x->n; i++) {
        if (x->filho[i] == NULL) return -1;
        q = verificar(x->filho[i], i == 0 ? min : x->chave[i - 1], i == x->n ? max : x->chave[i], 0);
        if (q < 0 || (p >= 0 && q != p)) return -1;
        p = q;
    }
    return p + 1;
}

static void liberar(NoB *x)
{
    int i;
    if (x == NULL) return;
    for (i = 0; i <= x->n; i++) liberar(x->filho[i]);
    free(x);
}

int main(void)
{
    NoB *r = NULL;
    int i;
    /* 10, 20, 30 numa árvore de ordem 3: o nó [10 20 30] divide e 20 sobe. */
    inserir_b(&r, 10);
    inserir_b(&r, 20);
    assert(r->n == 2 && r->filho[0] == NULL);
    inserir_b(&r, 30);
    assert(r->n == 1 && r->chave[0] == 20);
    assert(r->filho[0]->n == 1 && r->filho[0]->chave[0] == 10);
    assert(r->filho[1]->n == 1 && r->filho[1]->chave[0] == 30);
    inserir_b(&r, 20); /* repetida não entra */
    assert(verificar(r, -1L, 1000000L, 1) == 1);
    liberar(r);
    r = NULL;
    srand(11);
    for (i = 0; i < 2000; i++) {
        inserir_b(&r, rand() % 50000);
        assert(verificar(r, -1L, 1000000L, 1) >= 0);
    }
    for (i = 0; i < 1000; i++) inserir_b(&r, 60000 + i); /* crescente */
    assert(verificar(r, -1L, 1000000L, 1) >= 0);
    for (i = 0; i < 1000; i++) assert(buscar_b(r, 60000 + i));
    assert(!buscar_b(r, 59999 + 2000));
    liberar(r);
    puts("OK");
    return 0;
}
