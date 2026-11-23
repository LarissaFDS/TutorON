---
id: seguranca-firewall-filtro-de-pacotes-gateway-de-aplicacao-proxy-estado-regras-dmz
titulo: Firewalls: filtro de pacotes (por endereço, porta e protocolo), filtro com estado, gateway de nível de aplicação (proxy), ordem das regras, negação por padrão e DMZ
assunto: seg-04-seguranca-em-redes
tipo: prova
questao: Reposição AB2, questão 2; Material da semana 12; trabalho com topologia no Packet Tracer (AB2 2020.2)
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
Segurança de Sistemas Computacionais (IC-UFAL), Reposição AB2, questão 2; Material da semana 12; trabalho com topologia no Packet Tracer (AB2 2020.2) (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Firewall:** sistema que aplica a política de segurança na fronteira entre redes, permitindo ou bloqueando o tráfego.

**Filtro de pacotes** (camadas de rede e transporte): decide **pacote a pacote** pelos campos do cabeçalho:
- IP de origem e destino;
- protocolo;
- portas de origem e destino;
- *flags* TCP;
- interface.

É rápido e barato, mas não entende o conteúdo. Sem estado, também não sabe se uma resposta pertence a uma conexão aberta de dentro.

**Filtro com estado (*stateful*):** guarda uma **tabela de conexões** e aceita respostas só de conexões iniciadas dentro da política.

**Gateway de nível de aplicação (*proxy*):**
- o cliente fala com o *proxy*, e o *proxy* fala com o servidor;
- entende o protocolo (HTTP, SMTP), autentica usuários, filtra conteúdo e registra comandos;
- é mais seguro e detalhado, mas mais lento, e precisa de um *proxy* por serviço.

**Regras:**
- são avaliadas **em ordem**, e vale a **primeira** que casa;
- termine com **negar tudo** (*default deny*): o que não está liberado está proibido;
- regras mais específicas vêm antes das gerais.

**DMZ:** rede intermediária com os servidores públicos (*web*, *e-mail*). A internet alcança a DMZ, mas não a rede interna.

**Trabalho com topologia** (Packet Tracer): o projeto é avaliado. Escreva a tabela de regras a partir da política (quem acessa o quê) e teste cada regra com um caso que deve passar **e** um que deve ser bloqueado.

**Verificação:** `test_regras_primeira_que_casa` implementa um avaliador pequeno com `ipaddress` (primeira regra que casa, negação por padrão) e confere que a ordem das regras muda o resultado e que HTTPS para a DMZ passa enquanto SSH vindo da internet é bloqueado.
