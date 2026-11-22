---
id: prog1-aula04-variaveis-es
titulo: Aula 4 — variáveis, tipos, scanf, printf, atribuição e a média de 3 números
assunto: prog1-03-variaveis-tipos-es
tipo: material_estudo
resolucao: sim
curso: Engenharia de Computação (UFAL), Programação 1 (ECOM002); slides do Prof. Rodrigo de Barros Paes; semestre não identificado
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 4 (Elementos básicos; livro, capítulo 5)
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
A memória é uma grande tabela de endereços. Uma **variável** reserva espaço: o tipo diz quanto e o nome (identificador) dá acesso. Identificadores: letras, dígitos e `_`, sem espaço nem acento, sem começar por dígito (`num1`, `x12`, `minha_variavel`). Uma variável não inicializada tem lixo de memória.

| Tipo | Uso | scanf / printf |
|---|---|---|
| `int` | inteiro | `%d` |
| `long int` | inteiro maior | `%ld` |
| `char` | caractere | `%c` |
| `float` | real | `%f` / `%f` |
| `double` | real mais preciso | `%lf` / `%f` |

`scanf("%f", &x);` lê um float e guarda no endereço de x: o `&` é obrigatório. Vários de uma vez: `scanf("%d%f%lf", &a, &b, &c);`. `printf("A soma de %d e %d é %d\n", a, b, a + b);` troca cada `%d` por um valor, na ordem. Atribuição: `variavel = expressao;`. Operadores: `+ - * /` e `%` (resto).

```c
float media3(float x, float y, float z)
{
    return (x + y + z) / 3; /* sem parênteses, só z seria dividido por 3 */
}
```

Com 6, 7 e 8 a média é 7; sem os parênteses, `x + y + z / 3` dá 6 + 7 + 2,67 ≈ 15,67, porque `/` é feito antes de `+`. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: a tabela do slide dá `int` com 2 bytes e −32767 a +32767. Isso é só o mínimo do padrão; no gcc atual `int` tem 4 bytes (até 2147483647). A faixa de float "2^-37 a 2^+37" está errada: é cerca de 10⁻³⁸ a 10³⁸, com uns 7 dígitos de precisão; double vai a cerca de 10³⁰⁸, com uns 15 dígitos.
- O slide diz que identificadores começam com letra; `_` também pode, mas nomes que começam com `_` são reservados em vários casos, então evite.
- No `printf`, `%f` serve para float e double; no `scanf`, double exige `%lf`.
