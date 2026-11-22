/* Exercícios de CC (estilo Huxley): parênteses com pilha, profundidade de um nó e BFS
   (blocos ed-cc-parenteses-pilha, ed-cc-profundidade-arvore-texto, ed-cc-bfs-distancia-predecessor). */
#include <assert.h>
#include <stdio.h>
#include <string.h>

#define MAXV 16

int balanceada(const char *s)
{
    char pilha[256];
    int topo = 0;
    for (; *s; s++) {
        if (*s == '(' || *s == '[' || *s == '{') {
            if (topo == 256) return 0;
            pilha[topo++] = *s;
        } else if (*s == ')' || *s == ']' || *s == '}') {
            char abre = *s == ')' ? '(' : *s == ']' ? '[' : '{';
            if (topo == 0 || pilha[--topo] != abre) return 0;
        }
    }
    return topo == 0;
}

static void pula_espacos(const char **s)
{
    while (**s == ' ') (*s)++;
}

int profundidade(const char **s, int alvo, int nivel)
{
    int achou = -1, v, n, e, d;
    pula_espacos(s);
    (*s)++; /* consome '(' */
    pula_espacos(s);
    if (**s == ')') {
        (*s)++; /* árvore vazia: () */
        return -1;
    }
    if (sscanf(*s, "%d%n", &v, &n) != 1) return -1;
    *s += n;
    if (v == alvo) achou = nivel;
    e = profundidade(s, alvo, nivel + 1);
    d = profundidade(s, alvo, nivel + 1);
    pula_espacos(s);
    (*s)++; /* consome ')' */
    if (achou < 0) achou = e >= 0 ? e : d;
    return achou;
}

void bfs(int n, int adj[][MAXV], int origem, int dist[], int pred[])
{
    int fila[MAXV], ini = 0, fim = 0, i, u, v;
    for (i = 0; i < n; i++) {
        dist[i] = -1;
        pred[i] = -1;
    }
    dist[origem] = 0;
    fila[fim++] = origem;
    while (ini < fim) {
        u = fila[ini++];
        for (v = 0; v < n; v++)
            if (adj[u][v] && dist[v] < 0) {
                dist[v] = dist[u] + 1;
                pred[v] = u;
                fila[fim++] = v;
            }
    }
}

static int prof(const char *arvore, int alvo)
{
    const char *s = arvore;
    return profundidade(&s, alvo, 0);
}

int main(void)
{
    const char *t = "(5(4(11(7()())(2()()))()) (8(13()())(4()(1()()))))";
    int adj[MAXV][MAXV] = {{0}}, dist[MAXV], pred[MAXV];
    int arestas[][2] = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {3, 4}, {5, 6}};
    size_t k;

    assert(balanceada("{[()()]}") && balanceada("") && balanceada("a(b)c"));
    assert(!balanceada("(]") && !balanceada("(()") && !balanceada("())(") && !balanceada("([)]"));

    assert(prof(t, 5) == 0 && prof(t, 8) == 1 && prof(t, 13) == 2);
    assert(prof(t, 7) == 3 && prof(t, 1) == 3 && prof(t, 4) == 1); /* o 4 aparece duas vezes: vale o mais raso */
    assert(prof(t, 99) == -1 && prof("()", 1) == -1 && prof("(-3()())", -3) == 0);

    for (k = 0; k < sizeof arestas / sizeof arestas[0]; k++)
        adj[arestas[k][0]][arestas[k][1]] = adj[arestas[k][1]][arestas[k][0]] = 1;
    bfs(7, adj, 0, dist, pred);
    assert(dist[0] == 0 && dist[1] == 1 && dist[2] == 1 && dist[3] == 2 && dist[4] == 3);
    assert(pred[3] == 1 && pred[4] == 3 && dist[5] == -1 && dist[6] == -1 && pred[5] == -1);

    printf("OK\n");
    return 0;
}
