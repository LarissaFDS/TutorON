---
id: so-entrada-saida-controlador-driver-dma-raid
titulo: Entrada e saída — controlador × driver, E/S programada, por interrupção e por DMA, camadas da gerência de E/S, papel do SO, RAID
assunto: so-07-entrada-saida
tipo: prova
questao: variante da AB2, questões 9 e 10; Prova 2, questões 8 e 9; caderno, cap. 7 (lista 5 da turma, questão 3)
resolucao: sim
fonte: Prova 2 do Prof. André Aquino (UFAL), fotos da turma com gabarito; variante da AB2 com resolução e respostas compartilhadas da turma; Lista 5 da turma (2021); resumo de estudo de aluna (2017), cap. 7; slides de gerência de E/S
fontes_catalogo: ufal-aquino-prova2-fotos,turma-resolucao-ab2-variante,turma-respostas-so,turma-listas-2021,turma-resumos-2017,ufal-aquino-slides-so
autoria: Provas do Prof. André Aquino (UFAL); resoluções de alunos parafraseadas, conferidas e corrigidas pela equipe TutorON
licenca: Não declarada (provas); slides sob CC BY-NC-SA 4.0; paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
Provas do Prof. André Aquino. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Controlador × driver:** o **controlador** é hardware (registradores, buffer e lógica) ligado ao dispositivo: controlador SATA, USB, de rede. O **driver** é software do núcleo que conhece os registradores de **um** controlador e oferece ao SO uma interface padrão: driver da placa de rede, do disco NVMe. **Correção:** uma resposta da turma deu como exemplo de driver o "Gerenciador de Dispositivos", que é um programa de administração do Windows, não um driver.

**Formas de interação:** E/S **programada** (o processador consulta o estado em laço: espera ocupada); **por interrupção** (o controlador avisa a cada dado ou etapa); **DMA** (o controlador de DMA copia o bloco inteiro entre dispositivo e memória sem o processador). Com DMA o driver **ainda precisa** de tratador de interrupção: há **uma** interrupção no fim da transferência inteira (verificar erros, acordar a tarefa), em vez de uma por palavra.

**Camadas:** aplicação → biblioteca → chamadas de sistema → subsistema de E/S independente de dispositivo (buffers, cache, escalonamento) → driver → tratador de interrupção → controlador → dispositivo. Separar o **controle do dispositivo** (driver) do **gerenciamento de E/S** é bom projeto porque isola as características de hardware das características funcionais (Prova 2, questão 8; gabarito conferido).

**Prova 2, questão 9** (correta): os sistemas de E/S usam interrupções que levam ao modo núcleo e precisam ser tratadas pelo SO. Falsas: o SO **é** responsável pelas abstrações e rotinas de baixo nível, **escalona** os acessos, envia comandos além de ler e escrever e **impede** o acesso direto do programa de usuário ao dispositivo.

**RAID com 4 discos de 8 TB:** maior espaço útil: RAID 0 (32 TB, sem tolerância); maior tolerância: RAID 1 espelhando nos 4 (8 TB úteis, tolera 3 falhas); equilíbrio: RAID 5 (24 TB úteis, tolera 1 falha).

**Verificação:** espaço útil do RAID 5 = $(n - 1) \times 8 = 24$ TB, do RAID 1 em 4 cópias = 8 TB; uma interrupção por transferência no DMA contra uma por palavra na E/S por interrupção.
