/* Strings: '\0', fgets e contagem (bloco prog1-strings). */
#include <assert.h>
#include <stdio.h>
#include <string.h>

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

int conta_char(const char s[], char c)
{
    int i, k = 0;
    for (i = 0; s[i] != '\0'; i++) {
        if (s[i] == c) {
            k++;
        }
    }
    return k;
}

int main(void)
{
    char c[9] = "casa";
    char frase[19];
    char palavra[20] = "Tudo";
    FILE *f = tmpfile();
    assert(sizeof c == 9 && tamanho(c) == 4 && strlen(c) == 4 && c[4] == '\0');
    assert(sizeof "programa" == 9); /* 8 letras + '\0' */
    assert(tamanho("") == 0 && conta_char("abacate", 'a') == 3 && conta_char("", 'a') == 0);
    if (f != NULL) {
        fputs("o rato\nTudo vale a pena\n", f);
        rewind(f);
        assert(fgets(frase, sizeof frase, f) != NULL);
        assert(strcmp(frase, "o rato\n") == 0 && tamanho(frase) == 7);
        tira_quebra(frase);
        assert(strcmp(frase, "o rato") == 0 && tamanho(frase) == 6);
        assert(fscanf(f, "%19s", palavra) == 1 && strcmp(palavra, "Tudo") == 0); /* %s para no espaço */
        fclose(f);
    }
    tira_quebra(palavra); /* sem '\n': não muda nada */
    assert(strcmp(palavra, "Tudo") == 0);
    puts("OK");
    return 0;
}
