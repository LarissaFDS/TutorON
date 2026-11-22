---
id: sd_dist-definicao-exemplos-desafios-transparencia
titulo: O que é um sistema distribuído, exemplos (busca na Web, jogos online, nuvem, sistemas financeiros) e desafios: heterogeneidade, abertura, segurança, escalabilidade, falhas, concorrência e transparência
assunto: sd_dist-01-caracterizacao-e-modelos
tipo: prova
questao: AB1 de 2017 Q1
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2017
fontes_catalogo: ufal-leandro-provas-sd
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
status_resolucao: validada
revisao_humana: pendente
---
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB1 de 2017 Q1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Definição:** sistema em que componentes de hardware e software em **computadores ligados em rede** se comunicam e coordenam **apenas trocando mensagens**. Consequências: **concorrência** (vários processos ao mesmo tempo), **ausência de relógio global** e **falhas independentes** (um nó cai e os outros continuam). A motivação principal é **compartilhar recursos**.

**Exemplos (pede-se dois, com características):**
- **busca na Web**: milhares de máquinas, sistema de arquivos distribuído e processamento paralelo de grandes volumes (MapReduce) para indexar a Web;
- **jogos online massivos (MMOG)**: estado do mundo replicado ou particionado entre servidores, baixa latência para milhares de jogadores;
- **sistemas financeiros**: eventos (cotações) distribuídos a muitos interessados com ordem e confiabilidade;
- **computação em nuvem**: armazenamento e processamento oferecidos como serviço pela rede.

**Desafios:**
- **heterogeneidade** de redes, hardware, sistemas operacionais e linguagens (resolvida com protocolos e **middleware**);
- **abertura**: interfaces publicadas permitem estender o sistema;
- **segurança**: confidencialidade, integridade e disponibilidade;
- **escalabilidade**: funcionar bem com muito mais usuários e recursos;
- **tratamento de falhas**: detectar, mascarar, tolerar e recuperar;
- **concorrência** no acesso a recursos compartilhados;
- **transparência**: esconder a distribuição. Tipos: de acesso, de localização, de concorrência, de replicação, de falha, de mobilidade, de desempenho e de escala.

Evolução citada nas provas: sistemas **primitivos** (10 a 100 nós numa rede local, serviços simples como impressão e arquivos), **adaptados à Internet** (rede de redes) e **contemporâneos** (móveis, ubíquos, nuvem).

**Verificação:** `test_caracterizacao` confere que o bloco cobre a definição, quatro exemplos e os sete desafios da questão; é questão conceitual, sem código a executar.
