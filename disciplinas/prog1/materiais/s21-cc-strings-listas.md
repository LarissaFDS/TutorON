---
id: prog1-cc-strings-listas
titulo: Listas da turma de Ciência da Computação — strings: tirar o Enter do fgets, remover vogais ou espaços, maiúsculas e substituir caractere
assunto: prog1-09-strings
tipo: exercicio_resolvido
resolucao: sim
curso: Ciência da Computação (UFAL), Programação 1; turma e semestre não identificados
fonte: Códigos de exercícios de Programação 1 da turma de Ciência da Computação (UFAL), lista 5 (strings), pasta "c_descomplicado"
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
O `fgets` guarda o Enter (`'\n'`) quando ele cabe no vetor. Para remover um caractere de uma string, copie para a frente só o que fica, com dois índices:

```c
void tira_enter(char *s)
{
    s[strcspn(s, "\n")] = '\0';
}

void remove_char(char *s, char c)
{
    int i, j = 0;
    for (i = 0; s[i] != '\0'; i++) {
        if (s[i] != c) {
            s[j] = s[i];
            j++;
        }
    }
    s[j] = '\0';
}

void maiusculas(char *s)
{
    int i;
    for (i = 0; s[i] != '\0'; i++) {
        s[i] = (char)toupper((unsigned char)s[i]);
    }
}
```

Conferido: "a  b c" sem espaços vira "abc"; "abc 1!" em maiúsculas vira "ABC 1!". `remove_vogais` faz o mesmo que `remove_char`, mas testa se o caractere é vogal: "aeiou xyz eu" vira " xyz ". Para trocar a letra a por o, percorra a string e atribua: "banana" vira "bonono". Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: na turma, as funções de remover vogais e espaços puxavam o resto da string uma posição para trás e seguiam para o índice seguinte. Assim, o caractere que caía na posição atual não era testado: com "a  b c", sobra "a bc", e com "oaeb ia", sobra "ab a". Os dois índices evitam isso.
- Fazer maiúscula com `s[i] - 32` só serve para letras minúsculas. O espaço (32) vira `'\0'` e corta a string: "ab cd" vira "AB". Use `toupper`, de `<ctype.h>`.
- `strlwr` e `strupr` não são do C padrão. `t = strlen(s); s[t - 1] = '\0';` apaga a última letra quando não há Enter. `fgets(nome, MAX + 1, stdin)` num vetor de MAX posições pode estourar: use `sizeof nome`.
- Para comparar strings, use `strcmp(a, b) == 0`. A comparação feita à mão parava no fim da primeira string.
