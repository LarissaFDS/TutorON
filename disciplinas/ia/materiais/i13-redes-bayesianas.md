---
id: ia-incerteza-redes-bayesianas-grafo-aciclico-tabelas-de-probabilidade-condicional-inferencia-regra-de-bayes
titulo: Incerteza: probabilidade condicional e regra de Bayes; redes bayesianas (grafo acíclico dirigido, tabelas de probabilidade condicional), representação do conhecimento e inferência por enumeração
assunto: ia-04-incerteza-e-aprendizado
tipo: lista
questao: Lista 2 (2020.2), questão 2 sobre redes bayesianas
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
Inteligência Artificial (IC-UFAL, 2020.2), Lista 2 (2020.2), questão 2 sobre redes bayesianas (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Regra de Bayes:** $P(H \mid E) = \dfrac{P(E \mid H)\,P(H)}{P(E)}$; em palavras, a crença em H depois da evidência E é proporcional à verossimilhança vezes a crença anterior.

**Rede bayesiana:** **grafo acíclico dirigido** em que cada nó é uma variável aleatória e cada arco indica influência direta. Cada nó tem uma **tabela de probabilidade condicional (TPC)** dados os pais. A conjunta fatora:
$$P(x_1,\dots,x_n) = \prod_i P(x_i \mid \text{pais}(X_i))$$
Isso exige bem menos números do que a tabela conjunta completa ($2^n - 1$ para $n$ variáveis booleanas).

**Exemplo (não é o do alarme, como pede a lista):** Internet (I) e Biblioteca (B) são pais de Aprovação (A). $P(I)=0{,}5$ e $P(B)=0{,}5$; $P(A \mid I,B)=0{,}9$, $P(A \mid I,\lnot B)=0{,}7$, $P(A \mid \lnot I,B)=0{,}6$, $P(A \mid \lnot I,\lnot B)=0{,}2$.
- **Inferência causal:** $P(A) = 0{,}25\,(0{,}9+0{,}7+0{,}6+0{,}2) = 0{,}6$.
- **Diagnóstica:** $P(I \mid A) = \dfrac{0{,}5\,(0{,}5\cdot0{,}9+0{,}5\cdot0{,}7)}{0{,}6} = \dfrac{0{,}4}{0{,}6} \approx 0{,}667$.

**Inferência:** por enumeração (soma sobre as variáveis ocultas), eliminação de variáveis ou amostragem; ferramentas como o Netica fazem isso e mostram as crenças atualizadas a cada evidência.

Na lista, explique a estrutura (quais arcos e por quê), dê as TPCs e mostre **uma conta** de inferência; percentuais tirados da ferramenta, sem a conta, não mostram o raciocínio.

**Verificação:** `test_rede_bayesiana` faz a enumeração do exemplo e confere $P(A)=0{,}6$ e $P(I \mid A) \approx 0{,}667$.
