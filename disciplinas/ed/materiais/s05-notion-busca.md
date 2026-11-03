---
id: ed-notion-busca
titulo: Anotações da turma (Notion) — busca linear e busca binária, com a análise
assunto: ed-03-busca
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Busca / Análise da busca"
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
Busca linear: olha um por um; pior caso n comparações, O(n). Busca binária: só em vetor ordenado; compara com o meio e descarta metade. Status da resolução: corrigida (a anotação original tinha erros; correção da equipe TutorON, não é gabarito do professor).

```c
int busca_linear(const int v[], int n, int x)
{
    int i;
    for (i = 0; i < n; i++) {
        if (v[i] == x) {
            return i;
        }
    }
    return -1; /* só depois de olhar todos */
}

int busca_binaria(const int v[], int n, int x)
{
    int ini = 0, fim = n - 1;
    while (ini <= fim) {
        int meio = ini + (fim - ini) / 2;
        if (v[meio] == x) {
            return meio;
        }
        if (v[meio] < x) {
            ini = meio + 1;
        } else {
            fim = meio - 1;
        }
    }
    return -1;
}
```

`ini + (fim - ini) / 2` evita o estouro de `ini + fim` com índices grandes.

Análise: com t comparações a busca binária cobre no máximo $n = 2^t - 1$ elementos, logo $t = \log_2(n + 1)$ no pior caso: O(log n). O melhor caso é 1 comparação, quando o elemento procurado está no meio.

Correções da equipe
- Divergência: o código da anotação imprimia "not found" dentro do laço (as chaves estavam no lugar errado), uma vez por elemento diferente. O "não achou" só vale depois do laço.
- Dizia que o melhor caso da binária é o primeiro elemento: é o do meio.
- Calculava o tamanho com `sizeof(v)/4.0`, supondo int de 4 bytes e dividindo em double; use `sizeof v / sizeof v[0]`.
