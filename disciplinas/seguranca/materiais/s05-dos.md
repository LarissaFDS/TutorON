---
id: seguranca-negacao-de-servico-ddos-syn-flood-smurf-ping-of-death-defesas
titulo: Negação de serviço (DoS e DDoS): SYN flood e conexões semiabertas, ataque Smurf (ICMP para endereço de broadcast com origem falsificada), Ping of Death, e defesas como SYN cookies
assunto: seg-02-ameacas-e-ataques
tipo: prova
questao: AB1 2020.2, questão 2; Reposição AB2 e Final, questões 4 e 5; Lista 5
resolucao: sim
fonte: Provas (2020.1 e 2020.2) e listas semanais de Segurança de Sistemas Computacionais do IC-UFAL
curso: Ciência da Computação (UFAL), COMP403 Segurança de Sistemas Computacionais (ênfase Sistemas de Informação); provas de 2020.1 e 2020.2 (algumas com cabeçalho de Engenharia da Computação)
fontes_catalogo: ufal-seguranca-provas-listas
autoria: Questões das provas e listas da disciplina (IC-UFAL; professor não identificado nos PDFs); explicação da equipe TutorON
licenca: Não declarada (provas e listas); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Segurança de Sistemas Computacionais (IC-UFAL), AB1 2020.2, questão 2; Reposição AB2 e Final, questões 4 e 5; Lista 5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Só defesa e conceitos: o acervo não traz roteiro de ataque nem código de exploração.

**DoS × DDoS:** a negação de serviço esgota um recurso (banda, CPU, memória, tabela de conexões) para que usuários legítimos não sejam atendidos. **DDoS** usa muitas máquinas ao mesmo tempo, normalmente uma *botnet* de computadores infectados.

**SYN flood:** abusa do *handshake* de três vias do TCP (SYN → SYN-ACK → ACK). O atacante envia muitos SYN com origem falsa e nunca manda o ACK. Cada pedido ocupa uma entrada na **fila de conexões semiabertas** até expirar. Com a fila cheia, clientes legítimos são recusados.

Defesas contra SYN flood:
- **SYN cookies**: o servidor não guarda estado e codifica a informação no número de sequência do SYN-ACK;
- fila maior e *timeout* menor;
- limitar a taxa de SYN no *firewall*;
- serviços de mitigação.

**Smurf:** envia ICMP *echo request* ao **endereço de broadcast** de uma rede intermediária, com a origem **falsificada** como o IP da vítima. Todas as máquinas respondem à vítima, e cada pacote vira $N$ respostas (amplificação). É um ataque de rede, não um cavalo de Troia.

Defesas contra Smurf:
- roteadores **não encaminham broadcast direcionado** (padrão desde a RFC 2644);
- hosts não respondem a *echo* para broadcast;
- filtragem de origem falsificada na borda (BCP 38).

**Ping of Death:** pacote ICMP fragmentado que, remontado, passa de 65 535 bytes e estourava o *buffer* de sistemas antigos. Defesa: pilha TCP/IP corrigida, que verifica o tamanho na remontagem.

**Verificação:** `test_fila_semiaberta_syn_flood` simula uma fila de tamanho fixo: SYNs sem ACK a enchem e bloqueiam o cliente legítimo, e com SYN cookies (sem estado) ele é atendido; `test_amplificacao_smurf` confere que 1 pedido a um broadcast com $N$ hosts gera $N$ respostas à vítima.
