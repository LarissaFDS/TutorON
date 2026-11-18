---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações manuscritas de aluno, 2025.2); PDFs e imagens fora do repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações; as figuras de slides da editora foram descritas, não copiadas
revisao_humana: pendente
fontes_catalogo: ufal-oac-anotacoes-otavio-2025-2
id: oac-otavio-projeto2-hazards
titulo: Anotações de aluno (2025.2) — Projeto 2: hazard de dados, quando o forwarding não resolve (load-use), bolha e flush de desvio
assunto: oac-14-pipeline-hazards
tipo: material_estudo
fonte: Anotações manuscritas "Projeto 2 - Pipeline" (11 páginas), turma 2025.2
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de OAC 2025.2, Prof. Erick de Andrade Barboza); revisão da equipe TutorON
status_resolucao: corrigida
---
Anotações de um aluno sobre o Projeto 2 (pipeline IF, ID, EX, MEM, WB). Status da resolução: corrigida (ver "Correções"). Projeto avaliado: só conceitos, sem implementação.

Hazard de dados: uma instrução lê um registrador que a anterior ainda não escreveu. O forwarding leva o resultado de EX/MEM ou MEM/WB direto à entrada da ULA e resolve dependências entre instruções de ULA, sem bolha.
Quando o forwarding não resolve: load-use. O lw só tem o dado no fim do MEM, e a instrução seguinte precisa dele no início do EX. Ciclo a ciclo (com forwarding):
```text
ciclo:          1  2  3  4  5  6  7
lw  x1, 0(x2)   IF ID EX ME WB
add x3, x1, x4     IF ID ID EX ME WB
```
Uma bolha: 2 instruções levam 5 + 1 + 1 = 7 ciclos (5 para encher o pipeline, +1 por instrução seguinte, +1 de stall).
Detecção: MemReadE = 1 e (Rs1D = RdE ou Rs2D = RdE) → StallF = StallD = 1 (PC e IF/ID congelam) e FlushE = 1 (zera o controle em ID/EX: RegWrite = MemWrite = 0).
Desvio tomado, resolvido em EX (PCSrcE = 1): as 2 instruções buscadas depois são descartadas, FlushD = FlushE = 1, 2 bolhas.
Prioridade do forwarding: 10 = EX/MEM (mais recente) antes de 01 = MEM/WB; 00 = banco de registradores.

Correções da equipe: (1) as condições não testam rd ≠ x0; sem isso, escrever em x0 faria forwarding de valor errado. (2) Uma página chama o valor do banco (00) de "mais recente"; é o contrário, o mais recente é EX/MEM. (3) Os sinais "Reg_ControlWB_E/M" usados com RdM e RdW são o RegWrite de M e de W; os nomes enganam. (4) O exemplo usa sd (RV64); no RV32 é sw.
