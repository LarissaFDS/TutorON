---
id: ed-cc-parenteses-pilha
titulo: Balanceamento de parênteses, colchetes e chaves com pilha: empilhar o que abre e conferir o par no que fecha
assunto: ed-07-pilhas-filas
tipo: exercicio
resolucao: sim
fonte: Exercício de balanceamento de parênteses com pilha, da pasta de exercícios da turma de CC
curso: Ciência da Computação (UFAL), material de Estrutura de Dados da turma de CC
fontes_catalogo: ufal-cc-ed-huxley
autoria: Enunciado: problema do Huxley (juiz on-line usado no IC-UFAL), parafraseado pela equipe TutorON; código e explicação da equipe TutorON, escritos com auxílio de IA e testados
licenca: Não declarada (página do Huxley salva pela turma); as páginas não estão no repositório
publicacao_transcricao: não se aplica: o bloco reescreve com texto e código próprios
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Como saber se uma expressão tem parênteses, colchetes e chaves balanceados? Use uma **pilha**. Status da resolução: validada (código da equipe TutorON, compilado com -Wall -Wextra -Werror e testado em tests_acervo/c_ed/cc_huxley.c; não é gabarito do professor).

Ideia: todo símbolo que abre vai para a pilha. Todo símbolo que fecha precisa encontrar, no topo, o símbolo que abre do mesmo tipo; se a pilha estiver vazia ou o topo for de outro tipo, a expressão não está balanceada. No fim, a pilha precisa estar vazia (senão sobrou algo aberto). Os outros caracteres são ignorados.

```c
int balanceada(const char *s)
{
    char pilha[256];
    int topo = 0;
    for (; *s; s++) {
        if (*s == '(' || *s == '[' || *s == '{') {
            if (topo == 256) return 0;
            pilha[topo++] = *s;
        } else if (*s == ')' || *s == ']' || *s == '}') {
            char abre = *s == ')' ? '(' : *s == ']' ? '[' : '{';
            if (topo == 0 || pilha[--topo] != abre) return 0;
        }
    }
    return topo == 0;
}
```

Casos que o teste cobre: `{[()()]}` e a cadeia vazia estão balanceadas; `(]`, `(()`, `())(` e `([)]` não. O último é o erro clássico de quem só conta quantos abrem e quantos fecham: a contagem bate, mas a ordem não.

Custo: O(n) de tempo e até O(n) de pilha.

**Verificação:** compilado sem avisos e testado com asserts, com e sem AddressSanitizer.
