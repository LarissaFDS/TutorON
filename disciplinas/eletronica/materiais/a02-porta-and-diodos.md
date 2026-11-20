---
id: eletronica-anot-porta-and-diodos
titulo: Porta AND com diodos de silício (lógica negativa): entradas −5 V e 0 V, resistor de 2,2 kΩ para −5 V; qual diodo conduz e Vo = −0,7 V
assunto: eletronica-02-circuitos-diodo
tipo: resolucao
resolucao: sim
fonte: Anotações "Aplicações de diodos" (24 set. 2026), questão 1 (exercício de livro, parafraseado)
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

**Circuito (descrito):** dois diodos de silício com os ânodos nas entradas, $-5$ V (D1) e 0 V (D2), e os cátodos juntos no nó de saída $V_o$; um resistor de 2,2 kΩ liga $V_o$ a $-5$ V.

**Hipótese:** o resistor puxa $V_o$ para baixo, então o diodo da entrada mais alta (D2, 0 V) conduz. Silício: $V_A - V_K = 0{,}7$ → $0 - V_o = 0{,}7$ → $V_o = -0{,}7$ V.

**Conferir D1:** $V_A - V_K = -5 - (-0{,}7) = -4{,}3$ V, menor que 0,7 V: D1 bloqueado. Corrente em D2: $I = \frac{-0{,}7 - (-5)}{2{,}2\ \mathrm{k\Omega}} = 1{,}95$ mA $> 0$, sentido direto.

Saída constante de $-0{,}7$ V (nível "alto" da lógica negativa só se as duas entradas forem $-5$ V).

**Verificação:** as duas hipóteses fecham (D2 com corrente direta de 1,95 mA, D1 com $-4{,}3$ V reverso); a LKT na malha 0 V → D2 → 2,2 kΩ → $-5$ V dá $0 - 0{,}7 - 2{,}2\cdot1{,}95 + 5 = 0$.
