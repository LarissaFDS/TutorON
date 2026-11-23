---
id: seguranca-ipsec-ah-esp-modo-transporte-tunel-associacao-de-seguranca-requisitos
titulo: IPsec: cabeçalho de autenticação (AH) e carga de segurança encapsulada (ESP), requisitos atendidos pelo ESP, modo transporte e modo túnel, associação de segurança (SA) e VPN
assunto: seg-04-seguranca-em-redes
tipo: prova
questao: AB2, questão 2 (ESP); Lista 11, questões 3 e 5
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
Segurança de Sistemas Computacionais (IC-UFAL), AB2, questão 2 (ESP); Lista 11, questões 3 e 5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**IPsec** protege na **camada de rede**, de forma transparente para as aplicações. É a base de muitas VPNs.

**AH (*Authentication Header*):**
- integridade e autenticação da origem de todo o datagrama, inclusive de partes do cabeçalho IP que não mudam no caminho;
- proteção contra reprodução por número de sequência;
- **sem sigilo**.

**ESP (*Encapsulating Security Payload*):** atende **confidencialidade** (cifra a carga), **integridade**, **autenticação da origem** e **proteção contra reprodução**. Com o modo túnel, também esconde parte da análise de tráfego. A autenticação do ESP não cobre o cabeçalho IP externo. Por isso o ESP é o mais usado, e o AH tem problemas com NAT.

**Diferenças principais AH × ESP** (Lista 11, questão 5):
- sigilo: só o ESP;
- cobertura da autenticação: o AH cobre o cabeçalho IP, o ESP não;
- números de protocolo: 51 para o AH e 50 para o ESP.

**Modos:**
- **transporte:** protege a carga do datagrama original, de host a host;
- **túnel:** encapsula o datagrama **inteiro** num novo datagrama IP. Usado entre roteadores ou *gateways* (VPN entre redes). É o modo mais comum com ESP.

**Associação de segurança (SA):** "conexão lógica" **simplex** entre dois pontos. Guarda:
- algoritmos e chaves;
- número de sequência;
- identificador (SPI).

São necessárias duas SAs para os dois sentidos. As SAs são **estabelecidas antes** e reaproveitadas para muitos pacotes (manualmente ou pelo IKE). Por isso, na Lista 11, questão 3 ("um novo SA para cada pacote"), a resposta é **falso**.

**Verificação:** `test_janela_anti_reproducao` implementa a janela deslizante de números de sequência do IPsec (RFC 4303): aceita fora de ordem dentro da janela, recusa repetidos e muito antigos.
