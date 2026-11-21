---
id: so-escalonamento-disco-subindo
titulo: Escalonamento de disco — FCFS, SSTF, SCAN, C-SCAN, LOOK e C-LOOK para os pedidos 95, 164, 36, 68, 17, 115 com a cabeça no bloco 50 subindo
assunto: so-07-entrada-saida
tipo: lista
questao: caderno, cap. 7 (lista 5 da turma, questão 1)
resolucao: sim
fonte: Lista 5 da turma (2021) sobre o caderno de exercícios do Prof. Maziero; slides do Prof. André Aquino (UFAL), gerência de E/S
fontes_catalogo: turma-listas-2021,maziero-caderno-2014,ufal-aquino-slides-so
autoria: Exercício do Prof. Maziero; resolução de aluno conferida por simulação pela equipe TutorON
licenca: Exercício sob CC BY-NC-SA 3.0 (Maziero); resolução de aluno parafraseada
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exercício do caderno do Prof. Maziero. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Fila de pedidos, nessa ordem: 95, 164, 36, 68, 17, 115. Disco com blocos 0 a 199. A cabeça acabou de atender o bloco 50 e está **subindo** (indo para 199). O custo é a soma dos deslocamentos $|b_{i+1} - b_i|$.

| Política | Percurso | Total |
|---|---|---|
| FCFS (ordem de chegada) | 50 → 95 → 164 → 36 → 68 → 17 → 115 | 45 + 69 + 128 + 32 + 51 + 98 = **423** |
| SSTF (o mais próximo) | 50 → 36 → 17 → 68 → 95 → 115 → 164 | 14 + 19 + 51 + 27 + 20 + 49 = **180** |
| SCAN (elevador, vai até a borda) | 50 → 68 → 95 → 115 → 164 → 199 → 36 → 17 | 114 + 35 + 163 + 19 = **331** |
| C-SCAN (sobe até 199, volta a 0, sobe de novo) | 50 → … → 164 → 199 → 0 → 17 → 36 | 149 + 199 + 36 = **384** |
| LOOK (inverte no último pedido) | 50 → 68 → 95 → 115 → 164 → 36 → 17 | 114 + 128 + 19 = **261** |
| C-LOOK (do último pedido salta ao menor) | 50 → … → 164 → 17 → 36 | 114 + 147 + 19 = **280** |

Pontos de atenção:
- No SSTF, de 50 o mais próximo é 36 (distância 14), não 68 (18): o SSTF **ignora o sentido** de movimento e pode deixar pedidos distantes em inanição.
- SCAN e C-SCAN vão até a **borda** (199) mesmo sem pedido lá; LOOK e C-LOOK param no último pedido.
- Neste resultado o retorno do C-SCAN (199 → 0) foi contado como deslocamento; há livros que não o contam (aí daria 185). Diga qual convenção usou.

**Verificação:** todas as políticas atendem os mesmos 6 pedidos; o SSTF dá o menor total (180) e o FCFS o maior (423); simulado em `tests_acervo/so_verif.py`.
