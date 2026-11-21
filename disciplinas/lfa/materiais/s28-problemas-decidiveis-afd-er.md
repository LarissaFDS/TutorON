---
id: lfa-decidiveis-a-er-afd-todas-equivalencia
titulo: Problemas decidíveis sobre AFD e expressões regulares — A_ER (ER gera w), L_AFD = {<A> | A aceita {a,b}*}, equivalência entre AFD e ER, A_AFD, E_AFD, EQ_AFD
assunto: lfa-08-decidibilidade-parada
tipo: lista
questao: 3, 4 e 5
resolucao: sim
fonte: Lista de Teoria da Computação 2016.2 (UFAL), questões 3, 4 e 5; aula 7 das notas de Sipser (MIT), problemas decidíveis sobre AF
fontes_catalogo: ufal-lista-decidibilidade-2016-2,lee-sipser-notas-2012
autoria: Lista de Teoria da Computação da UFAL (2016.2, professor não identificado no arquivo); resolução da equipe TutorON
licenca: Não declarada (lista); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista de 2016.2, questões 3 a 5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Método:** para provar que um problema é decidível, descreva um **decisor**: uma MT que recebe a codificação $\langle \dots \rangle$, **sempre para** e responde certo. Use algoritmos já conhecidos (simulação de AFD, ER→AFN, construção de subconjuntos, minimização, teste de vazio).

**Q3. $A_{ER} = \{\langle R, w\rangle \mid R$ gera $w\}$ é decidível.** Decisor $D$, com entrada $\langle R, w\rangle$:
1. Converta $R$ num AFN $N$ (Thompson) e depois num AFD $M$ (subconjuntos). As duas conversões terminam.
2. Simule $M$ sobre $w$ (termina em $|w|$ passos).
3. Aceite se $M$ aceitar; senão, rejeite.

**Q4. $L_{AFD} = \{\langle A\rangle \mid A$ é AFD e $L(A) = \{a,b\}^*\}$ é decidível.**
1. Complete $\delta$ com um estado morto.
2. Marque os estados atingíveis a partir do inicial (busca em grafo).
3. Aceite se **todo** estado atingível é final.

Equivalente: $L(A) = \Sigma^*$ se, e só se, $\overline{L(A)} = \emptyset$ (troque os finais e teste o vazio, $E_{AFD}$).

**Q5. Equivalência de AFD e ER:** $EQ_{AFD,ER} = \{\langle A, R\rangle \mid L(A) = L(R)\}$.
1. Converta $R$ em AFD $B$.
2. Monte o AFD da **diferença simétrica** $C$, que aceita $(L(A) \cap \overline{L(B)}) \cup (\overline{L(A)} \cap L(B))$, pelo produto.
3. Teste se $L(C) = \emptyset$: aceite se for vazia.

Todos os passos terminam.

Base usada: $A_{AFD}$ (simular), $E_{AFD}$ (nenhum final atingível) e $EQ_{AFD}$ (diferença simétrica vazia) são decidíveis.

**Verificação:** os três decisores estão em `tests_acervo/lfa_verif.py` (`er_gera`, `afd_aceita_tudo`, `afd_equivale_er`) e acertam os exemplos do teste. Por exemplo: o AFD do número par de zeros é equivalente a $(1^*01^*0)^*1^*$ e não é equivalente a $(00)^*1^*$ (contraexemplo 010).
