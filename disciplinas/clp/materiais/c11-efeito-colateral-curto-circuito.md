---
id: clp-efeito-colateral-avaliacao-curto-circuito-sobrecarga-de-operadores
titulo: Efeito colateral em funções e de que formas ocorre; avaliação em curto-circuito, vantagens e efeito na legibilidade; vantagens e desvantagens da sobrecarga de operadores
assunto: clp-05-expressoes-e-controle
tipo: prova
questao: AB2 2011.2 Q2, Q6 e Q7
resolucao: sim
fonte: Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (IC-UFAL)
curso: Ciência da Computação (UFAL), Conceitos de Linguagens de Programação (CCOM027); provas de 2011.2 a 2013.1
fontes_catalogo: ufal-alcino-provas-clp
autoria: Questões do Prof. Alcino Dall'Igna Jr. (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB2 2011.2 Q2, Q6 e Q7 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Efeito colateral funcional:** a função **altera algo além de devolver o valor**: modifica um **parâmetro** passado por referência (ou ponteiro) ou uma **variável global** (ou faz entrada e saída). O problema aparece quando a função está numa expressão e altera outro operando:
```c
int a = 10;
int fun(int *x) { *x = 20; return 5; }
/* b = a + fun(&a);  dá 15 ou 25, conforme a ordem de avaliação dos operandos */
```
Em C a ordem dos operandos de `+` não é especificada. Java fixa da esquerda para a direita (15).

**Avaliação em curto-circuito:** o resultado é determinado **sem avaliar todos os operandos**: em `x && y`, se `x` é falso, `y` não é avaliado; em `x || y`, se `x` é verdadeiro, idem. Vantagens: economiza tempo e permite proteções como
```c
while (i < n && v[i] != chave) i++;   /* não lê v[n] */
```
**Efeito na legibilidade:** **piora** quando o operando não avaliado tem **efeito colateral**. Em `(a > b) || (b++ / 3)`, o `b++` só acontece às vezes, e o leitor precisa perceber isso. Ada deixa explícito com `and then` e `or else`.

**Sobrecarga de operadores definida pelo programador:**
- vantagens: **escritabilidade** e, bem usada, **legibilidade** (`a + b` para matrizes ou complexos em vez de `soma(a, b)`);
- desvantagens: mal usada, **prejudica a legibilidade** (o leitor não sabe o que `+` faz), permite dar ao operador um significado fora do usual, e complica o compilador e a detecção de erros (um erro de digitação ainda compila).

**Verificação:** `test_efeito_colateral_e_curto_circuito` compila com gcc um programa em que o `b++` do segundo operando de `||` só roda quando o primeiro é falso, e a busca protegida não lê além do vetor; e confere em Python a sobrecarga de `+` com `__add__`.
