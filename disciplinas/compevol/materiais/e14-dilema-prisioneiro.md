---
id: compevol-dilema-do-prisioneiro-estrategias-evoluidas-axelrod-codificacao-70-bits
titulo: Aplicação: evoluir estratégias para o dilema do prisioneiro iterado (Axelrod), codificação da estratégia por memória das três últimas jogadas, olho por olho
assunto: compevol-03-outras-metaheuristicas
tipo: exercicio_resolvido
questao: Mitchell (1995), seção do dilema do prisioneiro; apostila de Lucas, seção 7.2
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: mitchell-overview-1995,lucas-apostila-ag
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Mitchell (1995), seção do dilema do prisioneiro; apostila de Lucas, seção 7.2 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Dilema do prisioneiro:** dois jogadores escolhem **cooperar** (C) ou **trair** (D). Pagamentos usados por Axelrod (pontos do jogador da linha):

| | outro C | outro D |
|---|---|---|
| **C** | 3 | 0 |
| **D** | 5 | 1 |

Numa rodada, trair é sempre melhor individualmente, mas os dois traindo ganham 1 cada, menos que os 3 de cooperar. No jogo **iterado**, a cooperação pode compensar.

**Codificação de Axelrod:** a estratégia decide pela **memória das 3 últimas rodadas**. Cada rodada tem 4 resultados (CC, CD, DC, DD), logo $4^3 = 64$ históricos possíveis; um bit por histórico diz C ou D (**64 bits**). Mais **6 bits** para as 3 rodadas "hipotéticas" anteriores ao início: **70 bits** por cromossomo, e $2^{70}$ estratégias.

**Experimento:** a aptidão é a pontuação média contra um conjunto de estratégias (ou contra a própria população). O AG evoluiu estratégias que pontuavam como o **olho por olho** (*tit for tat*: coopera na primeira rodada e depois repete a última jogada do outro), ou melhor contra aquele conjunto fixo. Elas tinham traços parecidos: não trair primeiro, retaliar uma traição, perdoar.

**Lição:** a aptidão pode depender da **população** (coevolução); estratégias boas contra um conjunto fixo podem não ser robustas contra outros.

**Verificação:** `test_dilema_do_prisioneiro` confere $4^3 + 6 = 70$ bits e simula 200 rodadas: olho por olho contra si mesmo faz 600 pontos, sempre trair contra olho por olho faz $5 + 199 = 204$, e olho por olho perde só a primeira rodada.
