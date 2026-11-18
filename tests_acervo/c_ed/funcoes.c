/* Ponteiros para funções e filter (versão revisada do bloco ed-02). */
#include <assert.h>
#include <stdio.h>

int filter(const int v[], int n, int (*ok)(int), int saida[])
{
    int i, k = 0;
    for (i = 0; i < n; i++) if (ok(v[i])) saida[k++] = v[i];
    return k; /* 0 se nenhum passou */
}

static int par(int x)
{
    return x % 2 == 0;
}

static int negativo(int x)
{
    return x < 0;
}

int main(void)
{
    int v[] = {1, 2, 3, 4, 6};
    int saida[5];
    int (*testes[])(int) = {par, negativo};
    assert(filter(v, 0, par, saida) == 0); /* vetor vazio */
    assert(filter(v, 5, testes[0], saida) == 3 && saida[0] == 2 && saida[2] == 6);
    assert(filter(v, 5, testes[1], saida) == 0); /* nenhum passa: devolve 0, sem lixo */
    puts("OK");
    return 0;
}
