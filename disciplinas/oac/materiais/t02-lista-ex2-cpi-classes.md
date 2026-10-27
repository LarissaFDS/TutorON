---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-lista-ex2
titulo: Lista cap. 1, Exercício 2 — CPI global com quatro classes de instrução (P1 × P2)
assunto: oac-02-desempenho
tipo: lista
questao: 2
fonte: OAC - RISC-V - Exercícios.pdf | pp. 1–2
autoria: Lista de exercícios da turma (autor não identificado no arquivo; exercícios no estilo do cap. 1 de Patterson & Hennessy), parafraseada pela equipe TutorON; resolução da equipe TutorON (a lista não traz resolução)
fontes_catalogo: ufal-oac-lista-cap1
verificacao: conferida_por_codigo
status_resolucao: validada
---
Lista de exercícios de OAC, capítulo 1, Exercício 2 (enunciado parafraseado). Status da resolução: validada (resolução da equipe TutorON, conferida por código; não é gabarito do professor).

Duas implementações da mesma ISA. Classes A, B, C e D. P1: 2,5 GHz, CPIs 1, 2, 3 e 2. P2: 3 GHz, CPIs 2, 2, 2 e 2. Programa com 1,0×10⁶ instruções: 10% A, 20% B, 50% C, 20% D. Qual é mais rápido? a) CPI global de cada um; b) ciclos de clock de cada um.

Resolução
a) CPI médio = Σ (frequência relativa × CPI da classe).
P1: 0,1×1 + 0,2×2 + 0,5×3 + 0,2×2 = 0,1 + 0,4 + 1,5 + 0,4 = **2,4**.
P2: todas as classes têm CPI 2 → **2,0**.
b) Ciclos = Instruções × CPI. P1: 1,0×10⁶ × 2,4 = **2,4×10⁶ ciclos**. P2: **2,0×10⁶ ciclos**.
Tempo = Ciclos / Frequência. P1: 2,4×10⁶ / 2,5×10⁹ = 0,96 ms. P2: 2,0×10⁶ / 3×10⁹ ≈ 0,667 ms.
**P2 é mais rápido**, cerca de 0,96 / 0,667 ≈ 1,44 vez.

Verificação: o tempo médio por instrução é CPI / f: P1 = 2,4 / 2,5 GHz = 0,96 ns; P2 = 2 / 3 GHz ≈ 0,667 ns. A razão é a mesma, 1,44.
