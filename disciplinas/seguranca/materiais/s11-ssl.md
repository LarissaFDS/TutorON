---
id: seguranca-protocolo-ssl-tls-camada-porta-443-handshake-registro-numero-de-sequencia
titulo: Protocolo SSL/TLS: camada na arquitetura TCP/IP, porta 443 (HTTPS), apresentação (handshake), segredo mestre, nonces, registro com MAC e número de sequência, servidor falso descoberto
assunto: seg-04-seguranca-em-redes
tipo: prova
questao: AB2 e Final, questão SSL; AB2 2020.2; Lista 11, questões 1, 2 e 4
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
Segurança de Sistemas Computacionais (IC-UFAL), AB2 e Final, questão SSL; AB2 2020.2; Lista 11, questões 1, 2 e 4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Onde fica:** entre a **camada de transporte** (TCP) e a **de aplicação**. A aplicação usa SSL/TLS como um "TCP seguro". O TLS é o sucessor padronizado do SSL, que está obsoleto. Portas conhecidas:
- **443** para HTTPS;
- 993 para IMAPS;
- 995 para POP3S;
- 465 e 587 (com STARTTLS) para SMTP.

**Serviços:** sigilo, integridade e autenticação do servidor, com autenticação do cliente opcional.

**Apresentação** (versão didática):
1. o cliente envia a lista de algoritmos e um **nonce do cliente**;
2. o servidor escolhe os algoritmos e envia o **certificado** e o seu **nonce**;
3. o cliente confere o certificado e envia o **segredo pré-mestre** cifrado com a chave pública do servidor;
4. os dois derivam o **segredo mestre** e as chaves de sessão (cifra e MAC em cada sentido) a partir do pré-mestre e dos dois nonces;
5. cada lado envia um **MAC de todas as mensagens da apresentação** (*Finished*). Se alguém alterou a lista de algoritmos, o MAC não confere.

**Nonces** (Lista 11, questão 1): impedem a reprodução de uma conexão gravada. As chaves mudam a cada conexão, então os registros antigos não se encaixam.

**Servidor falso com o certificado de outra pessoa** (Lista 11, questão 2): qualquer um pode reenviar um certificado público. Mas o falso servidor **não tem a chave privada** correspondente. Ele não consegue decifrar o segredo pré-mestre, então não deriva as mesmas chaves, e o **MAC das mensagens da apresentação** falha. É aí que o cliente descobre.

**Registro:** tipo, versão, comprimento, dados e MAC. O **número de sequência não é um campo do registro** (Lista 11, questão 4: falso). Cada lado o mantém e o inclui no cálculo do MAC, o que detecta reordenação e remoção de registros.

**Verificação:** `test_mac_com_numero_de_sequencia` simula registros com MAC sobre (número de sequência ‖ dados): a ordem certa passa e registros trocados de ordem ou repetidos são recusados, sem o número aparecer no registro.
