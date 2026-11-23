# Curadoria — Segurança de Sistemas Computacionais

Situação: **em validação**. Revisão humana pendente em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `Ênfases/Sistemas de Informação/COMP403 -
Segurança de Sistemas Computacionais`). Há provas AB1, AB2, reposições e final de 2020.1, provas de
2020.2 (código COMP270 no cabeçalho), listas semanais 1, 2, 3, 5, 6, 8, 9, 10 e 11, slides semanais,
um modelo de política de segurança e o enunciado de um trabalho com topologia no Packet Tracer.
Algumas provas têm cabeçalho de Engenharia da Computação: a disciplina é a mesma e não foi duplicada.

**Professor não identificado** nos PDFs das provas e listas; não foi atribuído.

**Ementa não conferida.** A ementa oficial de COMP403 não estava disponível para conferência e não foi
inventada. Os tópicos vêm das provas e listas:
- requisitos de segurança e política;
- ameaças e ataques (engenharia social, Pharming, sniffing, malware, DoS, spoofing, Pentest);
- criptografia e autenticação (RSA, hash, MAC, assinatura, certificados, nonce, KDC, PPP, AAA);
- segurança em redes (SSL/TLS, IPsec, WEP, firewall).

## O que entrou
15 blocos (`materiais/s01`–`s15`), um por tópico cobrado, com os enunciados parafraseados.
As provas não têm gabarito do professor: as resoluções são da equipe TutorON.

**Só defesa e conceitos.** Nenhum bloco traz código de exploração, roteiro de ataque ou comando
para varrer ou derrubar sistemas de terceiros; o `rigor.md` diz isso. Os exemplos conferidos nos
testes são defensivos:
- RSA com primos pequenos;
- HMAC;
- desafio e resposta com nonce;
- CHAP;
- janela anti-reprodução do ESP;
- linearidade do CRC-32;
- fila de conexões semiabertas com SYN cookies;
- avaliador de regras de firewall;
- filtragem de origem (BCP 38).

Tudo está em `tests_acervo/test_disciplina_seguranca.py`.

## O que ficou de fora
- **Provas de 2020.2 respondidas:** trazem nome e matrícula de aluno e as respostas dele. Usados só
  os enunciados; nenhuma resposta nem dado pessoal foi copiado.
- **Respostas das listas:** são de aluno; não usadas.
- **Trabalho de política de segurança (Equipe 1) e arquivo `.pkt`:** trabalho avaliado de alunos;
  não versionado. O bloco de firewall explica como montar e testar regras, sem o trabalho pronto.
- **`norma1.pdf` e `norma2.pdf`:** normas técnicas protegidas; só referência (`normas-iso-27000`).
- **Slides:** baseados em Stallings e em Kurose e Ross (livros protegidos); só referência.
- **Modelo de PSI e artigo sobre roteador Cisco:** usados como evidência dos tópicos, não versionados.

## Fronteiras
Redes de Computadores (`redes`) cobre camadas, endereçamento e roteamento; aqui ficam os mecanismos de
segurança. O isolamento é testado nos dois sentidos.

## Pendências
- Revisão humana dos 15 blocos e conferência do professor.
- Conferir a ementa oficial de COMP403 antes de promover a MVP.
- Rodar as perguntas de exemplo com a IA real e conferir.
