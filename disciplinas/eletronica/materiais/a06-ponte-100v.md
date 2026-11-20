---
id: eletronica-anot-ponte-100v-piv
titulo: Ponte retificadora com diodos ideais, entrada de 100 V de pico e carga de 2,2 kΩ: Vo de pico 100 V, corrente máxima 45,45 mA e PIV de 100 V
assunto: eletronica-03-retificadores
tipo: resolucao
resolucao: sim
fonte: Anotações "Aplicações de diodos" (24 set. 2026), questão 2 (exercício de livro, parafraseado)
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

**Enunciado (paráfrase):** ponte de quatro diodos ideais, entrada senoidal de 100 V de pico, carga de 2,2 kΩ; pede $v_o$, PIV e corrente máxima em cada diodo.

- Semiciclo positivo: D1 e D3 conduzem; ideal, sem queda: $V_{o,pico} = 100$ V.
- Semiciclo negativo: D2 e D4 conduzem; a carga vê de novo $+100$ V de pico (onda completa).
- Corrente máxima (a mesma em cada diodo que conduz): $I_{max} = 100/2{,}2\ \mathrm{k\Omega} = 45{,}45$ mA.
- PIV: na ponte ideal, o diodo bloqueado fica em paralelo reverso com a entrada pelo par que conduz: PIV $= V_m = 100$ V.
- Valor médio na carga: $2(100)/\pi = 63{,}66$ V.

**Verificação:** no pico positivo, D2 e D4 ficam com $-100$ V (bloqueados) e a LKT na malha da fonte com D1, carga e D3 fecha com $100 - 0 - 100 - 0 = 0$.
