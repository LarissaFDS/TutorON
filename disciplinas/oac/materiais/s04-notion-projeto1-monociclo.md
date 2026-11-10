---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações de alunos no Notion da turma); imagens e arquivos anexos não estão no repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações; trechos de código curtos foram conferidos
revisao_humana: pendente
fontes_catalogo: ufal-oac-notion
id: oac-notion-projeto1-monociclo
titulo: Projeto 1 da turma (Notion) — RISC-V monociclo em SystemVerilog: módulos e correções para jal e addi
assunto: oac-13-datapath-controle
tipo: material_estudo
fonte: Notion da turma, página "Projeto 1 OAC" e os anexos riscvsingle_p1.sv (original e modificado) e riscvtest.s, lidos em 02/11/2026
autoria: Alunos da turma de OAC (UFAL); revisão da equipe TutorON
status_resolucao: corrigida
---
Projeto 1: corrigir o design de um RISC-V monociclo em SystemVerilog (base: slide 29 das aulas 11–12) até o testbench, que não pode ser alterado, imprimir "Simulation succeeded" no Icarus Verilog (EDA Playground). Entrega: o .sv, o .s em assembly e o .txt com o código de máquina. O programa de teste (de Harris & Harris) usa add, sub, and, or, slt, addi, lw, sw, beq e jal e deve gravar 25 no endereço 100. Status da resolução: corrigida (dois itens das anotações; ver abaixo).

Módulos: top (só ligações); riscvsingle (controller + datapath); controller = maindec (gera RegWrite, ImmSrc, ALUSrc, MemWrite, ResultSrc, Branch, ALUOp e Jump a partir do opcode) + aludec (ALUOp, funct3 e funct7[5] → ALUControl de 3 bits); datapath com flopr do PC, somadores PC + 4 e PC + imediato, mux do PC, banco de registradores, extend (ImmGen), mux do 2º operando (ALUSrc), ULA (flag zero) e mux de 3 entradas do resultado (ULA, dado lido, PC + 4).

Correções que a turma fez no design:
1. PCSrc = (Branch & Zero) | Jump, para o jal desviar.
2. O maindec ganhou o sinal Jump e as linhas de controle de addi (RegWrite 1, ImmSrc 00, ALUSrc 1, ResultSrc 00) e de jal (RegWrite 1, ImmSrc 11, ResultSrc 10, Jump 1).
3. A entrada 2 do mux de resultado recebia 32 bits de zero; passou a receber PC + 4 (o jal grava o endereço de retorno).

Correções da equipe nas anotações:
- O extend recebe Instr[31:7], 25 bits, não 24.
- O WE da memória de dados vem do sinal MemWrite do controller, não do banco de registradores.
- ALUOp = 11 no addi está certo neste projeto: o aludec trata 10 e 11 no mesmo caso (decodifica por funct3), e o sub só sai com funct7[5] = 1 e op[5] = 1, o que exclui o addi. O código-base de Harris & Harris usa 10; as duas escolhas funcionam.
