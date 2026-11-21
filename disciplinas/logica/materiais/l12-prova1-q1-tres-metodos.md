---
id: logica-prova1-q1-tres-metodos
titulo: Prova 1 (2013), questão 1: (¬P → Q) ∧ (Q ∨ R) ∧ (R ∨ W) ∧ (R → ¬P) ∧ (W → ¬Q) ⊨ Q ∧ R por equivalências, tableau e resolução
assunto: logica-06-resolucao-proposicional
tipo: prova
resolucao: sim
questao: 1
fonte: Prova 1 de Lógica Aplicada à Computação, 15/05/2013 (Profs. Evandro Costa e Baldoino Fonseca, UFAL), questão 1
fontes_catalogo: ufal-baldoino-prova1-2013
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questão de prova (paráfrase do enunciado) com resolução. Prova é atividade avaliativa: o tutor guia, não entrega. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Enunciado (paráfrase):** verificar se $(\neg P\to Q)\land(Q\lor R)\land(R\lor W)\land(R\to\neg P)\land(W\to\neg Q)\models Q\land R$ (a) por um dos teoremas de consequência lógica, com equivalências; (b) por tableau; (c) por resolução, mostrando as cláusulas e a refutação.

**Resposta: a consequência é válida.**

**(a) Teorema T2:** basta mostrar que as premissas com $\neg(Q\land R)$ são insatisfazíveis. Reescrevendo por equivalências ($A\to B\equiv\neg A\lor B$, De Morgan), obtém-se a CNF abaixo, e as passagens do item (c) são equivalências e cortes que chegam a $\bot$.

**(b) Tableau** de premissas e $\neg(Q\land R)$, ramificando em $\neg Q\mid\neg R$. Ramo $\neg Q$: $Q\lor R$ força $R$; $R\to\neg P$ força $\neg P$; $\neg P\to Q$ abre $P$ (fecha com $\neg P$) ou $Q$ (fecha com $\neg Q$). Ramo $\neg R$: $Q\lor R$ força $Q$; $R\lor W$ força $W$; $W\to\neg Q$ abre $\neg W$ (fecha) ou $\neg Q$ (fecha). Todos os ramos fecham.

**(c) Cláusulas:** $\neg P\to Q$ vira $\{P,Q\}$; $R\to\neg P$ vira $\{\neg R,\neg P\}$; $W\to\neg Q$ vira $\{\neg W,\neg Q\}$; $\neg(Q\land R)$ vira $\{\neg Q,\neg R\}$. Refutação: 1. $\{P, Q\}$; 2. $\{Q, R\}$; 3. $\{R, W\}$; 4. $\{\neg R, \neg P\}$; 5. $\{\neg W, \neg Q\}$; 6. $\{\neg Q, \neg R\}$; 7. $\{R, \neg Q\}$ (3, 5); 8. $\{\neg Q\}$ (6, 7); 9. $\{R\}$ (2, 8); 10. $\{\neg P\}$ (4, 9); 11. $\{Q\}$ (1, 10); 12. $\square$ (8, 11).

**Verificação:** tabela-verdade das 16 valorações (nenhuma satisfaz premissas e nega $Q\land R$), cada resolvente recalculado e cada ramo do tableau conferido em Python.
