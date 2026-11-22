---
id: prog1-aula13-strings
titulo: Aula 13 — strings: o '\0', scanf com %s, fgets, tamanho e como inverter uma string
assunto: prog1-09-strings
tipo: material_estudo
resolucao: sim
curso: Engenharia de Computação (UFAL), Programação 1 (ECOM002); slides do Prof. Rodrigo de Barros Paes; semestre não identificado
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 13 (Strings; livro, capítulo 11)
fontes_catalogo: ufal-prog1-slides-paes
autoria: Slides do Prof. Rodrigo de Barros Paes (IC/UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio e código revisado; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
String é um vetor de `char` terminado por `'\0'`. `char c[9] = "programa";` usa as 9 posições (8 letras + `'\0'`); `"casa"` em `char c[9]` ocupa 5 e o resto não importa. Sempre reserve uma posição para o `'\0'`.

Ler: `scanf("%s", c)` (sem `&`) para no primeiro espaço: "Tudo vale a pena" vira "Tudo". Para a linha inteira, `fgets(frase, 19, stdin)`: lê até 18 caracteres e **guarda o Enter** (`"o rato\n"` tem 7 caracteres antes do `'\0'`). Imprimir: `printf("%s\n", frase)` ou `puts(frase)`.

```c
int tamanho(const char s[])
{
    int i = 0;
    while (s[i] != '\0') {
        i++;
    }
    return i;
}

void tira_quebra(char s[])
{
    s[strcspn(s, "\n")] = '\0'; /* fgets guarda o Enter, se couber */
}
```

`strlen` (de `string.h`) faz o mesmo que `tamanho`. Contar um caractere: percorra até o `'\0'` somando quando `s[i] == c` ("abacate" tem 3 'a').

**Como inverter uma string em C**: copiando para outro vetor, o caractere i vai para a posição `tam - 1 - i`, e no fim coloque o `'\0'`. No mesmo vetor, use dois índices, um no começo e um no fim, troque os dois caracteres (com `temp`) e aproxime os índices até se cruzarem; trocar até o fim desfaria a inversão. "PROGRAMAR" vira "RAMARGORP". Inverter string e palíndromo são questões do Huxley: o tutor guia, não entrega o programa. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: o slide apresenta `gets`. Ela não tem como saber o tamanho do vetor, causa estouro e foi removida do C11; use `fgets`.
- Com `%s`, limite o tamanho: `scanf("%19s", s)` para `char s[20]`.
