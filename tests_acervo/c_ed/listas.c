/* Lista genérica com void* e comparação por ponteiro de função (versão revisada do bloco ed-06). */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct gnode {
    void *item;
    struct gnode *prox;
} GNode;

int inteiros_iguais(const void *a, const void *b)
{
    return *(const int *)a == *(const int *)b;
}

GNode *add_generico(GNode *head, void *item)
{
    GNode *novo = malloc(sizeof *novo);
    if (novo == NULL) {
        return head;
    }
    novo->item = item;
    novo->prox = head;
    return novo;
}

GNode *buscar_generico(GNode *head, const void *alvo, int (*iguais)(const void *, const void *))
{
    for (; head != NULL; head = head->prox) {
        if (iguais(head->item, alvo)) {
            return head;
        }
    }
    return NULL;
}

/* Libera só os nós: os itens pertencem a quem os criou. */
void liberar_generico(GNode *head)
{
    while (head != NULL) {
        GNode *prox = head->prox;
        free(head);
        head = prox;
    }
}

int main(void)
{
    int a = 1, b = 2, c = 3, procurado = 2, ausente = 9;
    GNode *l = NULL;
    assert(buscar_generico(l, &procurado, inteiros_iguais) == NULL); /* vazia */
    l = add_generico(l, &a);
    l = add_generico(l, &b);
    l = add_generico(l, &c);
    assert(buscar_generico(l, &procurado, inteiros_iguais)->item == &b);
    assert(buscar_generico(l, &ausente, inteiros_iguais) == NULL);
    liberar_generico(l);
    puts("OK");
    return 0;
}
