---
id: prog1-cc-recursao-listas
titulo: Listas da turma de Ciência da Computação — recursão: soma de cubos, potência, multiplicação, fatorial duplo e a ordem da impressão
assunto: prog1-12-recursao
tipo: exercicio_resolvido
resolucao: sim
curso: Ciência da Computação (UFAL), Programação 1; turma e semestre não identificados
fonte: Códigos de exercícios de Programação 1 da turma de Ciência da Computação (UFAL), lista 8 (recursão), pasta "c_descomplicado"
fontes_catalogo: ufal-cc-prog1-codigos-c
autoria: Códigos de aluno(s) não identificados, sem os enunciados; reescritos pela equipe TutorON com auxílio de IA
licenca: Não declarada; os códigos originais não estão no repositório
publicacao_transcricao: não se aplica: o bloco reescreve as funções com código próprio, testado
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Toda função recursiva precisa de um **caso base** que a chamada sempre alcança. Exercícios da lista 8 da turma de Ciência da Computação, reescritos:

```c
int soma_cubos(int n)
{
    if (n <= 0) {
        return 0;
    }
    return n * n * n + soma_cubos(n - 1);
}

int potencia(int k, int n)
{
    if (n == 0) {
        return 1;
    }
    return k * potencia(k, n - 1);
}

int multiplica(int a, int b)
{
    if (b == 0) {
        return 0;
    }
    return a + multiplica(a, b - 1);
}

int fatorial_duplo(int n)
{
    if (n <= 1) {
        return 1;
    }
    return n * fatorial_duplo(n - 2);
}
```

Conferido: soma_cubos(3) = 1 + 8 + 27 = 36; potencia(2, 4) = 16; multiplica(3, 4) = 12; 5!! = 5 × 3 × 1 = 15; 8!! = 384.

Ordem da impressão: se o `printf` vem **antes** da chamada recursiva, n = 4 imprime 4 3 2 1 0; se vem **depois**, imprime 0 1 2 3 4, porque cada chamada só imprime quando a de baixo termina. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: nos códigos da turma, o caso base era n == 1 (soma de cubos, potência) ou b == 1 (multiplicação). Com n = 0 a recursão nunca para. O caso base passou a ser 0.
- A função chamada "ordem crescente" imprimia em ordem decrescente: o nome deve dizer o que a função faz.
- Numa versão, o `printf` estava indentado como se fizesse parte do `if`, sem chaves; só a primeira linha depois do `if` pertence a ele. Use chaves.
- (2n)!/n! calculado com int estoura a partir de n = 7 (14! > 2³¹ − 1). Uma função usada antes de ser declarada dá "implicit declaration": declare o protótipo antes.
