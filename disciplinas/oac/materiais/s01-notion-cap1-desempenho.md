---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações de alunos no Notion da turma); imagens e arquivos anexos não estão no repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações; trechos de código curtos foram conferidos
revisao_humana: pendente
fontes_catalogo: ufal-oac-notion
id: oac-notion-cap1-desempenho
titulo: Anotações da turma (Notion) — cap. 1: CPI, frequência, tempo de execução e armadilha do MIPS
assunto: oac-02-desempenho
tipo: material_estudo
fonte: Notion da turma, página "Capítulo 1" (texto; as imagens com fórmulas não foram lidas)
autoria: Alunos da turma de OAC (UFAL); revisão da equipe TutorON
status_resolucao: corrigida
---
Anotações dos alunos sobre o cap. 1. Status da resolução: corrigida (um item reescrito; ver abaixo).

Conceitos: CPI = ciclos médios por instrução; frequência de clock = ciclos por segundo; tempo de execução = número de instruções × CPI / frequência (= IC × CPI × período). O compilador pode mudar tanto o número de instruções quanto o CPI.

Cuidado registrado pela turma: MIPS (milhões de instruções por segundo) engana. Um processador com mais MIPS pode ser mais lento, porque o MIPS ignora quantas instruções o programa precisa. O que conta é a combinação de IC, CPI e clock.

Correção da equipe: as anotações dizem que reduzir o tempo em 30% com CPI 20% maior exige "aumento proporcional do clock". O aumento não é de 30% nem de 20%: de T = IC × CPI / f, com T' = 0,7 T e CPI' = 1,2 CPI, sai f' = (1,2 / 0,7) f ≈ 1,714 f, cerca de 71,4% a mais (mesma conta do Ex. 1 da lista).
