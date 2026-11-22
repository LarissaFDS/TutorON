---
id: prog1-cc-ponteiros-listas
titulo: Listas da turma de Ciência da Computação — ponteiros: alterar variáveis na função, aritmética de ponteiros, %p, ponteiro para ponteiro e void *
assunto: prog1-10-ponteiros
tipo: exercicio_resolvido
resolucao: sim
curso: Ciência da Computação (UFAL), Programação 1; turma e semestre não identificados
fonte: Códigos de exercícios de Programação 1 da turma de Ciência da Computação (UFAL), lista 9 (ponteiros) e exemplos de ponteiro, pasta "c_descomplicado"
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
Para uma função mudar variáveis de quem a chamou, ela recebe os endereços: `dobra(&x, &y)`.

```c
int dobra(int *a, int *b)
{
    *a = *a * 2;
    *b = *b * 2;
    return *a + *b;
}

void preenche(int *v, int n, int valor)
{
    int i;
    for (i = 0; i < n; i++) {
        *(v + i) = valor;
    }
}
```

Com x = 3 e y = 4, `dobra` devolve 14 e deixa x = 6 e y = 8.

Aritmética de ponteiros: `v + i` é o endereço de `v[i]`, e `*(v + i)` é o mesmo que `v[i]`. Por isso `scanf("%d", v + i)` lê direto na posição i, sem `&`.

Ponteiro para ponteiro: com `int *p = &x; int **pp = &p;`, `*pp` é p e `**pp` é x.

`void *` guarda o endereço de qualquer tipo, mas, para ler o valor, é preciso converter: `*(int *)generico`. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: um código da turma usava `*x2` antes de fazer `x2 = &x1`. Ponteiro sem valor aponta para qualquer lugar: é comportamento indefinido, e o `-Wall` avisa "used uninitialized".
- Endereços eram impressos com `%d`. O formato certo é `%p`, com conversão: `printf("%p\n", (void *)&x);`.
- O exemplo de `void *` fazia `void *p = 1500;` e `p++`. Inteiro não vira ponteiro sem conversão, e aritmética com `void *` não existe no C padrão (é extensão do gcc, e o `-pedantic` avisa).
- Uma função `int` de ordenar três números não tinha `return`. Se ela não devolve nada, declare-a `void`.
