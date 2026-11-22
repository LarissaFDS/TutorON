---
id: ed-ufcg-rubro-negra-insercao
titulo: Árvore rubro-negra — casos do conserto da inserção, com cores antes e depois, em C (UFCG)
assunto: ed-15-arvores-balanceadas
tipo: material_estudo
resolucao: sim
fonte: Slides de Estrutura de Dados da UFCG (DSC), Prof. Adalberto Cajueiro, 2013, aula "Árvore Rubro-Negra"; referência dos slides: Cormen et al., Algoritmos, cap. 14 (1ª ed.)
fontes_catalogo: ufcg-ed-cajueiro-slides
autoria: Conteúdo dos slides do Prof. Adalberto Cajueiro (UFCG), parafraseado e reescrito em C pela equipe TutorON com auxílio de IA
licenca: Não declarada nos slides
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código C novo; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inserção: insira como numa ABB e pinte o nó novo N de vermelho (assim a altura negra não muda). Só a regra "vermelho não tem filho vermelho" pode quebrar. Seja P o pai, G o avô e T o tio (irmão de P). Status da resolução: validada (conferida pela equipe TutorON com programa C; não é gabarito do professor).

- Caso 1, N é a raiz. Antes: N vermelho. Depois: N preto.
- Caso 2, P preto. Nada a fazer.
- Caso 3, P e T vermelhos (G preto). Antes: G preto; P, T e N vermelhos. Depois: P e T pretos, G vermelho, N vermelho. G pode ter ficado com pai vermelho: repita com N = G.
- Caso 4, T preto e zigue-zague (N filho direito de P, P filho esquerdo de G, ou o espelho). Gire em P para virar linha reta; as cores não mudam; o antigo P passa a ser o N do caso 5.
- Caso 5, T preto e linha reta. Antes: G preto, P vermelho, N vermelho. Depois de girar em G: P preto no lugar de G, com N e G vermelhos como filhos.

```c
void consertar_insercao(RB **raiz, RB *n)
{
    while (n->pai != NULL && n->pai->cor == VERMELHO) {
        RB *p = n->pai, *g = p->pai; /* p vermelho não é raiz: g existe */
        RB *tio = (p == g->esq) ? g->dir : g->esq;
        if (cor(tio) == VERMELHO) { /* tio vermelho: recolorir e subir */
            p->cor = PRETO;
            tio->cor = PRETO;
            g->cor = VERMELHO;
            n = g;
            continue;
        }
        if (p == g->esq && n == p->dir) { /* zigue-zague: vira linha reta */
            rotacao_esq(raiz, p);
            n = p;
            p = n->pai;
        } else if (p == g->dir && n == p->esq) {
            rotacao_dir(raiz, p);
            n = p;
            p = n->pai;
        }
        p->cor = PRETO; /* linha reta: pai preto, avô vermelho, gira o avô */
        g->cor = VERMELHO;
        if (n == p->esq) rotacao_dir(raiz, g);
        else rotacao_esq(raiz, g);
    }
    (*raiz)->cor = PRETO;
}
```

`cor(NULL)` devolve PRETO (folha NIL). Os casos 4 e 5 terminam o laço; só o caso 3 sobe.
