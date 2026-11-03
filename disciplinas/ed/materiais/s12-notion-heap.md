---
id: ed-notion-heap
titulo: Anotações da turma (Notion) — fila de prioridade e heap máximo (vetor a partir do índice 1)
assunto: ed-08-heap-fila-prioridade
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Fila de Prioridade / Heap (Apêndice)"
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
Heap máximo em vetor com raiz em 1: pai de i é i/2, filhos 2i e 2i + 1. Inserir sobe (O(log n)); remover o máximo troca a raiz pelo último e desce com max_heapify (O(log n)). Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

```c
int enqueue(Heap *h, int item)
{
    int i;
    if (h->size >= MAX_HEAP_SIZE) {
        return 0;
    }
    i = ++h->size;
    h->data[i] = item;
    while (i > 1 && h->data[i / 2] < h->data[i]) {
        troca(&h->data[i], &h->data[i / 2]);
        i /= 2;
    }
    return 1;
}

void heapsort(int data[], int size)
{
    int i;
    for (i = size / 2; i >= 1; i--) {
        max_heapify(data, size, i);
    }
    for (i = size; i >= 2; i--) {
        troca(&data[1], &data[i]);
        max_heapify(data, i - 1, 1);
    }
}
```

A fila de prioridade da aula com lista ordenada também funciona (insere O(n), remove O(1), FIFO entre prioridades iguais), mas vaza a memória.

Correções da equipe
- Divergência: a anotação tinha `MAX_HEAP_SIZE 100`, `data[100]` e o teste `size >= MAX` antes de `data[++size]`. Com size = 99, escreve `data[100]`, uma posição fora do vetor (o AddressSanitizer acusa stack-buffer-overflow). Com índice a partir de 1, o vetor precisa de `MAX_HEAP_SIZE + 1` posições.
- `heapsort` supunha o vetor já em forma de heap; faltava construí-lo (laço de n/2 até 1).
- `max_heapify` era usada antes de ser declarada, e um parâmetro `heap` sem uso gerava aviso com `-Wextra`.
