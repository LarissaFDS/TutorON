---
id: prog1-ec2-recursao-acumulador
titulo: Recursão com acumulador em C e o return esquecido na chamada recursiva
assunto: prog1-12-recursao
tipo: material_estudo
resolucao: sim
curso: Engenharia de Computação (UFAL), 2º período; códigos de exercícios de uma turma de Programação, sem enunciado, professor nem semestre identificados
fonte: Códigos C de exercícios do material do 2º período de Engenharia de Computação; um deles usa recursão com acumulador sem return na chamada; usados só como evidência do tópico e do erro
fontes_catalogo: ufal-ec2-prog1-codigos-c
autoria: Funções escritas e testadas pela equipe TutorON com auxílio de IA; nenhum código da turma foi copiado
licenca: Não declarada (códigos de aluno); o bloco usa código próprio
publicacao_transcricao: não se aplica: o bloco tem texto e código próprios; os códigos da turma não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo com código conferido. Status da resolução: validada (código da equipe TutorON, não é gabarito do professor; compilado e testado).

Na recursão comum, a conta é feita **na volta** (`return n + soma(n - 1)`). Com **acumulador**, o resultado parcial vai como parâmetro **na ida**, e o caso base só devolve o que já foi acumulado.

```c
int soma_acum(int n, int acc)
{
    if (n == 0) {
        return acc;
    }
    return soma_acum(n - 1, acc + n);
}

int pot_acum(int base, int exp, int acc)
{
    if (exp == 0) {
        return acc;
    }
    return pot_acum(base, exp - 1, acc * base);
}
```

A primeira chamada leva o valor neutro da operação: `soma_acum(10, 0)` dá 55 e `pot_acum(2, 10, 1)` dá 1024. Começar a soma com 1 ou a potência com 0 dá resultado errado.

**Erro comum: esquecer o `return` na chamada recursiva.** Escrever só `soma_acum(n - 1, acc + n);` no fim da função faz o valor calculado lá embaixo ser descartado: a função chega ao fim sem devolver nada, o que é comportamento indefinido em C. Às vezes "funciona" por acaso (o valor sobra num registrador) e falha em outro compilador ou com otimização. O `gcc -Wall` avisa: *control reaches end of non-void function*. Trate esse aviso como erro.

Também é comum alterar o acumulador dentro da chamada (`resp = i * resp` como argumento): funciona, mas confunde; passe a expressão (`acc * base`) sem atribuir.

**Verificação:** as funções foram compiladas com `-Wall -Wextra -pedantic -Werror` e AddressSanitizer/UBSan e testadas; a versão sem `return` gera o aviso citado no `gcc -Wall`.
