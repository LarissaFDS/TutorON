---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações manuscritas de aluno, 2025.2); PDFs e imagens fora do repositório
publicacao_transcricao: não se aplica: o enunciado é parafraseado e só os dados foram mantidos
revisao_humana: pendente
fontes_catalogo: ufal-oac-anotacoes-otavio-2025-2
id: oac-otavio-ab2-q1-cache
titulo: Revisão AB2 (aluno, 2025.2) — Q1: misses em cache de 16 blocos com mapeamento direto, associativa por conjunto de 2 vias e totalmente associativa
assunto: oac-15-hierarquia-memoria
tipo: lista
fonte: Anotações manuscritas "Revisão AB2" (7 páginas), turma 2025.2, questão 1
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de OAC 2025.2, Prof. Erick de Andrade Barboza); revisão da equipe TutorON
status_resolucao: validada
---
Resolução de um aluno, não gabarito do professor. Status da resolução: validada (refeita por simulador de cache).

Dados: cache de 16 blocos de 1 palavra; endereços de palavra 1, 4, 8, 5, 20, 17, 19, 58, 9, 11, 4, 43, 5, 6, 9, 17. Com bloco de 1 palavra, o endereço já é o endereço do bloco (com blocos maiores, divida antes).

a) Mapeamento direto: índice = bloco mod 16. 1→1, 4→4, 8→8, 5→5, 20→4 (tira o 4), 17→1 (tira o 1), 19→3, 58→10, 9→9, 11→11, 4→4 (miss: 20 tirou o 4; falta de conflito), 43→11 (tira o 11), 5 hit, 6 miss, 9 hit, 17 hit. Total: 13 misses, 3 hits.
b) Associativa por conjunto de 2 vias: 16 / 2 = 8 conjuntos, conjunto = bloco mod 8, LRU. O 4 volta como hit, porque 4 e 20 cabem juntos no conjunto 4; 43 tira o 19 (LRU do conjunto 3). Total: 12 misses, 4 hits.
c) Totalmente associativa (16 vias): 12 misses, todos compulsórios (só há 12 blocos distintos); 4 hits.

Diferença: no mapeamento direto cada bloco tem um único lugar, e dois blocos com o mesmo índice se expulsam mesmo com a cache vazia (falta de conflito). Na associativa por conjunto, o índice escolhe o conjunto e o bloco pode ocupar qualquer via dele: menos conflitos, mas mais comparadores de tag e hit time maior.
Classificação: a primeira referência a um bloco é falta compulsória, não de conflito. Ex.: 1, 4, 8, 5, 20, 17 no mapeamento direto de 16 blocos dá 6 misses, todos compulsórios.
