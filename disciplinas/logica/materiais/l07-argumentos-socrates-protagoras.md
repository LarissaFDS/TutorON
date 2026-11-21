---
id: logica-argumentos-classicos
titulo: Argumentos clássicos dos slides: Sócrates e Platão, João e Maria, Protágoras e Euathlus
assunto: logica-03-consequencia-equivalencia
tipo: material_estudo
resolucao: sim
fonte: Slides de Lógica Clássica Proposicional e Linguagens Proposicionais (Baldoino Fonseca, UFAL), exemplos de formalização
fontes_catalogo: ufal-baldoino-slides-proposicional
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Sócrates e Platão.** $P$: Sócrates está disposto a visitar Platão; $Q$: Platão está disposto a visitar Sócrates. Sócrates: $Q\to P$. Platão: $(P\to\neg Q)\land(\neg P\to Q)$. Pergunta: vale $P$ ou $\neg P$?
- Se $P$ fosse F, a segunda premissa forçaria $Q$=V e a primeira forçaria $P$=V: contradição. A única valoração que satisfaz as premissas é $P$=V, $Q$=F. Logo $\{Q\to P,\;(P\to\neg Q)\land(\neg P\to Q)\}\models P$: Sócrates está disposto; Platão não.
- João e Maria tem a mesma forma ($A$: João disposto; $B$: Maria disposta): $(B\to A)\land(A\to\neg B)\land(\neg A\to B)\models A$.

**Protágoras e Euathlus.** $A$: Euathlus ganha o caso; $B$: ganha o primeiro caso; $C$: deve pagar. Protágoras: $((A\to B)\land(B\to C)\land(\neg A\to C))\to C$. Euathlus: $((A\to\neg C)\land(\neg A\to\neg B)\land(\neg B\to\neg C))\to\neg C$.
- **Os dois argumentos são válidos** (cada fórmula é tautologia), mas as seis premissas juntas são **insatisfazíveis**. Cada um escolheu premissas a seu favor; a lógica garante a forma do argumento, não a verdade das premissas.

**Verificação:** por tabela-verdade em Python: as consequências de Sócrates e de João e Maria, as duas tautologias do paradoxo e a insatisfazibilidade das seis premissas.
