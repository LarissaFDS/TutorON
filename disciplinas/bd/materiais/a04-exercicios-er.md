---
id: bd-aula-exercicios-er
titulo: Exercícios de BD — modelo ER da floricultura e da escola (turmas, professores e salas)
assunto: bd-03-modelo-er
tipo: exercicio_resolvido
resolucao: sim
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 2 "Modelagem Conceitual", exercícios
fontes_catalogo: ufal-bd-slides
autoria: Profª Maria Cristina Tenório (enunciados); resolução da equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
status_resolucao: pendente_professor
revisao_humana: pendente
---
Status da resolução: pendente de confirmação do professor (resolução da equipe TutorON; os slides não trazem gabarito). Diagrama ER em texto, notação de Chen.

**Floricultura.** Clientes têm RG, nome, telefone e endereço. Produtos têm nome, tipo (flor, vaso, planta), preço e quantidade em estoque. Cada compra guarda o cliente, a data, o valor total e os produtos comprados.

- Entidades: CLIENTE (RG chave, nome, telefone, endereço composto), PRODUTO (código chave, nome, tipo, preço, qtd_estoque), COMPRA (número chave, data, valor_total).
- Cardinalidade dos relacionamentos: CLIENTE —faz— COMPRA é 1:N. Um cliente faz várias compras; cada compra é de um só cliente (participação total da compra).
- COMPRA —contém— PRODUTO: N:M, com o atributo quantidade no relacionamento. Uma compra tem vários produtos e um produto aparece em várias compras.
- O enunciado não dá chave para produto nem para compra: código e número são escolha da equipe. O valor total pode ser derivado (soma de preço × quantidade); guardá-lo é decisão de projeto.

**Escola.** Uma escola tem várias turmas; uma turma tem vários professores e um professor dá aula em várias turmas; uma turma tem sempre aula na mesma sala, e uma sala recebe várias turmas em horários diferentes.

- ESCOLA —tem— TURMA: 1:N (cada turma é de uma escola).
- TURMA —tem— PROFESSOR: N:M.
- SALA —recebe— TURMA: 1:N (cada turma numa sala; a sala com várias turmas). O horário fica na turma, pois a sala é sempre a mesma para ela.
- Atributos e chaves não são dados no enunciado; use, por exemplo, código para turma, matrícula para professor e número para sala.
