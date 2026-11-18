---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações manuscritas de aluno, 2025.2); PDFs e imagens fora do repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações
revisao_humana: pendente
fontes_catalogo: ufal-oac-anotacoes-otavio-2025-2
id: oac-otavio-ab2-cpu-gpu
titulo: Revisão AB2 (aluno, 2025.2) — cap. 6: diferença entre CPU e GPU
assunto: oac-16-paralelismo
tipo: material_estudo
fonte: Anotações manuscritas "Revisão AB2", turma 2025.2, página do cap. 6
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de OAC 2025.2, Prof. Erick de Andrade Barboza); revisão da equipe TutorON
status_resolucao: validada
---
Resumo de um aluno para a AB2. Status da resolução: validada (afirmações conceituais conferidas com o cap. 6 do livro).

A anotação diz que, no cap. 6, o foco da revisão são as questões 1, 2 e 3; o resto é revisão.

CPU: caches maiores e poucas threads por núcleo; controle complexo (previsão de desvio, execução fora de ordem); generalista, boa para código sequencial cheio de decisões, como o do sistema operacional.
GPU: caches menores e muitas threads; núcleos simples executando a mesma instrução sobre muitos dados (estilo SIMD; a NVIDIA chama de SIMT); especializada em gráficos e matrizes, extremamente paralela. Ela esconde a latência da memória trocando de thread, em vez de depender de caches grandes.
