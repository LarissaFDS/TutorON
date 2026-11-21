---
id: iec-ipv4-classe-c-mascara-broadcast
titulo: IPv4 classe C: inventar rede, endereço de máquina, broadcast e máscara
assunto: iec-10-redes-internet
tipo: prova
questao: 9
semestre: 2016.1
resolucao: sim
fonte: Fotos da Reavaliação AB2 de Introdução à Engenharia de Computação (ECOM006), UFAL, 2016.1, Q9
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

**Enunciado (Reavaliação AB2, Q9):** inventar o endereço de uma rede local (sem sub-redes) IPv4 classe C (primeiros bits 110), um endereço de máquina, o broadcast e a máscara.

**Classes do endereçamento original (RFC 791):** classe A começa com 0, B com 10 e C com **110**. Em classe C, os 3 primeiros octetos são a **rede** e o último octeto é o **host**. Primeiro octeto: de 11000000 = 192 a 11011111 = 223.

**Exemplo (escolha da equipe; qualquer rede de 192 a 223 serve):**
- Rede: **192.168.10.0** (host todo em 0). Primeiro octeto 192 = 11000000, que começa com 110.
- Máscara: **255.255.255.0** (/24): 24 bits 1 na parte de rede.
- Máquina: **192.168.10.25** (qualquer host de 1 a 254).
- Broadcast: **192.168.10.255** (host todo em 1).
- Hosts utilizáveis: $2^8-2=254$ (tira o endereço da rede e o de broadcast).

Como achar: rede = IP **AND** máscara, bit a bit; broadcast = rede **OR** (inverso da máscara).

**Verificação:** 192.168.10.25 AND 255.255.255.0 = 192.168.10.0 (a mesma rede); 192.168.10.0 OR 0.0.0.255 = 192.168.10.255; e 192 em binário começa com 110.
