---
id: prog1-cc-alocacao-dinamica
titulo: Listas da turma de Ciência da Computação — malloc, calloc, realloc e free: vetor de tamanho lido e matriz dinâmica
assunto: prog1-14-alocacao-dinamica
tipo: exercicio_resolvido
resolucao: sim
curso: Ciência da Computação (UFAL), Programação 1; turma e semestre não identificados
fonte: Códigos de exercícios de Programação 1 da turma de Ciência da Computação (UFAL), lista 10 (alocação dinâmica) e exemplos de malloc e calloc, pasta "c_descomplicado"
fontes_catalogo: ufal-cc-prog1-codigos-c
autoria: Códigos de aluno(s) não identificados, sem os enunciados; reescritos pela equipe TutorON com auxílio de IA
licenca: Não declarada; os códigos originais não estão no repositório
publicacao_transcricao: não se aplica: o bloco reescreve as funções com código próprio, testado
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Na turma de Ciência da Computação, a lista 10 de Programação 1 usa alocação dinâmica básica. O vetor tem o tamanho lido do teclado: `malloc` pede a memória, `free` devolve. Listas encadeadas e outras estruturas ficam para Estrutura de Dados.

```c
int *cria_vetor(int n)
{
    if (n <= 0) {
        return NULL;
    }
    return malloc((size_t)n * sizeof(int)); /* NULL se faltar memória */
}

int **cria_matriz(int linhas, int colunas)
{
    int i;
    int **m = malloc((size_t)linhas * sizeof(int *));
    if (m == NULL) {
        return NULL;
    }
    for (i = 0; i < linhas; i++) {
        m[i] = calloc((size_t)colunas, sizeof(int)); /* calloc zera */
        if (m[i] == NULL) {
            while (i > 0) {
                free(m[--i]);
            }
            free(m);
            return NULL;
        }
    }
    return m;
}

void libera_matriz(int **m, int linhas)
{
    int i;
    for (i = 0; i < linhas; i++) {
        free(m[i]); /* primeiro as linhas, depois o vetor de ponteiros */
    }
    free(m);
}
```

Regras: confira se o resultado é `NULL`; dê um `free` para cada `malloc`; `malloc` não zera a memória (`calloc` zera); para aumentar, use `novo = realloc(v, ...)` e só então `v = novo`. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: um exemplo da turma imprimia o conteúdo de um vetor vindo do `malloc` sem ter escrito nele (valores indeterminados) e não liberava a memória.
- O exercício de contar pares não tinha `free`. O de múltiplos de x calculava a contagem e não a imprimia; com x = 0, `v[i] % x` é divisão por zero (comportamento indefinido).
- `v = realloc(v, ...)` perde o vetor antigo se o `realloc` falhar.
