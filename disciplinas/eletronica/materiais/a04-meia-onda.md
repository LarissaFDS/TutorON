---
id: eletronica-anot-meia-onda
titulo: Retificador de meia onda: 220 V RMS, 60 Hz, carga de 10 Ω; pico 311,1 V, queda do diodo, Vmed = Vpico/π, corrente média, PIV e corrente RMS
assunto: eletronica-03-retificadores
tipo: resolucao
resolucao: sim
fonte: Anotações "Simulação de retificadores" (9 set. 2026, simulação no Falstad), p. 1–2, e "Revisão prova 1" (19 set. 2026), p. 2–3
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Meia onda:** fonte → diodo → carga $R$. Só o semiciclo em que o diodo conduz chega à carga; no outro, $v_o = 0$.

**Exemplo:** $V_{rms} = 220$ V, $f = 60$ Hz, $R = 10\ \Omega$.
- pico da fonte: $V_{s,pico} = \sqrt{2}\,V_{rms} = 311{,}13$ V;
- pico na carga = pico menos a queda do diodo: no simulador a queda foi 0,984 V, então $V_{o,pico} = 310{,}14$ V (com o modelo de 0,7 V: 310,43 V; ideal: 311,13 V);
- corrente máxima: $I_{o,max} = V_{o,pico}/R = 31{,}01$ A;
- tensão reversa máxima no diodo (PIV): o pico negativo da fonte, 311,13 V;
- tensão média: $V_{med} = V_{o,pico}/\pi = 98{,}72$ V (vê-pico sobre pi, cerca de 0,318 do pico); corrente média $I_{med} = V_{med}/R = 9{,}872$ A; a saída tem 60 Hz.

Fórmulas: ideal $I_{max} = V_m/R$; silício $I_{max} = (V_m - 0{,}7)/R$.

**Correção:** a revisão escreve "corrente RMS $= I_{med}/2$". Na meia onda, o valor eficaz é metade do **pico**: $I_{rms} = I_{max}/2$ (aqui 15,5 A), não metade da média (que daria 4,9 A).

**Verificação:** a integral numérica de meio seno de 310,14 V em um período dá média 98,72 V e RMS 155,07 V ($= V_{pico}/2$); a hipótese "diodo bloqueado no semiciclo negativo" confere com $V_D = -311$ V.
