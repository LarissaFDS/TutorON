---
id: eletronica-anot-ponte-resistores
titulo: Ponte com dois diodos ideais e dois resistores de 2,2 kΩ, carga de 2,2 kΩ e entrada de 100 V de pico: Vo de pico 50 V e tensão CC 31,8 V
assunto: eletronica-03-retificadores
tipo: resolucao
resolucao: sim
fonte: Anotações "Aplicações de diodos" (24 set. 2026), questão 3 (exercício de livro, parafraseado)
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

**Circuito (descrito):** a entrada liga o nó de cima ao nó de baixo. Do nó da esquerda (terra) sai D1 para o nó de cima (ânodo no terra); do nó de cima sai D2 para o nó da direita, que é a saída $v_o$. Dois resistores de 2,2 kΩ ligam o nó de baixo ao terra e à saída; a carga de 2,2 kΩ vai da saída ao terra.

**Semiciclo positivo (D2 conduz, D1 bloqueado):** nó de cima $= v_o$ e $v_o - V_B = 100$. A soma das correntes que saem do supernó para o terra é $V_B/2{,}2\mathrm{k} + v_o/2{,}2\mathrm{k} = 0$, então $v_o + V_B = 0$ e $v_o = 50$ V.

**Semiciclo negativo (D1 conduz, D2 bloqueado):** D1 prende o nó de cima no terra, então $V_B = 100$ V. Os dois resistores de 2,2 kΩ entre $V_B$ e o terra formam um divisor: $v_o = 100\cdot\frac{2{,}2}{2{,}2 + 2{,}2} = 50$ V.

Saída: onda completa com 50 V de pico; tensão CC $= 2(50)/\pi = 31{,}8$ V.

**Verificação:** a análise nodal (SymPy) dos dois semiciclos dá 50 V e confere os estados: no positivo, D1 fica com $-50$ V; no negativo, D2 fica com $0 - 50 = -50$ V.
