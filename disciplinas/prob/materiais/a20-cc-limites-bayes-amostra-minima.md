---
id: prob-cc-limites-bayes-amostra
titulo: Limites de P(A ∩ B) e P(A ∪ B), Bayes da pesquisa de mercado do celular, tentativas até achar um primo e tamanho mínimo de amostra para achar item defeituoso
assunto: prob-02-bayes
tipo: prova
questao: Avaliação de 26/06/2013, Q1, Q4, Q5 e Q7
semestre: 2013
resolucao: sim
fonte: Avaliações de Probabilidade e Estatística, Instituto de Computação da UFAL, Prof. Heitor S. Ramos Filho (turmas COMP221, COMP023, ECOM020) | Avaliação de 26/06/2013, Q1, Q4, Q5 e Q7
curso: Ciência da Computação (UFAL), turmas COMP221 e COMP023 de 2013 (prova comum com ECOM020)
autoria: Enunciados: provas do Prof. Heitor S. Ramos Filho, parafraseadas pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia os enunciados e não reproduz a prova
fontes_catalogo: ufal-cc-prob-provas-heitor-2013
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova de 2013 (enunciados parafraseados). Status da resolução: validada. Resolução da equipe TutorON, conferida com `scipy.stats`; não é gabarito do professor.

**Maior e menor valor possível de P(A ∩ B) e de P(A ∪ B)**, com $P(A)=3/4$ e $P(B)=1/3$. $P(A\cap B)\le\min=1/3$ (quando $B\subset A$) e $P(A\cap B)\ge P(A)+P(B)-1=1/12$ (quando $A\cup B$ é tudo). Para a união: $3/4\le P(A\cup B)\le1$, com os mesmos dois casos.

**Bayes: o celular vai ter sucesso, dado que a pesquisa previu sucesso?** S = sucesso, $P(S)=0{,}6$; $P(\text{prev}\mid S)=0{,}7$ e $P(\text{prev}\mid\bar S)=0{,}4$.
$$P(S\mid\text{prev})=\frac{0{,}6\cdot0{,}7}{0{,}6\cdot0{,}7+0{,}4\cdot0{,}4}=\frac{0{,}42}{0{,}58}\approx0{,}724.$$

**Quantos números de 1000 dígitos sortear até achar um primo?** Cada sorteio é primo com probabilidade cerca de 1/2302; o número de sorteios é geométrico, com média $1/p=2302$.

**Amostra mínima.** Lote de 1000 itens, 1% fora de conformidade; com a aproximação binomial pedida, $P(\text{ao menos um})=1-0{,}99^n\ge0{,}9$ dá $n\ge\dfrac{\ln0{,}1}{\ln0{,}99}\approx229{,}1$, logo $n=230$. A hipergeométrica exata (sem reposição) já chega a 0,9 com 205: a binomial superestima o tamanho.

**Verificação:** `scipy.stats.hypergeom` e `binom` para as amostras, conta direta para Bayes.
