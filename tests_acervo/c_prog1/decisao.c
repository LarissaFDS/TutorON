/* if, else if, operadores relacionais e lógicos (bloco prog1-decisao). */
#include <assert.h>
#include <math.h>
#include <stdio.h>

double novo_salario(double salario)
{
    if (salario <= 1000) {
        return salario * 1.15; /* 15% */
    } else if (salario <= 2000) {
        return salario * 1.10; /* 10% */
    } else {
        return salario * 1.05; /* 5% */
    }
}

double imposto_viagem(double gasto)
{
    if (gasto > 500) {
        return (gasto - 500) * 0.5;
    }
    return 0;
}

int escuro(int hora)
{
    return hora >= 18 || hora <= 5;
}

int main(void)
{
    double s = 950;
    /* o erro da primeira tentativa: ifs separados aplicam dois aumentos */
    if (s <= 1000) s = s * 1.15;
    if (s > 1000 && s <= 2000) s = s * 1.10;
    assert(fabs(s - 1201.75) < 1e-9);
    assert(fabs(novo_salario(950) - 1092.5) < 1e-9);
    assert(fabs(novo_salario(1000) - 1150) < 1e-9 && fabs(novo_salario(2000) - 2200) < 1e-9);
    assert(fabs(novo_salario(2050) - 2152.5) < 1e-9);
    assert(imposto_viagem(820) == 160 && imposto_viagem(500) == 0 && imposto_viagem(0) == 0);
    assert(escuro(18) && escuro(23) && escuro(0) && escuro(5) && !escuro(6) && !escuro(17));
    assert((20 % 2 == 0 && 18 % 2 == 0) == 1 && (21 % 2 == 0 && 22 % 2 == 0) == 0);
    assert((1 ^ 1) == 0 && (1 ^ 0) == 1 && (!5) == 0 && (!0) == 1);
    puts("OK");
    return 0;
}
