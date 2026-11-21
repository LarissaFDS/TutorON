---
id: so-alocacao-arquivos-contigua-encadeada-indexada
titulo: Alocação de arquivos em disco — contígua, encadeada e indexada; leituras e escritas para inserir um bloco no início ou no fim de um arquivo de 500 blocos
assunto: so-06-arquivos
tipo: prova
questao: Prova 2, questão 6; variante da AB2, questão 5; caderno, cap. 6 (lista 6 da turma, questão 13)
resolucao: sim
fonte: Prova 2 do Prof. André Aquino (UFAL), fotos da turma com gabarito; resolução da turma de uma variante da AB2; Lista 6 da turma (2021) e resolução de aluna (2017) sobre o caderno do Prof. Maziero
fontes_catalogo: ufal-aquino-prova2-fotos,turma-resolucao-ab2-variante,turma-listas-2021,turma-resumos-2017,maziero-caderno-2014,ufal-aquino-slides-so
autoria: Prova do Prof. André Aquino (UFAL) e exercício do Prof. Maziero; resoluções de alunos parafraseadas, conferidas e corrigidas pela equipe TutorON
licenca: Não declarada (prova); caderno sob CC BY-NC-SA 3.0; paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Prova 2 e caderno do Prof. Maziero. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

| Alocação | Como é | Acesso sequencial | Acesso aleatório | Problemas |
|---|---|---|---|---|
| Contígua | blocos consecutivos; o diretório guarda o 1º bloco e o tamanho | excelente (pouco movimento da cabeça) | direto: bloco = início + posição ÷ tamanho do bloco | fragmentação externa; crescer é difícil |
| Encadeada | cada bloco aponta para o próximo (ou a FAT guarda os ponteiros) | bom | ruim: percorre a cadeia | um ponteiro corrompido perde o resto do arquivo |
| Indexada | o i-node guarda a lista de blocos | bom | direto pelo índice | espaço do índice; arquivos grandes precisam de índices indiretos |

**Prova 2, questão 6** (alocação contígua): I (guarda o número do primeiro bloco) **verdadeira**; II (leitura com desempenho excelente) **verdadeira**; III (melhora o acesso aleatório) **verdadeira**; IV (minimiza a fragmentação) **falsa**: gera fragmentação externa entre arquivos. Resposta: **somente I, II e III** (gabarito da turma conferido). **Correção:** a resolução da variante da AB2 marcou III como falsa; o acesso aleatório é um ponto forte da contígua.

**Caderno, cap. 6** (arquivo de 500 blocos; contígua só com espaço **antes** do arquivo; encadeada com o diretório em memória apontando o 1º bloco; indexada com i-node de um nível no disco):

| Alocação | Inserir no início (leituras, escritas) | Inserir no fim |
|---|---|---|
| Contígua | 0, 1 (grava no espaço livre antes) | 500, 501 (desloca o arquivo todo um bloco para trás e grava o novo) |
| Encadeada | 0, 1 (novo bloco aponta para o antigo primeiro) | 500, 2 (percorre a cadeia; grava o novo e reescreve o ponteiro do último) |
| Indexada | 1, 2 (lê o i-node; grava o bloco e o i-node) | 1, 2 |

**Correção:** a lista da turma deu 501 escritas para inserir no fim da encadeada, repetindo a linha da contígua; só o novo e o último antigo são escritos: **2 escritas**.

**Verificação:** na encadeada o fim custa 500 leituras porque o diretório só aponta o primeiro bloco; na indexada a posição não importa, porque só o i-node muda. Contas em `tests_acervo/so_verif.py`.
