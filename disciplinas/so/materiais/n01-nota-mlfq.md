---
id: so-nota-filas-multinivel-realimentacao
titulo: Nota da equipe — filas multinível com realimentação (MLFQ)
assunto: so-02-tarefas-escalonamento
tipo: nota
resolucao: nao
fonte: Nota da equipe TutorON escrita com apoio de IA, a partir das ideias gerais do OSTEP (cap. 8), sem transcrição
fontes_catalogo: ostep,maziero-socm-2013
autoria: Equipe TutorON com apoio de IA; sem revisão humana
licenca: Texto próprio
publicacao_transcricao: não se aplica
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Filas multinível com realimentação: várias filas de prontas, cada uma com uma prioridade e, em geral, um quantum maior nas filas de prioridade menor. Uma tarefa nova entra na fila mais alta; se gastar o quantum inteiro, desce uma fila; se liberar o processador antes (por E/S), fica onde está. Assim, tarefas interativas ficam no topo e tarefas de processamento longo descem. Para evitar inanição, de tempos em tempos todas as tarefas voltam para a fila mais alta (envelhecimento).

**Verificação:** nota sem revisão humana; fica fora da busca até ser revisada.
