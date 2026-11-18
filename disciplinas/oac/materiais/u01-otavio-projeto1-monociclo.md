---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações manuscritas de aluno, 2025.2); PDFs e imagens fora do repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações; as figuras de slides da editora foram descritas, não copiadas
revisao_humana: pendente
fontes_catalogo: ufal-oac-anotacoes-otavio-2025-2
id: oac-otavio-projeto1-monociclo
titulo: Anotações de aluno (2025.2) — Projeto 1: quais sinais de controle ficam ativos no datapath monociclo em cada instrução (addi, lw, sw, jal, beq)
assunto: oac-13-datapath-controle
tipo: material_estudo
fonte: Anotações manuscritas "Projeto 1 - SingleCycle" (5 páginas), turma 2025.2
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de OAC 2025.2, Prof. Erick de Andrade Barboza); revisão da equipe TutorON
status_resolucao: corrigida
---
Anotações de um aluno sobre o Projeto 1 (processador monociclo RISC-V). Status da resolução: corrigida (um sinal; ver "Correções"). Projeto avaliado: o bloco explica o datapath, não traz a implementação.

O que faltava no código-base, segundo as anotações: decodificação de jal e addi no decodificador principal, sinal Jump entrando no PCSrc (PCSrc = Branch·Zero OR Jump) e PC + 4 como terceira entrada do mux de resultado (para o jal gravar o endereço de retorno).

Sinais de controle ativos em cada instrução (datapath monociclo do livro, cap. 4):
- addi: ALUSrc = 1 (imediato), RegWrite = 1, MemWrite = 0, Branch = 0, resultado vem da ULA.
- lw x10, 4(s0): ALUSrc = 1, ULA soma (ALUOp = 00), MemRead = 1, resultado vem da memória, RegWrite = 1.
- sw x10, 8(s0): ALUSrc = 1, ULA soma, MemWrite = 1, RegWrite = 0; seleção do resultado = X.
- jal: Jump = 1, resultado = PC + 4, RegWrite = 1; o destino é PC + imediato (somador de desvio, não a ULA).
- beq x1, x2, L: ALUSrc = 0 (compara dois registradores), ULA subtrai (ALUOp = 01), Zero = 1 se iguais; Branch = 1; PCSrc = Branch·Zero escolhe PC + imm (imediato tipo B, em múltiplos de 2 bytes) ou PC + 4. RegWrite = 0 e MemWrite = 0.

Caminho do beq: busca no PC → banco lê rs1 e rs2 → ULA faz rs1 − rs2 → Zero vai à porta AND com Branch → mux do PC. Em paralelo, o gerador de imediato monta o deslocamento e o somador calcula PC + imm. Nada é escrito.

Correções da equipe: (1) as anotações põem MemtoReg = 00 no beq; como RegWrite = 0, o valor é X (não importa). (2) A anotação de que o extend não tinha configuração para os tipos B e I não foi confirmada no código; confira o ImmSrc no seu próprio .sv.
