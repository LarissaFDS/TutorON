---
id: redes-janela-congestionamento-partida-lenta-tahoe-reno
titulo: Janela de congestionamento do TCP — partida lenta (dobra a cada rodada até o threshold), prevenção de congestionamento (+1 por rodada), perda: Tahoe volta a 1, Reno à metade; a figura das rodadas 1 a 15
assunto: redes-05-congestionamento
tipo: prova
questao: AB1 2017 Q7; AB2 2020.1 Q3; final 2020.1 Q4
resolucao: sim
fonte: Provas de 2017 e 2020.1 de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL); figura das fases do controle de congestionamento
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
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), AB1 2017 Q7; AB2 2020.1 Q3; final 2020.1 Q4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Para que serve a cwnd:** limita quantos segmentos o emissor pode ter sem confirmação; a taxa é cerca de cwnd/RTT (janela por tempo de ida e volta). Crescendo e diminuindo a cwnd, o TCP procura a banda disponível.

**Fases (figura da prova; janela em segmentos, por rodada):**
- **Partida lenta:** começa com cwnd = 1 e **dobra** a cada rodada (+1 por ACK): 1, 2, 4, 8. Ao chegar ao **threshold** (`ssthresh`, 8 na figura), passa à fase seguinte.
- **Prevenção de congestionamento:** cresce **1 segmento por rodada** (aumento aditivo): 9, 10, 11, 12.
- **Perda na rodada 8, com cwnd = 12:** o novo threshold é a metade, **6**.
  - **TCP Tahoe:** cwnd volta a **1** e refaz a partida lenta (1, 2, 4) até o novo threshold e então cresce linear: 1, 2, 4, 6, 7, 8, 9 nas rodadas 9 a 15.
  - **TCP Reno** (perda detectada por 3 ACKs duplicados, recuperação rápida): cwnd cai para o **novo threshold, 6**, e segue linear: 6, 7, …, 12.

O "dente de serra" da outra figura (sobe linear, cai à metade) é o **AIMD** (aumento aditivo, diminuição multiplicativa) do Reno em regime. Um *timeout* leva cwnd a 1 também no Reno.

Erro comum: dizer que a partida lenta é "lenta" no crescimento; ela é exponencial. O nome vem de começar com 1.

**Verificação:** `test_tahoe_e_reno` simula as duas variantes com threshold 8 e perda na rodada 8 e reproduz as duas curvas da figura rodada a rodada (Tahoe 1, 2, 4, 6, 7, 8, 9 e Reno 6 a 12 nas rodadas 9 a 15).
