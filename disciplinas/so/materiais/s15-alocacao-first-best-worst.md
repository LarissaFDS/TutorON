---
id: so-alocacao-first-best-worst-fit
titulo: Alocação de memória em partições — first-fit, best-fit e worst-fit com buracos de 10, 4, 7, 30, 12 e 20 MB; fragmentação externa
assunto: so-05-memoria
tipo: prova
questao: variante da AB2, questão 2; caderno, cap. 5 (lista 4 da turma, questão 5)
resolucao: sim
fonte: Resolução da turma de uma variante da AB2 do Prof. André Aquino (UFAL); Lista 4 da turma (2021) sobre o caderno do Prof. Maziero
fontes_catalogo: turma-resolucao-ab2-variante,turma-respostas-so,turma-listas-2021,maziero-caderno-2014,ufal-aquino-slides-so
autoria: Questão de prova do Prof. André Aquino (UFAL) e do caderno do Prof. Maziero; resoluções de alunos conferidas por simulação pela equipe TutorON
licenca: Não declarada (prova); caderno sob CC BY-NC-SA 3.0; paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Variante da AB2 e caderno do Prof. Maziero (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Buracos livres, nessa ordem: B1 = 10, B2 = 4, B3 = 7, B4 = 30, B5 = 12, B6 = 20 (MB). Pedidos, nessa ordem: 5, 10 e 2 MB. Qual o tamanho final de B4?

Estratégias: **first-fit** (primeiro buraco que cabe, percorrendo do início), **best-fit** (o menor que cabe), **worst-fit** (o maior). Monte a tabela pedido a pedido, **atualizando** os tamanhos:

| Pedido | First-fit | Best-fit | Worst-fit |
|---|---|---|---|
| 5 | B1: 10 → 5 | B3: 7 → 2 | B4: 30 → 25 |
| 10 | B4: 30 → 20 (B1 tem só 5) | B1: 10 → 0 | B4: 25 → 15 |
| 2 | B1: 5 → 3 | B3: 2 → 0 | B6: 20 → 18 (agora o maior é B6) |
| B4 no fim | **20 MB** | **30 MB** | **15 MB** |

Alternativa correta: "com worst-fit, B4 termina com 15 MB". As outras (first-fit 24 MB, best-fit 6 ou 7 MB, worst-fit 9 MB) não batem.

Erro comum: no worst-fit, mandar o pedido de 2 MB também para B4 (dando 13 MB). Depois do segundo pedido B4 tem 15 MB e B6 tem 20 MB: o maior passou a ser B6.

**Fragmentação externa:** sobram muitos buracos pequenos, que somados atenderiam um pedido, mas nenhum sozinho atende (o best-fit tende a gerar sobras minúsculas, como os 0 e 2 MB acima). Remédios: compactação (mover as áreas, caro) ou paginação, que elimina a fragmentação externa e deixa só a **interna** (a última página do processo pode ficar meio vazia).

**Verificação:** em cada coluna a memória livre total cai de 83 MB para 83 − 17 = 66 MB (first-fit: 3 + 4 + 7 + 20 + 12 + 20 = 66; worst-fit: 10 + 4 + 7 + 15 + 12 + 18 = 66); simulado em `tests_acervo/so_verif.py`.
