---
id: so-ab2-escalonamento-disco-descendo
titulo: AB2 — escalonamento de disco com a cabeça que passou por 76 e 50 (descendo); FCFS, SSTF, SCAN e LOOK e o erro de confundir SCAN, LOOK e C-LOOK
assunto: so-07-entrada-saida
tipo: prova
questao: 8
resolucao: sim
fonte: Variante da AB2 do Prof. André Aquino (UFAL), com resolução da turma e respostas compartilhadas da turma
fontes_catalogo: turma-resolucao-ab2-variante,turma-respostas-so,ufal-aquino-slides-so
autoria: Questão de prova do Prof. André Aquino (UFAL); resoluções de alunos conferidas por simulação e corrigidas pela equipe TutorON
licenca: Não declarada (prova); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Variante da AB2 (enunciado parafraseado): os mesmos pedidos 95, 164, 36, 68, 17, 115, disco de 0 a 199, mas a cabeça **acabou de percorrer os blocos 76 e 50, nessa ordem**: está em 50 e **descendo** (para 0). Determine os deslocamentos e o total para FCFS, SSTF, SCAN e LOOK. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

Primeiro passo: tirar o **sentido** do histórico. 76 → 50 é descida.

| Política | Percurso | Total |
|---|---|---|
| FCFS | 50 → 95 → 164 → 36 → 68 → 17 → 115 | **423** |
| SSTF | 50 → 36 → 17 → 68 → 95 → 115 → 164 | 14 + 19 + 51 + 27 + 20 + 49 = **180** |
| SCAN | 50 → 36 → 17 → **0** → 68 → 95 → 115 → 164 | 50 + 164 = **214** |
| LOOK | 50 → 36 → 17 → 68 → 95 → 115 → 164 | 33 + 147 = **180** |

**Correção:** a resolução da turma deu para o SCAN o percurso do LOOK (parando em 17, sem ir à borda 0) e, para o LOOK, o percurso 50 → 36 → 17 → 164 → 115 → 95 → 68, que é o do **C-LOOK** (salta do menor pedido ao maior e continua no mesmo sentido; total 276). Nas respostas compartilhadas, o FCFS aparece com 363 blocos e um colega já pede correção: o certo é **423**. Aqui o LOOK coincide com o SSTF, mas isso é acaso da posição dos pedidos.

Com a cabeça **subindo** (outro exercício do caderno), os totais mudam: SCAN 331 e LOOK 261. O sentido inicial é dado do problema; não o ignore.

**Verificação:** no SCAN descendo, o percurso é 50 até 0 (50 blocos) e depois 0 até 164 (164 blocos): 214; no LOOK, 50 até 17 (33) e 17 até 164 (147): 180. Simulado em `tests_acervo/so_verif.py`.
