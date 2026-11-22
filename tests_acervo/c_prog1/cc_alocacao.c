/* malloc, calloc, realloc e free das listas da turma de Ciência da Computação (bloco prog1-cc-alocacao-dinamica). */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

int *cria_vetor(int n)
{
    if (n <= 0) {
        return NULL;
    }
    return malloc((size_t)n * sizeof(int)); /* NULL se faltar memória */
}

int conta_pares(const int *v, int n)
{
    int i, pares = 0;
    for (i = 0; i < n; i++) {
        if (v[i] % 2 == 0) {
            pares++;
        }
    }
    return pares;
}

int **cria_matriz(int linhas, int colunas)
{
    int i;
    int **m = malloc((size_t)linhas * sizeof(int *));
    if (m == NULL) {
        return NULL;
    }
    for (i = 0; i < linhas; i++) {
        m[i] = calloc((size_t)colunas, sizeof(int)); /* calloc zera */
        if (m[i] == NULL) {
            while (i > 0) {
                free(m[--i]);
            }
            free(m);
            return NULL;
        }
    }
    return m;
}

void libera_matriz(int **m, int linhas)
{
    int i;
    for (i = 0; i < linhas; i++) {
        free(m[i]); /* primeiro as linhas, depois o vetor de ponteiros */
    }
    free(m);
}

int main(void)
{
    int i, j, *maior;
    int *v = cria_vetor(5);
    int **m;
    assert(cria_vetor(0) == NULL);
    if (v == NULL) {
        return 1;
    }
    for (i = 0; i < 5; i++) {
        v[i] = i - 2; /* -2 -1 0 1 2 */
    }
    assert(conta_pares(v, 5) == 3);
    maior = realloc(v, 8 * sizeof(int)); /* nunca v = realloc(v, ...) */
    if (maior == NULL) {
        free(v);
        return 1;
    }
    v = maior;
    for (i = 5; i < 8; i++) {
        v[i] = i;
    }
    assert(v[0] == -2 && v[4] == 2 && conta_pares(v, 8) == 4);
    free(v);
    m = cria_matriz(2, 3);
    if (m == NULL) {
        return 1;
    }
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 3; j++) {
            assert(m[i][j] == 0);
        }
    }
    m[1][2] = 9;
    assert(m[1][2] == 9);
    libera_matriz(m, 2);
    puts("OK");
    return 0;
}
