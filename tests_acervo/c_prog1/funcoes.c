/* Funções, parâmetros por valor e retorno (bloco prog1-funcoes). */
#include <assert.h>
#include <math.h>
#include <stdio.h>

int maior2(int a, int b)
{
    if (a > b) {
        return a;
    }
    return b;
}

int maior3(int a, int b, int c)
{
    return maior2(maior2(a, b), c);
}

double area_circulo(double raio)
{
    const double PI = 3.14159265358979;
    return PI * raio * raio;
}

void decrementa(int quantidade)
{
    while (quantidade) {
        --quantidade;
    }
    /* aqui quantidade vale 0, mas só a cópia local mudou */
}

int main(void)
{
    int x = 3;
    decrementa(x);
    assert(x == 3); /* passagem por valor */
    assert(maior2(2, 5) == 5 && maior2(5, 2) == 5 && maior2(4, 4) == 4 && maior2(-1, -3) == -1);
    assert(maior3(1, 2, 3) == 3 && maior3(3, 2, 1) == 3 && maior3(2, 3, 1) == 3 && maior3(-5, -5, -5) == -5);
    assert(fabs(area_circulo(1) - 3.14159265358979) < 1e-12 && area_circulo(0) == 0);
    assert(fabs(area_circulo(2) - 12.56637061435916) < 1e-9);
    puts("OK");
    return 0;
}
