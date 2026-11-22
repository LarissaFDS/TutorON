---
id: lfa-cc-reavaliacao-2016-er-afn-afd
titulo: Reavaliação da AB1 de 2016.1 (Profa. Eliana) — AFD para a ER (11+00)*01(010)*, AFD da união "contém 0101 ou não contém 110", AFN com yy duas vezes convertido em AFD
assunto: lfa-03-expressoes-gramaticas-regulares
tipo: prova
questao: 1 a 3
resolucao: sim
fonte: Reavaliação AB1 2016.1 de Linguagens Formais e Autômatos, Profa. Eliana (IC-UFAL), na pasta da turma de Ciência da Computação
curso: Ciência da Computação (UFAL), pasta da turma de Teoria da Computação (COMP376); prova de 2016.1
fontes_catalogo: ufal-eliana-reavaliacao-2016-1
autoria: Questões da Profa. Eliana (UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDF não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Reavaliação da AB1 de 2016.1, Profa. Eliana (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Q1 — AFD para $(11+00)^*01(010)^*$:** estados A (inicial), B, C, F (final), G, H. $A \xrightarrow{1} B \xrightarrow{1} A$ e $A \xrightarrow{0} C \xrightarrow{0} A$ (pares 11 e 00); $C \xrightarrow{1} F$ (lido o 01); $F \xrightarrow{0} G \xrightarrow{1} H \xrightarrow{0} F$ (cada bloco 010). As demais transições vão para um estado morto. Gramática regular lida do autômato: $A \to 1B \mid 0C$, $B \to 1A$, $C \to 0A \mid 1F \mid 1$, $F \to 0G$, $G \to 1H$, $H \to 0F \mid 0$. Com o estado morto, o AFD mínimo tem 7 estados.

**Q2 — $L = L_1 \cup L_2$, com $L_1$ = "contém 0101" e $L_2$ = "não contém 110":** use a **construção do produto** dos AFD de cada um (5 e 4 estados): o estado é o par de progressos, final se achou 0101 **ou** ainda não achou 110. São 14 pares atingíveis e 11 estados no AFD mínimo. A ER sai do AFD por eliminação de estados (fica longa). Teste: 0110 está fora, 01010 dentro.

**Q3 — AFN com estados $q_1$ a $q_5$ sobre $\{x,y\}$:** $\delta(q_1,x)=\{q_1\}$, $\delta(q_1,y)=\{q_1,q_2\}$, $\delta(q_2,y)=\{q_3\}$, $\delta(q_3,x)=\{q_3\}$, $\delta(q_3,y)=\{q_3,q_4\}$, $\delta(q_4,y)=\{q_5\}$, $\delta(q_5,x)=\delta(q_5,y)=\{q_5\}$; final $q_5$. Reconhece as palavras com **duas ocorrências de yy que não se sobrepõem** (yyyy e yyxyy sim; yyy não).

| $\delta'$ | x | y |
|---|---|---|
| → $\{q_1\}$ | $\{q_1\}$ | $\{q_1,q_2\}$ |
| $\{q_1,q_2\}$ | $\{q_1\}$ | $\{q_1,q_2,q_3\}$ |
| $\{q_1,q_2,q_3\}$ | $\{q_1,q_3\}$ | $\{q_1,q_2,q_3,q_4\}$ |
| $\{q_1,q_3\}$ | $\{q_1,q_3\}$ | $\{q_1,q_2,q_3,q_4\}$ |
| $\{q_1,q_2,q_3,q_4\}$ | $\{q_1,q_3\}$ | $\{q_1,\dots,q_5\}$ |
| $\{q_1,\dots,q_5\}$ (final) | $\{q_1,q_3,q_5\}$ | $\{q_1,\dots,q_5\}$ |
| $\{q_1,q_3,q_5\}$ (final) | $\{q_1,q_3,q_5\}$ | $\{q_1,\dots,q_5\}$ |

Erros comuns: trocar as colunas da tabela ($q_2$ e $q_4$ só têm transição em y); usar interseção na Q2.

**Verificação:** `test_reavaliacao_2016_1` confere as três questões em todas as palavras até comprimento 12.
