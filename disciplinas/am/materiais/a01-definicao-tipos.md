---
id: am-definicao-quando-usar-supervisionada-nao-supervisionada-reforco
titulo: O que é Aprendizagem de Máquina, quando existe a real necessidade de aplicá-la e os três tipos: supervisionada, não supervisionada e por reforço
assunto: am-01-fundamentos-e-kdd
tipo: prova
questao: AB1 Q1
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
status_resolucao: validada
revisao_humana: pendente
---
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), AB1 Q1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Definição:** ramo da Inteligência Artificial em que o programa **melhora seu desempenho numa tarefa com a experiência** (dados ou interação), em vez de ter todas as regras escritas à mão. Formulação clássica (Mitchell): um programa aprende com a experiência $E$ numa tarefa $T$, medida por $P$, se seu desempenho em $T$, medido por $P$, melhora com $E$.

**Quando existe a real necessidade:**
1. **não se sabe programar a solução** com regras explícitas (reconhecer rostos, filtrar spam, diagnosticar a partir de exames);
2. o **ambiente é dinâmico** e exige **adaptação** contínua (preferências de usuários, fraudes que mudam), e reprogramar à mão seria caro e lento.
Se há uma fórmula ou algoritmo conhecido e estável, não é preciso aprender.

**Três tipos:**
- **Supervisionada:** cada exemplo de treino tem a **saída desejada** (rótulo). Saída **discreta** é **classificação** (doente ou não); saída **contínua** é **regressão** (preço). Ex.: k-NN, árvores de decisão.
- **Não supervisionada:** **sem rótulos**; busca **padrões e grupos** na distribuição dos dados. Ex.: agrupamento com k-means, regras de associação.
- **Por reforço:** não há base de exemplos rotulados; um **agente interage com o ambiente**, recebe **recompensas ou penalidades** e aprende uma **política** que maximiza a recompensa acumulada. Ex.: agentes de jogos (xadrez, Go), robôs.

Diferença-chave: supervisionada aprende com respostas certas; não supervisionada, sem respostas; por reforço, com uma nota que pode vir atrasada.

**Verificação:** `test_tres_tipos_com_scikit_learn` treina um k-NN com rótulos (acerta mais de 90% na base Iris), agrupa a mesma base sem rótulos com k-means (3 grupos) e roda um Q-learning que aprende só com recompensas.
