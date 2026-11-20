---
id: eletronica-anot-diodo-modelos
titulo: Como saber se o diodo está conduzindo: modelos ideal (fio) e de silício (queda de 0,7 V), hipótese de estado e conferência
assunto: eletronica-01-diodo-modelos
tipo: resolucao
resolucao: sim
fonte: Anotações "Diodos" (11 set. 2026), p. 1–3, e "Revisão prova 1" (19 set. 2026), p. 1
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

**Tensão no diodo:** $V_D = V_A - V_K$ (ânodo menos cátodo). Corrente direta entra pelo ânodo.

| Estado | Diodo ideal | Diodo de silício (queda constante) |
|---|---|---|
| conduzindo (ligado) | $V_D = 0$: fio | $V_D \approx 0{,}7$ V: fonte de 0,7 V |
| bloqueado (desligado) | $I_D = 0$: circuito aberto | $I_D \approx 0$: circuito aberto |

Linear por partes: fonte de 0,7 V em série com $r_d$; só use se o enunciado der $r_d$.

**Como saber se o diodo está conduzindo (método das anotações):**
1. identifique ânodo e cátodo; 2. suponha um estado (ligado ou desligado); 3. troque o diodo pelo modelo (fio, fonte de 0,7 V ou aberto); 4. calcule; 5. **confira a hipótese**: ligado exige $I_D > 0$ no sentido ânodo → cátodo; desligado exige $V_D$ abaixo de 0 (ideal) ou de 0,7 V (silício). Se falhar, troque a hipótese. Com entrada senoidal, repita para cada semiciclo e junte o gráfico.

**Correção:** as anotações dizem que o diodo conduz "pois a corrente entra no ânodo". Quem decide é a tensão: conduz quando $V_A - V_K$ alcança o limiar (0 V ideal, 0,7 V silício). Também chamam de 220 V o pico de uma rede de 220 V; 220 V é o valor eficaz (RMS), e o pico é $220\sqrt{2} \approx 311$ V (pico igual a raiz de dois vezes o RMS).

No retificador de meia onda ideal: semiciclo positivo, diodo ligado, $v_o = v_s$; semiciclo negativo, diodo aberto, $v_o = 0$.

**Verificação:** em todos os exemplos do acervo a hipótese de estado é conferida no fim (corrente no sentido direto ou tensão reversa no diodo bloqueado), e os valores são refeitos em `tests_acervo/test_disciplina_eletronica.py`.
