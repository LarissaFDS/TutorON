/* Recursão: fatorial, soma de vetor e Fibonacci (bloco prog1-recursao). */
#include <assert.h>
#include <stdio.h>

long fat(int n)
{
    if (n <= 1) {
        return 1; /* condição de parada: 0! = 1! = 1 */
    }
    return n * fat(n - 1);
}

int soma_rec(const int v[], int i, int tam)
{
    if (i == tam) {
        return 0; /* acabou o vetor */
    }
    return v[i] + soma_rec(v, i + 1, tam);
}

int fib(int n)
{
    if (n < 2) {
        return n; /* fib(0) = 0, fib(1) = 1 */
    }
    return fib(n - 1) + fib(n - 2);
}

int main(void)
{
    int num[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    assert(fat(0) == 1 && fat(1) == 1 && fat(5) == 120 && fat(12) == 479001600L);
    assert(soma_rec(num, 0, 10) == 55 && soma_rec(num, 0, 0) == 0 && soma_rec(num, 9, 10) == 10);
    assert(fib(0) == 0 && fib(1) == 1 && fib(4) == 3 && fib(10) == 55);
    puts("OK");
    return 0;
}
