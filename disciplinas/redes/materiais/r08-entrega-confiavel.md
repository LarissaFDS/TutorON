---
id: redes-tcp-entrega-confiavel-go-back-n-retransmissao-seletiva
titulo: Como o TCP garante entrega confiável sobre o IP não confiável — temporizador, ACK, retransmissão, Go-Back-N × retransmissão seletiva, retransmissão rápida com 3 ACKs duplicados
assunto: redes-04-transporte-tcp
tipo: prova
questao: final 2020.1 Q5; reposição AB2 2020.1 Q3
resolucao: sim
fonte: Prova final e reposição da AB2 de 2020.1 de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Redes de Computadores 1 (COMP — Prof. Leandro Melo de Sales); provas de 2020.1
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
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), final 2020.1 Q5; reposição AB2 2020.1 Q3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**A abordagem:** o IP pode perder, duplicar, atrasar ou embaralhar datagramas. O TCP constrói um canal confiável com:
- **soma de verificação** para detectar segmentos corrompidos (são descartados);
- **números de sequência** para ordenar e descartar duplicatas;
- **ACKs cumulativos** do receptor;
- **temporizador**: sem ACK até o *timeout*, o emissor **retransmite**;
- **janela deslizante** (*pipeline*): vários segmentos em trânsito sem esperar cada ACK.

**Go-Back-N (GBN):** o receptor só aceita em ordem e manda ACK cumulativo; ao estourar o temporizador do mais antigo, o emissor retransmite **ele e todos os seguintes já enviados**. Simples, mas desperdiça banda com uma perda.

**Retransmissão seletiva (SR):** o receptor guarda os segmentos fora de ordem e confirma **cada um**; o emissor tem um temporizador por segmento e retransmite **só o perdido**.

**O TCP é um meio-termo:** ACK cumulativo como o GBN, mas o receptor costuma guardar segmentos fora de ordem e o emissor retransmite **só o mais antigo não confirmado**, com um único temporizador. **Retransmissão rápida:** 3 ACKs duplicados indicam perda e ele retransmite sem esperar o *timeout*. A opção **SACK** informa os blocos recebidos, aproximando-o da SR.

Exemplo com janela 4 e perda do segmento 2 (de 0 a 5): o GBN reenvia 2, 3, 4 e 5; a SR reenvia só o 2.

**Verificação:** `test_go_back_n_e_seletiva` simula os dois protocolos com perda de um segmento e confere quantas retransmissões cada um faz (4 no GBN, 1 na SR, no exemplo) e que o receptor entrega tudo em ordem nos dois.
