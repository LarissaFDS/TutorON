/* Strings das listas da turma de Ciência da Computação (bloco prog1-cc-strings-listas). */
#include <assert.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

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

int eh_vogal(char c)
{
    return c != '\0' && strchr("aeiouAEIOU", c) != NULL;
}

void remove_vogais(char *s)
{
    int i, j = 0;
    for (i = 0; s[i] != '\0'; i++) {
        if (!eh_vogal(s[i])) {
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

void substitui(char *s, char de, char para)
{
    int i;
    for (i = 0; s[i] != '\0'; i++) {
        if (s[i] == de) {
            s[i] = para;
        }
    }
}

int main(void)
{
    char a[] = "linha\n", b[] = "sem enter", c[] = "a  b c", d[] = "aeiou xyz eu", e[] = "abc 1!", f[] = "banana";
    tira_enter(a);
    tira_enter(b);
    assert(strcmp(a, "linha") == 0 && strcmp(b, "sem enter") == 0);
    remove_char(c, ' ');
    assert(strcmp(c, "abc") == 0);
    remove_vogais(d);
    assert(strcmp(d, " xyz ") == 0);
    maiusculas(e);
    assert(strcmp(e, "ABC 1!") == 0);
    substitui(f, 'a', 'o');
    assert(strcmp(f, "bonono") == 0);
    assert(strcmp("ab", "abc") != 0 && strcmp("abc", "abc") == 0);
    puts("OK");
    return 0;
}
