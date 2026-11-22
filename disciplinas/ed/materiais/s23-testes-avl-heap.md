---
id: ed-testes-avl-heap
titulo: Como testar se a AVL está balanceada e se o heap está certo — verificador, pré-ordens esperadas e build-heap
assunto: ed-10-arvores
tipo: material_estudo
resolucao: sim
fonte: Roteiro "Dicas para Testes AVL e Heap" (exercícios de teste em Java; autoria não identificada no arquivo), reescrito em C
fontes_catalogo: dicas-testes-avl-heap
autoria: Roteiro de testes de autoria não identificada, parafraseado e reescrito em C pela equipe TutorON com auxílio de IA; pré-ordens esperadas calculadas pela equipe
licenca: Não declarada no arquivo
publicacao_transcricao: não se aplica: o bloco reescreve com texto e código próprios; o roteiro não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Para testar se a AVL está balanceada (e não só se ela parece balanceada), não confie no campo altura guardado: recalcule a altura de baixo para cima e confira, em cada nó, a ordem da ABB, a altura guardada e o fator de balanceamento (−1, 0 ou 1). Chame o verificador depois de cada inserção e de cada remoção, não só no fim: uma AVL que está balanceada só no fim pode esconder um erro de rotação no meio. Status da resolução: validada (pré-ordens conferidas pela equipe TutorON em C e numa implementação independente em Python; não é gabarito do professor).

```c
int eh_avl(const Avl *a, long min, long max)
{
    int he, hd;
    if (a == NULL) return 0;
    if (a->chave <= min || a->chave >= max) return -1;
    he = eh_avl(a->esq, min, a->chave);
    hd = eh_avl(a->dir, a->chave, max);
    if (he < 0 || hd < 0 || abs(he - hd) > 1) return -1;
    if (a->altura != 1 + (he > hd ? he : hd)) return -1;
    return a->altura;
}
```

Sequências do roteiro (altura do nó folha = 1; na remoção, nó com dois filhos troca pelo sucessor):
- Árvore vazia: pré-ordem vazia; remover 12 não quebra.
- Inserir 1, 4, 7, 10, 13, 2, 5, 8, 11, 14, 3, 15, 6, 12, 9: pré-ordem 10 4 2 1 3 7 5 6 8 9 13 11 12 14 15, altura 5. Confere com o teorema da altura: $h < 1{,}44\log_2(n+2)$.
- Remover 6: 10 4 2 1 3 7 5 8 9 13 11 12 14 15. Remover 11: 10 4 2 1 3 7 5 8 9 13 12 14 15. Remover 10 (entra 12, e a raiz rebalanceia): 7 4 2 1 3 5 12 8 9 14 13 15.
- Inserir 22, 18, 20 (zigue-zague, rotação dupla): 20 18 22.
Se a sua remoção usar o antecessor, as pré-ordens depois de remover 10 mudam; o verificador continua valendo.

Heap: compare com uma referência (em Java, PriorityQueue; em C, ordenar uma cópia) e teste a propriedade direto no vetor:

```c
int eh_heap_min(const int v[], int n)
{
    int i;
    for (i = 1; i < n; i++)
        if (v[(i - 1) / 2] > v[i]) return 0;
    return 1;
}
```

Casos: extrair de heap vazio sinaliza erro (o roteiro em Java devolve null); build-heap mínimo de 15 14 13 10 11 12 9 8 7 dá 7 8 9 10 11 12 13 14 15. Teste também que o verificador reprova uma árvore ou um vetor estragado de propósito.
