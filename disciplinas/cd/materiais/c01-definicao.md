---
id: cd-ciencia-de-dados-definicao-diferenca-aprendizagem-de-maquina-estatistica-mineracao
titulo: Defina Ciência de Dados e diferencie de Aprendizagem de Máquina, Estatística, Mineração de Dados e Big Data; importância do conhecimento de domínio
assunto: cd-01-fundamentos
tipo: prova
questao: AB1 2020.1 Q1; Final 2020.1 Q1; REAV AB1 2020.2 Q1; AB1 2021.1 Q1 e Q4; Lista 1 Q1-Q3
resolucao: sim
fonte: Provas e listas de Ciência de Dados do Prof. Bruno Pimentel (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Ciência de Dados (COMP401); turmas 2020.1, 2020.2 e 2021.1
fontes_catalogo: ufal-pimentel-provas-cd
autoria: Questões do Prof. Bruno Pimentel (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
status_resolucao: validada
revisao_humana: pendente
---
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB1 2020.1 Q1; Final 2020.1 Q1; REAV AB1 2020.2 Q1; AB1 2021.1 Q1 e Q4; Lista 1 Q1-Q3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Ciência de Dados:** área **interdisciplinar** que extrai **conhecimento útil para decisões** a partir de dados. Cobre o ciclo inteiro: formular a pergunta, **coletar e integrar** dados, **limpar e pré-processar**, **explorar** (estatística descritiva e visualização), **modelar** (aprendizagem de máquina, estatística inferencial), **avaliar** e **comunicar** o resultado. Junta três competências: computação, estatística e **conhecimento do domínio**.

**Diferenças:**
- **Estatística:** ramo da matemática que coleta, resume e faz **inferência** com quantificação da incerteza (intervalos, testes de hipótese). Na Ciência de Dados, ela descreve os dados, verifica suposições e sustenta conclusões.
- **Aprendizagem de Máquina:** subárea da IA com algoritmos que **aprendem padrões** para prever ou agrupar. Na Ciência de Dados, é **uma etapa** (a modelagem), não o processo todo.
- **Mineração de Dados:** etapa do KDD que aplica algoritmos para **descobrir padrões** em grandes bases; usa aprendizagem de máquina e estatística.
- **Big Data:** dados com **volume, velocidade e variedade** que excedem ferramentas tradicionais (ver o bloco de Big Data). É um **tipo de dado e de infraestrutura**; a Ciência de Dados pode trabalhar com dados grandes ou pequenos.

Em uma frase: a estatística dá o rigor, a aprendizagem de máquina dá os modelos, a mineração busca padrões, o Big Data é a escala, e a Ciência de Dados usa tudo isso para responder uma **pergunta de negócio ou de pesquisa**.

**Conhecimento de domínio:** diz que pergunta vale a pena, que variáveis importam, se um valor é erro ou caso raro e se o resultado faz sentido. Sem ele, o modelo pode achar correlações espúrias ou usar variáveis que vazam a resposta (*data leakage*).

**Verificação:** `test_fundamentos_tem_as_diferencas` confere que o bloco distingue as cinco áreas e cita o conhecimento de domínio; é questão conceitual, sem código a executar.
