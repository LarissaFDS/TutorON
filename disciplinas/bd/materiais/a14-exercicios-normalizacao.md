---
id: bd-aula-exercicios-normalizacao
titulo: Exercícios de BD — normalização: relação Aluno na 1FN e relação BOLETIM na 2FN
assunto: bd-07-dependencia-normalizacao
tipo: exercicio_resolvido
resolucao: sim
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 5 "Normalização", exercícios
fontes_catalogo: ufal-bd-slides,watt-dbdesign
autoria: Profª Maria Cristina Tenório (enunciados); resolução da equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Status da resolução: pendente de confirmação do professor (resolução da equipe TutorON). As DFs foram conferidas por um script de fecho de atributos nos testes do TutorON.

**Exercício 1 (1FN).** Aluno = {Matricula, Nome, Idade, DataNasc, DataMatricula, Disciplinas}. Disciplinas é multivalorado (um aluno cursa várias). Decomposição:
- Aluno(Matricula, Nome, Idade, DataNasc, DataMatricula)
- AlunoDisciplina(Matricula, Disciplina), chave {Matricula, Disciplina}.
Observação: Idade é derivável de DataNasc; guardar as duas causa inconsistência com o tempo. Pode-se calcular a idade na consulta.

**Exercício 2 (2FN).** BOLETIM = {matricula_aluno, codigo_materia, numero_prova, nota, data_prova, nome_aluno, endereco_aluno, nome_materia}.

DFs (hipóteses da equipe a partir dos nomes):
- matricula_aluno → nome_aluno, endereco_aluno
- codigo_materia → nome_materia
- codigo_materia, numero_prova → data_prova (a prova é a mesma para a turma)
- matricula_aluno, codigo_materia, numero_prova → nota

Chave candidata: {matricula_aluno, codigo_materia, numero_prova}; o fecho dela tem todos os atributos. As três primeiras DFs são parciais (dependem de parte da chave), então BOLETIM não está na 2FN. Decomposição na 2FN:
- Aluno(matricula_aluno, nome_aluno, endereco_aluno)
- Materia(codigo_materia, nome_materia)
- Prova(codigo_materia, numero_prova, data_prova)
- Nota(matricula_aluno, codigo_materia, numero_prova, nota)

Todas também estão na 3FN: nenhuma tem DF entre atributos não primários. Se a data da prova puder variar por aluno (segunda chamada), a DF de Prova não vale e data_prova fica em Nota.
