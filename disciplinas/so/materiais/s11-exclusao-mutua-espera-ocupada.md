---
id: so-exclusao-mutua-espera-ocupada
titulo: Exclusão mútua — variável "ocupado" falha, inibição de interrupções, TSL/test-and-set, espera ocupada; o que pode ser usado pelo usuário
assunto: so-04-coordenacao-impasses
tipo: lista
questao: caderno, cap. 4, questões 3 e 5; AB1 (respostas da turma), questão 5
resolucao: sim
fonte: Lista 3 da turma (2021) sobre o caderno do Prof. Maziero, cap. 4; respostas compartilhadas da turma (AB1); slides do Prof. André Aquino (UFAL)
fontes_catalogo: turma-listas-2021,turma-respostas-so,maziero-caderno-2014,ufal-aquino-slides-so
autoria: Resoluções de alunos parafraseadas, conferidas e corrigidas pela equipe TutorON
licenca: Caderno sob CC BY-NC-SA 3.0 (Maziero); respostas de alunos sem licença declarada, parafraseadas
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
Caderno do Prof. Maziero, cap. 4, e AB1. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Por que uma variável `ocupado` não basta** (questão 5): as duas tarefas executam

```c
while (ocupado) {}   /* espera ocupada */
ocupado = 1;         /* entra */
/* seção crítica */
ocupado = 0;         /* sai */
```

Intercalação que quebra a exclusão mútua, com `ocupado = 0`: A testa `ocupado` (0) e sai do `while`; antes de A gravar 1, B é escalonada, testa (ainda 0) e sai do `while`; A grava 1 e entra; B grava 1 e entra. **As duas estão na seção crítica.** O teste e a atribuição precisam ser uma operação **atômica**.

**Soluções:**
- **Inibir interrupções** dentro da seção crítica: sem interrupções não há troca de contexto. Só funciona com um processador e é instrução **privilegiada**: serve ao núcleo, nunca a processos de usuário.
- **Instruções atômicas** (TSL, *test-and-set*, *swap*, *compare-and-swap*): testam e gravam numa só instrução. Corrigem o problema acima, mas a tarefa que espera fica girando no laço (**espera ocupada**, *spinlock*): gasta processador e não garante ordem de chegada. Úteis no núcleo e em multiprocessadores, para esperas curtas.
- **Semáforos e mutexes** do sistema: a tarefa que não pode entrar é **suspensa** (sem gastar processador). São a ferramenta dos processos de usuário.

**Correção:** (AB1, questão 5) a resposta da turma diz que TSL deve ser reservada ao sistema por ser privilegiada; TSL **não** é privilegiada (qualquer programa pode executá-la; bibliotecas de *spinlock* a usam). O que é exclusivo do núcleo é inibir interrupções. Semáforos podem ser usados pelos processos de usuário (via chamadas de sistema ou bibliotecas).

**Verificação:** a intercalação mostrada tem as duas tarefas lendo 0 antes de qualquer escrita, o que basta para violar a exclusão mútua; com teste e escrita numa só instrução essa intercalação deixa de existir.
