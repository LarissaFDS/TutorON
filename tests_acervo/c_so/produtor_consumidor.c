/* Produtor/consumidor com buffer limitado: semáforos "vagas" e "itens" e um mutex. */
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

#define N 5         /* capacidade do buffer */
#define ITENS 1000  /* itens produzidos */

int buffer[N];
int entra = 0, sai = 0;
sem_t vagas, itens;
pthread_mutex_t trava = PTHREAD_MUTEX_INITIALIZER;
long total = 0;

void *produtor(void *arg)
{
    (void)arg;
    for (int i = 1; i <= ITENS; i++) {
        sem_wait(&vagas);             /* espera uma vaga (down) */
        pthread_mutex_lock(&trava);
        buffer[entra] = i;
        entra = (entra + 1) % N;
        pthread_mutex_unlock(&trava);
        sem_post(&itens);             /* avisa que há um item (up) */
    }
    return NULL;
}

void *consumidor(void *arg)
{
    (void)arg;
    for (int i = 1; i <= ITENS; i++) {
        sem_wait(&itens);
        pthread_mutex_lock(&trava);
        total += buffer[sai];
        sai = (sai + 1) % N;
        pthread_mutex_unlock(&trava);
        sem_post(&vagas);
    }
    return NULL;
}

int main(void)
{
    pthread_t p, c;
    sem_init(&vagas, 0, N); /* o buffer começa com N vagas */
    sem_init(&itens, 0, 0); /* e nenhum item */
    pthread_create(&p, NULL, produtor, NULL);
    pthread_create(&c, NULL, consumidor, NULL);
    pthread_join(p, NULL);
    pthread_join(c, NULL);
    sem_destroy(&vagas);
    sem_destroy(&itens);
    printf("total = %ld (esperado %d)\n", total, ITENS * (ITENS + 1) / 2);
    return total == ITENS * (ITENS + 1) / 2 ? 0 : 1;
}
