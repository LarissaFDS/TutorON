/* Structs das listas da turma de Ciência da Computação (bloco prog1-cc-structs-listas). */
#include <assert.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    char rua[50];
    int numero;
} Endereco;

typedef struct {
    char nome[50];
    int idade;
    Endereco ender;
} Pessoa;

typedef struct {
    int matricula;
    char nome[50];
    float nota[3];
} Aluno;

float media_aluno(const Aluno *a)
{
    return (a->nota[0] + a->nota[1] + a->nota[2]) / 3;
}

int acima_da_media(const Aluno turma[], int n, float media)
{
    int i, quantos = 0;
    for (i = 0; i < n; i++) {
        if (media_aluno(&turma[i]) > media) {
            quantos++;
        }
    }
    return quantos;
}

int main(void)
{
    Pessoa p, copia;
    Aluno turma[3] = {{1, "Ana", {7, 8, 9}}, {2, "Bia", {5, 5, 5}}, {3, "Caio", {10, 9, 8}}};
    strcpy(p.nome, "Exemplo");
    p.idade = 31;
    strcpy(p.ender.rua, "Rua 1");
    p.ender.numero = 101;
    copia = p; /* atribuição copia todos os campos, inclusive os vetores */
    copia.ender.numero = 7;
    assert(p.ender.numero == 101 && strcmp(copia.ender.rua, "Rua 1") == 0);
    assert(media_aluno(&turma[0]) == 8.0f && media_aluno(&turma[1]) == 5.0f);
    assert(acima_da_media(turma, 3, 7.0f) == 2);
    puts("OK");
    return 0;
}
