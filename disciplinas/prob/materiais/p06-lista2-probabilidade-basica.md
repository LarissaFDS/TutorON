---
id: prob-ec4-lista2-basica
titulo: Lista 2 de probabilidade básica com respostas conferidas: moedas, fichas, travessas de salgados, alarmes, jornais, vacinas de três fabricantes (Bayes) e mamografia
assunto: prob-01-probabilidade-basica
tipo: lista
questao: Lista 2, Q1 a Q18
semestre: 2025.2
resolucao: sim
fonte: Probabilidade - Lista 2.pdf | pp. 1–3
curso: Engenharia de Computação (UFAL), ECOM020
autoria: Enunciados e respostas: lista de exercícios de probabilidade da turma (autor não identificado no arquivo), parafraseados pela equipe TutorON; conferência da equipe TutorON com frações exatas em Python
licenca: Não declarada (material da disciplina); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia os enunciados e não reproduz a lista
fontes_catalogo: ufal-prob-ec4-lista2-basica
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Lista 2 de probabilidade (enunciados parafraseados), com as respostas que vêm no arquivo conferidas pela equipe TutorON. Status da resolução: corrigida (duas respostas do arquivo estão incompletas ou erradas; o resto confere).

Respostas que conferem: três moedas iguais 1/4; grávida só no 4º mês 0,8³ · 0,2 = 10,24%; ficha verde ou amarela 9/14; pastel 1/2 · 3/8 + 1/2 · 4/6 = 25/48; só um dos alarmes (95% e 90%) 0,95 · 0,10 + 0,05 · 0,90 = 14%; ímpar de 1 a 11 menor que 5: 2/6 = 1/3; ímpar de 1 a 20 ser 13: 1/10; homem ou prestador (35 efetivos, 20 homens; 15 prestadores, 5 mulheres): (30 + 15 − 10)/50 = 7/10; quatro cores em ordem sem reposição 4/16 · 4/15 · 4/14 · 4/13 = 8/1365; divisível por 3 ou 4 de 1 a 15: 7/15; 4 filhos: 3 e 1 (8/16) é mais provável que 2 e 2 (6/16); jornais (370 de 470) 78,72%; vacina defeituosa 0,45 · 1,5% + 0,35 · 2% + 0,20 · 2,75% = 1,925%; mamografia 0,008/(0,008 + 0,09504) ≈ 7,8%; três dados diferentes 5/9; soma 21 com dois d20: 20/400 = 1/20.

**Correções.**
- Bilhetes (4 de 50): o arquivo só dá 46/50, que é a chance de **não** ganhar. Ganhar: 4/50 = 8%.
- Vacina defeituosa ser chinesa (Bayes): 0,0055/0,01925 = 2/7 ≈ **28,57%**, não 28,75% (dígitos trocados).
- Carta ás, preta ou "número maior que 7": 10/13 só sai se valete, dama e rei contarem como maiores que 7 (4 + 26 + 24 − 2 − 12 = 40 cartas). Contando só 8, 9 e 10, são 34 cartas: 17/26. Vale dizer qual convenção se usa.

**Verificação:** frações refeitas com `fractions` em `tests_acervo/test_disciplina_prob.py`.
