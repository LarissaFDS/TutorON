---
id: ia-logica-fuzzy-conjuntos-nebulosos-funcoes-de-pertinencia-inferencia-de-mamdani-defuzzificacao-centroide-gorjeta
titulo: Sistemas baseados em regras fuzzy: conjuntos nebulosos e funções de pertinência, operadores mínimo e máximo, inferência de Mamdani, agregação e defuzzificação pelo centroide; exemplo da gorjeta
assunto: ia-04-incerteza-e-aprendizado
tipo: lista
questao: Lista 2 (2020.2), questão 3 sobre regras fuzzy com inferência de Mamdani
resolucao: sim
fonte: Listas 1 e 2 de Inteligência Artificial (IC-UFAL), 2020.2, Prof. Evandro de Barros Costa
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufal-ia-listas-2020-2
autoria: Questões do Prof. Evandro de Barros Costa (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), Lista 2 (2020.2), questão 3 sobre regras fuzzy com inferência de Mamdani (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Conjunto fuzzy:** cada elemento tem um **grau de pertinência** $\mu(x) \in [0,1]$, em vez de pertencer ou não. Funções comuns: triangular e trapezoidal.

**Operadores (Zadeh):** E = mínimo, OU = máximo, NÃO = $1-\mu$.

**Inferência de Mamdani**, em quatro passos:
1. **fuzzificação:** obter a pertinência das entradas nítidas em cada termo;
2. **avaliação das regras:** a força de "se serviço é bom E comida é ótima então gorjeta é generosa" é o **mínimo** das pertinências;
3. **implicação e agregação:** cada conclusão é **cortada** na força da regra (mínimo) e as conclusões são unidas pelo **máximo**;
4. **defuzzificação:** o **centroide** $z^* = \dfrac{\int z\,\mu(z)\,dz}{\int \mu(z)\,dz}$ dá o valor nítido.

**Exemplo:** serviço de 0 a 10 e gorjeta de 0 a 25 %. Com serviço 7, suponha $\mu_{\text{bom}}(7)=0{,}6$ e $\mu_{\text{excelente}}(7)=0{,}4$, e as regras "bom → média" e "excelente → generosa". A saída é a união de "média" cortada em 0,6 e "generosa" cortada em 0,4; o centroide fica entre os centros das duas, puxado para "média".

**Mamdani × Sugeno:** em Mamdani as conclusões são conjuntos fuzzy (é preciso defuzzificar); em Sugeno são funções das entradas, e a saída é uma média ponderada.

Na lista, desenhe as funções de pertinência, escreva as regras e mostre um caso com os números de cada passo.

**Verificação:** `test_mamdani_centroide` implementa o exemplo com funções triangulares e confere que o centroide fica entre os centros de "média" e "generosa", mais perto de "média".
