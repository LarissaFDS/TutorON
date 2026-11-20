---
id: pcom-anot-largura-banda-am-dsb
titulo: Largura de banda do sinal AM e DSB: BT = 2W (largura de transmissão é o dobro da banda da mensagem); a portadora não muda a banda; convenção unilateral e bilateral (± f)
assunto: pcom-02-am-dsb
tipo: material_estudo
resolucao: sim
fonte: Anotações "fórmulas fundamentais para a prova 1" (7 set. 2026), p. 1 e 4; Anotações "Simulação Modulação AM" (30 ago. 2026), p. 7–9
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Princípios de Comunicação 2026.2; docente Jobson de Araújo Nascimento, conforme os cabeçalhos das simulações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de listas e de provas parafraseados; fotos de slide, capturas de tela e figuras coladas não foram copiadas
fontes_catalogo: ufal-pcom-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

Se a mensagem ocupa de 0 a $W$ Hz, tanto o DSB-SC quanto o AM convencional ocupam de $f_c - W$ a $f_c + W$: **largura de banda de transmissão $B_T = 2W$** (duas bandas laterais). Somar a portadora não muda essa largura.

**Exemplo:** mensagem de 4 kHz em AM: $B_T = 2 \cdot 4 = 8$ kHz ($2\pi \cdot 8000 \approx 50\,265$ rad/s). Com portadora em 100 kHz, o sinal ocupa de 96 a 104 kHz. Para outra banda de mensagem, aplique a mesma regra.

**Simulação da turma:** tom de 300 Hz ($600\pi$ rad/s) e portadora de 3 kHz: bandas em 2700 e 3300 Hz ($5400\pi$ e $6600\pi$ rad/s), $B_T = 600$ Hz ($1200\pi$ rad/s), com e sem portadora.

**Convenção:** a largura de banda é medida nas frequências positivas. As anotações às vezes contam de $-f$ a $+f$ (espectro bilateral): "largura de banda do filtro $2f_c$" na folha de fórmulas é a largura bilateral de um passa-baixas que vai até $f_c$. Diga sempre qual das duas está usando.

Correção: a folha de fórmulas chama de "largura de banda do sinal modulado" a distância entre a borda da mensagem e $f_c$ ($f_c - f_d$ no esboço); a largura do sinal modulado é a faixa ocupada em torno de $f_c$, $2W$.

**Verificação:** FFT de um AM com tom de 4 kHz e portadora de 100 kHz: componentes só em 96, 100 e 104 kHz, largura ocupada 8 kHz.
