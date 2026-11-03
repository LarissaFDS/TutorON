---
id: ed-notion-ponteiros-lista
titulo: Anotações da turma (Notion) — ponteiros, malloc e lista encadeada em C
assunto: ed-01-ponteiros-memoria
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Ponteiros"
fontes_catalogo: ufal-ed-notion
autoria: Anotações de alunos da turma de Estrutura de Dados (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código revisado; o original não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Ponteiro guarda um endereço: `int *p = &x;` faz p apontar para x; `*p` lê ou escreve x. Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

Nó de lista: cada nó guarda o item e o ponteiro para o próximo nó (`prox`). O último nó tem `prox` igual a NULL, e a lista vazia é o próprio ponteiro `head == NULL`.

```c
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

void liberar(Node *head)
{
    while (head != NULL) {
        Node *prox = head->prox;
        free(head);
        head = prox;
    }
}
```

Para inserir no fim, percorre-se até o nó cujo ponteiro para o próximo é nulo (`p->prox == NULL`) e liga-se o novo nó ali, depois de fazer `novo->prox = NULL;`.

Correções da equipe
- Divergência: o código da anotação declarava `typedef struct ... Noe;` e usava `Node`: não compila. Aqui o nome é um só (`Node`).
- Os `#include` estavam colados numa linha e a linha `int *p = &` estava cortada.
- Faltava conferir se `malloc` devolveu NULL e a lista nunca era liberada (vazamento): `liberar` percorre e dá `free` em cada nó, guardando `prox` antes.
