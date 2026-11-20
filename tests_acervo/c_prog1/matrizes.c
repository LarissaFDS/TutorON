/* Matrizes: percorrer, somar e transpor (bloco prog1-matrizes). */
#include <assert.h>
#include <stdio.h>

#define MAX 100

void transpor(int lin, int col, int a[][MAX], int t[][MAX])
{
    int i, j;
    for (i = 0; i < lin; i++) {
        for (j = 0; j < col; j++) {
            t[j][i] = a[i][j];
        }
    }
}

void somar(int lin, int col, int a[][MAX], int b[][MAX], int c[][MAX])
{
    int i, j;
    for (i = 0; i < lin; i++) {
        for (j = 0; j < col; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
}

static int a[MAX][MAX], b[MAX][MAX], c[MAX][MAX];

int main(void)
{
    float notas[5][4] = {{0}};
    int i, j, k = 1;
    notas[0][0] = 5.5f;
    notas[4][1] = 8.0f;
    assert(notas[4][1] == 8.0f && notas[3][3] == 0.0f);
    for (i = 0; i < 2; i++)
        for (j = 0; j < 3; j++) a[i][j] = k++; /* 1 2 3 / 4 5 6 */
    transpor(2, 3, a, c);
    assert(c[0][0] == 1 && c[0][1] == 4 && c[2][0] == 3 && c[2][1] == 6 && c[1][1] == 5);
    for (i = 0; i < 2; i++)
        for (j = 0; j < 3; j++) b[i][j] = 10;
    somar(2, 3, a, b, c);
    assert(c[0][0] == 11 && c[1][2] == 16);
    puts("OK");
    return 0;
}
