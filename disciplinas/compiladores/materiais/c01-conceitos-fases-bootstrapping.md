---
id: comp-conceitos-linguagem-fonte-objeto-fases-e-passos-de-compilacao-diagramas-t-bootstrapping
titulo: Conceitos: linguagem-fonte e objeto, alto e baixo nível, fases e passos de compilação, diagramas T e bootstrapping
assunto: comp-01-fundamentos-e-analise-lexica
tipo: exercicio_resolvido
questao: questões de conceitos das provas de 2009 e 2010 e do POSCOMP 2003
resolucao: sim
fonte: Provas de Compiladores do Prof. Marcus Ramos (2009 e 2010), cópias da pasta da turma
curso: Ciência da Computação (UFAL), COMP263 Compiladores; provas de 2013 a 2017.1 e trabalhos de 2017.1 (o código ECOM045 aparece no cabeçalho da AB1 de 2017.1)
fontes_catalogo: ramos-provas-compiladores
autoria: Questões e respostas das provas do Prof. Marcus Ramos; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Compiladores (Ciência da Computação), questões de conceitos das provas de 2009 e 2010 e do POSCOMP 2003 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Linguagem-fonte** é a entrada de um processador de linguagens; **linguagem-objeto**, a saída. Alto nível: perto da linguagem natural (portável, legível, com abstrações). Baixo nível: perto do hardware; a **linguagem de montagem** só troca os códigos numéricos da **linguagem de máquina** por mnemônicos.

**Fases** são etapas coesas da tradução: análise léxica, sintática, semântica (de contexto), geração de código intermediário, otimização, geração de código. **Passo** é uma leitura completa do programa (do arquivo ou de uma representação intermediária, como a árvore). Um compilador de um passo executa todas as fases numa só leitura.

**Diagrama T:** um compilador $X/Y/Z$ traduz da linguagem $X$ para $Y$ e está escrito em $Z$. Compilar o compilador $X/Y/Z$ com um compilador $Z/W/W$ dá $X/Y/W$.

**Bootstrapping:** escrever o compilador da linguagem $L$ na própria $L$ (ou num subconjunto dela), compilando versões cada vez maiores com a anterior. Exemplo da prova de 2009, partindo de C/x86/x86:
- Java1/x86n/C compilado por C/x86/x86 dá Java1/x86n/x86;
- Java2/x86n/Java1 compilado por Java1/x86n/x86 dá Java2/x86n/x86, e assim até Java completo;
- por fim Java/x86/Java (com otimização) compilado duas vezes dá Java/x86/x86, que compila a si mesmo.
Vantagens: a linguagem é usada e testada cedo e cresce aos poucos (fonte maior, código-objeto melhor).

**POSCOMP 2003:** o compilador detecta **erros de sintaxe** do programa; erros que dependem da execução (resultados, aritméticos) não são vistos em tempo de compilação.

**Verificação:** `test_diagramas_t` compõe os diagramas T da sequência do bootstrapping.
