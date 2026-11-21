/* O mesmo contador, agora com a seção crítica protegida por um mutex. */
#include <pthread.h>
#include <stdio.h>

#define PASSOS 100000

long soma = 0;
pthread_mutex_t trava = PTHREAD_MUTEX_INITIALIZER;

void *corpo(void *arg)
{
    (void)arg;
    for (int i = 0; i < PASSOS; i++) {
        pthread_mutex_lock(&trava);   /* entra na seção crítica */
        soma += 1;
        pthread_mutex_unlock(&trava); /* sai da seção crítica */
    }
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
    return soma == 2 * PASSOS ? 0 : 1;
}
