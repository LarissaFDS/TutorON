---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-prova2016-2-q2-q4-vf
titulo: Prova do módulo 3 (2016.2), Q2 a Q4 — verdadeiro ou falso sobre políticas de escrita da cache, coerência, memória virtual, TLB e RAID
assunto: oac-15-hierarquia-memoria
tipo: gabarito
questao: 2-4
fonte: prova2016.2-GABARITO.pdf | pp. 1–2
autoria: Enunciado: Prof. Erick de Andrade Barboza (prova do módulo 3 de OAC, UFAL, 2016.2), parafraseado pela equipe TutorON; gabarito e justificativas do professor, resumidos pela equipe TutorON
fontes_catalogo: ufal-oac-prova-2016-2
verificacao: nao_verificada
status_resolucao: validada
---
Prova do módulo 3 de OAC (2016.2), Questões 2 a 4: assertivas de V ou F, justificando as falsas. Status da resolução: validada (gabarito do professor; questão conceitual, sem conta para conferir). A Q5 (tipo de barramento num diagrama) ficou de fora: o diagrama não aparece no arquivo.

**Q2, cache.** (a) Write-through atualiza cache e memória juntas: **V**. (b) Write-back tem desempenho pior por acessar mais a memória: **F**, é o contrário; só escreve na memória quando o bloco modificado sai da cache. (c) Em multiprocessadores, write-update invalida as outras cópias: **F**, quem invalida é o write-invalidate; o update atualiza as cópias. (d) No snooping, cada cache monitora leituras e escritas no barramento: **V**. (e) A maior parte do custo da hierarquia vem do nível mais alto: **F**; o nível mais baixo é mais barato por GB, mas tem tantos GB que custa mais no total.

**Q3, memória virtual.** (a) O espaço virtual nunca é menor que o físico: **V**. (b) Paginação permite espaço contíguo e segmentação não: **F**; as duas permitem espaço não contíguo; a diferença é página de tamanho fixo × segmento de tamanho variável. (c) A tradução usa a tabela de páginas/segmentos, na memória principal ou num hardware próprio (MMU): **V**. (d) Dá para ter hit na cache, miss no TLB e hit na tabela de páginas (TLB desatualizado): **V**. (e) Page fault é como um cache miss: a página não está na memória principal, e o sistema operacional a traz do disco: **V**.

**Q4, RAID.** (a) RAID é comum em servidores porque dependabilidade é essencial: **V**. (b) RAID 1 exige no mínimo três discos: **F**; é espelhamento N + N, então o mínimo é dois. (c) RAID 3, 4 e 5 usam paridade: **V**. (d) Escrever no RAID 4 exige ler todos os discos: **F**; com paridade por bloco, basta ler o disco do bloco e o de paridade. (e) Striping melhora o desempenho porque vários blocos são acessados em paralelo: **V**.
