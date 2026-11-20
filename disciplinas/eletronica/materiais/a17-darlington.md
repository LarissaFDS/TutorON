---
id: eletronica-anot-darlington
titulo: Configuração Darlington: dois TBJ em cascata (emissor do primeiro na base do segundo), ganho βD = β1 + β2 + β1β2 ≈ β1β2
assunto: eletronica-06-tbj-regioes
tipo: resolucao
resolucao: sim
fonte: Anotações "Exercício parte 2" (22 out. 2026), p. 7–8
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

**Ligação:** os coletores são ligados juntos; o emissor de Q1 alimenta a base de Q2; a entrada é a base de Q1 e a saída é o emissor de Q2.

**Dedução:** $I_{E1} = (1 + \beta_1)I_B$ e $I_{B2} = I_{E1}$; $I_{E2} = (1 + \beta_2)I_{B2} = (1 + \beta_2)(1 + \beta_1)I_B$. Definindo $I_E = (\beta_D + 1)I_B$:
$$\beta_D = \beta_1 + \beta_2 + \beta_1\beta_2 \approx \beta_1\beta_2$$
(beta Darlington é beta um mais beta dois mais o produto, quase o produto).

Exemplo: $\beta_1 = \beta_2 = 100$ dá $\beta_D = 10\,200$. Na base, a queda é de dois $V_{BE}$: cerca de 1,4 V para silício.

**Verificação:** SymPy expande $(1 + \beta_1)(1 + \beta_2) - 1$ e chega a $\beta_1 + \beta_2 + \beta_1\beta_2$.
