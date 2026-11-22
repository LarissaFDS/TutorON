---
id: prob-cc-servidor-erlang-weibull
titulo: Requisições num servidor Web (Poisson e exponencial), pacotes de 5 mensagens (Erlang), erros num setor de disco e vida de sensores (Weibull × exponencial)
assunto: prob-07-exponencial
tipo: prova
questao: 2ª Avaliação de 07/08/2013, Q1 a Q3; Avaliação de 26/06/2013, Q6
semestre: 2013
resolucao: sim
fonte: Avaliações de Probabilidade e Estatística, Instituto de Computação da UFAL, Prof. Heitor S. Ramos Filho (turmas COMP221, COMP023, ECOM020) | 2ª Avaliação de 07/08/2013, Q1 a Q3; Avaliação de 26/06/2013, Q6
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

**Servidor com tempo entre requisições exponencial de média 1 s.** O número de requisições em 1 s é Poisson(1). Mais de três: $1-e^{-1}(1+1+\tfrac12+\tfrac16)\approx0{,}0190$. Em 30 intervalos independentes, nenhum com mais de três: $(1-0{,}0190)^{30}\approx0{,}563$. Intervalo sem nenhuma requisição com probabilidade 0,1: $e^{-t}=0{,}1$, $t=\ln10\approx2{,}30$ s.

**Pacote de 5 mensagens, chegadas Poisson de 30 por minuto (0,5 por segundo).** O tempo de montagem é Erlang ($r=5$, $\lambda=0{,}5$/s): média $r/\lambda=10$ s e desvio $\sqrt r/\lambda\approx4{,}47$ s. $P(T<10)=1-\sum_{k=0}^{4}e^{-5}\tfrac{5^k}{k!}\approx0{,}560$ e $P(T<5)\approx0{,}109$ (com $\lambda t=2{,}5$).

**Erros num setor de disco.** Um erro a cada $10^5$ bits e setor de $4096\cdot8=32768$ bits: $\lambda\approx0{,}328$ por setor. Mais de um erro: $1-e^{-\lambda}(1+\lambda)\approx0{,}0433$. Setor com erro: $1-e^{-\lambda}\approx0{,}279$, então a média de setores lidos até o primeiro erro é $1/0{,}279\approx3{,}58$.

**Weibull ($\beta=2$, $\delta=4000$ h).** $P(X>3000)=e^{-0{,}75^2}\approx0{,}570$ e $P(X>6000\mid X>3000)=e^{-(1{,}5^2-0{,}75^2)}\approx0{,}185$. Uma exponencial com a mesma média ($4000\,\Gamma(1{,}5)\approx3545$ h) daria $\approx0{,}429$ nos **dois** itens: falta de memória. A Weibull com $\beta>1$ modela desgaste.

**Verificação:** `scipy.stats.poisson`, `gamma` (Erlang) e a fórmula da Weibull.
