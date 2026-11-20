---
id: prog1-aula06-07-decisao
titulo: Aulas 6 e 7 — if, else, else if, operadores relacionais e lógicos
assunto: prog1-04-decisao
tipo: material_estudo
resolucao: sim
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aulas 6 (Decisão) e 7 (E se não for verdade?; livro, capítulo 7)
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
`if (idade >= 18) { ... } else { ... }`. Relacionais: `>`, `<`, `>=`, `<=`, `==` (igual), `!=` (diferente). Em C não há tipo booleano básico: 0 é falso, qualquer outro valor é verdadeiro, e as comparações dão 1 ou 0. Lógicos: `&&` (e), `||` (ou), `!` (não). O slide usa `^` como ou exclusivo; em C ele é o XOR **bit a bit**, que só funciona como lógico quando os dois lados valem 0 ou 1. Casal com idades pares: `if (a % 2 == 0 && b % 2 == 0)`.

Diferença entre = e == no if (erro clássico): `=` é atribuição e `==` é comparação. `if (x = 5)` **atribui** 5 e é sempre verdadeiro; compare com `==`. O `-Wall` avisa.

Escolher uma entre várias faixas: use `else if`. Com `if`s separados, um salário de 950 recebe 15% (vira 1092,50) e depois cai na faixa de 1000 a 2000 e ganha mais 10% (1201,75).

```c
double novo_salario(double salario)
{
    if (salario <= 1000) {
        return salario * 1.15; /* 15% */
    } else if (salario <= 2000) {
        return salario * 1.10; /* 10% */
    } else {
        return salario * 1.05; /* 5% */
    }
}

double imposto_viagem(double gasto)
{
    if (gasto > 500) {
        return (gasto - 500) * 0.5;
    }
    return 0;
}
```

Com 820 dólares, o imposto é 160; com 500 ou menos, 0. Teste as fronteiras (1000, 2000, 500). Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: o código do salário nos slides não tem `;` depois das atribuições e imprime o salário real com `%d`. Corrigido: `;` e `%.2f` com double.
- Depois do `else if`, a condição `salario > 1000` é redundante: só se chega ali se a anterior foi falsa.
