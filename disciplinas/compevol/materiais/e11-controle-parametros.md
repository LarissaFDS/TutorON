---
id: compevol-controle-de-parametros-deterministico-adaptativo-autoadaptativo-graficos
titulo: Controle de parâmetros de um algoritmo evolucionário: determinístico, adaptativo e autoadaptativo; gráficos de melhor aptidão e média da população por geração e de soluções avaliadas (atividade 1 da ABN2)
assunto: compevol-04-atividades-2021
tipo: exercicio
questao: Atividade 1 da ABN2 (2021.1)
resolucao: sim
fonte: Atividades da turma 2021.1 de Computação Evolucionária (UFAL), página do curso
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: ufal-ce-atividades-2021,dianati-gaes
autoria: Atividade da turma 2021.1 (UFAL; docente não identificada no material); resolução conceitual da equipe TutorON
licenca: Não declarada (atividade); paráfrase, capturas de tela não versionadas
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Atividade 1 da ABN2 (2021.1) (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

A atividade pede um projeto de AE com controle de parâmetros. É **avaliativa**: aqui vão os conceitos, não o projeto pronto.

**Ajuste × controle:** *ajuste* (*tuning*) é escolher valores fixos antes de rodar (por tentativa ou busca); *controle* é **mudar os parâmetros durante a execução**. Três tipos (classificação de Eiben, Hinterding e Michalewicz):
1. **determinístico:** muda por uma **regra fixa no tempo**, sem olhar a busca. Ex.: $p_m(t) = p_0 \left(1 - \frac{t}{T}\right) + p_{\min}$, ou $\sigma(t) = \sigma_0 \cdot 0{,}99^t$;
2. **adaptativo:** muda com base em **retorno da busca**. Ex.: a regra do 1/5 da estratégia evolutiva; aumentar $p_m$ quando a diversidade da população cai;
3. **autoadaptativo:** o parâmetro vai **dentro do cromossomo** e evolui junto com a solução. Ex.: cada indivíduo carrega seu $\sigma$, com $\sigma' = \sigma\,e^{\tau N(0,1)}$.

**Gráficos pedidos:**
- **soluções consideradas:** número de avaliações da aptidão em cada geração e o **acumulado** até ela (com população $n$ e sem cache, $n$ por geração e $n \cdot t$ acumulado; com elitismo e cache, menos);
- **aptidão:** a do **melhor indivíduo** e a **média da população** a cada geração. O melhor (com elitismo) nunca piora; a média se aproxima dele quando a população converge. Uma distância que some cedo indica **perda de diversidade**.

Para comparar os três controles, rode várias sementes e plote a média das curvas.

**Verificação:** `test_controle_de_parametros` implementa os três controles numa EE na esfera com semente fixa, confere que o determinístico segue a regra, que o adaptativo e o autoadaptativo reduzem $\sigma$ perto do ótimo, e que o acumulado de avaliações é $n \cdot t$.
