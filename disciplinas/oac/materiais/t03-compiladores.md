---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-compiladores
titulo: Impacto do compilador no desempenho — CPI médio, razão de frequências e speedup (Lista Ex. 3 e Prova 1 Q3)
assunto: oac-02-desempenho
tipo: gabarito
questao: 3
fonte: Prova 1 -_2025.1_-_GABARITO.pdf | p. 2 (versão A) e p. 5 (versão B); OAC - RISC-V - Exercícios.pdf | p. 2
autoria: Enunciado: Prof. Erick de Andrade Barboza (Prova 1 de OAC, UFAL, 2025.1), parafraseado pela equipe TutorON; gabarito original da prova; resolução revisada pela equipe TutorON
fontes_catalogo: ufal-oac-prova1-2025-1,ufal-oac-lista-cap1
verificacao: conferida_por_codigo
status_resolucao: corrigida
---
Prova 1 de OAC (2025.1), Questão 3, igual nas duas versões, e Lista cap. 1, Exercício 3 (enunciado parafraseado). Status da resolução: corrigida (item b difere do gabarito original no arredondamento e precisa de interpretação; resolução da equipe TutorON).

Compilador A: 1,0×10⁹ instruções, 1,1 s. Compilador B: 1,2×10⁹ instruções, 1,5 s. Ciclo de 1 ns.
a) CPI médio de cada um. b) Se rodam em dois processadores com o mesmo tempo, quão mais rápido é o clock do processador com o código de A em relação ao de B? c) Um compilador novo gera 6,0×10⁸ instruções com CPI 1,1: qual o speedup em relação a A e a B no processador original?

Resolução
a) CPI = Tempo / (Instruções × Tempo de ciclo). A: 1,1 / (10⁹ × 10⁻⁹) = **1,1**. B: 1,5 / (1,2×10⁹ × 10⁻⁹) = **1,25**. (Gabarito: igual.)
b) Mesmo tempo T: f = Instruções × CPI / T. f_A ∝ 10⁹ × 1,1 = 1,1×10⁹; f_B ∝ 1,2×10⁹ × 1,25 = 1,5×10⁹. f_B / f_A = 1,5 / 1,1 ≈ **1,36**.
Gabarito original: f_B / f_A = 1,37. Divergência: 1,5 / 1,1 = 1,3636…, que arredonda para 1,36. Interpretação: o processador que roda o código de B precisa de clock ≈ 1,36 vez maior; o do código de A pode ter clock ≈ 0,73 vez o de B (ou seja, não é "mais rápido", é mais lento).
c) T_novo = 6×10⁸ × 1,1 × 1 ns = 0,66 s. Speedup sobre A = 1,1 / 0,66 ≈ **1,67**; sobre B = 1,5 / 0,66 ≈ **2,27**. (Gabarito: igual.)

Verificação: com f_A = 1 GHz, A leva 1,1 s; com f_B = 1,3636 GHz, B leva 1,5×10⁹ / 1,3636×10⁹ = 1,1 s.
