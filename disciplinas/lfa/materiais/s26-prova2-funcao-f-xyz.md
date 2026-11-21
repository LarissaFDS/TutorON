---
id: lfa-prova2-funcao-f-quatro-componentes
titulo: Prova 2 (2017.1), questão 1 — F(x, y, z) = (x+y+z, 2z, x+2, y+y) como programa LPM e como função recursiva primitiva; enunciado incompleto
assunto: lfa-07-funcoes-recursivas-programas
tipo: prova
questao: 1
resolucao: sim
fonte: Segunda avaliação de Teoria da Computação 2017.1, Profa. Eliana (UFAL), questão 1
fontes_catalogo: ufal-eliana-prova2-2017-1
autoria: Questão de prova da Profa. Eliana (UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Prova 2 de 2017.1, questão 1. O arquivo da prova traz só a função $F(x, y, z) = (x+y+z,\; 2z,\; x+2,\; y+y)$; o texto do pedido está faltando. Status da resolução: pendente_professor. A resolução é da equipe TutorON e não é gabarito do professor.

**Pendente:** pelo restante da prova (questão 3 em LPM) e pela lista de 2014.1 da mesma professora, o pedido deve ser "apresente o programa em LPM" ou "apresente a função recursiva primitiva". Confira com o professor ou com a prova original. As duas leituras estão abaixo.

**Como programa LPM sem GOTO** (entradas $x, y, z$, saídas $s_1, \dots, s_4$):
```
s1 ← x;  LOOP y: s1 ← s1+1 END;  LOOP z: s1 ← s1+1 END
s2 ← 0;  LOOP z: s2 ← s2+1;  s2 ← s2+1 END
s3 ← x;  s3 ← s3+1;  s3 ← s3+1
s4 ← y;  LOOP y: s4 ← s4+1 END
```

**Como função recursiva primitiva** (cada componente separada):
- $F_1 = \text{soma}(\text{soma}(\pi_1, \pi_2), \pi_3)$;
- $F_2 = \text{soma}(\pi_3, \pi_3)$, ou $\text{mult}(2, \pi_3)$;
- $F_3 = S(S(\pi_1))$;
- $F_4 = \text{soma}(\pi_2, \pi_2)$.

Exemplo: $F(1, 2, 3) = (6, 6, 3, 4)$.

Erro comum: em LOOP $y$: $s_4 \leftarrow s_4 + 1$, começar com $s_4 \leftarrow 0$ em vez de $s_4 \leftarrow y$, o que dá $y$ em vez de $2y$.

**Verificação:** o interpretador LPM e as funções recursivas primitivas de `tests_acervo/lfa_verif.py` dão o mesmo $F$ que a fórmula direta para $x, y, z$ de 0 a 5.
