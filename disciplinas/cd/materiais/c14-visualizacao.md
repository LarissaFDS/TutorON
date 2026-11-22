---
id: cd-visualizacao-de-dados-seis-etapas-contar-historia-engajamento-grafico
titulo: Como a visualização de dados ajuda o cientista de dados; seis etapas para apresentar resultados (contexto, visual adequado, eliminar a saturação, focar a atenção, pensar como designer, contar uma história); engajar o público; gráfico de recebidos × processados
assunto: cd-04-series-meta-visualizacao
tipo: prova
questao: AB2 2020.1 Q5; AB2 2020.2 Q6; REAV AB2 2020.2 Q5; AB2 2021.1 Q6; Lista 2 Q6
resolucao: sim
fonte: Provas e listas de Ciência de Dados do Prof. Bruno Pimentel (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Ciência de Dados (COMP401); turmas 2020.1, 2020.2 e 2021.1
fontes_catalogo: ufal-pimentel-provas-cd
autoria: Questões do Prof. Bruno Pimentel (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB2 2020.1 Q5; AB2 2020.2 Q6; REAV AB2 2020.2 Q5; AB2 2021.1 Q6; Lista 2 Q6 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Como ajuda:** na **análise exploratória** (achar padrões, outliers, erros e relações que tabelas e médias escondem, como no quarteto de Anscombe) e na **comunicação** dos resultados para quem decide.

**Seis etapas** (roteiro de Cole Nussbaumer Knaflic, *Storytelling with Data*, citado só como referência):
1. **entender o contexto:** quem é o público, o que ele precisa decidir e qual a mensagem principal (análise **explanatória**, não só exploratória);
2. **escolher o visual adequado:** linhas para tempo, barras para comparar categorias (começando do zero), dispersão para relação; evitar pizza com muitas fatias e 3D;
3. **eliminar a saturação** (*clutter*): tirar bordas, grades e rótulos redundantes;
4. **focar a atenção:** cor, tamanho e posição só no que importa; o resto em cinza;
5. **pensar como designer:** alinhamento, títulos que dizem a conclusão, acessibilidade (contraste, daltonismo);
6. **contar uma história:** começo (contexto), meio (o que os dados mostram) e fim (a ação recomendada).

**Engajar o público:** título com a **conclusão** ("o atraso começou em junho"), destacar um ponto, anotações no gráfico, comparar com uma meta, poucos números por slide, e terminar com o que se pede.

**Exercício (Lista 2 Q6):** recebidos e processados por mês. Gráfico de **linhas** com as duas séries, ou das **diferenças**: de janeiro a maio a equipe processa quase tudo (diferença de 0 a 4); a partir de junho surge um **acúmulo**: 11, 9, **46** (agosto), 34, 35, 25 e 37. O acúmulo do segundo semestre soma 197 pedidos. Destaque o intervalo junho–dezembro em cor e escreva no título: "a partir de junho, a equipe deixou de dar conta da demanda".

**Verificação:** `test_recebidos_processados` refaz as diferenças mês a mês, confere que antes de junho nenhuma passa de 4 e que o acúmulo de junho a dezembro soma 197.
