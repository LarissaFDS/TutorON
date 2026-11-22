---
id: prog1-cc-structs-listas
titulo: Listas da turma de Ciência da Computação — typedef struct, struct dentro de struct, vetor de structs e ler texto depois de número
assunto: prog1-11-structs
tipo: exercicio_resolvido
resolucao: sim
curso: Ciência da Computação (UFAL), Programação 1; turma e semestre não identificados
fonte: Códigos de exercícios de Programação 1 da turma de Ciência da Computação (UFAL), lista 6 (structs) e exemplos de struct, pasta "c_descomplicado"
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
Com `typedef struct { ... } Aluno;`, o tipo se chama só `Aluno`, sem escrever `struct`. Uma struct pode ter outra dentro dela: num `Pessoa` com um campo `Endereco ender`, o acesso vai de fora para dentro, `p.ender.numero`. Uma atribuição `copia = p;` copia todos os campos, até os vetores. Já `copia.nome = p.nome` não compila: para vetores de char, use `strcpy`.

```c
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
```

`a->nota[0]` é o mesmo que `(*a).nota[0]`. Conferido: com as notas (7, 8, 9), (5, 5, 5) e (10, 9, 8), as médias são 8, 5 e 9, e dois alunos ficam acima de 7.

Ler um número e depois um texto: `scanf("%d", &a.matricula);` deixa o Enter na entrada, e o `fgets` seguinte lê uma linha vazia. Consuma o Enter antes, com `getchar()`, ou leia a linha inteira com `fgets` e converta com `sscanf`. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: num exemplo da turma, o campo `idade` recebia o ano atual (2017), e a "idade" era calculada como ano − número da casa. Use nomes que digam o que o campo guarda.
- O `\n` estava no meio da mensagem ("tem %d\n anos").
- No vetor de alunos, o `fgets` do nome vinha logo depois do `scanf` das notas do aluno anterior, e por isso lia uma linha vazia.
