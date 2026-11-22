---
id: prob-cc-overbooking-media-amostral
titulo: Overbooking: aproximação normal da binomial com correção de continuidade e número máximo de passagens; probabilidade da média amostral
assunto: prob-09-aproximacao-normal-tcl
tipo: prova
questao: 2ª Avaliação de 07/08/2013, Q4 e Q5
semestre: 2013
resolucao: sim
fonte: Avaliações de Probabilidade e Estatística, Instituto de Computação da UFAL, Prof. Heitor S. Ramos Filho (turmas COMP221, COMP023, ECOM020) | 2ª Avaliação de 07/08/2013, Q4 e Q5
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

**Overbooking.** 200 passagens para 185 lugares; cada passageiro aparece com probabilidade 0,9, independente. X ~ Binomial(200; 0,9), média 180 e desvio $\sqrt{18}\approx4{,}24$. Com correção de continuidade:
$$P(X\le185)\approx\Phi\!\left(\frac{185{,}5-180}{4{,}24}\right)=\Phi(1{,}30)\approx0{,}903.$$
A binomial exata dá 0,907.

**Quantas passagens vender para que todos tenham lugar com probabilidade 0,95?** Procure o maior n com $\Phi\!\left(\frac{185{,}5-0{,}9n}{\sqrt{0{,}09n}}\right)\ge0{,}95$: com 198 dá cerca de 0,958, e com 199 cai para 0,935. Resposta: 198 passagens (a binomial exata também dá 198).

**Média amostral.** Amostras de 25 de uma normal com média 100 e desvio 10: $\bar X$ tem desvio $10/\sqrt{25}=2$. A probabilidade de $\bar X$ cair entre a média menos 1,8 desvio e a média mais 1,0 desvio é $\Phi(1)-\Phi(-1{,}8)\approx0{,}805$, para qualquer média e desvio.

Erros comuns: esquecer a correção de continuidade (0,5) e usar o desvio da população (10) no lugar do desvio da média (2).

**Verificação:** `scipy.stats.norm` e `binom`, com varredura de n de 190 a 199.
