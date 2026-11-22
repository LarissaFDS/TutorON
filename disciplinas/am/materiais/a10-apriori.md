---
id: am-apriori-regras-de-associacao-suporte-confianca-juncao-e-poda
titulo: Descreva o algoritmo Apriori de mineração de regras de associação: suporte, confiança, itemsets frequentes, junção e poda, geração das regras
assunto: am-03-agrupamento-e-associacao
tipo: prova
questao: AB2 Q3
resolucao: sim
fonte: Provas de Aprendizagem de Máquina do Prof. Aydano Machado (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Aprendizagem de Máquina (COMP390); provas AB1 e AB2 (uma delas de 2021.1)
fontes_catalogo: ufal-aydano-provas-am, ufal-aydano-slides-am
autoria: Questões do Prof. Aydano Machado (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), AB2 Q3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Regra de associação** $A \Rightarrow B$ ($A$ e $B$ conjuntos de itens disjuntos), numa base de transações:
- **suporte** $= \frac{\#\text{transações com } A \cup B}{\#\text{transações}}$;
- **confiança** $= \frac{\text{sup}(A \cup B)}{\text{sup}(A)}$: das transações com $A$, a fração que também tem $B$.
O problema: achar todas as regras com suporte $\ge$ SupMin e confiança $\ge$ ConfMin.

**Apriori, fase 1: itemsets frequentes.** Princípio: **todo subconjunto de um itemset frequente é frequente** (e todo superconjunto de um infrequente é infrequente).
1. $L_1$: itens com suporte $\ge$ SupMin.
2. Para $k = 2, 3, \ldots$:
   - **junção:** gere candidatos $C_k$ unindo dois itemsets de $L_{k-1}$ que coincidem nos $k-2$ primeiros itens (em ordem);
   - **poda:** descarte o candidato que tenha **algum** subconjunto de tamanho $k-1$ fora de $L_{k-1}$ (não só o que tira o primeiro item);
   - **conte** o suporte dos que sobraram numa passada pela base; $L_k$ são os frequentes.
3. Pare quando $L_k$ for vazio.

**Fase 2: regras.** Para cada itemset frequente $F$ e cada subconjunto não vazio $A \subset F$, gere $A \Rightarrow F \setminus A$ se a confiança passar de ConfMin. Note que o algoritmo gera **itemsets** primeiro e **regras** depois.

**Exemplo:** transações {pão, leite}, {pão, fralda, cerveja, ovos}, {leite, fralda, cerveja, refri}, {pão, leite, fralda, cerveja}, {pão, leite, fralda, refri}; SupMin = 60% (3 de 5). $L_1$ = {pão, leite, fralda, cerveja}; $L_2$ = {pão, leite}, {pão, fralda}, {leite, fralda}, {fralda, cerveja}; {pão, leite, fralda} tem suporte 2/5 e cai. Regra cerveja ⇒ fralda: suporte 3/5, confiança 3/3 = 100%.

**Verificação:** `test_apriori` implementa junção, poda e contagem em Python, confere $L_1$, $L_2$ e a regra cerveja ⇒ fralda, e compara com uma busca por força bruta em todos os subconjuntos.
