---
id: iec-redes-tcpip-www-dns
titulo: Internet: camadas TCP/IP, protocolos (IP, TCP, UDP, HTTP, FTP), tecnologias da WWW e DNS
assunto: iec-10-redes-internet
tipo: prova
questao: 1, 2, 3, 7, 8
semestre: 2016.1
resolucao: sim
fonte: Fotos da Reavaliação AB2 de Introdução à Engenharia de Computação (ECOM006), UFAL, 2016.1, Q1, 2, 3, 7, 8
fontes_catalogo: ufal-iec-reav-ab2-2016
autoria: Enunciados: reavaliação da disciplina (professor não identificado na prova), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Camadas do modelo TCP/IP** (de cima para baixo) e protocolos:
- **Aplicação:** HTTP (transferência de hipertexto), FTP (arquivos), SMTP (e-mail), DNS (nomes).
- **Transporte:** TCP (com conexão, confiável, ordenado) e UDP (sem conexão, sem garantia de entrega).
- **Rede (internet):** IP, responsável pelo **endereçamento, roteamento e encaminhamento** de pacotes entre redes.
- **Enlace/física:** Ethernet, Wi-Fi; o ARP traduz endereço IP em endereço físico (MAC).

**Questões (Reavaliação AB2):**
- Q1: as três tecnologias essenciais da WWW: **HTML** (linguagem das páginas), **URL** (endereço do recurso) e **HTTP** (protocolo de transferência).
- Q2: UDP, TCP e FTP ficam em Transporte, Transporte e Aplicação: alternativa **(D)**.
- Q3: roteamento e encaminhamento de pacotes: camada de **rede** (internet), protocolo IP.
- Q7: o **DNS** traduz nomes de domínio em endereços IP (e o inverso), num banco de dados **distribuído e hierárquico** (raiz, domínios de topo, servidores autoritativos); também guarda apelidos (CNAME) e servidores de e-mail (MX) e pode distribuir carga entre vários IPs.
- Q8: roteamento, transporte e hipertexto: **IP, TCP e HTTP**, alternativa **(A)**. Cuidado: HTML é linguagem de marcação, não protocolo; FTP transfere arquivos; ARP não roteia.

**Verificação:** em cada alternativa marcada, confira a camada de cada protocolo na lista acima: UDP e TCP só em transporte, FTP e HTTP só em aplicação, IP só em rede.
