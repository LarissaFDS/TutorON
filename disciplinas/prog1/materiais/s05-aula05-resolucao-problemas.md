---
id: prog1-aula05-resolucao-problemas
titulo: Aula 5 — resolver problemas: divisão inteira, resto, casas decimais e testar com vários valores
assunto: prog1-03-variaveis-tipos-es
tipo: material_estudo
resolucao: sim
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 5 (Resolução de problemas; livro, capítulo 6)
fontes_catalogo: ufal-prog1-slides-paes
autoria: Slides do Prof. Rodrigo de Barros Paes (IC/UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio e código revisado; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Os exercícios da aula 5 (segundos em X minutos, calculadora com as quatro operações, IMC, troco da máquina de café, área do triângulo, quadrado de `#`) treinam o mesmo roteiro: ler, calcular, imprimir **exatamente** o formato pedido.

Divisão inteira e resto estão no bloco próprio sobre `/` e `%`.

Casas decimais: `printf("%.3f\n", x);` imprime com 3 casas. `%f` sozinho imprime 6 casas (5 e 8 na calculadora: 40.000000, 0.625000, 13.000000, -3.000000).

Exemplo de conta: IMC = massa / altura². Com 77 kg e 1,81 m, 77 / (1,81 × 1,81) ≈ 23,5. Em C: `imc = massa / (altura * altura);` (os parênteses importam).

Teste com vários valores, não só o do enunciado: para "segundos em X minutos", tente 0, 30, 100 e 2000 (0, 1800, 6000, 120000). Valores grandes mostram se o tipo escolhido estoura. Status da resolução: validada (contas conferidas por código pela equipe TutorON).
