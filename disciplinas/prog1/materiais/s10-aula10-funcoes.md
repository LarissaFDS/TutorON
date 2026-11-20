---
id: prog1-aula10-funcoes
titulo: Aula 10 — funções, decomposição, parâmetros por valor e retorno
assunto: prog1-06-funcoes
tipo: material_estudo
resolucao: sim
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 10 (Funções; livro, capítulo 9)
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
Copiar e colar código obriga a mudar todas as cópias quando algo muda. Uma **função** reaproveita o trecho, facilita a manutenção e permite **decompor** o problema. Exemplo da aula: a função `casa(h)` desenha uma casa chamando `parede(h - 2)` duas vezes, `parede(h)` duas vezes e `parede(h - 2)` mais duas; `parede(altura)` imprime o caractere altura vezes. `#define Q '#'` troca o caractere em um só lugar.

Sintaxe: `tipo_de_retorno nome(parametros) { bloco }`. `void` quando não devolve nada.

```c
int maior2(int a, int b)
{
    if (a > b) {
        return a;
    }
    return b;
}

int maior3(int a, int b, int c)
{
    return maior2(maior2(a, b), c);
}

void decrementa(int quantidade)
{
    while (quantidade) {
        --quantidade;
    }
    /* aqui quantidade vale 0, mas só a cópia local mudou */
}
```

**Passagem por valor**: o parâmetro recebe uma cópia. Depois de `decrementa(x)`, x continua com o valor de antes. Para a função mudar a variável de quem chamou, é preciso ponteiro (aula 14). Teste `maior3` com o maior em cada posição e com valores iguais. Área do círculo: `return PI * raio * raio;` (em C, `^` não é potência). Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: no slide, `imprimir_varios` é declarada `int` e não tem `return`; usar o valor devolvido seria comportamento indefinido. Como ela só imprime, o tipo certo é `void`.
- Nas chamadas `parede(h-2)` do slide falta o `;`.
