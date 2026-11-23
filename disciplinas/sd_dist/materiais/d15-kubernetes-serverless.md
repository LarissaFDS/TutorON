---
id: sd_dist-kubernetes-orquestracao-pods-autoescala-cloud-functions-serverless
titulo: O que é Kubernetes, com exemplo de uso (pods, estado desejado, autoescala), e o que são cloud functions (serverless, FaaS)
assunto: sd_dist-04-tecnologias
tipo: prova
questao: AB2 2020.1 Q7; AB2 2020.2
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB2 2020.1 Q7; AB2 2020.2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Kubernetes:** orquestrador de containers mais usado. Agrupa containers em **pods**, mantém o **estado desejado** declarado (ex.: "3 réplicas da API"), faz **autoescala**, **atualizações graduais** (*rolling updates*) e recuperação automática. Exemplo: uma loja virtual com a API em 3 pods atrás de um *Service*; na Black Friday, o *Horizontal Pod Autoscaler* sobe para 20 pods pela carga de CPU, e se um nó cai, os pods são recriados em outro.

**Cloud functions (serverless, FaaS):** o desenvolvedor envia só uma **função**, que roda **acionada por eventos** (requisição HTTP, arquivo enviado, mensagem numa fila). O provedor cuida de servidores e escala (até zero) e **cobra por execução**. Ex.: AWS Lambda, Google Cloud Functions. Limites: tempo máximo de execução, *cold start*, sem estado local.

**Verificação:** `test_tecnologias_tem_conceito_e_exemplo` confere que o bloco define Kubernetes e cloud functions com exemplo; Kubernetes não roda nos testes.
