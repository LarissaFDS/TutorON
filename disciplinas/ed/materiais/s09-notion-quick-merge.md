---
id: ed-notion-quick-merge
titulo: Anotações da turma (Notion) — Quick sort e Merge sort em C, com a falha de memória do merge
assunto: ed-05-ordenacao
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Ordenação (Quick sort, Merge sort)"
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
Quick sort da aula (pivô do meio, dois índices se aproximando): conferido contra `qsort` em 200 000 vetores aleatórios com muitos repetidos, sem falha. Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor). (A correção é só no Merge sort.)

```c
void quick_sort(int v[], int size)
{
    int a = 0, b = size - 1;
    int pivo;
    if (size <= 1) {
        return;
    }
    pivo = v[size / 2];
    while (a < b) {
        while (v[a] < pivo) {
            a++;
        }
        while (v[b] > pivo) {
            b--;
        }
        if (a <= b) {
            troca(&v[a], &v[b]);
            a++;
            b--;
        }
    }
    quick_sort(v, b + 1);
    quick_sort(v + a, size - a);
}
```

Custo: O(n log n) em média, O(n²) no pior caso. Não é estável.

Merge sort: divide ao meio, ordena cada metade e intercala. O(n log n) em todos os casos, estável (o `<=` mantém a ordem dos iguais), usa memória extra O(n).

```c
static void merge(int v[], int ini, int meio, int fim, int aux[])
{
    int i = ini, j = meio, k = ini;
    while (i < meio && j < fim) {
        aux[k++] = (v[i] <= v[j]) ? v[i++] : v[j++]; /* <= mantém estável */
    }
    while (i < meio) {
        aux[k++] = v[i++];
    }
    while (j < fim) {
        aux[k++] = v[j++];
    }
    memcpy(v + ini, aux + ini, (size_t)(fim - ini) * sizeof v[0]);
}
```

Correções da equipe
- Divergência: o merge da anotação imprimia `L[n1]` e `R[n2]`, uma posição depois do fim de cada vetor auxiliar. É leitura fora dos limites (comportamento indefinido); o AddressSanitizer acusa heap-buffer-overflow. A versão acima não lê fora e aloca o auxiliar uma vez só, testando o `malloc`.
