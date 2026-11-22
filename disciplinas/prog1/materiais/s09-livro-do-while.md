---
id: prog1-livro-do-while
titulo: Diferença entre while e do-while: o teste no fim garante uma execução
assunto: prog1-05-repeticao
tipo: material_estudo
resolucao: sim
curso: Engenharia de Computação e Ciência da Computação (UFAL): o livro está na bibliografia dos dois PPCs; turma não se aplica
fonte: Livro "Aprendendo a Programar Programando na Linguagem C", Jaime Evaristo (IC/UFAL), 3ª ed. digital, seção 4.4 (O comando do while)
fontes_catalogo: ufal-evaristo-livro
autoria: Livro do Prof. Jaime Evaristo (IC/UFAL), parafraseado e corrigido pela equipe TutorON com auxílio de IA
licenca: Não declarada para obras derivadas (a capa diz "Edição Digital, cópias autorizadas")
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio e código revisado; o livro não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Qual a diferença entre while e do-while? No `while` a condição é testada **antes** de cada volta, então o bloco pode rodar zero vezes. No `do { ... } while (condicao);` o teste fica **no fim**: o bloco roda pelo menos uma vez. Note o `;` depois do `while` do do-while.

Uso típico (livro, seção 4.4): validar a entrada. Com `while` é preciso ler uma vez antes do laço e outra dentro; com do-while basta uma leitura dentro: repita "digite o mês" enquanto o mês for menor que 1 ou maior que 12. Outro uso: "Deseja continuar (S/N)?" ao fim de cada execução.

Exemplo em que a diferença muda o resultado: contar os dígitos de n.

```c
int digitos_while(int n)
{
    int k = 0;
    while (n != 0) {
        n = n / 10;
        k++;
    }
    return k; /* devolve 0 para n = 0: errado */
}

int digitos(int n)
{
    int k = 0;
    do {
        n = n / 10;
        k++;
    } while (n != 0);
    return k; /* o corpo roda ao menos uma vez: 0 tem 1 dígito */
}
```

Para 12345 as duas dão 5; para 0, a versão com `while` dá 0 e a com do-while dá 1. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: o exemplo do livro usa `main()` sem tipo, que o C99 não aceita; use `int main(void)`.
- No "Deseja continuar", `scanf("%c", &Resp)` lê o Enter que sobrou da leitura anterior; use `scanf(" %c", &Resp)`. `toupper` precisa de `#include <ctype.h>`.
