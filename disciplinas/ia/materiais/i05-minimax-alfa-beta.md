---
id: ia-arvore-de-jogos-minimax-poda-alfa-beta-funcao-de-avaliacao-antecipacao-limitada-horizonte
titulo: Árvores de jogos: soma zero, função de avaliação, minimax, antecipação limitada e efeito horizonte, poda alfa-beta
assunto: ia-02-busca-e-jogos
tipo: material_estudo
questao: slide 06 (Árvore de Jogos: Minimax e Poda Alfa-Beta)
resolucao: sim
fonte: Slides de Inteligência Artificial do Prof. Jacson R. C. Silva (Departamento de Computação, CCA-UFES), usados na turma da UFAL
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufes-jeiks-slides
autoria: Slides do Prof. Jacson R. C. Silva (UFES), usados como material da turma da UFAL; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), slide 06 (Árvore de Jogos: Minimax e Poda Alfa-Beta) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Árvore de jogo:** a raiz é o estado inicial, os níveis alternam as jogadas de **MAX** e **MIN** e as folhas são estados finais. Jogos de **soma zero** (vitória 1, empate 0, derrota −1), sem acaso e com informação completa.

**Função de avaliação** (avaliador estático): estima o valor de uma posição quando não dá para ir até as folhas. Costuma ser linear ponderada; no xadrez, $9r + 5t + 3c + 3b + p$ (rainhas, torres, cavalos, bispos, peões).

**Minimax:**
$$\text{MINIMAX}(n)=\begin{cases}\text{UTILIDADE}(n) & n \text{ terminal}\\ \max_s \text{MINIMAX}(s) & n \text{ é MAX}\\ \min_s \text{MINIMAX}(s) & n \text{ é MIN}\end{cases}$$
Em palavras: MAX escolhe o maior valor supondo que MIN joga de forma ótima (pior caso para MAX).

**Exemplo:** MAX na raiz com três nós MIN de folhas (3, 12, 8), (2, 4, 6) e (14, 5, 2). Os MIN valem 3, 2 e 2; a raiz vale **3**.

**Antecipação limitada:** corta a busca numa profundidade fixa e usa uma heurística, por exemplo no jogo da velha $H(n) = X(n) - O(n)$ (linhas ainda abertas para X menos as abertas para O). Risco: **efeito horizonte**.

**Poda alfa-beta:** $\alpha$ é o melhor valor já garantido para MAX e $\beta$ para MIN; corta-se quando $\alpha \ge \beta$. No exemplo, depois da folha 2 do segundo nó MIN (valor $\le 2 < 3$), as folhas 4 e 6 **são podadas**. O resultado é igual ao do minimax; com boa ordenação, o custo cai de $O(b^d)$ para cerca de $O(b^{d/2})$.

**Verificação:** `test_minimax_alfa_beta` confere o valor 3 da raiz e que a poda deixa de visitar as folhas 4 e 6.
