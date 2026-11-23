---
id: redes-tcp-numero-sequencia-reconhecimento-cumulativo-byte-stream
titulo: TCP: para que servem os números de sequência e de reconhecimento, reconhecimento cumulativo (seq 88 com 8 bytes → ACK 96), por que o TCP é byte-stream, serviços do TCP
assunto: redes-04-transporte-tcp
tipo: prova
questao: AB2 2020.1 Q2; reposição AB1 2020.1 Q4; AB1 2017 Q9; final 2017 Q4
resolucao: sim
fonte: Provas de 2017 e 2020.1 de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Redes de Computadores 1 (COMP — Prof. Leandro Melo de Sales); provas de 2017 e 2020.1
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
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), AB2 2020.1 Q2; reposição AB1 2020.1 Q4; AB1 2017 Q9; final 2017 Q4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Byte-stream:** o TCP entrega à aplicação um **fluxo contínuo de bytes**, sem fronteiras de mensagem. Dois `send` de 5 bytes podem chegar num único `recv` de 10, e um `send` de 10 pode chegar em pedaços. Quem precisa de mensagens marca as fronteiras no protocolo da aplicação (tamanho no início, delimitador).

**Número de sequência:** posição, no fluxo, do **primeiro byte** de dados do segmento (começa num valor aleatório escolhido no *handshake*). **Número de reconhecimento (ACK):** o **próximo byte que o receptor espera**.

Exemplo: chega um segmento com seq = 88 e 8 bytes de dados (bytes 88 a 95). O receptor responde ACK = **96**.

**Reconhecimento cumulativo:** ACK = n confirma **todos** os bytes até n − 1. Se chegam os bytes 88–95 e 104–111, mas não 96–103, o receptor continua mandando ACK = 96 (ACK duplicado), mesmo tendo os bytes de 104 a 111.

Para que servem: detectar perdas e duplicatas, reordenar e confirmar. São a base da entrega confiável e do controle de fluxo.

**Serviços do TCP (questão de 2017):** conexão **ponto a ponto** (não multiponto), entrega garantida e **em ordem**, controle de fluxo, controle de congestionamento, multiplexação, **full-duplex** e envio em **pipeline** (vários segmentos sem esperar ACK). O TCP **não garante banda** nem atraso. Na questão de múltipla escolha, a alternativa completa é a que lista esses itens, sem "multiponto" e sem "garantia de banda".

**Verificação:** `test_sequencia_e_ack` simula um receptor com ACK cumulativo (88 + 8 → 96; com buraco, ACK duplicado 96 até o buraco ser preenchido, então salta para 112) e confere com um socket TCP em localhost que um `send` de 10 bytes lido com `recv(4)` vem em pedaços.
