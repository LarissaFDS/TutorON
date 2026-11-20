---
id: prog1-aula09-repeticao
titulo: Aula 9 — repetição com while e for, contador, break e laços aninhados
assunto: prog1-05-repeticao
tipo: material_estudo
resolucao: sim
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 9 (Repetição; livro, capítulo 8)
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
`while (expressao) { bloco }` repete enquanto a expressão for verdadeira; ela é testada **antes** de cada volta. Para imprimir n vezes uma frase, use um contador: inicialize (`contador = 0`), teste (`contador < n`) e incremente (`contador = contador + 1`) dentro do laço. Esquecer o incremento dá laço infinito.

O `for` junta as três partes: `for (i = 0; i < n; i++)`. Cada parte é opcional: `for ( ; n >= 0; --n)` conta de n até 0, e `for ( ; ; )` só para com `break`.

```c
int soma_1_a_n(int n)
{
    int i, soma = 0;
    for (i = 1; i <= n; i++) {
        soma += i;
    }
    return soma;
}
```

Com n = 0 o laço não roda e a soma é 0; com n = 100 dá 5050. Erro de uma volta a mais: `for (i = 0; i <= n; i++)` roda n + 1 vezes.

Primo (exercício do livro e Huxley 260): procure um divisor entre 2 e a metade de n (ou até a raiz); se achar, não é primo. Lembre que 0 e 1 não são primos. O tutor não entrega o programa do Huxley.

Figuras com laços aninhados: o laço de fora conta as linhas e o de dentro imprime os caracteres de cada linha. Para o triângulo de altura n, a linha i tem i asteriscos; para o triângulo centralizado de largura 2n − 1, a linha i tem n − i espaços e 2i − 1 asteriscos. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: nos exemplos de `for` sem incremento, falta `;` em `--n` e as aspas são curvas (“%d”), que não compilam; use aspas retas.
