---
id: redes-dns-resolucao-iterativa-registro-mx
titulo: Serviço DNS: para que serve, resolução de www.ic.ufal.br (servidor local, raiz, TLD .br, autoritativo, cache e TTL) e como um servidor de e-mail descobre o servidor MX do destinatário
assunto: redes-02-aplicacao
tipo: prova
questao: prova AB1 2020.1 Q3 e Q2 (PLE); final 2020.1 Q3; reposição AB1 2020.1 Q2; provas de 2012 e 2017
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
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), prova AB1 2020.1 Q3 e Q2 (PLE); final 2020.1 Q3; reposição AB1 2020.1 Q2; provas de 2012 e 2017 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Para que serve:** traduzir nomes (`www.ic.ufal.br`) em endereços IP, e também dar apelidos (CNAME), servidores de e-mail (MX) e distribuir carga. É um banco de dados **distribuído e hierárquico**: raiz, domínios de topo (`.br`), domínios autoritativos (`ufal.br`). Usa UDP na porta 53.

**Resolução de `www.ic.ufal.br`:**
1. A aplicação pede ao *resolver* do sistema, que pergunta ao **servidor DNS local** (do provedor ou da instituição), em consulta **recursiva**: "me dê a resposta final".
2. Sem a resposta em cache, o servidor local faz consultas **iterativas**: a um servidor **raiz**, que indica os servidores do **TLD `.br`**; esses indicam os servidores **autoritativos de `ufal.br`** (ou de `ic.ufal.br`, se houver delegação), que respondem o registro **A** com o IP.
3. O servidor local guarda as respostas em **cache** pelo **TTL** de cada registro e devolve o IP. Próximas consultas não passam pela raiz.

**E-mail para `gates@microsoft.com` saindo de `aluno@ic.ufal.br`:** o servidor SMTP do remetente consulta no DNS o registro **MX de `microsoft.com`**. A resposta lista os nomes dos servidores de correio com uma **preferência** (menor número = tentar primeiro). Ele resolve o nome escolhido para IP (registro A ou AAAA) e abre uma conexão TCP na **porta 25**, onde entrega a mensagem por SMTP. Se o primeiro falhar, tenta o de preferência seguinte.

Erros comuns: dizer que o computador do usuário consulta a raiz diretamente; confundir o registro MX (nome do servidor de correio) com o endereço IP.

**Verificação:** `test_dns_iterativo` simula a hierarquia (raiz → `.br` → `ufal.br`) com dicionários: o servidor local segue as indicações até o registro A, guarda em cache (a segunda consulta não toca a raiz) e o MX de maior prioridade é o de menor número.
