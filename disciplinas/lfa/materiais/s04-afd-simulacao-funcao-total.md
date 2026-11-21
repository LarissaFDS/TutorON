---
id: lfa-afd-subcadeia-aa-bb-simulacao
titulo: AFD para cadeias com aa ou bb como subcadeia, algoritmo de simulação do AFD (aceita/rejeita), função de transição total e estado morto (sumidouro)
assunto: lfa-02-automatos-finitos
tipo: material_estudo
resolucao: nao
fonte: Apostila 02 (Profa. Simone Prado, UNESP), exemplo 02; atividade prática de Teoria da Computação 2015.1 (Prof. Thyago, UFAL), algoritmo do AFD
fontes_catalogo: unesp-prado-apostilas-tc,ufal-thyago-atividade-2015-1
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
**Exemplo 02 da apostila:** $L = \{w \in \{a,b\}^* \mid w$ tem $aa$ ou $bb$ como subcadeia$\}$, com $M = (\{q_0, q_1, q_2, q_f\}, \{a,b\}, \delta, q_0, \{q_f\})$. $q_1$ = "o último símbolo foi a", $q_2$ = "o último foi b", $q_f$ = "já apareceu aa ou bb".

| $\delta$ | a | b |
|---|---|---|
| → $q_0$ | $q_1$ | $q_2$ |
| $q_1$ | $q_f$ | $q_2$ |
| $q_2$ | $q_1$ | $q_f$ |
| $q_f$ (final) | $q_f$ | $q_f$ |

**Simulação** (algoritmo da atividade prática, em palavras): estado atual ← $q_0$; para cada símbolo da entrada, se existe $\delta$(estado atual, símbolo), vá para ele, senão **rejeite**; no fim, aceite se o estado atual é final. O algoritmo sempre para, porque lê cada símbolo uma vez.

```python
def aceita(delta, q0, finais, w):
    q = q0
    for s in w:
        if (q, s) not in delta:
            return False  # transição indefinida: rejeita
        q = delta[q, s]
    return q in finais
```

**Função total:** no AFD da definição formal, $\delta$ é total. Se o desenho omite transições, complete com um **estado morto** $d$ não final, com $d \xrightarrow{a,b} d$, e mande para $d$ cada transição que faltava. O autômato completado aceita a mesma linguagem; isso é pré-requisito da minimização e da construção do complemento (trocar finais e não finais só funciona com $\delta$ total).

A atividade prática pede o programa em Java; o código acima é Python e serve para conferir a ideia. Escrever o programa é trabalho do aluno.

**Verificação:** a tabela foi simulada para todas as cadeias até comprimento 10 e comparada com o teste direto "aa ou bb em $w$": aceitas aa, abb, babaa; rejeitadas $\varepsilon$, abab, ba.
