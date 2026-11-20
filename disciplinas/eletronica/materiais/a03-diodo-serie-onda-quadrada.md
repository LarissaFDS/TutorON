---
id: eletronica-anot-diodo-serie-quadrada
titulo: Diodo de silício em série com resistores e com bateria, entrada quadrada de ±12 V: Vo = 5,09 V e Vo = 15,3 V
assunto: eletronica-02-circuitos-diodo
tipo: resolucao
resolucao: sim
fonte: Anotações "Aplicações de diodos" (24 set. 2026), questão 4 (exercício de livro, parafraseado)
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

**(a)** Entrada quadrada de $\pm12$ V → diodo de silício em série → 2,2 kΩ → saída $v_o$ sobre 1,8 kΩ para o terra.
- $v_i = +12$ V, diodo ligado: LKT $12 - 0{,}7 - I(2{,}2\mathrm{k} + 1{,}8\mathrm{k}) = 0$ → $I = 11{,}3/4\ \mathrm{k\Omega} = 2{,}825$ mA; $v_o = 1{,}8\mathrm{k}\cdot I = 5{,}085 \approx 5{,}09$ V.
- $v_i = -12$ V: diodo reverso, $I = 0$, $v_o = 0$.

**(b)** Entrada → diodo de silício → bateria de 4 V (negativo do lado do diodo, positivo do lado da saída, somando) → $v_o$ sobre 10 kΩ.
- $v_i = +12$ V: $v_o = 12 - 0{,}7 + 4 = 15{,}3$ V; $I = 15{,}3/10\ \mathrm{k\Omega} = 1{,}53$ mA.
- $v_i = -12$ V: suponha desligado → $v_o = 0$, cátodo em $-4$ V, ânodo em $-12$ V: $V_D = -8$ V, bloqueado (confere). O diodo só conduziria para $v_i > -3{,}3$ V.

**Verificação:** em (a) LKT $12 - 0{,}7 - 2{,}825\cdot2{,}2 - 5{,}085 = 0$; em (b) as hipóteses de estado foram conferidas nos dois níveis.
