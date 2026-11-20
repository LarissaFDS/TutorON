/* while, for e do-while (bloco prog1-repeticao). */
#include <assert.h>
#include <stdio.h>

int digitos_while(int n)
{
    int k = 0;
    while (n != 0) {
        n = n / 10;
        k++;
    }
    return k; /* devolve 0 para n = 0: errado */
}

int digitos(int n)
{
    int k = 0;
    do {
        n = n / 10;
        k++;
    } while (n != 0);
    return k; /* o corpo roda ao menos uma vez: 0 tem 1 dígito */
}

int soma_1_a_n(int n)
{
    int i, soma = 0;
    for (i = 1; i <= n; i++) {
        soma += i;
    }
    return soma;
}

int main(void)
{
    int contador = 0, n = 4, vezes = 0, i;
    while (contador < n) {
        vezes++;
        contador = contador + 1;
    }
    assert(vezes == 4);
    for (i = 0, vezes = 0; i < n; i++) vezes++;
    assert(vezes == 4);
    for (i = 0, vezes = 0; i <= n; i++) vezes++; /* <= roda uma vez a mais */
    assert(vezes == 5);
    assert(digitos_while(0) == 0 && digitos(0) == 1);
    assert(digitos(7) == 1 && digitos(10) == 2 && digitos(12345) == 5 && digitos(-42) == 2);
    assert(digitos_while(12345) == 5);
    assert(soma_1_a_n(0) == 0 && soma_1_a_n(1) == 1 && soma_1_a_n(100) == 5050);
    puts("OK");
    return 0;
}
