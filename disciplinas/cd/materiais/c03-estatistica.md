---
id: cd-estatistica-em-ciencia-de-dados-media-mediana-assimetria-teste-de-normalidade
titulo: De que forma a Estatística auxilia a Ciência de Dados (três aplicações); média × mediana e assimetria (crie V1 com mediana menor que a média e V2 com mediana maior); histograma e teste de normalidade
assunto: cd-01-fundamentos
tipo: prova
questao: AB1 2020.1 Q3; AB1 2020.2 Q3; Lista 1 Q4-Q5
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
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB1 2020.1 Q3; AB1 2020.2 Q3; Lista 1 Q4-Q5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Aplicações da Estatística na Ciência de Dados:**
1. **descritiva:** resumir e explorar (média, mediana, desvio padrão, quartis, correlação, histogramas, box plots) e achar erros e outliers;
2. **inferência:** estimar com incerteza (intervalos de confiança) e **testar hipóteses** (o modelo A é melhor que o B? a diferença é significativa?);
3. **amostragem e desenho de experimentos:** amostras representativas, testes A/B;
4. **modelagem:** regressão, modelos probabilísticos (Naive Bayes), séries temporais; verificar suposições (normalidade, independência).

**Média × mediana:** a média é puxada por valores extremos; a mediana não. Assimetria à **direita** (cauda longa de valores altos): **mediana < média**. À **esquerda**: **mediana > média**.

Exemplo (Lista 1 Q4):
- $V_1 = [1, 2, 3, 4, 100]$: mediana 3, média 22: **mediana < média**;
- $V_2 = [-100, 1, 2, 3, 4]$: mediana 2, média $-18$: **mediana > média**.

**Histograma e normalidade (Q5)** em Python:
```python
import matplotlib.pyplot as plt
from scipy import stats

def analisar(dados, alfa=0.05):
    for nome, v in dados.items():
        plt.figure(); plt.hist(v, bins="auto"); plt.title(nome)
        estat, p = stats.shapiro(v)
        print(nome, "normal" if p > alfa else "não normal", round(p, 4))
```
O teste de **Shapiro-Wilk** tem hipótese nula "os dados vêm de uma normal": $p > 0{,}05$ **não rejeita** a normalidade (não prova que é normal). Com 5 valores o teste tem pouco poder; para amostras grandes, veja também o gráfico Q-Q.

**Verificação:** `test_media_mediana_e_normalidade` confere as medianas e médias de $V_1$ e $V_2$, roda `stats.shapiro` e mostra que uma amostra normal de 200 valores não é rejeitada e uma exponencial é.
