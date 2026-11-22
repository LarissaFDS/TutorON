---
id: prog1-aula02-algoritmos
titulo: Aula 2 — algoritmo, instrução, estado e representação de quantidades
assunto: prog1-01-algoritmos-representacao
tipo: material_estudo
curso: Engenharia de Computação (UFAL), Programação 1 (ECOM002); slides do Prof. Rodrigo de Barros Paes; semestre não identificado
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 2 (Introdução; livro, capítulos 1 a 3)
fontes_catalogo: ufal-prog1-slides-paes
autoria: Slides do Prof. Rodrigo de Barros Paes (IC/UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
revisao_humana: pendente
---
O computador executa instruções sem questionar se fazem sentido; por isso cada passo precisa ser detalhado. **Algoritmo** é um conjunto de passos (instruções) que resolve um problema.

Exemplo da aula: atravessar o homem, a raposa, a galinha e o milho numa canoa que leva um item por vez (a raposa come a galinha; a galinha come o milho). Antes de escrever as instruções, escolha uma **representação**: quem está em cada margem, como nomear os personagens, como registrar uma travessia. Uma forma é escrever as letras de cada margem, como `HRGM | ____` no estado inicial. Cada instrução ("leve a galinha para o outro lado") muda o **estado**: `RM | HG`.

Estado passo a passo: para "quantos minutos se passaram desde o início do dia?", o algoritmo usa horas e minutos: minutos = horas × 60 + minutos. Com 10:15 dá 615; com 11 e 20, 680; com 22 e 40, 1360. Anotar o valor de cada variável a cada passo (teste de mesa) é a forma de conferir um algoritmo à mão.

Hardware: dispositivos de entrada (teclado, mouse) e de saída (monitor, impressora); a CPU executa as instruções; a RAM guarda as variáveis enquanto o programa roda (não persiste); o disco guarda arquivos de forma persistente.

Quantidades: o sistema decimal usa 10 símbolos e combina-os para quantidades maiores. No computador é simples distinguir dois estados elétricos, então usa-se o binário (0 e 1): 0000, 0001, 0010, 0011, 0100… Letras também viram números: na tabela ASCII, 'A' é 65, ou 1000001 em binário.
