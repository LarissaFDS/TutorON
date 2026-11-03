/* Lista simplesmente encadeada (versão revisada dos blocos ed-01 e ed-06).
   Casos: lista vazia, um elemento, remover o primeiro e o último. */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int item;
    struct node *prox;
} Node;

Node *add_inicio(Node *head, int item)
{
    Node *novo = malloc(sizeof *novo);
    if (novo == NULL) {
        return head; /* sem memória: a lista fica como estava */
    }
    novo->item = item;
    novo->prox = head;
    return novo;
}

Node *add_fim(Node *head, int item)
{
    Node *novo = malloc(sizeof *novo);
    Node *p = head;
    if (novo == NULL) {
        return head;
    }
    novo->item = item;
    novo->prox = NULL;
    if (head == NULL) {
        return novo;
    }
    while (p->prox != NULL) {
        p = p->prox;
    }
    p->prox = novo;
    return head;
}

Node *remover(Node *head, int item)
{
    Node *anterior = NULL;
    Node *p = head;
    while (p != NULL && p->item != item) {
        anterior = p;
        p = p->prox;
    }
    if (p == NULL) {
        return head; /* não achou (inclui a lista vazia) */
    }
    if (anterior == NULL) {
        head = p->prox; /* era o primeiro */
    } else {
        anterior->prox = p->prox; /* meio ou último */
    }
    free(p);
    return head;
}

int tamanho(const Node *head)
{
    int n = 0;
    for (; head != NULL; head = head->prox) {
        n++;
    }
    return n;
}

void liberar(Node *head)
{
    while (head != NULL) {
        Node *prox = head->prox;
        free(head);
        head = prox;
    }
}

int main(void)
{
    Node *l = NULL;
    assert(tamanho(l) == 0);
    l = remover(l, 7); /* remover da lista vazia não quebra */
    assert(l == NULL);

    l = add_inicio(l, 1); /* um elemento */
    assert(tamanho(l) == 1 && l->prox == NULL);
    l = remover(l, 1);
    assert(l == NULL);

    l = add_fim(l, 1);
    l = add_fim(l, 2);
    l = add_fim(l, 3);
    l = remover(l, 1); /* primeiro */
    assert(l->item == 2 && tamanho(l) == 2);
    l = remover(l, 3); /* último */
    assert(l->item == 2 && l->prox == NULL);
    l = remover(l, 99); /* ausente */
    assert(tamanho(l) == 1);
    liberar(l);
    puts("OK");
    return 0;
}
