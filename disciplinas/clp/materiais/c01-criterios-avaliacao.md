---
id: clp-razoes-criterios-legibilidade-escritabilidade-confiabilidade
titulo: Por que estudar conceitos de linguagens, critérios de avaliação (legibilidade, escritabilidade, confiabilidade, custo) e as premissas de FORTRAN, COBOL e PL/I
assunto: clp-01-criterios-e-historia
tipo: prova
questao: AB1 2013.1 Q1-Q3
resolucao: sim
fonte: Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (IC-UFAL)
curso: Ciência da Computação (UFAL), Conceitos de Linguagens de Programação (CCOM027); provas de 2011.2 a 2013.1
fontes_catalogo: ufal-alcino-provas-clp
autoria: Questões do Prof. Alcino Dall'Igna Jr. (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
status_resolucao: validada
revisao_humana: pendente
---
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB1 2013.1 Q1-Q3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Razões para estudar (Q1; basta explicar duas):**
- aumenta a capacidade de **expressar ideias**: quem conhece recursos de outras linguagens consegue simulá-los na sua;
- ajuda a **escolher a linguagem** adequada a um projeto;
- facilita **aprender linguagens novas**: os conceitos (escopo, tipos, passagem de parâmetros) se repetem;
- faz **entender a implementação** e usar melhor a linguagem (o custo de uma recursão, de uma coerção);
- contribui para o **avanço da computação**: linguagens melhores se impõem quando quem escolhe as entende.

**Critérios (Q2):**
- **Legibilidade:** facilidade de **ler e entender** programas. Contribuem a simplicidade, a ortogonalidade (poucas construções que se combinam de forma regular), os tipos de dados adequados, as estruturas de controle e a sintaxe clara.
- **Escritabilidade:** facilidade de **escrever** programas para um domínio. Contribuem a simplicidade, a ortogonalidade, o suporte a abstração e a expressividade.
- **Confiabilidade da linguagem:** o quanto a linguagem **ajuda a obter programas que se comportam conforme a especificação**: verificação de tipos, tratamento de exceções e restrição a apelidos (*aliasing*). Atenção: o professor lembra que é a confiabilidade da linguagem, não a de um programa escrito nela.
- **Custo:** treinamento, escrita, compilação, execução, manutenção.

**Premissas (Q3):**
- **FORTRAN:** computação **científica**, com ponto flutuante e arrays, e código executável **eficiente**, comparável ao escrito à mão.
- **COBOL:** aplicações **comerciais**, com aritmética decimal, registros, relatórios e sintaxe próxima do inglês.
- **PL/I:** **uma só linguagem** para os dois domínios (e para programação de sistemas), juntando os recursos de ambas; ficou grande e complexa.

**Verificação:** `test_criterios_nao_tem_conta` confere que o bloco cobre as três perguntas da prova; é questão conceitual, sem código a executar.
