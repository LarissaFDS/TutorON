/* struct, vetor de structs e passagem para função (bloco prog1-structs). */
#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

struct cliente {
    int codigo;
    char nome[50];
    int dia, mes, ano;
};

int idade_em(struct cliente c, int ano_atual)
{
    return ano_atual - c.ano; /* aproximada: ignora dia e mês */
}

float media_idades(const struct cliente clientes[], int tam, int ano_atual)
{
    int i, soma = 0;
    if (tam == 0) {
        return 0;
    }
    for (i = 0; i < tam; i++) {
        soma += idade_em(clientes[i], ano_atual);
    }
    return (float)soma / tam;
}

void muda_codigo(struct cliente *c, int novo)
{
    c->codigo = novo; /* o mesmo que (*c).codigo */
}

int main(void)
{
    struct cliente v[3];
    struct cliente um = {1, "Ana", 10, 5, 2000};
    v[0] = um;
    v[1] = um;
    v[1].ano = 2001;
    v[2] = um;
    v[2].ano = 1999;
    strcpy(v[2].nome, "Bia");
    assert(idade_em(um, 2026) == 26);
    assert(fabsf(media_idades(v, 3, 2026) - 26.0f) < 1e-6f && media_idades(v, 0, 2026) == 0);
    muda_codigo(&v[0], 7);
    assert(v[0].codigo == 7 && um.codigo == 1 && strcmp(v[2].nome, "Bia") == 0);
    puts("OK");
    return 0;
}
