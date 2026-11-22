---
id: ed-cc-profundidade-arvore-texto
titulo: Profundidade de um valor em uma árvore binária dada como texto (5(4()())(8()())): ler recursivamente sem montar a árvore
assunto: ed-10-arvores
tipo: exercicio
resolucao: sim
fonte: Huxley, problema 547 (Profundidade de um valor em uma árvore binária), salvo na pasta da turma de CC
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
Como achar a profundidade de um valor em uma árvore binária escrita como texto, em formato `(valor(esquerda)(direita))`, com `()` para a árvore vazia? Status da resolução: validada (código da equipe TutorON, compilado com -Wall -Wextra -Werror e testado em tests_acervo/c_ed/cc_huxley.c; não é gabarito do professor).

A gramática é recursiva, então a leitura também é: consuma `(`; se vier `)`, é a árvore vazia; senão leia o número, leia a subárvore esquerda, leia a direita e consuma `)`. Passe o nível como parâmetro e devolva a profundidade em que achou o valor (ou −1).

```c
int profundidade(const char **s, int alvo, int nivel)
{
    int achou = -1, v, n, e, d;
    pula_espacos(s);
    (*s)++; /* consome '(' */
    pula_espacos(s);
    if (**s == ')') {
        (*s)++; /* árvore vazia: () */
        return -1;
    }
    if (sscanf(*s, "%d%n", &v, &n) != 1) return -1;
    *s += n;
    if (v == alvo) achou = nivel;
    e = profundidade(s, alvo, nivel + 1);
    d = profundidade(s, alvo, nivel + 1);
    pula_espacos(s);
    (*s)++; /* consome ')' */
    if (achou < 0) achou = e >= 0 ? e : d;
    return achou;
}
```

Para a árvore do enunciado, `(5(4(11(7()())(2()()))()) (8(13()())(4()(1()()))))`, com a raiz na profundidade 0: 8 está em 1, 13 em 2, 7 e 1 em 3, e 99 não está (−1). O valor 4 aparece duas vezes: o código devolve a ocorrência da esquerda, aqui a mais rasa (1). Confira pelo enunciado se a raiz conta 0 ou 1 e o que imprimir quando o valor não existe.

Cuidados: o texto pode ter espaços entre as subárvores (o exemplo tem); números negativos são lidos pelo `%d`; o ponteiro é passado por endereço (`const char **`) para que cada chamada continue de onde a outra parou.

**Verificação:** compilado sem avisos e testado com asserts, inclusive árvore vazia e valor negativo.
