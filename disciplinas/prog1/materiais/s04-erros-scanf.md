---
id: prog1-erros-scanf
titulo: Por que o scanf não lê? & esquecido, formato errado, Enter que sobra e fflush(stdin)
assunto: prog1-03-variaveis-tipos-es
tipo: material_estudo
resolucao: sim
fonte: Slides de Programação 1 (UFAL), Prof. Rodrigo de Barros Paes, Aula 4 (scanf); livro de Jaime Evaristo, seções 2.7 e 5.6 (fflush)
fontes_catalogo: ufal-prog1-slides-paes,ufal-evaristo-livro
autoria: Slides do Prof. Rodrigo de Barros Paes e livro do Prof. Jaime Evaristo (IC/UFAL), parafraseados e corrigidos pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor; o livro diz "cópias autorizadas", sem licença para obras derivadas)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio e código revisado; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Meu scanf não lê o número: as causas mais comuns, nesta ordem.

1. **Faltou o `&`**: `scanf("%d", n)` passa o valor (lixo) em vez do endereço; o programa pode travar ou não guardar nada. Certo: `scanf("%d", &n)`. Para string (`char s[50]`) não vai `&`: o nome do vetor já é o endereço.
2. **Formato não bate com o tipo**: double com `%f` no scanf lê errado; use `%lf`. int com `%f` também.
3. **O Enter que sobrou**: depois de `scanf("%d", &n)`, o `'\n'` digitado fica na entrada. Um `scanf("%c", &c)` seguinte lê esse `'\n'` e "pula" a leitura. Solução: um espaço antes, `" %c"`, que descarta espaços e quebras de linha.
4. **Entrada que não é do tipo**: digitar "abc" para `%d` não lê nada, e o valor fica no buraco. O `scanf` devolve quantos itens leu; teste `if (scanf("%d", &n) != 1)`.
5. **Separador**: com `"%d,%d"` o usuário tem que digitar a vírgula; para números separados por espaço use `"%d %d"` ou `"%d%d"`.

```c
int le_numero_e_letra(const char *entrada, int *n, char *c)
{
    return sscanf(entrada, "%d %c", n, c); /* o espaço antes de %c pula o Enter */
}
```

Com a entrada "12", Enter, "x", essa função lê 12 e 'x'; com `"%d%c"`, o `%c` recebe o `'\n'`. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: o livro recomenda `fflush(stdin)` antes de ler caracteres. No padrão C, `fflush` em entrada é comportamento indefinido; funciona em alguns compiladores do Windows e não no Linux. Use `" %c"` ou leia até o fim da linha com um laço de `getchar()`.
- `=` em `if (x = 5)` e `==` são outro erro clássico, explicado no bloco de decisão.
