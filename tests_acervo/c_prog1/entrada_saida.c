/* Tipos, operadores e scanf/printf (blocos prog1-variaveis-es e prog1-erros-scanf). */
#include <assert.h>
#include <math.h>
#include <stdio.h>

float media3(float x, float y, float z)
{
    return (x + y + z) / 3; /* sem parênteses, só z seria dividido por 3 */
}

int minutos_do_dia(int horas, int minutos)
{
    return horas * 60 + minutos;
}

int le_numero_e_letra(const char *entrada, int *n, char *c)
{
    return sscanf(entrada, "%d %c", n, c); /* o espaço antes de %c pula o Enter */
}

int main(void)
{
    int n = 0, lidos;
    char c = '?';
    double d = 0;
    assert(fabsf(media3(6, 7, 8) - 7.0f) < 1e-6f);
    assert(fabsf((6 + 7 + 8.0f / 3) - 15.666667f) < 1e-4f); /* a média sem parênteses */
    assert(minutos_do_dia(10, 15) == 615 && minutos_do_dia(0, 0) == 0 && minutos_do_dia(23, 59) == 1439);
    assert(7 / 2 == 3 && 7 % 2 == 1 && -7 / 2 == -3 && -7 % 2 == -1);
    assert(fabs((double)7 / 2 - 3.5) < 1e-12 && fabs(7 / 2.0 - 3.5) < 1e-12);
    lidos = le_numero_e_letra("12\nx", &n, &c);
    assert(lidos == 2 && n == 12 && c == 'x');
    lidos = sscanf("12\nx", "%d%c", &n, &c); /* sem o espaço, %c lê o '\n' */
    assert(lidos == 2 && c == '\n');
    assert(sscanf("abc", "%d", &n) == 0); /* entrada que não é número: nada lido */
    assert(sscanf("3.5", "%lf", &d) == 1 && fabs(d - 3.5) < 1e-12);
    assert((int)'A' == 65 && 'a' - 'A' == 32);
    puts("OK");
    return 0;
}
