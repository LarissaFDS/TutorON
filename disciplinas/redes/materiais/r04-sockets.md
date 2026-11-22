---
id: redes-sockets-bind-listen-accept-cliente-servidor-p2p
titulo: Sockets: o que são, o que define um socket, bind, listen e accept e os erros que emitem, servidor com várias conexões simultâneas, cliente/servidor × P2P
assunto: redes-03-sockets-multiplexacao
tipo: prova
questao: prova 1 2012 Q3; AB1 2017 Q4; AB1 2020.1 Q4 (duas versões); final 2020.1 Q2 e Q8
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
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), prova 1 2012 Q3; AB1 2017 Q4; AB1 2020.1 Q4 (duas versões); final 2020.1 Q2 e Q8 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Socket** é a porta entre o processo de aplicação e a camada de transporte: o programa escreve e lê nele, e o sistema operacional cuida do resto. Fica definido por **protocolo de transporte** (TCP ou UDP), **endereço IP** e **número de porta**; uma conexão TCP é identificada pelos quatro valores (IP e porta de origem, IP e porta de destino).

**Servidor TCP, passo a passo (Python, mesma API de C e Java):**
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 5000))   # associa IP e porta
s.listen()                   # passa a aceitar pedidos de conexão
conn, addr = s.accept()      # bloqueia; devolve um socket NOVO por cliente
```
- `bind`: erro se a porta já está em uso (`EADDRINUSE`) ou se falta permissão (portas abaixo de 1024 em Unix);
- `listen`: erro se o socket não foi associado ou é UDP;
- `accept`: bloqueia; pode falhar se o socket for fechado ou a chamada interrompida;
- no cliente, `connect` a uma porta sem servidor dá **conexão recusada**.

**Várias conexões simultâneas:** o socket de escuta só recebe pedidos; cada `accept` devolve um socket próprio da conexão. Atenda cada um numa **thread** (ou com `select`) e volte ao `accept`.

**Cliente/servidor × P2P:** no cliente/servidor há um servidor sempre ligado, com endereço fixo, e os clientes não falam entre si. No P2P (BitTorrent), pares intermitentes são clientes e servidores ao mesmo tempo, e a capacidade cresce com o número de pares (autoescalável), mas é mais difícil de gerenciar e proteger.

**Verificação:** `test_sockets` cria um servidor em localhost com uma thread por conexão, atende dois clientes ao mesmo tempo, confere que um segundo `bind` na mesma porta falha e que `connect` numa porta sem servidor é recusado.
