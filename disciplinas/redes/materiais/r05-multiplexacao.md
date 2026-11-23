---
id: redes-multiplexacao-demultiplexacao-portas-campo-protocolo
titulo: Multiplexação e demultiplexação entre aplicação e transporte (portas, 4-tupla do TCP) e entre transporte e rede (campo Protocolo do IPv4: 6 TCP, 17 UDP); o que TCP e UDP têm em comum
assunto: redes-03-sockets-multiplexacao
tipo: prova
questao: prova 1 2012 Q2; AB1 2020.1 Q5; AB2 2017 Q1; AB2 2020.1 Q1; finais
resolucao: sim
fonte: Provas de 2012, 2017 e 2020.1 de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Redes de Computadores 1 (COMP — Prof. Leandro Melo de Sales); provas de 2012, 2017 e 2020.1
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
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), prova 1 2012 Q2; AB1 2020.1 Q5; AB2 2017 Q1; AB2 2020.1 Q1; finais (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Aplicação ↔ transporte.** **Multiplexar** (no emissor): juntar os dados que vêm de vários sockets, pôr em cada segmento o cabeçalho com **porta de origem e de destino** e passar tudo à camada de rede. **Demultiplexar** (no receptor): olhar o cabeçalho e entregar cada segmento ao socket certo.
- **UDP**: o socket é achado por (IP de destino, porta de destino). Dois remetentes diferentes para a mesma porta caem no mesmo socket.
- **TCP**: o socket é achado pela **4-tupla** (IP e porta de origem, IP e porta de destino). Por isso um servidor web na porta 80 tem um socket separado para cada cliente.

**Transporte ↔ rede.** O datagrama IPv4 tem o campo **Protocolo** (8 bits), que diz a quem entregar a carga: **6 = TCP**, **17 = UDP**, 1 = ICMP. Ao receber, a camada de rede retira o cabeçalho IP e usa esse campo para entregar ao TCP ou ao UDP. (No IPv6 é o campo *Next Header*.)

**O que TCP e UDP têm em comum (prova de 2012):** justamente a **multiplexação/demultiplexação por portas**, além da **soma de verificação** (*checksum*) no cabeçalho. Todo o resto (conexão, entrega confiável, ordem, controle de fluxo e de congestionamento) é só do TCP.

Erros comuns: dizer que o UDP não usa portas; esquecer que, no TCP, o IP e a porta de **origem** também escolhem o socket.

**Verificação:** `test_multiplexacao` abre dois sockets UDP em portas diferentes e confere que cada um recebe só o que foi enviado à sua porta; dois clientes TCP na mesma porta do servidor ganham sockets distintos (4-tuplas diferentes); `socket.IPPROTO_TCP` e `socket.IPPROTO_UDP` valem 6 e 17.
