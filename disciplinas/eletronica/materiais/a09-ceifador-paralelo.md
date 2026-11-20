---
id: eletronica-anot-ceifador-paralelo
titulo: Ceifador paralelo com diodo de silício e entrada senoidal de 10 V de pico: Vo = vi/2 até 1,4 V, depois 0,7 V; −5 V no semiciclo negativo; IR máx = 9,3 mA
assunto: eletronica-04-ceifadores-grampeadores
tipo: resolucao
resolucao: sim
fonte: Anotações "Exercícios" (17 set. 2026), exercício 26 (de livro, parafraseado)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Circuito:** $v_i$ (seno de 10 V de pico) → 1 kΩ em série → nó de saída; do nó ao terra, um diodo de silício (ânodo no nó) em paralelo com a carga de 1 kΩ. Qual a tensão de saída deste ceifador?

**Semiciclo positivo:** com o diodo desligado, a saída é o divisor $v_o = v_i/2$. O diodo só liga quando $v_o$ chega a 0,7 V, ou seja, para $v_i \ge 1{,}4$ V; daí em diante $v_o = 0{,}7$ V (ceifado). Corrente máxima no resistor série, no pico: $I_R = \frac{10 - 0{,}7}{1\ \mathrm{k\Omega}} = 9{,}3$ mA (0,7 mA vão para a carga, 8,6 mA para o diodo).

**Semiciclo negativo:** diodo reverso (aberto), divisor: $v_o = v_i/2$, mínimo de $-5$ V.

**Correção:** a anotação desenha $v_o = 0{,}7$ V durante todo o semiciclo positivo. Entre 0 e 1,4 V de entrada o diodo ainda não conduz e $v_o = v_i/2$ sobe de 0 a 0,7 V. O 9,3 mA da anotação está certo.

**Verificação:** varrendo $v_i$ de $-10$ a $10$ V com o modelo de queda constante (hipótese conferida em cada ponto), $v_o$ máximo é 0,7 V, mínimo $-5$ V, e o joelho fica em $v_i = 1{,}4$ V.
