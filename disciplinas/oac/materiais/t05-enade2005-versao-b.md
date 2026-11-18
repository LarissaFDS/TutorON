---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-prova1-b-q2-enade
titulo: ENADE 2005 adaptado — CPI médio de M1 (1 GHz) e M2 (250 MHz): Prova 1, versão B, Q2
assunto: oac-02-desempenho
tipo: gabarito
questao: 2
fonte: Prova 1 -_2025.1_-_GABARITO.pdf | pp. 4–5 (versão B)
autoria: Enunciado: Prof. Erick de Andrade Barboza (Prova 1 de OAC, UFAL, 2025.1), parafraseado pela equipe TutorON; gabarito original da prova; resolução revisada pela equipe TutorON; adaptada da questão do ENADE 2005 (INEP)
fontes_catalogo: ufal-oac-prova1-2025-1
verificacao: conferida_por_codigo
status_resolucao: corrigida
---
Prova 1 de OAC (2025.1), versão B, Questão 2 — a mesma questão do ENADE 2005, mas com M1 a 1 GHz e **M2 a 250 MHz**. Não confundir com a versão A (M2 a 500 MHz, resposta E). Status da resolução: corrigida (a alternativa do gabarito está certa; a conta do gabarito arredonda os CPIs; resolução da equipe TutorON).

Duas máquinas M1 e M2 implementam o mesmo conjunto de instruções, dos tipos A, B e C. Ciclos por instrução: A = 5 em M1 e 3 em M2; B = 2 em M1 e 1 em M2; C = 10 em M1 e 4 em M2. O programa P tem 50% de instruções A, 30% B e 20% C. Alternativas: (A) duas vezes mais rápido em M1; (B) duas vezes mais rápido em M2; (C) quatro vezes mais rápido em M1; (D) quatro vezes mais rápido em M2; (E) no mesmo tempo nas duas.

Resolução
CPI médio M1 = 0,5×5 + 0,3×2 + 0,2×10 = **5,1**; CPI médio M2 = 0,5×3 + 0,3×1 + 0,2×4 = **2,6**.
Tempo médio por instrução: M1 = 5,1 / 10⁹ Hz = **5,1 ns**; M2 = 2,6 / (2,5×10⁸ Hz) = **10,4 ns**.
Razão 10,4 / 5,1 ≈ 2,04: P roda cerca de duas vezes mais rápido em M1. **Alternativa (A).**

O que o gabarito original fez: arredondou os CPIs para 6 e 3 ciclos e obteve 6 ns e 12 ns (razão 2). A alternativa coincide, mas o arredondamento do CPI médio não é correto; use 5,1 e 2,6.

Verificação: o período de M2 é 4 ns; 2,6 × 4 ns = 10,4 ns, e 10,4 / 5,1 ≈ 2.
