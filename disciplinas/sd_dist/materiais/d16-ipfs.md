---
id: sd_dist-ipfs-enderecamento-por-conteudo-cid-dag-de-merkle-dht
titulo: Características do IPFS (InterPlanetary File System): endereçamento por conteúdo, CID, DAG de Merkle, DHT e troca de blocos
assunto: sd_dist-04-tecnologias
tipo: prova
questao: AB2 2020.1 Q6
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2020.1
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 2020.1 Q6 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**IPFS (InterPlanetary File System):** sistema de arquivos **P2P** com **endereçamento por conteúdo**: cada arquivo (em blocos) é identificado por um **CID**, derivado do **hash do conteúdo**, e não por onde está. Os blocos formam um **DAG de Merkle** (estrutura com deduplicação e verificação de integridade). Uma **DHT** (Kademlia) diz quais pares têm cada CID, e a troca de blocos (Bitswap) lembra o BitTorrent. Conteúdo igual tem o mesmo CID; mudou o conteúdo, mudou o CID. Por padrão, é público.

Diferença para o endereçamento por **localização** (HTTP): uma URL diz **onde** buscar e quebra se o servidor sai do ar; um CID diz **o quê**, e qualquer par que tenha o conteúdo pode servi-lo, com integridade conferida pelo próprio hash.

**Verificação:** `test_enderecamento_por_conteudo` confere com `hashlib` que conteúdos iguais têm o mesmo endereço SHA-256, que mudar um byte muda o endereço e que uma árvore de Merkle detecta o bloco alterado.
