/* Ponteiros: &, *, troca e NULL (bloco prog1-ponteiros). */
#include <assert.h>
#include <stddef.h>
#include <stdio.h>

void troca_sem_ponteiro(int x, int y)
{
    int temp = x;
    x = y;
    y = temp; /* troca só as cópias */
    (void)x;
    (void)y;
}

void troca(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void ordena3(int *a, int *b, int *c)
{
    if (*a > *b) troca(a, b);
    if (*b > *c) troca(b, c);
    if (*a > *b) troca(a, b);
}

int main(void)
{
    int a = 5, b = 3, x, y, z;
    int primeiro, segundo;
    int *p = NULL;
    assert(p == NULL);
    troca_sem_ponteiro(a, b);
    assert(a == 5 && b == 3);
    troca(&a, &b);
    assert(a == 3 && b == 5);
    p = &primeiro; /* o quiz da aula */
    *p = 10;
    p = &segundo;
    *p = 20;
    assert(primeiro == 10 && segundo == 20 && p == &segundo);
    for (x = 1; x <= 3; x++)
        for (y = 1; y <= 3; y++)
            for (z = 1; z <= 3; z++) {
                int i = x, j = y, k = z;
                ordena3(&i, &j, &k);
                assert(i <= j && j <= k && i + j + k == x + y + z);
            }
    puts("OK");
    return 0;
}
