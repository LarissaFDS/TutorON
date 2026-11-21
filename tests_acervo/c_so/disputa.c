/* Condição de disputa: duas threads somam 1 a "soma" sem exclusão mútua. */
#include <pthread.h>
#include <stdio.h>

#define PASSOS 100000

long soma = 0;

void *corpo(void *arg)
{
    (void)arg;
    for (int i = 0; i < PASSOS; i++)
        soma += 1; /* ler, somar e escrever não é atômico */
    return NULL;
}

int main(void)
{
    pthread_t a, b;
    pthread_create(&a, NULL, corpo, NULL);
    pthread_create(&b, NULL, corpo, NULL);
    pthread_join(a, NULL);
    pthread_join(b, NULL);
    printf("soma = %ld (esperado %d)\n", soma, 2 * PASSOS);
    return 0;
}
