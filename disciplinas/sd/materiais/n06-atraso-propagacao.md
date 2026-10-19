---
id: sd-nota-atraso
titulo: Nota — atraso de propagação, caminho crítico e formas de onda
assunto: sd-06-analise-temporal
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: kuphaldt-lec-vol4,mit-ocw-6004
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Análise temporal de circuitos combinacionais

Atraso de propagação (t_pd): tempo entre a mudança de uma entrada e a saída da porta estabilizar. O atraso de um circuito é o do caminho crítico, o caminho mais demorado de qualquer entrada até a saída, somando os atrasos das portas desse caminho.

Procedimento:
1. Liste cada caminho de entrada até a saída (ou calcule, porta por porta, o instante em que cada saída fica pronta: o instante máximo das entradas mais o atraso da porta).
2. O maior valor na saída é o atraso do circuito.
3. Para reduzir o atraso: simplifique a expressão (menos níveis), troque portas lentas por equivalentes, use forma de dois níveis (SOP: NOT → AND → OR) ou balanceie a árvore de portas.

Exemplo com AND = 3, OR = 4 e NOT = 1 (u.t.): uma SOP de dois níveis com entradas negadas tem caminho máximo NOT + AND + OR = 1 + 3 + 4 = 8 u.t., qualquer que seja o número de termos, desde que cada porta aceite todas as suas entradas. Uma expressão em cascata, como ((A·B + C)·D + E), soma AND + OR a cada nível e fica mais lenta.

Formas de onda: para desenhar a saída de um circuito combinacional, divida o tempo nos instantes em que alguma entrada muda; em cada intervalo, calcule a saída pela expressão (ou pela tabela-verdade). Considerando atrasos, desloque cada mudança da saída pelo atraso do caminho; caminhos com atrasos diferentes podem gerar pulsos espúrios (glitches, ou hazards).

Em sistemas de tempo real, o requisito é o atraso máximo permitido; compare o caminho crítico com esse limite antes e depois da simplificação.
