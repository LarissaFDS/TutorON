/* Ponteiros das listas da turma de Ciência da Computação (bloco prog1-cc-ponteiros-listas). */
#include <assert.h>
#include <stdio.h>

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

int main(void)
{
    int x = 3, y = 4, v[5], i;
    int *p = &x;
    int **pp = &p;
    char letra = 'a';
    char *pc = &letra;
    void *generico = &x;
    assert(dobra(&x, &y) == 14 && x == 6 && y == 8);
    preenche(v, 5, 7);
    for (i = 0; i < 5; i++) {
        assert(v[i] == 7 && *(v + i) == v[i] && &v[i] == v + i);
    }
    assert(**pp == 6 && *pp == &x && *pc == 'a');
    assert(*(int *)generico == 6);
    puts("OK");
    return 0;
}
