---
id: ed-notion-ordenacao-simples
titulo: Anotações da turma (Notion) — Selection sort, Bubble sort e Insertion sort em C
assunto: ed-05-ordenacao
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Ordenação"
fontes_catalogo: ufal-ed-notion
autoria: Anotações de alunos da turma de Estrutura de Dados (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código revisado; o original não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Os três da aula, conferidos contra `qsort` com milhares de vetores aleatórios (vazios, de 1 elemento, com repetidos e já ordenados). Status da resolução: validada (conferida pela equipe TutorON; não é gabarito do professor).

```c
void insertion_sort(int v[], int n)
{
    int i, j;
    for (i = 1; i < n; i++) {
        int chave = v[i];
        for (j = i - 1; j >= 0 && v[j] > chave; j--) {
            v[j + 1] = v[j];
        }
        v[j + 1] = chave;
    }
}
```

- Selection: acha o menor do resto e troca para a posição i. Sempre ~n²/2 comparações, mesmo ordenado. Não é estável.
- Bubble: troca vizinhos fora de ordem; cada passada leva o maior ao fim. Estável.
- Insertion: desloca os maiores para abrir espaço para a chave. Estável; O(n) quando o vetor já está ordenado, O(n²) no pior caso.

Melhoria sugerida pela equipe (não é erro da aula): no Bubble, parar quando uma passada inteira não faz troca:

```c
void bubble_sort(int v[], int n)
{
    int i, j, trocou = 1;
    for (i = 0; i < n - 1 && trocou; i++) {
        trocou = 0; /* passada sem troca: já está ordenado */
        for (j = 0; j < n - 1 - i; j++) {
            if (v[j] > v[j + 1]) {
                troca(&v[j], &v[j + 1]);
                trocou = 1;
            }
        }
    }
}
```
