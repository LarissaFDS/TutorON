---
id: oac-cc-pipeline-reordenar-ciclo
titulo: Pipeline de 5 estágios sem forwarding: qual troca de instruções resolve o conflito de dados; tempo de ciclo do estágio com registradores de 2 ns; multicore, superpipeline e superescalar
assunto: oac-14-pipeline-hazards
tipo: prova
fonte: Provas de OAC do Prof. Erick de Andrade Barboza (IC-UFAL, cursos de Engenharia e Ciência da Computação) | Prova 2 de 2017.2 (Q1, Q4 e Q5)
curso: Ciência da Computação (UFAL), prova comum às turmas de Engenharia e Ciência da Computação, 2017.2
autoria: Enunciados: provas do Prof. Erick de Andrade Barboza, parafraseadas pela equipe TutorON; resolução da equipe TutorON com auxílio de IA, conferida com o gabarito do professor e por simulação
licenca: Não declarada (prova com gabarito); os PDFs não estão no repositório
publicacao_transcricao: não se aplica: o enunciado é parafraseado e só os dados foram mantidos
fontes_catalogo: ufal-cc-oac-provas-erick-2017
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões da prova 2 de 2017.2 (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com o gabarito do professor e em Python; a prova é de 2017 e usa MIPS, não RISC-V).

**Sequência:** `or $6,$4,$2`, `and $5,$4,$3`, `add $1,$2,$2`, `mul $3,$2,$1`, `sub $1,$1,$4`. Pipeline de 5 estágios sem forwarding, com escrita no banco de registradores na primeira metade do ciclo e leitura na segunda. Assim, quem lê o registrador precisa estar **pelo menos 3 instruções depois** de quem o escreve.
- Conflitos originais: `add` escreve $1, e `mul` (1 depois) e `sub` (2 depois) leem $1.
- I. Trocar `add` e `or` põe o `add` em primeiro: `mul` fica 3 depois e `sub` 4 depois. **Resolve.**
- II. Trocar `add` e `and` deixa o `mul` 2 depois do `add`. Não resolve.
- III. Um `nop` entre `add` e `mul` deixa o `mul` 2 depois. Não resolve.
- Resposta: só I (alternativa A).

**Tempo de ciclo do pipeline.** Ciclo de 20 ns; uma instrução gasta 2 ciclos na busca, 1 na decodificação, 2 na busca de operandos e 3 na execução. Sequencial: $8\times20=160$ ns. Com 4 estágios indivisíveis (40, 20, 40 e 60 ns) e 2 ns por registrador de estágio, o ciclo é o do estágio mais lento: $60+2=62$ ns.

**Termos:** multicore = vários processadores num encapsulamento; superpipeline = muitos estágios; superescalar = vários pipelines em paralelo; pipeline dinâmico = execução fora de ordem; multiprocessadores = vários processadores com espaço de endereços compartilhado (alternativa b).

**Verificação:** as distâncias entre escrita e leitura foram conferidas em Python para a sequência original e para as três mudanças.
