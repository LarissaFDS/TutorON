---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações manuscritas de aluno, 2025.2); PDFs e imagens fora do repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações
revisao_humana: pendente
fontes_catalogo: ufal-oac-anotacoes-otavio-2025-2
id: oac-otavio-hierarquia-memoria
titulo: Anotações de aluno (2025.2) — hierarquia de memória: localidade, SRAM/DRAM/Flash/disco, mapeamento direto e políticas de escrita
assunto: oac-15-hierarquia-memoria
tipo: material_estudo
fonte: Anotações manuscritas "Hierarquia de Memória" (3 páginas), turma 2025.2
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de OAC 2025.2, Prof. Erick de Andrade Barboza); revisão da equipe TutorON
status_resolucao: corrigida
---
Anotações de um aluno sobre o cap. 5. Status da resolução: corrigida (dois itens de tecnologia de memória; ver "Correções").

Localidade temporal (o que foi usado volta a ser usado) e espacial (vizinhos são usados em seguida) justificam a hierarquia: memórias pequenas e rápidas perto do processador, grandes e lentas longe. Bloco (linha) é a unidade copiada entre níveis. Hit: o dado está no nível superior; miss: busca no inferior e paga a penalidade.
Tecnologias: SRAM (cache, rápida, cara); DRAM (memória principal, precisa de refresh); Flash/SSD (não volátil, desgaste por escrita); disco magnético (mais lento, mais barato por byte).

Mapeamento direto: índice = (endereço do bloco) mod (número de blocos da cache). Atenção: endereço do bloco = endereço em bytes ÷ bytes por bloco. Ex.: bloco 101 numa cache de 8 blocos vai para 101 mod 8 = 5; a tag guarda os bits restantes (101 div 8 = 12) e o bit de validade diz se a linha tem dado.
Escrita: write-through grava na cache e na memória (com write buffer para não parar o processador); write-back grava só na cache, marca dirty e escreve ao substituir. Write miss: write allocate traz o bloco para a cache; no-write-allocate grava só na memória.

Correções da equipe: (1) transferir dado na subida e na descida do clock é a DDR (double data rate), não toda DRAM síncrona (SDRAM). (2) QDR é usada em SRAM síncrona, não em DRAM.
