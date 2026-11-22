---
id: prog1-aula15-structs
titulo: Aula 15 — estruturas (struct): campos, vetor de structs e passagem para funções
assunto: prog1-11-structs
tipo: material_estudo
resolucao: sim
curso: Engenharia de Computação (UFAL), Programação 1 (ECOM002); slides do Prof. Rodrigo de Barros Paes; semestre não identificado
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 15 (Estruturas; livro, capítulo 13)
fontes_catalogo: ufal-prog1-slides-paes
autoria: Slides do Prof. Rodrigo de Barros Paes (IC/UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio e código revisado; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Desafio da aula: cadastrar clientes de uma locadora (código, nome, data de nascimento, sexo). Com variáveis soltas, cada função precisa de seis parâmetros e cada cliente vira seis vetores paralelos. Um `struct` cria um tipo novo, composto de tipos que já existem:

```c
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
```

Declarar: `struct cliente um_cliente;`. Acessar um campo: `um_cliente.ano`. Vetor de structs: `struct cliente a[5];` e `a[2].nome`. Não esqueça o `;` depois da `}` da definição.

Passar a struct por valor (`struct cliente c`) entrega uma cópia: alterar `c` dentro da função não muda o original. Para alterar, passe o endereço e use `->`. Copiar string para o campo: `strcpy(c.nome, "Ana")`, não `c.nome = "Ana"`. Ler o nome com espaços: `fgets(c.nome, sizeof c.nome, stdin)`.

Exercício da aula: `media_idades`; o caso de tamanho 0 evita dividir por zero. Status da resolução: validada (conferida por código pela equipe TutorON).
