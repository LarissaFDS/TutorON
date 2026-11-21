---
id: lfa-lista-decidibilidade-afd-m-figura
titulo: Lista de decidibilidade 2016.2, questão 2 — pertinência de <M, 0100>, <M> em A_AFD, A_ER e L_AFD para um AFD M dado em figura (como codificar e testar)
assunto: lfa-08-decidibilidade-parada
tipo: lista
questao: 2 (a), (b) e (c)
resolucao: sim
fonte: Lista de Teoria da Computação 2016.2 (UFAL), questão 2
fontes_catalogo: ufal-lista-decidibilidade-2016-2,lee-sipser-notas-2012
autoria: Lista de Teoria da Computação da UFAL (2016.2, professor não identificado no arquivo); resolução da equipe TutorON
licenca: Não declarada (lista); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: sem_resolucao
status_resolucao: pendente_professor
revisao_humana: pendente
---
Lista de 2016.2, questão 2: dado um AFD $M$ (desenhado na lista, sobre $\{0,1\}$), dizer se (a) $\langle M, 0100\rangle$ pertence a $A_{AFD}$, (b) $\langle M\rangle$ pertence a $A_{ER}$ e (c) $\langle M\rangle$ pertence a $L_{AFD}$, justificando. Status da resolução: pendente_professor. A resolução é da equipe TutorON e não é gabarito do professor.

**Pendente:** o AFD da questão é uma figura que não veio legível no arquivo; só se leem os rótulos 0, 1 e "0, 1". Sem a tabela de transição, não dá para responder (a) nem (c). Peça ao aluno a tabela de $M$ (estados, inicial, finais, $\delta$) e confira com o professor.

O que dá para responder sem a figura:
- **(a)** $\langle M, 0100\rangle \in A_{AFD}$ se, e só se, $M$ aceita 0100. Simule: $q_0 \xrightarrow{0} \cdot \xrightarrow{1} \cdot \xrightarrow{0} \cdot \xrightarrow{0} \cdot$ e veja se o último estado é final.
- **(b)** $\langle M\rangle$ **não** pertence a $A_{ER}$, por **tipo**: $A_{ER}$ contém pares $\langle R, w\rangle$ com $R$ uma expressão regular. A codificação de um AFD sozinho não está nesse formato. Membros de uma linguagem são cadeias com o formato da codificação; cadeias mal formadas são rejeitadas pelo decisor no primeiro passo.
- **(c)** $\langle M\rangle \in L_{AFD}$ se, e só se, todo estado atingível de $M$ é final (com $\delta$ completa). Se $M$ tem algum estado atingível não final, a resposta é não. No mesmo exemplo, $L_{AFD}$ fala de $\{a,b\}^*$, mas $M$ é sobre $\{0,1\}$; confirme com o professor se a lista quis dizer $\{0,1\}^*$.

Erro comum: responder sobre $L(M)$ quando a pergunta é sobre a **codificação** $\langle M\rangle$ como palavra de uma linguagem de problemas.

**Verificação:** os decisores `afd_aceita_tudo` e a simulação de AFD de `tests_acervo/lfa_verif.py` respondem (a) e (c) assim que a tabela de $M$ for informada; sem ela, nada foi calculado.
