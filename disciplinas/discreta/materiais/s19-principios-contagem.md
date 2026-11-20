---
id: discreta-principios-contagem
titulo: Princípios de contagem — multiplicação, adição, inclusão-exclusão e casa dos pombos
assunto: discreta-11-combinatoria
tipo: material_estudo
resolucao: sim
fonte: Slides e lista de Contagem do Prof. Leandro Balby Marinho (UFCG); slides de Conjuntos do Prof. Lucas Amorim (cardinalidade da união)
fontes_catalogo: ufcg-discreta-leandro,ufal-discreta-slides-lucas
autoria: Prof. Leandro Balby Marinho (UFCG) e Prof. Lucas Benevides Viana de Amorim (IC/UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material dos professores)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Antes de contar, responda duas perguntas: **a ordem importa?** e **pode repetir?** A mesma frase de enunciado pode ter respostas diferentes conforme essas escolhas, e a resposta deve dizer qual foi a interpretação.

**Princípio da multiplicação**: se uma tarefa tem etapas sucessivas com $n_1, n_2, \dots, n_k$ opções (independentes), há $n_1 \cdot n_2 \cdots n_k$ maneiras. Ex.: senhas de 3 algarismos (0 a 9). Com repetição: $10^3 = 1000$. Sem repetição: 10 · 9 · 8 = 720. Placas com 3 letras (26) e 4 algarismos, com repetição: $26^3 \cdot 10^4 = 175\,760\,000$.

**Princípio da adição**: se a tarefa se faz de um jeito **ou** de outro, sem sobreposição, somam-se as contagens. Ex.: escolher um representante entre 12 alunos de uma turma ou 15 de outra: 27.

**Inclusão-exclusão** (quando há sobreposição): $|A \cup B| = |A| + |B| - |A \cap B|$, e para três conjuntos $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$. Ex.: de 1 a 100, os divisíveis por 2 ou por 3 são 50 + 33 − 16 = **67**.

**Complemento**: às vezes é mais fácil contar o que não serve. Senhas de 3 algarismos com pelo menos um repetido: 1000 − 720 = 280.

**Casa dos pombos**: se n + 1 objetos vão para n caixas, alguma caixa recebe pelo menos 2. Forma geral: com N objetos em k caixas, alguma tem pelo menos ⌈N/k⌉. Ex.: entre 13 pessoas, duas fazem aniversário no mesmo mês; entre 25 pessoas, pelo menos ⌈25/12⌉ = 3 nasceram no mesmo mês. Numa prova, diga quem são os objetos e quem são as caixas.

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** 1000, 720, 280, 175 760 000 e 67 conferidos por enumeração em Python; ⌈25/12⌉ = 3.
