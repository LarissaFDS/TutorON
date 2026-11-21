---
id: so-semaforos-produtor-consumidor
titulo: Semáforos — down e up (sem_wait e sem_post), inicialização, produtor e consumidor com buffer limitado em C
assunto: so-04-coordenacao-impasses
tipo: material_estudo
resolucao: sim
fonte: Slides do Prof. André Aquino (UFAL), coordenação entre tarefas (semáforos e problemas clássicos); caderno do Prof. Maziero, cap. 4; programa conferido em tests_acervo/c_so/produtor_consumidor.c
fontes_catalogo: ufal-aquino-slides-so,maziero-caderno-2014,maziero-socm-2013
autoria: Conteúdo dos slides do Prof. André Aquino (UFAL); programa em C da equipe TutorON, executado com ThreadSanitizer
licenca: Slides sob CC BY-NC-SA 4.0 (Aquino); paráfrase e código da equipe
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
**Semáforo:** um contador inteiro com uma fila de tarefas suspensas e duas operações atômicas.
- `down(s)` (P, `sem_wait`): decrementa; se o valor ficar negativo (na versão do livro) ou se for 0 (na versão POSIX), a tarefa é **suspensa** na fila do semáforo.
- `up(s)` (V, `sem_post`): incrementa e, se houver tarefa suspensa, acorda uma.
O **valor inicial** define o significado: 1 = mutex (uma tarefa por vez); N = N recursos livres; 0 = espera por um evento. Usar um semáforo sem `sem_init` é erro: o valor é indefinido.

Produtor e consumidor com buffer de N posições: `vagas` começa em N, `itens` em 0, e um mutex protege os índices do buffer.

```c
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
```

O consumidor é simétrico: `sem_wait(&itens)`, retira com o mutex, `sem_post(&vagas)`. Em `main`: `sem_init(&vagas, 0, N)` e `sem_init(&itens, 0, 0)`.

Erro clássico: trocar a ordem e fazer `pthread_mutex_lock` **antes** de `sem_wait(&vagas)`. Com o buffer cheio, o produtor dorme segurando o mutex, e o consumidor nunca consegue retirar: **impasse**.

**Monitor:** estrutura da linguagem que junta dados e procedimentos com exclusão mútua automática; **variáveis de condição** (`wait`, `signal`) permitem esperar dentro dele. Em C, `pthread_mutex_t` + `pthread_cond_t` fazem esse papel.

**Verificação:** com N = 5 e 1000 itens, o consumidor soma 1 + 2 + … + 1000 = 500 500, igual à fórmula $n(n+1)/2$; o programa passa no ThreadSanitizer sem aviso.
