---
id: am-aprendizagem-por-reforco-q-learning-exploracao-explotacao-equacao
titulo: Como funciona a aprendizagem por reforço e o Q-learning: agente, ambiente, recompensa, política, retorno atrasado, dilema exploração × explotação e regra de atualização de Q
assunto: am-04-reforco
tipo: prova
questao: AB2 Q4 (2021.1)
resolucao: sim
fonte: Provas de Aprendizagem de Máquina do Prof. Aydano Machado (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Aprendizagem de Máquina (COMP390); provas AB1 e AB2 (uma delas de 2021.1)
fontes_catalogo: ufal-aydano-provas-am
autoria: Questões do Prof. Aydano Machado (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), AB2 Q4 (2021.1) (enunciados parafraseados). Status da resolução: corrigida (a fórmula da resposta da turma foi corrigida). A resolução é da equipe TutorON e não é gabarito do professor.

**Aprendizagem por reforço:** um **agente** observa o **estado** $s$, escolhe uma **ação** $a$, o **ambiente** devolve uma **recompensa** $r$ e o próximo estado $s'$. O objetivo é uma **política** $\pi(s)$ que maximize o **retorno descontado** $\sum_t \gamma^t r_t$ (fator de desconto $0 \le \gamma < 1$). Não há exemplos rotulados nem modelo completo do ambiente.

Dois pontos centrais:
- **retorno atrasado** (atribuição de crédito): a ação boa pode só render no fim; buscar o melhor imediato pode prender o agente num ótimo local;
- **exploração × explotação:** testar ações novas para descobrir algo melhor ou usar o que já se sabe. Solução usual: **$\varepsilon$-gulosa** (com probabilidade $\varepsilon$, ação aleatória; senão, a de maior $Q$).

**Q-learning:** aprende a função valor-ação $Q(s, a)$, o retorno esperado de fazer $a$ em $s$ e agir bem depois, e converge para $Q^*$ (com exploração suficiente e taxa de aprendizado decrescente).
1. inicialize $Q(s, a)$ arbitrariamente (zeros);
2. em cada episódio, a partir do estado inicial, repita até o estado final: escolha $a$ pela política $\varepsilon$-gulosa, execute, observe $r$ e $s'$ e atualize
$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$
Em palavras: some a $Q$ uma fração $\alpha$ (taxa de aprendizado) do **erro de diferença temporal**: a recompensa mais o desconto vezes o **melhor** $Q$ do próximo estado, menos o $Q$ atual. A fórmula da resposta da turma ("retorno + diferença entre $Q$ atual e $Q$ do próximo estado") **omitia $\gamma$ e o máximo**: está **corrigida** aqui.
3. política final: $\pi(s) = \arg\max_a Q(s, a)$.

**Verificação:** `test_q_learning_corredor` treina Q-learning num corredor de 5 casas (recompensa 1 na última), com semente fixa: a política aprendida é "direita" em todo estado, e $Q$ do estado anterior ao final converge para 1 e o de duas casas antes para $\gamma$.
