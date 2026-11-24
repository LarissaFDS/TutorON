---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-prova2016-2-q1-cache
titulo: Prova do módulo 3 (2016.2), Q1 — cache de 8 blocos com os endereços 1, 4, 8, 5, 20, 11, 4, 43, 5, 6, 9, 14, 1, 8, 11, 22, 6 (direto, 2 vias, totalmente associativa, LRU)
assunto: oac-15-hierarquia-memoria
tipo: gabarito
questao: 1
fonte: prova2016.2-GABARITO.pdf | p. 1
autoria: Enunciado: Prof. Erick de Andrade Barboza (prova do módulo 3 de OAC, UFAL, 2016.2), parafraseado pela equipe TutorON; gabarito do professor; estados finais e classificação das faltas pela equipe TutorON, conferidos por simulador
fontes_catalogo: ufal-oac-prova-2016-2
verificacao: conferida_por_codigo
status_resolucao: validada
---
Prova do módulo 3 de OAC (2016.2), Questão 1 (enunciado parafraseado). Status da resolução: validada (o gabarito dá 15, 15 e 14 faltas; a equipe refez a simulação e confirmou).

Cache de 8 blocos de 1 palavra, vazia no início, substituição LRU. Endereços: 1, 4, 8, 5, 20, 11, 4, 43, 5, 6, 9, 14, 1, 8, 11, 22, 6 (17 acessos, 11 endereços distintos). Com bloco de 1 palavra, o endereço já é o número do bloco.

**Mapeamento direto** (índice = endereço mod 8): acertos só no segundo 5 e no segundo 8. **15 faltas** (11 compulsórias e 4 de conflito: o 4 volta depois que o 20 o tirou; o 1, depois do 9; o 11, depois do 43; o 6, depois do 22). Estado final: 0→8, 1→1, 3→11, 4→4, 5→5, 6→6.

**Associativa por conjunto de 2 vias** (4 conjuntos, conjunto = endereço mod 4): acertos no segundo 5 e no segundo 11. **15 faltas** (11 compulsórias e 4 de conflito: 4, 1, 8 e 6). Estado final: conjunto 0 com 4 e 8; conjunto 1 com 9 e 1; conjunto 2 com 22 e 6; conjunto 3 com 43 e 11.

**Totalmente associativa** (8 vias): acertos no segundo 4, no segundo 5 e no último 6. **14 faltas**: 11 compulsórias e 3 de capacidade (1, 8 e 11 voltam depois de saírem pelo LRU, porque há 11 endereços distintos para 8 blocos). Estado final: 5, 9, 14, 1, 8, 11, 22, 6.

Conclusão do gabarito: com esta ordem de acessos, passar do mapeamento direto para 2 vias não ganhou nada, e a totalmente associativa ganhou só 1 falta. Mais associatividade não garante menos faltas: o resultado depende da ordem dos acessos.
