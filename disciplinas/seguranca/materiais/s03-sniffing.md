---
id: seguranca-packet-sniffing-modo-promiscuo-wireshark-contramedidas-criptografia
titulo: Packet Sniffing (captura de pacotes), interface em modo promíscuo, Wireshark para análise do próprio tráfego, serviços sem criptografia e contramedidas
assunto: seg-02-ameacas-e-ataques
tipo: prova
questao: AB1 2020.1, questões 3 e 4; Reposição AB1, questão 2; Lista 1, questão 3; Lista 2, questões 4 e 5; Lista 5, questão 4
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
Segurança de Sistemas Computacionais (IC-UFAL), AB1 2020.1, questões 3 e 4; Reposição AB1, questão 2; Lista 1, questão 3; Lista 2, questões 4 e 5; Lista 5, questão 4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Só defesa e conceitos: o acervo não traz roteiro de ataque nem código de exploração.

**Packet sniffing:** capturar os pacotes que passam pelo meio. É atividade normal do administrador, que usa analisadores como o Wireshark para diagnosticar a rede. Vira ameaça quando alguém captura senhas e dados que trafegam **sem criptografia**: HTTP, FTP, Telnet, POP3 e IMAP sem TLS, SNMP v1.

**Modo promíscuo:** a placa de rede normalmente entrega ao sistema só os quadros endereçados ao seu MAC (e *broadcast*). Em modo promíscuo, ela entrega **todos** os quadros que chegam. Num *hub* ou Wi-Fi aberto, isso inclui o tráfego dos outros. Num *switch*, o sniffer só vê o próprio tráfego, a menos que haja espelhamento de porta ou um ataque ao *switch*.

**Contramedidas:**
- **criptografia de ponta a ponta**: HTTPS, SSH em vez de Telnet, SFTP, IMAPS, VPN/IPsec. É a principal, porque o pacote capturado fica ilegível;
- *switches* em vez de *hubs*, com segurança de porta e VLANs;
- Wi-Fi com WPA2/WPA3, nunca WEP;
- detectar interfaces em modo promíscuo (ferramentas de detecção, IDS);
- senhas descartáveis e autenticação forte.

**Exercício de laboratório** (Lista 2, questão 5): capture **o seu próprio** tráfego na sua máquina e procure protocolos em texto aberto (DNS, HTTP). Isso mostra por que trocar por versões cifradas. Capturar tráfego de terceiros sem autorização é ilegal.

Para mapear o segmento de rede que você administra, o NMAP (portas e serviços) e o Wireshark (tráfego) se complementam: um mostra o que está aberto, o outro o que trafega.

**Verificação:** `test_texto_aberto_versus_cifrado` mostra que a senha aparece nos bytes de uma requisição HTTP sem TLS e não aparece no mesmo conteúdo cifrado (Fernet, se disponível, ou XOR com chave aleatória).
