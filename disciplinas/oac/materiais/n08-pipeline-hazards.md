---
id: oac-nota-pipeline-hazards
titulo: Nota — pipeline de 5 estágios: hazards estruturais, de dados e de controle; forwarding e stall
assunto: oac-14-pipeline-hazards
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: pattersonhennessy-cod-riscv,ripes,cs61c-berkeley
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Pipeline do RISC-V (Patterson & Hennessy, seções 4.5 a 4.9). Tópico fundamental do livro; confirmado no Projeto 2 da turma (bloco oac-notion-projeto2-pipeline).

Estágios: IF (busca), ID (decodificação e leitura de registradores), EX (ALU), MEM (memória de dados), WB (escrita no registrador). Em regime, termina uma instrução por ciclo; o tempo de cada instrução não diminui, a vazão aumenta. Speedup ideal ≈ número de estágios, se os estágios forem equilibrados.

Hazards:
- Estrutural: dois estágios precisam do mesmo recurso no mesmo ciclo (por isso há memórias separadas de instruções e de dados).
- De dados: uma instrução precisa de um resultado que ainda não foi escrito. Ex.: add x1, x2, x3 seguido de sub x4, x1, x5. Solução: forwarding (adiantamento) da saída da ALU para a entrada da ALU, sem bolha.
- Load-use: lw x1, 0(x2) seguido de add x3, x1, x4. O dado só existe no fim do MEM; mesmo com forwarding, é preciso 1 stall (bolha). O compilador pode reordenar instruções independentes para preencher esse ciclo.
- De controle: o desvio só é resolvido mais tarde no pipeline. Soluções: stall, predição (prever não tomado e descartar se errar; predição dinâmica com histórico) e resolver o desvio mais cedo, em ID.

Diagrama ciclo a ciclo (lw seguido de add dependente, com forwarding):
ciclo:  1  2  3  4  5  6  7
lw:     IF ID EX ME WB
add:       IF ID ** EX ME WB    (** = bolha de 1 ciclo)

Exceções: o pipeline descarta as instruções posteriores, salva o PC da instrução que causou a exceção (SEPC) e a causa (SCAUSE) e desvia para o tratador.
