---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (material de turma); o PDF original não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
revisao_humana: pendente
id: oac-lista-ex1
titulo: Lista cap. 1, Exercício 1 — P1, P2 e P3: instruções por segundo, ciclos e nova frequência
assunto: oac-02-desempenho
tipo: lista
questao: 1
fonte: OAC - RISC-V - Exercícios.pdf | p. 1
autoria: Lista de exercícios da turma (autor não identificado no arquivo; exercícios no estilo do cap. 1 de Patterson & Hennessy), parafraseada pela equipe TutorON; resolução da equipe TutorON (a lista não traz resolução)
fontes_catalogo: ufal-oac-lista-cap1
verificacao: conferida_por_codigo
status_resolucao: validada
---
Lista de exercícios de OAC, capítulo 1, Exercício 1 (enunciado parafraseado). Status da resolução: validada (resolução da equipe TutorON, conferida por código; não é gabarito do professor).

Dados: P1 tem 3 GHz e CPI 1,5; P2 tem 2,5 GHz e CPI 1,0; P3 tem 4,0 GHz e CPI 2,2. Os três executam o mesmo conjunto de instruções.
a) Qual tem o maior desempenho em instruções por segundo?
b) Se cada um executa um programa em 10 s, quantos ciclos e quantas instruções são executados?
c) Queremos reduzir o tempo em 30%, mas isso aumenta o CPI em 20%. Qual frequência é necessária?

Resolução
a) Instruções por segundo = Frequência / CPI.
P1 = 3×10⁹ / 1,5 = 2,0×10⁹; P2 = 2,5×10⁹ / 1,0 = 2,5×10⁹; P3 = 4×10⁹ / 2,2 ≈ 1,82×10⁹. **P2** tem o maior desempenho, apesar de ter a menor frequência.
b) Ciclos = Tempo × Frequência; Instruções = Ciclos / CPI.
P1: 3×10¹⁰ ciclos e 2×10¹⁰ instruções. P2: 2,5×10¹⁰ ciclos e 2,5×10¹⁰ instruções. P3: 4×10¹⁰ ciclos e ≈ 1,82×10¹⁰ instruções.
c) Tempo = Instruções × CPI / f. Com o mesmo número de instruções, Tempo novo = 0,7 × Tempo e CPI novo = 1,2 × CPI:
0,7 = 1,2 × f / f_novo → f_novo = (1,2 / 0,7) × f ≈ 1,714 × f.
P1: ≈ 5,14 GHz; P2: ≈ 4,29 GHz; P3: ≈ 6,86 GHz.

Verificação: em P1, 2×10¹⁰ instruções × 1,8 (CPI novo) / 5,14×10⁹ Hz ≈ 7,0 s = 70% de 10 s.
