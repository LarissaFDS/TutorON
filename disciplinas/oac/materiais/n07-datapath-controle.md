---
id: oac-nota-datapath-controle
titulo: Nota — datapath monociclo com unidade de controle: componentes e sinais de controle (R, lw, sw, beq)
assunto: oac-13-datapath-controle
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: pattersonhennessy-cod-riscv,ripes
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Datapath monociclo com a unidade de controle (descrição textual do slide do cap. 4 visto em aula; Patterson & Hennessy, seções 4.3 e 4.4).

Componentes: PC → memória de instruções; um somador PC + 4; um somador PC + (imediato) para o alvo do desvio; MUX que escolhe o próximo PC (PC+4 ou alvo), controlado por Branch AND Zero; banco de registradores (lê rs1 = Instruction[19-15] e rs2 = [24-20], escreve em rd = [11-7]); Imm Gen (gera o imediato estendido em sinal a partir de Instruction[31-0]); MUX ALUSrc (2º operando da ALU: registrador ou imediato); ALU com saída Zero; ALU control, que recebe ALUOp e Instruction[30,14-12]; memória de dados; MUX MemtoReg (escreve no registrador o resultado da ALU ou o dado lido). A unidade Control recebe o opcode, Instruction[6-0].

Sinais (1 = ativo; X = não importa):
| Instrução | ALUSrc | MemtoReg | RegWrite | MemRead | MemWrite | Branch | ALUOp |
| R (add, sub…) | 0 | 0 | 1 | 0 | 0 | 0 | 10 |
| lw | 1 | 1 | 1 | 1 | 0 | 0 | 00 |
| sw | 1 | X | 0 | 0 | 1 | 0 | 00 |
| beq | 0 | X | 0 | 0 | 0 | 1 | 01 |

Leitura para sw: a ALU soma rs1 + imediato (ALUSrc = 1, ALUOp = 00 → soma) para formar o endereço; rs2 vai para "Write data" da memória; MemWrite = 1. RegWrite = 0 porque nada é escrito no banco, e por isso MemtoReg é X. Branch = 0, então o próximo PC é PC + 4.
Para lw: mesmo endereço; MemRead = 1, MemtoReg = 1 e RegWrite = 1 levam o dado lido para rd.
Para beq: a ALU subtrai (ALUOp = 01); se Zero = 1 e Branch = 1, o PC recebe PC + imediato.

Ciclo único: o período de clock é fixado pela instrução mais lenta (lw: memória de instruções, registradores, ALU, memória de dados, registradores), o que motiva o pipeline.
