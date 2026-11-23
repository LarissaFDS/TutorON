---
id: sd_dist-replicacao-desempenho-tolerancia-a-falhas-disponibilidade
titulo: Como a replicação melhora o desempenho e a tolerância a falhas (disponibilidade 1 − pⁿ), custos de consistência
assunto: sd_dist-03-coordenacao-e-falhas
tipo: prova
questao: AB2 de 2017 Q4
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2017
fontes_catalogo: ufal-leandro-provas-sd
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 de 2017 Q4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Desempenho:**
- **cache e réplicas perto do cliente** (CDN, réplicas regionais): menos latência;
- **divisão da carga de leitura** entre várias réplicas: mais vazão; o servidor deixa de ser gargalo;
- **download de partes de várias fontes** (BitTorrent): soma a banda de várias réplicas.
Ganho real para dados **mais lidos que escritos**; cada escrita precisa ser propagada.

**Tolerância a falhas e disponibilidade:** com $n$ réplicas que falham de forma independente, cada uma indisponível com probabilidade $p$, o serviço só fica fora se **todas** estiverem fora:
$$\text{disponibilidade} = 1 - p^{n}$$
Em palavras: um menos a probabilidade de todas as réplicas falharem ao mesmo tempo. Com $p = 0{,}05$: uma réplica dá 95%, duas dão $1 - 0{,}0025 = 99{,}75\%$, três dão $99{,}9875\%$.

Se uma réplica cai no meio de uma transferência, o cliente continua com outra (*failover*). Para tolerar falhas **bizantinas** (réplicas que respondem errado), precisa-se de $3f + 1$ réplicas para $f$ falhas e votação.

**Custo:** manter as réplicas **consistentes**. Modelos: **primário e cópias** (escritas passam pelo primário), **replicação ativa** (todas executam as mesmas requisições em ordem total) e **consistência eventual** (aceita divergência temporária, como em bancos NoSQL). Mais réplicas significam escritas mais caras e mais coordenação.

**Verificação:** `test_disponibilidade_com_replicas` calcula $1 - p^n$ para $n = 1, 2, 3$ e confere com uma simulação de Monte Carlo de 200 000 sorteios (diferença menor que 0,3 ponto percentual).
