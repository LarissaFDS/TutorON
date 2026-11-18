---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-prova1-a-q2-enade
titulo: ENADE 2005 — CPI médio de M1 (1 GHz) e M2 (500 MHz): Prova 1, versão A, Q2, e Lista Ex. 4
assunto: oac-02-desempenho
tipo: gabarito
questao: 2
fonte: Prova 1 -_2025.1_-_GABARITO.pdf | pp. 1–2 (versão A); OAC - RISC-V - Exercícios.pdf | pp. 2–3
autoria: Enunciado: Prof. Erick de Andrade Barboza (Prova 1 de OAC, UFAL, 2025.1), parafraseado pela equipe TutorON; gabarito original da prova; resolução revisada pela equipe TutorON; questão original do ENADE 2005 (INEP)
fontes_catalogo: ufal-oac-prova1-2025-1,ufal-oac-lista-cap1
verificacao: conferida_por_codigo
status_resolucao: corrigida
---
Prova 1 de OAC (2025.1), versão A, Questão 2 — ENADE 2005, com M1 a 1 GHz e **M2 a 500 MHz**. A Lista cap. 1, Exercício 4, é a mesma questão. Status da resolução: corrigida (a alternativa do gabarito está certa, mas a conta do gabarito tem erros; resolução da equipe TutorON).

Duas máquinas M1 e M2 implementam o mesmo conjunto de instruções, dos tipos A, B e C. Ciclos por instrução: A = 5 em M1 e 3 em M2; B = 2 em M1 e 1 em M2; C = 10 em M1 e 4 em M2. O programa P tem 50% de instruções A, 30% B e 20% C. Alternativas: (A) duas vezes mais rápido em M1; (B) duas vezes mais rápido em M2; (C) quatro vezes mais rápido em M1; (D) quatro vezes mais rápido em M2; (E) no mesmo tempo nas duas.

Resolução
CPI médio M1 = 0,5×5 + 0,3×2 + 0,2×10 = 2,5 + 0,6 + 2,0 = **5,1**.
CPI médio M2 = 0,5×3 + 0,3×1 + 0,2×4 = 1,5 + 0,3 + 0,8 = **2,6**.
Tempo médio por instrução = CPI / f. M1: 5,1 / 10⁹ Hz = **5,1 ns**. M2: 2,6 / (5×10⁸ Hz) = **5,2 ns**.
Razão 5,2 / 5,1 ≈ 1,02: praticamente o mesmo tempo. **Alternativa (E).**

O que o gabarito original fez e por que foi corrigido: arredondou os CPIs médios para "6 ciclos" e "3 ciclos" (um CPI médio não precisa ser inteiro) e escreveu TempoM2 = 3 / 5 × 10⁻⁸ = 6×10⁻⁸, misturando frequência (5×10⁸ Hz) com período. A alternativa (E) está certa, mas o caminho não deve ser copiado.

Verificação: para N instruções, M1 gasta 5,1N ciclos de 1 ns e M2 gasta 2,6N ciclos de 2 ns = 5,2N ns.
