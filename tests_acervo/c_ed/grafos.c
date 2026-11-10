/* BFS e DFS em lista de adjacência (versão revisada do bloco ed-12). */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define MAXV 8

typedef struct adj {
    int v;
    struct adj *prox;
} Adj;

typedef struct {
    int n;
    Adj *vizinhos[MAXV];
    int visitado[MAXV];
} Grafo;

void criar(Grafo *g, int n)
{
    int i;
    g->n = n;
    for (i = 0; i < n; i++) { /* desde 0: nenhum vértice fica sem iniciar */
        g->vizinhos[i] = NULL;
        g->visitado[i] = 0;
    }
}

int aresta(Grafo *g, int a, int b)
{
    Adj *x = malloc(sizeof *x), *y = malloc(sizeof *y);
    if (x == NULL || y == NULL) {
        free(x);
        free(y);
        return 0;
    }
    x->v = b;
    x->prox = g->vizinhos[a];
    g->vizinhos[a] = x;
    y->v = a;
    y->prox = g->vizinhos[b];
    g->vizinhos[b] = y;
    return 1;
}

/* Grava a ordem de visita em ordem[]; devolve quantos visitou. */
int bfs(Grafo *g, int s, int ordem[], int dist[])
{
    int fila[MAXV], ini = 0, fim = 0, k = 0, i;
    Adj *p;
    for (i = 0; i < g->n; i++) {
        g->visitado[i] = 0;
        dist[i] = -1;
    }
    g->visitado[s] = 1;
    dist[s] = 0;
    fila[fim++] = s;
    while (ini < fim) {
        int u = fila[ini++];
        ordem[k++] = u;
        for (p = g->vizinhos[u]; p != NULL; p = p->prox) {
            if (!g->visitado[p->v]) {
                g->visitado[p->v] = 1; /* marca ao enfileirar, não ao sair */
                dist[p->v] = dist[u] + 1;
                fila[fim++] = p->v;
            }
        }
    }
    return k;
}

static int dfs_rec(Grafo *g, int u, int ordem[], int k)
{
    Adj *p;
    g->visitado[u] = 1;
    ordem[k++] = u;
    for (p = g->vizinhos[u]; p != NULL; p = p->prox) {
        if (!g->visitado[p->v]) {
            k = dfs_rec(g, p->v, ordem, k);
        }
    }
    return k;
}

int dfs(Grafo *g, int s, int ordem[])
{
    int i;
    for (i = 0; i < g->n; i++) {
        g->visitado[i] = 0;
    }
    return dfs_rec(g, s, ordem, 0);
}

void liberar(Grafo *g)
{
    int i;
    for (i = 0; i < g->n; i++) {
        while (g->vizinhos[i] != NULL) {
            Adj *prox = g->vizinhos[i]->prox;
            free(g->vizinhos[i]);
            g->vizinhos[i] = prox;
        }
    }
}

int main(void)
{
    Grafo g;
    int ordem[MAXV], dist[MAXV];
    criar(&g, 1); /* um vértice, sem arestas */
    assert(bfs(&g, 0, ordem, dist) == 1 && dfs(&g, 0, ordem) == 1);
    criar(&g, 6); /* 0-1, 0-2, 1-3, 2-3, 3-4; o 5 fica isolado */
    assert(aresta(&g, 0, 1) && aresta(&g, 0, 2) && aresta(&g, 1, 3));
    assert(aresta(&g, 2, 3) && aresta(&g, 3, 4));
    assert(bfs(&g, 0, ordem, dist) == 5);
    assert(ordem[0] == 0 && dist[3] == 2 && dist[4] == 3 && dist[5] == -1);
    assert(dfs(&g, 0, ordem) == 5 && !g.visitado[5]);
    liberar(&g);
    puts("OK");
    return 0;
}
