/* Recursão das listas da turma de Ciência da Computação (bloco prog1-cc-recursao-listas). */
#include <assert.h>
#include <stdio.h>
#include <string.h>

int soma_cubos(int n)
{
    if (n <= 0) {
        return 0;
    }
    return n * n * n + soma_cubos(n - 1);
}

int potencia(int k, int n)
{
    if (n == 0) {
        return 1;
    }
    return k * potencia(k, n - 1);
}

int multiplica(int a, int b)
{
    if (b == 0) {
        return 0;
    }
    return a + multiplica(a, b - 1);
}

int fatorial_duplo(int n)
{
    if (n <= 1) {
        return 1;
    }
    return n * fatorial_duplo(n - 2);
}

static char saida[64];
static int pos;

static void anota(int n)
{
    pos += sprintf(saida + pos, "%d ", n);
}

void antes_da_chamada(int n)
{
    if (n < 0) {
        return;
    }
    anota(n);
    antes_da_chamada(n - 1);
}

void depois_da_chamada(int n)
{
    if (n < 0) {
        return;
    }
    depois_da_chamada(n - 1);
    anota(n);
}

int main(void)
{
    assert(soma_cubos(0) == 0 && soma_cubos(1) == 1 && soma_cubos(3) == 36);
    assert(potencia(2, 0) == 1 && potencia(2, 4) == 16 && potencia(5, 1) == 5);
    assert(multiplica(3, 4) == 12 && multiplica(3, 0) == 0 && multiplica(0, 5) == 0);
    assert(fatorial_duplo(0) == 1 && fatorial_duplo(1) == 1 && fatorial_duplo(5) == 15);
    assert(fatorial_duplo(8) == 384);
    antes_da_chamada(4);
    pos += sprintf(saida + pos, "| ");
    depois_da_chamada(4);
    assert(strcmp(saida, "4 3 2 1 0 | 0 1 2 3 4 ") == 0);
    puts("OK");
    return 0;
}
