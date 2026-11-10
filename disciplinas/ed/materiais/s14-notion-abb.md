---
id: ed-notion-abb
titulo: Anotações da turma (Notion) — árvore binária de busca: inserir, buscar e percursos
assunto: ed-10-arvores
tipo: material_estudo
resolucao: sim
fonte: Notion da turma de Estrutura de Dados (UFAL, Eng. de Computação, 3º período), página "Árvore Binária de Busca"
fontes_catalogo: ufal-ed-notion
autoria: Anotações de alunos da turma de Estrutura de Dados (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código revisado; o original não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
ABB: à esquerda de cada nó só chaves menores, à direita só maiores. Busca e inserção custam O(h), com h a altura: O(log n) se a árvore está equilibrada, O(n) se as chaves chegam em ordem (a árvore vira uma lista). Status da resolução: validada (conferida pela equipe TutorON; não é gabarito do professor).

```c
Arv *inserir_abb(Arv *a, int chave)
{
    if (a == NULL) {
        return novo(chave);
    }
    if (chave < a->chave) {
        a->esq = inserir_abb(a->esq, chave);
    } else if (chave > a->chave) {
        a->dir = inserir_abb(a->dir, chave);
    }
    atualizar(a);
    return a;
}

Arv *buscar(Arv *a, int chave)
{
    while (a != NULL && a->chave != chave) {
        a = chave < a->chave ? a->esq : a->dir;
    }
    return a;
}
```

Percurso em ordem (esquerda, raiz, direita) lista as chaves em ordem crescente. Pré-ordem: raiz, esquerda, direita. Pós-ordem: esquerda, direita, raiz; é a ordem certa para liberar a árvore.

```c
void liberar(Arv *a)
{
    if (a != NULL) {
        liberar(a->esq);
        liberar(a->dir);
        free(a);
    }
}
```

Para não depender da ordem de chegada, a árvore AVL (árvore balanceada) mantém a altura O(log n) com uma rotação ou uma rotação dupla depois de cada inserção desbalanceada. A página AVL do Notion está vazia; o material de AVL da equipe aguarda revisão.

A lógica da aula está certa. Faltava testar o `malloc` e liberar a árvore. Na aula, chaves repetidas vão para a direita; aqui são ignoradas. As duas escolhas valem, desde que a busca siga a mesma regra.
