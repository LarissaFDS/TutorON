---
id: so-arquiteturas-monolitico-micronucleo
titulo: Arquiteturas de sistemas operacionais — monolítico, micronúcleo, camadas, híbrido, máquinas virtuais e contêineres
assunto: so-01-conceitos-estrutura
tipo: prova
questao: AB2 2020.1, questão 1; caderno, cap. 1, questão 17
resolucao: sim
fonte: Prova AB2 de 2020.1 (formulário on-line), Prof. André Aquino (UFAL), e respostas compartilhadas da turma; caderno do Prof. Maziero, cap. 1
fontes_catalogo: ufal-aquino-ab-2020-1,turma-respostas-so,maziero-caderno-2014,ufal-aquino-slides-so
autoria: Prova do Prof. André Aquino (UFAL); resposta de aluno parafraseada e conferida pela equipe TutorON
licenca: Não declarada (prova); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Prova AB2 de 2020.1 (enunciado parafraseado): o aluno escolhe **uma** arquitetura (monolítico, micronúcleo, camadas, híbrido, máquina virtual ou contêiner) e responde todas as questões (alocação de memória, substituição de páginas, E/S de rede, sistema de arquivos) explicando como os elementos do SO interagem **nessa** arquitetura. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

| Arquitetura | Como funciona | Ponto forte | Ponto fraco |
|---|---|---|---|
| Monolítico | todo o SO num só programa em modo núcleo | desempenho (chamadas diretas) | erro num driver derruba tudo; manutenção difícil |
| Micronúcleo | núcleo mínimo (tarefas, memória, IPC); drivers e arquivos como processos em modo usuário | robustez e modularidade | custo das mensagens e trocas de contexto |
| Camadas | cada camada usa só a de baixo | organização | rigidez e sobrecarga |
| Híbrido | micronúcleo com serviços críticos dentro do núcleo (Windows NT, macOS) | equilíbrio | complexidade |
| Máquina virtual | hipervisor dá a cada SO convidado um hardware virtual | isolamento, vários SOs | sobrecarga |
| Contêiner | espaços isolados sobre o **mesmo** núcleo | leve, rápido | isolamento menor que o da VM |

Na resposta da turma (micronúcleo), as chamadas de sistema viram **mensagens** entre processos servidores e cada serviço tem memória confinada: ganha tolerância a falhas e perde desempenho. Está correto.

Verdadeiro ou falso do caderno: "no micronúcleo as chamadas de sistema são implementadas por troca de mensagens" é **verdadeira**; "um hipervisor convidado executa sobre um SO hospedeiro" é **verdadeira**; "máquina virtual de sistema é feita para uma linguagem como Java" é **falsa** (isso é máquina virtual de aplicação); "núcleos monolíticos são usados pela robustez e fácil manutenção" é **falsa** (são usados pelo desempenho); "no micronúcleo os componentes são módulos dentro do núcleo" é **falsa**.

**Verificação:** cada linha da tabela foi conferida com o cap. 1 do livro do Maziero; os dois itens verdadeiros dão a alternativa "II e V corretas".
