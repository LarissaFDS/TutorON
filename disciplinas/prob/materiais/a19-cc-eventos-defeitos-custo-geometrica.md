---
id: prob-cc-eventos-defeitos-custo
titulo: Eventos em notação de conjuntos, dois defeitos independentes, lucro esperado com Poisson e custo até o primeiro sucesso (geométrica): correções do gabarito de 2013
assunto: prob-01-probabilidade-basica
tipo: prova
questao: Avaliação de 16/10/2013, Q1 a Q4 (folha com respostas)
semestre: 2013
resolucao: sim
fonte: Avaliações de Probabilidade e Estatística, Instituto de Computação da UFAL, Prof. Heitor S. Ramos Filho (turmas COMP221, COMP023, ECOM020) | Avaliação de 16/10/2013, Q1 a Q4 (folha com respostas)
curso: Ciência da Computação (UFAL), turmas COMP221 e COMP023 de 2013 (prova comum com ECOM020)
autoria: Enunciados: provas do Prof. Heitor S. Ramos Filho, parafraseadas pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia os enunciados e não reproduz a prova
fontes_catalogo: ufal-cc-prob-provas-heitor-2013
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Questões de prova de 2013 (enunciados parafraseados). Status da resolução: corrigida. Resolução da equipe TutorON, conferida com `scipy.stats`; não é gabarito do professor.

**Eventos A, B, C.** Ao menos um: $A\cup B\cup C$. Exatamente um: $(A\bar B\bar C)\cup(\bar AB\bar C)\cup(\bar A\bar BC)$. "Não mais de dois ocorrem" é o complementar de todos ocorrerem: $\overline{A\cap B\cap C}$.

**Dois tipos de defeito independentes**, $P(A)=0{,}1$ e $P(B)=0{,}05$, então $P(A\cap B)=0{,}005$. Não ter os dois: $1-0{,}005=0{,}995$. Ser defeituoso: $P(A\cup B)=0{,}145$. Só um tipo, sabendo que é defeituoso: $\dfrac{0{,}145-0{,}005}{0{,}145}\approx0{,}9655$.

**Lucro com falhas Poisson($t$).** $P=Ct-(X^2+X)$ e $E(X^2)=\operatorname{Var}X+(EX)^2=t+t^2$, logo $E(P)=Ct-t^2-2t$, máximo em $t=\dfrac{C-2}{2}$.

**Custo até o primeiro sucesso** (cada tentativa custa 1000 reais, cada falha mais 300, sucesso com probabilidade 0,2). X = número de tentativas é geométrica: $C=1000X+300(X-1)=1300X-300$, e $E(C)=1300\cdot5-300=6200$ reais. Custo maior que 2300 reais equivale a $X\ge3$: $P=0{,}8^2=0{,}64$.

**Divergência:** a folha de respostas dá $A\cap B\cap C$ para "não mais de dois", escreve $C=1000X-300$ no item a e responde 0,8 para "custo maior que 2300" (isso é $P(X\ge2)$, ou seja, custo de pelo menos 2300). **Correções da equipe:** o complementar, a fórmula $1300X-300$ e 0,64.

**Verificação:** `scipy.stats.geom` (média 5 e $P(X\ge3)=0{,}64$) e SymPy para o máximo de E(P).
