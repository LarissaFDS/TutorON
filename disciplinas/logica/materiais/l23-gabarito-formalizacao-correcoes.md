---
id: logica-gabarito-formalizacao-correcoes
titulo: Gabarito da lista de formalização em primeira ordem: o que está certo e o que foi corrigido
assunto: logica-09-primeira-ordem-formalizacao
tipo: exercicio
resolucao: sim
questao: Q1, Q3, Q4, Q6, Q8
fonte: Listas de Questões de lógica de primeira ordem (Baldoino Fonseca, UFAL), lista com gabarito (questões 1, 3, 4, 6 e 8)
fontes_catalogo: ufal-baldoino-lista-primeira-ordem
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
Exercício da turma (paráfrase do enunciado) com resolução. Status da resolução: corrigida (resolução da equipe TutorON, não é gabarito do professor; conferida com Python; o original tem erro apontado abaixo).

Uma das listas traz o gabarito das formalizações. Conferimos cada uma; resultado:

**Corretas:** Q1a $\forall x(x\in P\to\neg x\in N)$; Q1c $\forall x(x\in O\leftrightarrow\forall y(y\in x\to y\in N))$; Q1d (cláusula definida: existe um literal positivo e quaisquer dois positivos são iguais); Q4a–Q4d (trabalhos e avaliadores, com $a\ne b$, $a\ne c$, $b\ne c$ para "3 pessoas distintas"); Q6a, Q6b, Q6c e Q6e (grupo abeliano); Q8a–Q8f (professores, turmas, matrículas).

**Corrigidas:**
- **Q1b** ("o complementar de um positivo é negativo, e o de um negativo é positivo"): o gabarito usa $Comp(x,y)\leftrightarrow(\dots)$, o que também diria que quaisquer $x,y$ com a propriedade são complementares. Correto: $\forall x\forall y(Comp(x,y)\to((x\in P\to y\in N)\land(x\in N\to y\in P)))$.
- **Q1e**: "se $x$ é resolvente então existe um literal…" é uma implicação; o gabarito usa $\leftrightarrow$. Troque por $Res(x,y,z)\to\exists u\exists v(\dots)$.
- **Q3, S3** ("nenhuma pessoa desonesta é VIP"): o gabarito tem um símbolo trocado, "$\leftarrow V(x)$"; correto: $\forall x(D(x)\to\neg V(x))$.
- **Q6d** (comutatividade $x+y=y+x$): falta quantificar $v$. Correto: $\forall x\forall y\forall w\forall v(P(x,y,w)\land P(y,x,v)\to E(w,v))$.

Lembrete: o gabarito usa $\Rightarrow$ e $\Leftrightarrow$ para os conectivos $\to$ e $\leftrightarrow$.

**Verificação:** a correção de Q1b foi testada em Python com um modelo pequeno em que a versão do gabarito e a corrigida diferem; Q6d e as demais foram conferidas por leitura.
