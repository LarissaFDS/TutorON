---
id: logica-prova1-q2-greve
titulo: Prova 1 (2013), questão 2, e Lista Q4: a greve durou mais de 1 ano? Formalização e resolução
assunto: logica-06-resolucao-proposicional
tipo: prova
resolucao: sim
questao: 2
fonte: Prova 1 de Lógica Aplicada à Computação, 15/05/2013 (Profs. Evandro Costa e Baldoino Fonseca, UFAL), questão 2; Lista de Questões proposicional, Q4
fontes_catalogo: ufal-baldoino-prova1-2013, ufal-baldoino-lista-proposicional
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Questão de prova (paráfrase do enunciado) com resolução. Prova é atividade avaliativa: o tutor guia, não entrega. Status da resolução: pendente_professor (resolução da equipe TutorON, não é gabarito do professor; conferida com Python, mas a resposta esperada depende de uma premissa que o enunciado não traz).

**Enunciado (paráfrase):** S1: se o governo recusar um novo aumento, a greve terminará em menos de 1 ano, ou durará mais de 1 ano e os alunos perderão o ano. S2: o governo recusou, a greve terminou em menos de 1 ano e os alunos não perderam o ano. S3: a greve durou mais de 1 ano. Formalizar e provar, por resolução, que S3 segue de S1 e S2. "O que pode ser afirmado?" A Lista Q4 tem a mesma forma (congresso, lei, presidente pede demissão) e pede "prove ou disprove".

**Formalização:** $g$: governo recusa; $t$: termina em menos de 1 ano; $d$: dura mais de 1 ano; $a$: alunos perdem o ano. S1: $g\to(t\lor(d\land a))$; S2: $g\land t\land\neg a$; S3: $d$.

**Resultado: S3 não segue de S1 e S2, e $\neg$S3 também não segue.** Cláusulas: $\{\neg g,t,d\}$, $\{\neg g,t,a\}$, $\{g\}$, $\{t\}$, $\{\neg a\}$ e, para testar S3, $\{\neg d\}$. Não se chega a $\square$: a valoração $g$=V, $t$=V, $a$=F, $d$=F satisfaz tudo (contramodelo). Com $d$=V as premissas também ficam verdadeiras, então nada se pode afirmar sobre $d$ só com S1 e S2.

**O que depende do professor:** com a premissa implícita "se terminou em menos de 1 ano, não durou mais de 1 ano" ($t\to\neg d$), deriva-se $\neg d$: a greve **não** durou mais de 1 ano. O enunciado pede para "provar" S3, o que não é possível; a resposta esperada (afirmar $\neg$S3 com a premissa extra, ou só dizer que S3 não segue) não está no material.

**Verificação:** tabela-verdade em Python: S1, S2 $\not\models d$ e S1, S2 $\not\models\neg d$; com $t\to\neg d$, S1, S2 $\models\neg d$. Na leitura com "ou… ou" exclusivo da Lista Q4, o resultado é o mesmo.
