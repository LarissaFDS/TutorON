/* Busca linear e binária (versão revisada do bloco ed-03). */
#include <assert.h>
#include <stdio.h>

int busca_linear(const int v[], int n, int x)
{
    int i;
    for (i = 0; i < n; i++) {
        if (v[i] == x) {
            return i;
        }
    }
    return -1; /* só depois de olhar todos */
}

int busca_binaria(const int v[], int n, int x)
{
    int ini = 0, fim = n - 1;
    while (ini <= fim) {
        int meio = ini + (fim - ini) / 2;
        if (v[meio] == x) {
            return meio;
        }
        if (v[meio] < x) {
            ini = meio + 1;
        } else {
            fim = meio - 1;
        }
    }
    return -1;
}

int main(void)
{
    int v[] = {2, 3, 5, 7, 11, 13, 17};
    int n = (int)(sizeof v / sizeof v[0]);
    int i;
    assert(busca_linear(v, 0, 2) == -1); /* vetor vazio */
    assert(busca_binaria(v, 0, 2) == -1);
    assert(busca_binaria(v, 1, 2) == 0); /* um elemento */
    assert(busca_binaria(v, 1, 3) == -1);
    for (i = 0; i < n; i++) {
        assert(busca_linear(v, n, v[i]) == i);
        assert(busca_binaria(v, n, v[i]) == i);
    }
    assert(busca_binaria(v, n, 1) == -1 && busca_binaria(v, n, 18) == -1);
    assert(busca_binaria(v, n, 6) == -1);
    puts("OK");
    return 0;
}
