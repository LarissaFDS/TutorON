---
id: iec-portas-logicas
titulo: Portas lógicas básicas: NOT, AND, OR, NAND, NOR, XOR e XNOR com tabelas-verdade
assunto: iec-07-portas-boole
tipo: material_estudo
resolucao: sim
fonte: Slides do Capítulo 3 (O nível lógico digital) de Organização Estruturada de Computadores, Tanenbaum, 6ª ed., Pearson, slides 3, 4 e 10
fontes_catalogo: pearson-tanenbaum-slides
autoria: Slides da editora Pearson (baseados em Tanenbaum), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Protegido (© 2014 Pearson, todos os direitos reservados): só paráfrase e referência por seção
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

Uma **porta lógica** calcula uma função de sinais binários (0 e 1). Com $A$ e $B$ como entradas:

| A | B | AND $A\cdot B$ | OR $A+B$ | NAND $\overline{A\cdot B}$ | NOR $\overline{A+B}$ | XOR $A\oplus B$ | XNOR $\overline{A\oplus B}$ |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

- **NOT** (inversor): $\overline{A}$ ("A barrado") troca 0 por 1.
- **XOR** (ou exclusivo): sai 1 quando as entradas são **diferentes**; $A\oplus B = \overline{A}B + A\overline{B}$. É o bit de soma do meio-somador.
- **XNOR**: sai 1 quando as entradas são **iguais**; é o comparador de igualdade de 1 bit.
- Uma **bolinha** no desenho indica inversão (na saída ou numa entrada). Por De Morgan, uma OR com todas as entradas invertidas equivale a uma NAND, e uma AND com entradas invertidas equivale a uma NOR.
- NAND e NOR são **universais**: só com um desses tipos se monta qualquer função. Em transistores, NAND e NOR são mais simples que AND e OR.
- Portas são vendidas em **circuitos integrados** (chips), em encapsulamentos como DIP.

**Verificação:** a coluna XNOR é a negação da XOR linha a linha, e a NAND é a negação da AND.
