/* Vetores e vetores como parâmetro (bloco prog1-vetores). */
#include <assert.h>
#include <math.h>
#include <stdio.h>

float media(const float n[], int tam)
{
    int i;
    float soma = 0;
    for (i = 0; i < tam; i++) {
        soma += n[i];
    }
    return soma / tam;
}

float variancia(const float n[], int tam)
{
    int i;
    float var = 0;
    float m = media(n, tam);
    for (i = 0; i < tam; i++) {
        var += (n[i] - m) * (n[i] - m);
    }
    return var / tam;
}

int indice_do_maior(const int v[], int tam)
{
    int i, im = 0;
    for (i = 1; i < tam; i++) {
        if (v[i] > v[im]) {
            im = i; /* > e não >=: fica o primeiro maior */
        }
    }
    return im;
}

int main(void)
{
    float notas[] = {8, 6, 7, 8, 7, 6, 6, 10};
    int tam = (int)(sizeof notas / sizeof notas[0]);
    int v[] = {3, 9, 2, 9, 1};
    int zeros[100] = {0};
    int parcial[5] = {5, 12};
    assert(tam == 8);
    assert(fabsf(media(notas, tam) - 7.25f) < 1e-6f);
    assert(fabsf(variancia(notas, tam) - 1.6875f) < 1e-6f);
    assert(fabs(sqrt(variancia(notas, tam)) - 1.299038) < 1e-6);
    assert(indice_do_maior(v, 5) == 1 && indice_do_maior(v, 1) == 0);
    assert(zeros[0] == 0 && zeros[99] == 0);
    assert(parcial[0] == 5 && parcial[1] == 12 && parcial[2] == 0 && parcial[4] == 0);
    puts("OK");
    return 0;
}
