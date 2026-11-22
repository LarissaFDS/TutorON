---
id: cd-series-temporais-componentes-tendencia-sazonalidade-ciclo-ruido-descoberta-de-informacao
titulo: Séries temporais: como ajudam na descoberta de informação, componentes (tendência, sazonalidade, ciclo, irregular), decomposição e previsão (ARIMA); dados de vendas de medicamentos
assunto: cd-04-series-meta-visualizacao
tipo: prova
questao: AB2 2020.1 Q4; REAV 2 2020.1 Q4; AB2 2020.2 Q4; REAV AB2 2020.2 Q3; AB2 2021.1 Q3; Lista 2 Q4 e Q8
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
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB2 2020.1 Q4; REAV 2 2020.1 Q4; AB2 2020.2 Q4; REAV AB2 2020.2 Q3; AB2 2021.1 Q3; Lista 2 Q4 e Q8 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Série temporal:** observações ordenadas no tempo, em geral a **intervalos regulares** (vendas mensais, temperatura diária). A ordem importa: valores próximos no tempo são correlacionados (**autocorrelação**).

**Componentes:**
- **tendência:** movimento de longo prazo (crescimento ou queda);
- **sazonalidade:** padrão que se repete com **período fixo e conhecido** (meses do ano, dias da semana);
- **ciclo:** oscilações de longo prazo **sem período fixo** (ciclos econômicos);
- **irregular** (ruído, resíduo): o que sobra, imprevisível.
Modelo **aditivo**: $Y_t = T_t + S_t + R_t$; **multiplicativo**, $Y_t = T_t \times S_t \times R_t$, quando a amplitude sazonal cresce com o nível.

**Como ajudam a descobrir informação:**
1. **descrever:** tendência (o negócio cresce?), sazonalidade (quando vende mais?);
2. **detectar anomalias:** picos e quedas fora do padrão, para investigar a causa;
3. **prever** valores futuros (ARIMA) para planejar estoque e equipe;

**Decomposição clássica:** a tendência é estimada por **média móvel** de comprimento igual ao período (12 para dados mensais); a sazonalidade é a média, por mês, da série sem tendência; o resto é o irregular.

**Medicamentos na Austrália (Lista 2 Q8):** a série mensal de vendas mostra **tendência crescente**, **sazonalidade anual** com pico em **janeiro** e queda em fevereiro, e **amplitude que cresce com o nível**: modelo multiplicativo (ou log da série). Não temos o arquivo do professor: confira com os dados.

**ARIMA(p, d, q):** autorregressivo de ordem $p$, $d$ diferenciações para tirar a tendência, média móvel de ordem $q$.

**Verificação:** `test_decomposicao` gera uma série mensal $10 + 0{,}5t + 5\sin(2\pi t/12)$ mais ruído, decompõe com média móvel centrada de 12 meses em NumPy e recupera a inclinação 0,5 e a amplitude sazonal 5 (tolerâncias de 0,05 e 0,5).
