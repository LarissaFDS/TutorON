---
id: lfa-maquina-de-turing-definicao-perguntas
titulo: Máquina de Turing — definição formal (Q, Σ, Γ, δ, q0, qaceita, qrejeita), pode escrever branco? alfabeto da fita igual ao de entrada? cabeça parada? um único estado?
assunto: lfa-06-maquinas-de-turing
tipo: lista
questao: Máquina de Turing, questão 1 (a) a (d)
resolucao: sim
fonte: Atividade teórica de Teoria da Computação 2015.1 (Prof. Thyago, UFAL), Máquina de Turing, questão 1; aula 6 das notas de Sipser (MIT)
fontes_catalogo: ufal-thyago-atividade-2015-1,lee-sipser-notas-2012
autoria: Atividade do Prof. Thyago Tenório Martins de Oliveira (UFAL); resolução da equipe TutorON
licenca: Não declarada (atividade); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: pendente_professor
revisao_humana: pendente
---
**Definição (Sipser):** $M = (Q, \Sigma, \Gamma, \delta, q_0, q_{aceita}, q_{rejeita})$.
- $\Sigma$ é o alfabeto de entrada, sem o branco $\sqcup$.
- $\Gamma$ é o alfabeto da fita, com $\sqcup \in \Gamma$ e $\Sigma \subseteq \Gamma$.
- $\delta: Q \times \Gamma \to Q \times \Gamma \times \{E, D\}$.
- $q_{aceita} \ne q_{rejeita}$.

A fita é infinita para a direita. Se a cabeça tenta ir à esquerda da primeira célula, ela fica onde está. A máquina para ao entrar em $q_{aceita}$ ou $q_{rejeita}$; ela pode não parar nunca.

Atividade 2015.1, MT, questão 1. Status da resolução: pendente_professor. A resolução é da equipe TutorON e não é gabarito do professor.
- **(a) Pode escrever o branco?** Sim: $\delta$ escreve qualquer símbolo de $\Gamma$, e $\sqcup \in \Gamma$. É assim que se apaga a fita.
- **(b) $\Gamma$ pode ser igual a $\Sigma$?** Não: $\sqcup \in \Gamma$ e $\sqcup \notin \Sigma$, então $\Gamma \ne \Sigma$ ($\Gamma$ tem ao menos um símbolo a mais).
- **(c) A cabeça pode ficar na mesma célula em dois passos seguidos?** Sim: na primeira célula, um movimento para a esquerda a deixa parada. (Em definições com movimento "fica", também.)
- **(d) Pode ter um único estado?** Na definição de Sipser, não: exige $q_{aceita} \ne q_{rejeita}$, então são ao menos dois estados.

**Pendente:** a resposta de (d) depende da definição adotada na disciplina. No livro de Menezes (Diverio e Menezes, máquinas universais), a máquina para quando não há transição e aceita por estado final. Nessa leitura, uma máquina de um só estado é possível: por exemplo, um estado inicial e final que aceita tudo sem se mover. Confirme com o professor qual definição vale na prova.

**Verificação:** as respostas (a), (b) e (c) seguem da definição; (c) também é observada no simulador `mt()` de `tests_acervo/lfa_verif.py` (cabeça na célula 0 depois de mover para a esquerda).
