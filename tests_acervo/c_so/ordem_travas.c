/* Evitar impasse quebrando a espera circular: toda thread pede as travas na mesma ordem global. */
#include <pthread.h>
#include <stdio.h>

#define PASSOS 100000

pthread_mutex_t conta_a = PTHREAD_MUTEX_INITIALIZER; /* ordem global: conta_a antes de conta_b */
pthread_mutex_t conta_b = PTHREAD_MUTEX_INITIALIZER;
long saldo_a = 1000000, saldo_b = 1000000;

void transfere(long *de, long *para, long valor)
{
    pthread_mutex_lock(&conta_a); /* sempre a mesma ordem, qualquer que seja o sentido */
    pthread_mutex_lock(&conta_b);
    *de -= valor;
    *para += valor;
    pthread_mutex_unlock(&conta_b);
    pthread_mutex_unlock(&conta_a);
}

void *a_para_b(void *arg)
{
    (void)arg;
    for (int i = 0; i < PASSOS; i++)
        transfere(&saldo_a, &saldo_b, 1);
    return NULL;
}

void *b_para_a(void *arg)
{
    (void)arg;
    for (int i = 0; i < PASSOS; i++)
        transfere(&saldo_b, &saldo_a, 1);
    return NULL;
}

int main(void)
{
    pthread_t x, y;
    pthread_create(&x, NULL, a_para_b, NULL);
    pthread_create(&y, NULL, b_para_a, NULL);
    pthread_join(x, NULL);
    pthread_join(y, NULL);
    printf("a + b = %ld (esperado 2000000)\n", saldo_a + saldo_b);
    return saldo_a + saldo_b == 2000000 ? 0 : 1;
}
