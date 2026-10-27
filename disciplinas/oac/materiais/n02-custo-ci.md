---
id: oac-nota-custo-ci
titulo: Nota — custo de circuito integrado: custo por die, dies por wafer e yield
assunto: oac-03-custo-ci
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: pattersonhennessy-cod-riscv
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Custo de circuitos integrados (Patterson & Hennessy, seção 1.5; slide do cap. 1 visto em aula).

Custo por die = Custo por wafer / (Dies por wafer × Yield)
Dies por wafer ≈ Área do wafer / Área do die
Yield = 1 / (1 + (Defeitos por área × Área do die / 2))²

Leitura: o yield (rendimento) é a fração de dies sem defeito. A relação com a área e com a taxa de defeitos não é linear: dobrar a área do die reduz o número de dies por wafer **e** o yield, então o custo por die cresce mais que o dobro.
- Custo e área do wafer são fixos para um processo de fabricação.
- A taxa de defeitos é determinada pelo processo de fabricação.
- A área do die é determinada pela arquitetura e pelo projeto do circuito.

Exemplo da equipe: defeitos = 0,02 por cm², die de 1 cm² → Yield = 1 / (1 + 0,02 × 1 / 2)² = 1 / 1,01² ≈ 0,980. Wafer de 700 cm² a US$ 5.000: ≈ 700 dies, custo por die ≈ 5000 / (700 × 0,980) ≈ US$ 7,29.
Com die de 2 cm² (mesmo wafer): ≈ 350 dies, Yield = 1 / 1,02² ≈ 0,961, custo ≈ 5000 / (350 × 0,961) ≈ US$ 14,86, mais que o dobro.

Cuidado: a fórmula de dies por wafer é aproximada (ignora os dies incompletos na borda do wafer). Use as unidades de forma coerente (defeitos por cm² com área em cm²).
