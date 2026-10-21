---
id: sd-av1-q19-25
titulo: Lista AV1 — circuitos de aplicação, atraso de propagação e identificação de circuitos (Q19–Q25)
assunto: sd-06-analise-temporal
tipo: lista
resolucao: nao
questao: 19-25
fonte: Lista de SD AV1.pdf | páginas 4–7 | questões 19 a 25
fontes_catalogo: ufal-sd-lista-av1
autoria: Enunciados: lista de exercícios da disciplina (UFAL); figuras não transcritas
licenca: Material da disciplina; uso no TutorON pendente de confirmação com o professor
curadoria: aprovado
natureza: material_da_disciplina
verificacao: sem_resolucao
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Lista de SD AV1 — Circuitos de Aplicações, Análise Temporal e Identificação de Circuitos

19. (Tanques da Embraer) Os tanques A e B têm sensores que enviam, em binário, de 0 a 10 a porcentagem de combustível (0 vazio, 10 cheio). O circuito deve acender LEDs indicando: A desbalanceado em relação a B (A < B); B desbalanceado em relação a A (B < A); A cheio; B cheio.
Ideia: 0 a 10 cabe em 4 bits; um comparador de magnitude de 4 bits fornece A < B e A > B; "cheio" é A = 10 = 1010₂, ou seja, a3·a2'·a1·a0'.

20. Implemente um sistema que recebe 4 números de 5 bits e garante que cada número fique no intervalo [Y1, Y2]: se for menor ou igual a Y1, a saída é Y1; se for maior ou igual a Y2, a saída é Y2; senão, o valor original.
Ideia: para cada número, dois comparadores (com Y1 e com Y2) e dois níveis de MUX 2:1 (saturação/clamp).

21. A partir dos sinais aplicados às entradas da figura, desenhe a forma de onda da saída. (Figura não transcrita.)

22. Um circuito de acionamento de alarme tem atrasos de propagação por porta (tabela na figura). a) Calcule o atraso de propagação do circuito. b) Simplificando o circuito, obtenha outro com menor atraso, mostrando como chegou nele e o novo atraso. Método: o atraso é o do caminho mais longo (caminho crítico) da entrada até a saída; simplificar a expressão reduz níveis de portas.

23. Em uma usina nuclear, Ta, Tb e Tc vêm de termômetros e S aciona o resfriamento. Pelo diagrama de tempo de t1 a t8 (figura), indique em que tempos o sistema foi acionado.

24 e 25. Diga, de forma resumida e direta, qual a função dos circuitos das figuras e explique como funcionam. (Figuras não transcritas.)
