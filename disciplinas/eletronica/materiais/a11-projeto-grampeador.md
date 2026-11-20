---
id: eletronica-anot-projeto-grampeador
titulo: Projeto de grampeador (exercício 40): transformar quadrada de ±20 V em saída de −10 V a +30 V com capacitor, diodo ideal e bateria de 10 V
assunto: eletronica-04-ceifadores-grampeadores
tipo: resolucao
resolucao: sim
fonte: Anotações "Exercícios" (17 set. 2026), exercício 40 (resolução do professor no quadro, fotografada; foto não copiada)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Pedido:** entrada quadrada de $\pm20$ V; saída quadrada de $-10$ V a $+30$ V, com diodos ideais.

**Raciocínio:** o pico a pico continua 40 V, então basta grampear o nível de baixo em $-10$ V (deslocamento de $+10$ V).

**Projeto (resolução do quadro):** capacitor em série da entrada para a saída; da saída ao terra, um diodo ideal com o ânodo numa bateria de 10 V cujo positivo vai ao terra (ânodo em $-10$ V); resistor de carga em paralelo.
- $v_i = -20$ V: o diodo conduz, $v_o = -10$ V, $V_C = v_i - v_o = -10$ V.
- $v_i = +20$ V: diodo aberto, $v_o = 20 - (-10) = 30$ V.

Regra geral: o diodo prende o extremo do lado do ânodo (conduz quando $v_o$ tenta passar do nível da bateria), e a constante de tempo $RC$ tem que ser muito maior que o meio período, para o capacitor não descarregar.

**Verificação:** com $v_o = 30$ V, o diodo fica com $V_D = -10 - 30 = -40$ V (bloqueado); a saída tem 40 V pico a pico, como a entrada.
