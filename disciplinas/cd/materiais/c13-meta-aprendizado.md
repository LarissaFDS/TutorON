---
id: cd-meta-aprendizado-meta-caracteristicas-meta-base-meta-aprendiz-recomendar-algoritmos
titulo: Meta-aprendizado: o que é, como ajuda empresas e usuários, e como construir um sistema (meta-características, meta-base, meta-aprendiz) para recomendar algoritmos ou hiperparâmetros do ARIMA
assunto: cd-04-series-meta-visualizacao
tipo: prova
questao: Final 2020.1 Q5; REAV 2 2020.1 Q5; AB2 2020.2 Q5; REAV AB2 2020.2 Q4; AB2 2021.1 Q4-Q5; Lista 2 Q5
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
Ciência de Dados, Prof. Bruno Pimentel (UFAL), Final 2020.1 Q5; REAV 2 2020.1 Q5; AB2 2020.2 Q5; REAV AB2 2020.2 Q4; AB2 2021.1 Q4-Q5; Lista 2 Q5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Meta-aprendizado:** "aprender a aprender". Usa a **experiência de problemas anteriores** para **recomendar**, num problema novo, o **algoritmo** ou os **hiperparâmetros** mais promissores, sem testar todas as opções.

**Construção do sistema:**
1. **Meta-características:** descrevem cada base de dados. Simples (número de exemplos, de atributos, de classes), **estatísticas** (assimetria, curtose, correlação média), de **teoria da informação** (entropia da classe) e *landmarkers* (desempenho de modelos baratos, como uma árvore de um nível). Para **séries temporais**: tamanho, força da tendência e da sazonalidade, autocorrelações, estacionariedade.
2. **Meta-base:** uma **linha por base de dados** anterior: as meta-características como atributos e, como **meta-rótulo**, o algoritmo ou a configuração que teve **melhor desempenho** nela (medido com validação, ex.: menor erro de previsão).
3. **Meta-aprendiz:** um classificador (árvore, k-NN, Random Forest) treinado na meta-base. Para uma base nova, extraem-se as meta-características e ele **prevê** o melhor algoritmo ou configuração.

**Exemplo ARIMA:** coletar muitas séries; para cada uma, testar uma grade de $(p, d, q)$ e guardar a de menor erro em dados de validação; meta-características da série como atributos; o meta-aprendiz recomenda $(p, d, q)$ para uma série nova.

**Empresas:** economizam **tempo e custo computacional** (menos testes), padronizam e automatizam a escolha de modelos (base do **AutoML**). **Usuários:** quem não é especialista recebe uma boa escolha inicial; o especialista explora menos.

**Verificação:** `test_meta_aprendizado` gera 40 bases sintéticas, rotula cada uma com o melhor entre k-NN e Naive Bayes por validação cruzada, extrai meta-características simples e mostra que um meta-aprendiz (árvore) acerta, em validação cruzada sobre as bases, pelo menos tanto quanto escolher sempre a classe mais frequente.
