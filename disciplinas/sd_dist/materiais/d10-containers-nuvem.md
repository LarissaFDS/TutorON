---
id: sd_dist-docker-containers-swarm-kubernetes-cloud-functions
titulo: O que são containers, Docker, Docker Network e Docker Swarm, por que containers são importantes e a diferença para máquina virtual
assunto: sd_dist-04-tecnologias
tipo: prova
questao: AB2 2020.1 Q1; AB2 2020.2
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2020.1 e 2020.2
fontes_catalogo: ufal-leandro-provas-sd
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
status_resolucao: validada
revisao_humana: pendente
---
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 2020.1 Q1; AB2 2020.2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Container:** processo isolado que leva **a aplicação e suas dependências** (bibliotecas, configuração) numa **imagem**, compartilhando o **núcleo do SO** do hospedeiro (isolamento com *namespaces* e limites com *cgroups* no Linux). Diferença para máquina virtual: a VM emula hardware e roda um **SO convidado inteiro**; o container não, por isso inicia em segundos e gasta menos memória.

**Por que são importantes** (a resposta que só lista vantagens de VM perdeu ponto em 2020.2): **mesmo ambiente** do desenvolvimento à produção ("na minha máquina funciona" deixa de ser desculpa), **implantação rápida e reprodutível**, densidade (muitos por máquina) e **base dos microsserviços** e da escala horizontal na nuvem.

**Docker:** plataforma para construir imagens (`Dockerfile`), distribuí-las (registro, como o Docker Hub) e rodar containers. **Docker Network:** redes virtuais entre containers (`bridge` numa máquina, `overlay` entre máquinas), com resolução de nomes pelo nome do serviço. **Docker Swarm:** **orquestrador** nativo do Docker: junta várias máquinas num *cluster*, roda **serviços** com N réplicas, faz balanceamento e reinicia containers que falham.

**Verificação:** `test_tecnologias_tem_conceito_e_exemplo` confere que o bloco define cada tecnologia perguntada e dá um exemplo de uso; Docker não roda nos testes.
