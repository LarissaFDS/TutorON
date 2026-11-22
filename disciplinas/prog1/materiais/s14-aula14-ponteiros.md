---
id: prog1-aula14-ponteiros
titulo: Aula 14 — ponteiros: endereço, &, *, troca de variáveis e NULL
assunto: prog1-10-ponteiros
tipo: material_estudo
resolucao: sim
curso: Engenharia de Computação (UFAL), Programação 1 (ECOM002); slides do Prof. Rodrigo de Barros Paes; semestre não identificado
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 14 (Ponteiros; livro, capítulo 12)
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
Um **ponteiro** guarda um endereço de memória. `&x` é o endereço de x; `int *p;` declara um ponteiro para int; `p = &x;` faz p apontar para x; `*p = 10;` muda o valor de x através de p. Regiões da memória vistas na aula: código, globais, pilha (parâmetros e variáveis locais) e heap (variáveis dinâmicas; `malloc` e `free` são aprofundados em Estrutura de Dados).

Desafio da aula: uma função que troque duas variáveis. Sem ponteiro não funciona, porque a função recebe cópias (passagem por valor). Com ponteiros, ela recebe os endereços:

```c
void troca_sem_ponteiro(int x, int y)
{
    int temp = x;
    x = y;
    y = temp; /* troca só as cópias */
    (void)x;
    (void)y;
}

void troca(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void ordena3(int *a, int *b, int *c)
{
    if (*a > *b) troca(a, b);
    if (*b > *c) troca(b, c);
    if (*a > *b) troca(a, b);
}
```

Chamada: `troca(&a, &b);` com a = 5 e b = 3 deixa a = 3 e b = 5. É o mesmo motivo do `&` no `scanf`. `ordena3` foi conferida com todas as 27 combinações de 1 a 3.

Quiz da aula: p aponta para `firstvalue`, recebe 10; depois aponta para `secondvalue`, recebe 20; o programa imprime 10 e 20.

`NULL` indica "não aponta para nada"; inicialize ponteiros com `NULL` e nunca use `*p` com p nulo ou não inicializado (o programa costuma cair com falha de segmentação). Status da resolução: validada (conferida por código pela equipe TutorON).
