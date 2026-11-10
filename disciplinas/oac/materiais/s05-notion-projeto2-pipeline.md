---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações de alunos no Notion da turma); imagens e arquivos anexos não estão no repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações; trechos de código curtos foram conferidos
revisao_humana: pendente
fontes_catalogo: ufal-oac-notion
id: oac-notion-projeto2-pipeline
titulo: Projeto 2 da turma (Notion) — pipeline RISC-V: stall de load-use, bolha por flush e flush em desvio
assunto: oac-14-pipeline-hazards
tipo: material_estudo
fonte: Notion da turma, página "Projeto 2 - Pipeline" e subpágina "Code" (SystemVerilog completo), lidas em 02/11/2026; a animação anexa não foi aberta
autoria: Alunos da turma de OAC (UFAL), com trechos gerados por assistente de IA; revisão da equipe TutorON
status_resolucao: corrigida
---
Projeto 2: pipeline de 5 estágios com registradores IF/ID (D), ID/EX (E), EX/MEM (M) e MEM/WB (W), forwarding e unidade de hazards. Status da resolução: corrigida (conceitos certos; duas ressalvas no código, ver abaixo).

Load-use: lw x3, 0(x1) seguido de add x5, x3, x4. O add precisa de x3 no início do seu EX (ciclo 4), mas o lw só tem o dado no fim do seu MEM (também ciclo 4). Forwarding não basta: é preciso um ciclo de stall. Qualquer instrução seguinte que leia o rd do lw cai nisso (tipo R, addi, store, desvio).

Detecção: lwStall = (instrução em E é load) & ((Rs1D == RdE) | (Rs2D == RdE)). A versão completa também exige RdE ≠ 0.
Stall: StallF = StallD = lwStall; o PC e o IF/ID não atualizam (enable = ~Stall).
Bolha: FlushE = 1 zera os bits de controle guardados no ID/EX (registrador com clear). A instrução vira um NOP: não escreve registrador nem memória.

Desvios: quando o desvio ou jal é resolvido em EX (PCSrcE = 1), as duas instruções buscadas depois estão erradas. FlushD = PCSrcE e FlushE = lwStall | PCSrcE. Sem branches nem jumps no programa, o flush não é necessário, mas o processador da disciplina tem beq e jal.

Forwarding (código da turma): ForwardAE = 10 se RegWriteM e RdM == Rs1E (dado de EX/MEM, prioridade); 01 se RegWriteW e RdW == Rs1E; senão 00. Igual para a porta B.
Correções da equipe no código: (1) nem a unidade de hazards nem a de forwarding testam se o registrador é x0. Uma instrução que escreve em x0 faria forwarding de um valor diferente de zero; acrescente Rs1E != 0 (e Rs2E, RdE) às condições. (2) No hazard_unit as saídas se chamam PCWrite e IF_IDWrite, mas estão ligadas a FlushD e FlushE; a lógica (FlushD = PCSrcE, FlushE = PCSrcE | stall) está certa, só os nomes enganam.
