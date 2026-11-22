---
id: sd_dist-blockchain-prova-de-trabalho-gasto-duplo-ipfs-enderecamento-por-conteudo
titulo: O que é uma blockchain e que problema resolve (gasto duplo sem autoridade central), prova de trabalho (Proof-of-Work) e sua importância; características do IPFS (endereçamento por conteúdo, CID, DHT)
assunto: sd_dist-04-tecnologias
tipo: prova
questao: AB2 2020.1 Q2 e Q6; AB2 2020.2
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2020.1 e 2020.2
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 2020.1 Q2 e Q6; AB2 2020.2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Blockchain:** registro (*ledger*) **replicado** entre muitos nós, formado por **blocos encadeados por hash**: cada bloco guarda o hash do anterior, e mudar um bloco antigo muda todos os hashes seguintes. É um livro-razão **só de acréscimo**, sem dono.

**Problema que resolve:** fazer nós que **não confiam uns nos outros**, sem autoridade central, **concordarem sobre a ordem das transações**. No dinheiro digital, isso é o **gasto duplo**: sem um banco, como impedir que a mesma moeda seja gasta duas vezes? A blockchain resolve com consenso sobre uma única história. (A resposta que só fala de "rastrear informações" e "contratos inteligentes" perdeu meio ponto em 2020.2.)

**Prova de trabalho (PoW):** para propor um bloco, o nó precisa achar um **nonce** tal que o hash do bloco fique **abaixo de um alvo** (na prática, começa com um certo número de zeros). Achar custa muitas tentativas; **conferir custa um hash**. Importância:
- **consenso** em rede aberta: vale a cadeia com **mais trabalho acumulado**;
- **resistência a ataques Sybil**: criar identidades falsas não dá votos, só poder de cálculo dá;
- **imutabilidade**: reescrever um bloco exige refazer o trabalho dele e de todos os seguintes, mais rápido que o resto da rede (seria preciso mais de 50% do poder de cálculo).
Custo: enorme gasto de energia; por isso surgiram alternativas como a prova de participação (*Proof-of-Stake*).

**Verificação:** `test_prova_de_trabalho` minera com `hashlib` um bloco com 4 zeros hexadecimais iniciais, confere que verificar é um único hash e que alterar uma transação invalida o bloco e o encadeamento seguinte.
