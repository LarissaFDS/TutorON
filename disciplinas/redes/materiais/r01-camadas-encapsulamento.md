---
id: redes-camadas-tcpip-encapsulamento-pdu
titulo: As 5 camadas da pilha TCP/IP e suas funções, por que organizar em camadas, encapsulamento e cabeçalhos — mensagem, segmento, datagrama e quadro
assunto: redes-01-camadas-encapsulamento
tipo: prova
questao: AB1 2017 Q1-Q2; AB1 2020.1 Q1 e Q5; reposição AB1 2020.1 Q5; finais
resolucao: sim
fonte: Provas AB1 de 2017 e 2020.1, reposição e provas finais de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Redes de Computadores 1 (COMP — Prof. Leandro Melo de Sales); provas de 2017 a 2020.1
fontes_catalogo: ufal-leandro-provas-redes
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), AB1 2017 Q1-Q2; AB1 2020.1 Q1 e Q5; reposição AB1 2020.1 Q5; finais (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**As 5 camadas (de cima para baixo), com a unidade de dados de cada uma:**
1. **Aplicação** — protocolos das aplicações (HTTP, SMTP, DNS, FTP); unidade: **mensagem**.
2. **Transporte** — comunicação processo a processo (portas); TCP (confiável, orientado a conexão, controle de fluxo e de congestionamento) ou UDP (sem conexão, melhor esforço); unidade: **segmento**.
3. **Rede** — leva o pacote de um hospedeiro a outro, atravessando roteadores: endereçamento IP e roteamento; unidade: **datagrama**.
4. **Enlace** — leva o quadro de um nó ao vizinho no mesmo enlace (Ethernet, Wi-Fi): endereço MAC, detecção de erros, acesso ao meio; unidade: **quadro**.
5. **Física** — bits no meio (cabo, fibra, rádio).

**Por que camadas:** cada camada usa só o serviço da de baixo e oferece serviço à de cima. Isso divide um problema grande, permite trocar a implementação de uma camada sem mexer nas outras (Wi-Fi no lugar de Ethernet, sem mudar o HTTP) e padroniza as interfaces.

**Encapsulamento:** ao descer, cada camada põe o seu **cabeçalho** na frente do que recebeu: mensagem → segmento (cabeçalho com as portas) → datagrama (cabeçalho com os IPs) → quadro (cabeçalho com os MACs e um campo de verificação no fim). Ao subir, cada camada lê e retira o seu cabeçalho e entrega a carga à camada certa. O cabeçalho serve para isso: guarda o que a camada par do outro lado precisa (endereços, portas, números de sequência, tipo do conteúdo, verificação de erro).

Analogia aceita pelo professor: carta dentro de envelope, dentro de malote, dentro de caminhão.

Erro comum: listar as 7 camadas OSI quando a pergunta pede as 5 da pilha da Internet.

**Verificação:** `test_encapsulamento` monta com `struct` um quadro com cabeçalhos Ethernet, IPv4 e UDP em volta de uma mensagem, desencapsula camada por camada e confere que cada cabeçalho indica a camada de cima (tipo 0x0800 = IPv4, protocolo 17 = UDP, porta de destino).
