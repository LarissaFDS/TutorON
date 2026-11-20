---
id: eletronica-anot-onda-completa-ponte
titulo: Retificador de onda completa em ponte: dois diodos conduzem por semiciclo, pico Vm − 2·0,7 V, Vmed = 2Vpico/π, 120 Hz, PIV; diferença para a meia onda
assunto: eletronica-03-retificadores
tipo: resolucao
resolucao: sim
fonte: Anotações "Simulação de retificadores" (9 set. 2026), p. 3–5, e "Revisão prova 1" (19 set. 2026), p. 3–4
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Diferença entre meia onda e onda completa:** a meia onda usa um diodo e aproveita só um semiciclo ($V_{med} = V_p/\pi$, saída de 60 Hz). A onda completa em ponte usa quatro diodos: em cada semiciclo **dois** conduzem em série, a corrente na carga tem sempre o mesmo sentido, $v_o = |v_s|$ (ideal), $V_{med} = 2V_p/\pi$ (dois vê-pico sobre pi, cerca de 0,636 do pico) e a saída tem o dobro da frequência (120 Hz para rede de 60 Hz).

**Pico:** ideal $V_{o,pico} = V_m$; silício $V_{o,pico} \approx V_m - 1{,}4$ V (duas quedas).

**Exemplo:** 220 V RMS, 60 Hz, $R = 10\ \Omega$; queda simulada de 0,983 V por diodo.
- $V_{s,pico} = 311{,}13$ V; $V_{o,pico} = 311{,}13 - 2(0{,}983) = 309{,}16$ V;
- $I_{o,max} = 30{,}92$ A;
- tensão reversa máxima num diodo bloqueado: $V_{s,pico} - V_D = 310{,}14$ V (na ponte ideal, PIV $= V_m$);
- $V_{med} = 2(309{,}16)/\pi = 196{,}82$ V; $I_{med} = 19{,}68$ A.

**Verificação:** a média numérica de $|309{,}16\sin\omega t|$ dá 196,82 V; na malha fonte → D1 → carga → D3 → fonte, no pico: $311{,}13 - 0{,}983 - 309{,}16 - 0{,}983 \approx 0$.
