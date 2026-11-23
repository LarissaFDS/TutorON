/* Ordenação de vetor (trocas e bolha) e recursão com acumulador (blocos prog1-ec2-*). */
#include <assert.h>
#include <stdio.h>

void ordena_trocas(int v[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                int aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }
}

void bolha(int v[], int n)
{
    int trocou = 1;
    for (int fim = n - 1; fim > 0 && trocou; fim--) {
        trocou = 0;
        for (int j = 0; j < fim; j++) {
            if (v[j] > v[j + 1]) {
                int aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
                trocou = 1;
            }
        }
    }
}

int soma_acum(int n, int acc)
{
    if (n == 0) {
        return acc;
    }
    return soma_acum(n - 1, acc + n);
}

int pot_acum(int base, int exp, int acc)
{
    if (exp == 0) {
        return acc;
    }
    return pot_acum(base, exp - 1, acc * base);
}

/* cópias com contador de comparações, só para conferir as contas do bloco */
static int comparacoes;

static void ordena_trocas_conta(int v[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            comparacoes++;
            if (v[i] > v[j]) {
                int aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }
}

static void bolha_conta(int v[], int n)
{
    int trocou = 1;
    for (int fim = n - 1; fim > 0 && trocou; fim--) {
        trocou = 0;
        for (int j = 0; j < fim; j++) {
            comparacoes++;
            if (v[j] > v[j + 1]) {
                int aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
                trocou = 1;
            }
        }
    }
}

static int ordenado(const int v[], int n)
{
    for (int i = 0; i + 1 < n; i++) {
        if (v[i] > v[i + 1]) {
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    /* todas as 4^5 = 1024 sequências de 5 valores entre 0 e 3 ficam ordenadas pelos dois métodos */
    for (int code = 0; code < 1024; code++) {
        int a[5], b[5], c = code;
        for (int k = 0; k < 5; k++) {
            a[k] = b[k] = c % 4;
            c /= 4;
        }
        ordena_trocas(a, 5);
        bolha(b, 5);
        assert(ordenado(a, 5) && ordenado(b, 5));
        for (int k = 0; k < 5; k++) {
            assert(a[k] == b[k]);
        }
    }
    int x[5] = {5, 1, 4, 2, 8};
    bolha(x, 5);
    assert(x[0] == 1 && x[1] == 2 && x[2] == 4 && x[3] == 5 && x[4] == 8);
    int y[1] = {7};
    bolha(y, 1);
    ordena_trocas(y, 1);
    assert(y[0] == 7);

    /* vetor já ordenado: a bolha para depois de 1 passada (n - 1 comparações); trocas faz sempre n(n-1)/2 */
    int s1[6] = {1, 2, 3, 4, 5, 6}, s2[6] = {1, 2, 3, 4, 5, 6};
    comparacoes = 0;
    bolha_conta(s1, 6);
    assert(comparacoes == 5);
    comparacoes = 0;
    ordena_trocas_conta(s2, 6);
    assert(comparacoes == 15);
    int r1[6] = {6, 5, 4, 3, 2, 1};
    comparacoes = 0;
    bolha_conta(r1, 6);
    assert(comparacoes == 15);

    assert(soma_acum(10, 0) == 55 && soma_acum(0, 0) == 0);
    assert(pot_acum(2, 10, 1) == 1024 && pot_acum(3, 0, 1) == 1);
    printf("OK\n");
    return 0;
}
