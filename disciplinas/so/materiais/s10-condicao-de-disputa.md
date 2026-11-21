---
id: so-condicao-de-disputa-secao-critica
titulo: O que é uma condição de disputa — intercalação de soma += 1 entre duas threads, seção crítica e as propriedades da exclusão mútua
assunto: so-04-coordenacao-impasses
tipo: material_estudo
resolucao: sim
fonte: Slides do Prof. André Aquino (UFAL), coordenação entre tarefas; caderno do Prof. Maziero, cap. 4, questão 1; programa conferido em tests_acervo/c_so/disputa.c
fontes_catalogo: ufal-aquino-slides-so,maziero-caderno-2014,maziero-socm-2013,turma-listas-2021
autoria: Conteúdo dos slides do Prof. André Aquino (UFAL); exemplo em C e intercalação da equipe TutorON, executados com ThreadSanitizer
licenca: Slides sob CC BY-NC-SA 4.0 (Aquino); paráfrase e código da equipe
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
**Condição de disputa** (*race condition*): erro que aparece quando duas ou mais tarefas acessam um dado compartilhado de forma concorrente e o resultado depende da **ordem** em que as instruções se intercalam. O trecho de código que acessa o dado compartilhado é a **seção crítica**.

```c
long soma = 0;              /* compartilhada pelas duas threads */

void *corpo(void *arg)
{
    (void)arg;
    for (int i = 0; i < PASSOS; i++)
        soma += 1; /* ler, somar e escrever não é atômico */
    return NULL;
}
```

`soma += 1` vira três passos: carregar `soma` num registrador, somar 1, gravar. Intercalação que perde uma soma (soma = 10 no início):

| Passo | Thread A | Thread B | soma na memória |
|---|---|---|---|
| 1 | lê 10 | | 10 |
| 2 | | lê 10 | 10 |
| 3 | soma: registrador = 11 | | 10 |
| 4 | | soma: registrador = 11 | 10 |
| 5 | grava 11 | | 11 |
| 6 | | grava 11 | 11 (deveria ser 12) |

Com duas threads de 100 000 passos, o programa deveria imprimir 200 000; nas execuções da equipe imprimiu menos, e o ThreadSanitizer (`gcc -pthread -fsanitize=thread`) acusa *data race*. A mesma conta com o depósito numa conta bancária perde dinheiro.

Uma solução para a seção crítica precisa de: **exclusão mútua** (no máximo uma tarefa dentro), **espera limitada** (quem espera entra em tempo finito), **independência das outras tarefas** (só as que disputam decidem) e **independência de fatores físicos** (não depender de velocidade ou temporização).

**Verificação:** a tabela termina com 11 em vez de 12; o programa com `pthread_mutex_lock` em volta de `soma += 1` (`tests_acervo/c_so/mutex_contador.c`) imprime 200 000 e passa no ThreadSanitizer sem aviso.
