---
id: ihc-system-usability-scale-sus-questionario-10-itens-calculo-da-pontuacao
titulo: System Usability Scale (SUS): questionário de 10 itens com escala de 1 a 5, cálculo da pontuação de 0 a 100 (itens ímpares e pares), interpretação e cuidados
assunto: ihc-02-avaliacao-de-usabilidade
tipo: exercicio
questao: trabalhos correlatos citados no projeto (medida de usabilidade com SUS)
resolucao: sim
fonte: Trabalhos correlatos citados no projeto da disciplina (2020.2); questionário SUS de John Brooke
curso: Ciência da Computação (UFAL), COMP395 Interação Homem-Máquina (ênfase Sistemas de Informação); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-ihc-etapas-projeto,brooke-sus
autoria: Fórmula de John Brooke (1986); explicação e exemplo da equipe TutorON
licenca: Não declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Interação Humano-Computador (IC-UFAL, 2020.2), trabalhos correlatos citados no projeto (medida de usabilidade com SUS) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**SUS** (John Brooke, 1986): questionário curto e muito usado para medir a **usabilidade percebida**. São 10 afirmações respondidas de 1 (discordo totalmente) a 5 (concordo totalmente), alternando positivas (itens ímpares) e negativas (itens pares).

**Cálculo:**
- item **ímpar**: contribuição = resposta − 1;
- item **par**: contribuição = 5 − resposta;
- some as 10 contribuições (de 0 a 40) e **multiplique por 2,5**.

$$\text{SUS} = 2{,}5\left[\sum_{i\ \text{ímpar}} (r_i - 1) + \sum_{i\ \text{par}} (5 - r_i)\right]$$

Em palavras: inverta os pares, desconte 1 dos ímpares, some tudo e multiplique por 2,5. O resultado vai de 0 a 100, mas **não é porcentagem**.

**Exemplo:** respostas 4, 2, 5, 1, 4, 2, 4, 2, 5, 1:
- ímpares (itens 1, 3, 5, 7, 9): 3 + 4 + 3 + 3 + 4 = 17;
- pares (itens 2, 4, 6, 8, 10): 3 + 4 + 3 + 3 + 4 = 17;
- total 34, e SUS = 34 × 2,5 = **85**.

**Interpretação:** a média de muitos estudos fica perto de **68**. Acima disso, a usabilidade percebida está acima da média. Compare versões ou produtos com o **mesmo** questionário e um número razoável de participantes. Com um usuário só (microteste), o SUS é ilustrativo e não conclusivo.

**Cuidados:**
- aplique **depois** das tarefas;
- não troque o sentido dos itens;
- item em branco recebe 3 (neutro), e isso deve ser registrado.

**Verificação:** `test_pontuacao_sus` calcula o exemplo (85), confere os extremos (0 e 100) e que respostas todas neutras (3) dão 50.
