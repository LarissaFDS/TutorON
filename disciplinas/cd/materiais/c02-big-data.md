---
id: cd-big-data-3-vs-5-vs-volume-velocidade-variedade-veracidade-valor-desafios
titulo: Big Data: os 3 Vs e os 5 Vs (volume, velocidade, variedade, veracidade, valor), relação com Ciência de Dados e desafios do cientista de dados
assunto: cd-01-fundamentos
tipo: prova
questao: AB1 2020.1 Q2; Final 2020.1 Q2; REAV 1 Q2; AB1 2020.2 Q1-Q2; REAV AB1 2020.2 Q2; AB1 2021.1 Q2
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
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB1 2020.1 Q2; Final 2020.1 Q2; REAV 1 Q2; AB1 2020.2 Q1-Q2; REAV AB1 2020.2 Q2; AB1 2021.1 Q2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**3 Vs:**
- **Volume:** quantidade enorme (terabytes a petabytes); não cabe na memória nem num único disco;
- **Velocidade:** dados chegam continuamente e precisam ser processados rápido (fluxos de sensores, cliques, transações), às vezes em tempo real;
- **Variedade:** formatos diferentes: **estruturados** (tabelas), **semiestruturados** (JSON, XML, logs) e **não estruturados** (texto, imagem, vídeo, áudio).

**5 Vs:** os três acima mais
- **Veracidade:** qualidade e confiabilidade (ruído, dados faltantes, fontes duvidosas, vieses);
- **Valor:** o dado só importa se gerar conhecimento útil para decisões.

**Relação com Ciência de Dados:** Big Data descreve **dados e infraestrutura** (armazenamento e processamento distribuídos, como Hadoop/HDFS e Spark); Ciência de Dados é o **processo de extrair conhecimento**. A Ciência de Dados usa Big Data quando a escala exige, mas também trabalha com bases que cabem num computador.

**Desafios do cientista de dados com Big Data:**
1. **armazenamento e processamento distribuídos**: algoritmos precisam ser paralelizáveis (MapReduce, Spark); nem todo método escala;
2. **integração** de fontes heterogêneas com esquemas e identificadores diferentes;
3. **qualidade (veracidade):** limpeza em escala, duplicatas, faltantes;
4. **velocidade:** processar fluxos e atualizar modelos sem parar o sistema;
5. **amostragem e viés:** muitos dados não garantem representatividade;
6. **privacidade e ética**: dados pessoais, LGPD;
7. **custo** de infraestrutura e comunicação dos resultados.

**Verificação:** `test_fundamentos_tem_as_diferencas` confere que os 5 Vs e os desafios estão no bloco; a parte de processamento é ilustrada em `test_media_em_blocos_como_mapreduce`, que calcula a média de 1 milhão de valores em blocos (como no MapReduce) e confere que é igual à média direta.
