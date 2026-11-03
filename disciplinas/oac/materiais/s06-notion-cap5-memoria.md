---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações de alunos no Notion da turma); imagens e arquivos anexos não estão no repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações; trechos de código curtos foram conferidos
revisao_humana: pendente
fontes_catalogo: ufal-oac-notion
id: oac-notion-cap5-memoria
titulo: Anotações da turma (Notion) — cap. 5: cache, políticas de escrita, AMAT, multinível, memória virtual e TLB
assunto: oac-15-hierarquia-memoria
tipo: material_estudo
fonte: Notion da turma, página "Capítulo 5" (resumo feito com assistente de IA a partir dos slides e da prova 2016.2)
autoria: Alunos da turma de OAC (UFAL), com assistente de IA; revisão da equipe TutorON
status_resolucao: validada
---
Resumo da turma para a prova do cap. 5. Status da resolução: validada (números conferidos).

Decompor o endereço: offset = log2(bytes do bloco); conjuntos = (tamanho da cache / bloco) / vias; índice = log2(conjuntos); tag = o resto. Exemplo: 8 KiB, bloco de 32 B, 2 vias → 256 linhas, 128 conjuntos, índice 7, offset 5, tag 32 − 12 = 20 bits.
Mapeamento direto, associativo por conjunto de n vias, totalmente associativo. Substituição: linha inválida primeiro; senão LRU (barato até poucas vias) ou aleatória.
Escrita: write-through grava cache e memória (usa write buffer); write-back só na cache, marca dirty e grava na substituição (menos tráfego). Write miss: no write-through, allocate ou write-around; no write-back, normalmente allocate.
3 Cs: compulsória, capacidade, conflito. Bloco maior reduz faltas compulsórias, mas aumenta a penalidade e pode poluir a cache.
AMAT = tempo de acerto + taxa de faltas × penalidade. CPI = CPI base + ciclos de stall (acessos × taxa × penalidade, separando I-cache e D-cache). Exemplo dos slides: sem L2, CPI ≈ 9; com L2 de 5 ns e taxa global de 0,5%, CPI ≈ 3,4 (2,6×).
Memória virtual: páginas fixas; tabela de páginas (PTE: número da página física + bits de validade, referência e dirty); sempre write-back; falta de página custa milhões de ciclos. Tamanho da tabela = 2^(bits virtuais − offset) × tamanho da PTE. TLB = cache de traduções; pode haver acerto na cache com falta na TLB.
V/F citados da prova 2016.2: snooping monitora o barramento; write-invalidate invalida as outras cópias; a maior parte do custo total não está no nível mais alto.
