---
id: prog1-aula16-recursao
titulo: Aula 16 — recursão: fatorial, soma de vetor, Fibonacci e palíndromo
assunto: prog1-12-recursao
tipo: material_estudo
resolucao: sim
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 16 (Recursão; livro, capítulo 14)
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
Uma função **recursiva** chama a si mesma com um problema menor e tem uma **condição de parada**. Fatorial: $n! = n \cdot (n-1)!$ (n fatorial é n vezes o fatorial de n − 1), com $0! = 1! = 1$. A aula desenrola fat(5) = 5·fat(4), …, fat(2) = 2·fat(1) = 2, e volta: 6, 24, 120.

```c
long fat(int n)
{
    if (n <= 1) {
        return 1; /* condição de parada: 0! = 1! = 1 */
    }
    return n * fat(n - 1);
}

int soma_rec(const int v[], int i, int tam)
{
    if (i == tam) {
        return 0; /* acabou o vetor */
    }
    return v[i] + soma_rec(v, i + 1, tam);
}

int fib(int n)
{
    if (n < 2) {
        return n; /* fib(0) = 0, fib(1) = 1 */
    }
    return fib(n - 1) + fib(n - 2);
}
```

`soma_rec(num, 0, 10)` com 1 a 10 dá 55. Sem condição de parada (ou se o problema não diminuir), as chamadas não acabam e a pilha estoura. O fatorial cresce rápido: 13! já não cabe num int de 32 bits; 20! é o maior que cabe em 64 bits. `fib` recursiva recalcula os mesmos valores muitas vezes (fib(4) chama fib(2) duas vezes) e fica lenta para n perto de 40.

Palíndromo recursivo (ideia da aula): compare o primeiro e o último caractere; se forem diferentes, não é palíndromo; se forem iguais, repita com o trecho de dentro. Pare com verdadeiro quando sobrar um caractere ou nenhum. Palíndromo, MDC recursivo e fatorial também são questões do Huxley: o tutor guia o raciocínio, não entrega o programa. Status da resolução: validada (conferida por código pela equipe TutorON).
