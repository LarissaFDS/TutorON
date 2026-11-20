---
id: prog1-aula07-08-troca-aninhadas
titulo: Aulas 7 e 8 — trocar duas variáveis, "assuma e corrija" e decisões aninhadas
assunto: prog1-04-decisao
tipo: material_estudo
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aulas 7 (seção 7.3) e 8 (Decisões aninhadas; seção 7.8)
fontes_catalogo: ufal-prog1-slides-paes
autoria: Slides do Prof. Rodrigo de Barros Paes (IC/UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Trocar o conteúdo de a e b: a primeira tentativa, `a = b; b = a;`, perde o valor de a (as duas ficam com o valor de b). O certo usa uma variável auxiliar:

`temp = a; a = b; b = temp;`

Estratégia "assuma e só aja se estiver errado": para imprimir dois números em ordem crescente, assuma que a é o menor; se `a > b`, troque; depois imprima a e b. Se forem iguais, a ordem tanto faz. A mesma ideia vale para achar o menor de três: guarde o primeiro como menor e troque se encontrar um menor. Os exercícios do Huxley das aulas (menor de 3, dois números em ordem crescente, eleitor, equação do segundo grau) são para o aluno fazer: o tutor guia o raciocínio, não entrega o código.

Decisões aninhadas: um `if` dentro de outro, quando a segunda pergunta só faz sentido depois da primeira. Exemplo da aula (radar): primeiro decida se o carro será multado (velocidade do carro maior que a da via); só então calcule quanto ultrapassou, em percentual, para escolher a faixa de pontos. Antes de programar, resolva "no papel e no lápis" com alguns valores, inclusive os que caem exatamente nas fronteiras das faixas.

Corrida de aventura (aula 8): validar um caminho é uma sequência de perguntas que dependem da resposta anterior (de onde se pode ir a partir do ponto atual). Desenhe o mapa e teste caminhos válidos e inválidos.
