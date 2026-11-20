---
id: prog1-divisao-inteira-resto
titulo: Por que 7 / 2 dá 3 em C? Divisão inteira, resto (%) e conversão para real
assunto: prog1-03-variaveis-tipos-es
tipo: material_estudo
resolucao: sim
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aulas 4 (operadores) e 6 (resto para testar par)
fontes_catalogo: ufal-prog1-slides-paes
autoria: Slides do Prof. Rodrigo de Barros Paes (IC/UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Por que 7 / 2 dá 3 em C? Divisão entre inteiros descarta a parte fracionária: `7 / 2` vale 3 e `7 % 2` vale 1 (resto). Para obter 3,5, um dos lados precisa ser real: `7 / 2.0` ou `(double)7 / 2`. Com negativos, o C arredonda para zero: `-7 / 2` é −3 e `-7 % 2` é −1.

O resto serve para muitos problemas: `n % 2 == 0` testa se é par; `n % 10` dá o algarismo das unidades; `n / 10` tira esse algarismo.

Erro comum: `float media = soma / n;` com `soma` e `n` inteiros faz a divisão inteira primeiro e só depois converte; o resultado já perdeu a parte fracionária. Converta antes: `(float)soma / n`. Exemplo da aula 6: `11 % 4` vale 3, porque 11 / 4 dá 2 e sobra 3. Status da resolução: validada (contas conferidas por código pela equipe TutorON).
