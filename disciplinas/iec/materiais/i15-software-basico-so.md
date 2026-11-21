---
id: iec-software-basico-so-compilacao
titulo: Software básico: compilador, montador, ligador e linkedição (ligação), carregador; processo, chamadas de sistema, modo usuário e modo núcleo
assunto: iec-04-software-basico
tipo: prova
questao: 4, 5, 6, 10
semestre: 2016.1
resolucao: sim
fonte: Fotos da Reavaliação AB2 de Introdução à Engenharia de Computação (ECOM006), UFAL, 2016.1, Q4, 5, 6, 10
fontes_catalogo: ufal-iec-reav-ab2-2016
autoria: Enunciados: reavaliação da disciplina (professor não identificado na prova), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Do código-fonte ao programa em execução:** o **compilador** faz análise léxica (tokens), sintática (gramática) e semântica (tipos) e gera código objeto; o **montador** traduz assembly em código de máquina; o **ligador** (linker) faz a **linkedição**: junta os códigos objeto e as **rotinas de biblioteca** (por exemplo, de E/S) num executável; o **carregador** (loader) põe o executável na memória. O **interpretador** executa instrução por instrução, sem gerar executável.

**Questões (Reavaliação AB2):**
- Q4: a fase que liga o código objeto principal às rotinas externas já existentes (E/S) é a **ligação (linkedição)**: alternativa **(E)**.
- Q5: **processo** é um programa em execução com seu contexto: espaço de endereçamento (código, dados, pilha), registradores e contador de programa, estado (pronto, executando, bloqueado) e recursos (arquivos abertos), descritos no bloco de controle de processo. O programa é passivo (arquivo); o processo é ativo.
- Q6: (V) a interface com o usuário pode ser texto (interpretador de comandos, shell) ou gráfica (GUI); (F) utilitários costumam ser **arquivos executáveis** separados e só alguns comandos são internos ao shell, então "nunca são executáveis" é falso; (V) as chamadas de sistema são o ponto de entrada no núcleo. Alternativa **(c)**.
- Q10: (V) o processador executa em modo usuário e modo núcleo; (V) em modo usuário não há acesso direto ao hardware nem à memória protegida; (V) em modo núcleo há privilégio máximo. Alternativa **(d)**.

**Verificação:** confira cada sequência V/F contra as alternativas: (V, F, V) só aparece em (c) na Q6; (V, V, V) só em (d) na Q10.
