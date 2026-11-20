---
id: eletronica-anot-grampeadores
titulo: Grampeadores com capacitor e diodo ideal, entrada quadrada de ±20 V: saída de 0 a 40 V, e com bateria de 5 V saída de −5 V a 35 V; excursão pico a pico de 40 V
assunto: eletronica-04-ceifadores-grampeadores
tipo: resolucao
resolucao: sim
fonte: Anotações "Aplicações de diodos" (24 set. 2026), questão 5, e "Exercícios" (17 set. 2026), exercício 37 (de livro, parafraseados)
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

**Como resolver um grampeador:** comece pelo semiciclo em que o diodo conduz. Nele o capacitor se carrega e $v_o$ fica preso no nível do diodo. Depois, com o diodo aberto, o capacitor mantém a tensão ($V_C = v_i - v_o$ constante, constante de tempo $RC$ grande) e $v_o = v_i - V_C$. O grampeador desloca o sinal sem mudar o pico a pico.

**(a)** $v_i$ → capacitor em série → saída; diodo ideal da saída ao terra (ânodo no terra), $R$ em paralelo.
- $v_i = -20$ V: o diodo conduz, $v_o = 0$, $V_C = v_i - v_o = -20$ V.
- $v_i = +20$ V: diodo aberto, $v_o = v_i - V_C = 20 - (-20) = 40$ V.
- Saída quadrada de 0 a 40 V.

**(b)** Igual, mas o diodo vai a uma bateria de 5 V com o positivo no terra (ânodo em $-5$ V).
- $v_i = -20$ V: conduz, $v_o = -5$ V, $V_C = -20 - (-5) = -15$ V.
- $v_i = +20$ V: $v_o = 20 - (-15) = 35$ V.
- Saída de $-5$ a 35 V.

Nos dois casos a excursão pico a pico é 40 V, a mesma da entrada.

**Verificação:** em (a), com $v_o = 40$ V o diodo fica com $-40$ V (aberto); em (b), com 35 V fica com $-40$ V. As hipóteses fecham.
