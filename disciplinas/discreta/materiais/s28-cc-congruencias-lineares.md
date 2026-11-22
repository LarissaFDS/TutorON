---
id: discreta-cc-congruencias-lineares
titulo: Resto de número negativo, inverso modular e congruência linear ax ≡ b (mod m) com todas as soluções (provas de CC)
assunto: discreta-09-aritmetica-modular-rsa
tipo: resolucao
resolucao: sim
questao: Prova 3 2020.1 e 2020.2; Reavaliação 2 e Final 2020.2
fonte: Provas do Prof. Bruno Pimentel (2020.1, 2020.2 e 2021.1) e revisão da monitoria da 3ª prova (2020.2)
curso: Ciência da Computação (UFAL), turmas de 2020.1 a 2021.1 (Prof. Bruno Pimentel)
fontes_catalogo: ufal-cc-discreta-provas-bruno,ufal-cc-discreta-monitoria
autoria: Prof. Bruno Pimentel (IC-UFAL) e revisão da monitoria, parafraseados (nomes dos monitores omitidos); resolução da equipe TutorON com auxílio de IA
licenca: Não declarada (provas do professor e material da monitoria)
publicacao_transcricao: não se aplica: o bloco parafraseia os enunciados e traz resolução própria; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Resolução da equipe TutorON, não é gabarito do professor. Status da resolução: validada.

**Negativo mod m:** o resto fica entre 0 e m − 1. $-155=-9\cdot19+16$, logo $-155 \bmod 19=16$; $-82 \bmod 15=8$; $-27 \bmod 10=3$. Responder −3 ou −7 é o erro típico.

**Inverso de a mod m** (existe só se $\mathrm{mdc}(a,m)=1$): faça Euclides e volte as contas até $1=sa+tm$; o inverso é s reduzido mod m. Resultados: $8^{-1}\equiv22 \pmod{25}$, $11^{-1}\equiv86 \pmod{135}$, $5^{-1}\equiv17 \pmod{21}$, $7^{-1}\equiv25 \pmod{29}$. Confira multiplicando: $11\cdot86=946=7\cdot135+1$.

**Congruência linear $ax\equiv b\pmod m$.** Seja $d=\mathrm{mdc}(a,m)$.
1. Se $d\nmid b$: sem solução.
2. Se $d=1$: solução única, $x\equiv b\,a^{-1}$. Ex.: $7x\equiv12 \pmod{40}$: $7^{-1}\equiv23$, $x\equiv12\cdot23=276\equiv36$. Também: $2x\equiv7 \pmod{17}$ dá $x=12$; $3x\equiv7 \pmod{20}$ dá $x=9$.
3. Se $d\mid b$ e $d>1$: divida tudo por d e resolva módulo $m/d$; há **d soluções** entre 0 e m − 1, espaçadas de $m/d$.
   - $9x\equiv18 \pmod{45}$: d = 9, $x\equiv2 \pmod 5$, soluções 2, 7, 12, …, 42 (nove);
   - $21x\equiv6 \pmod{69}$: d = 3, $7x\equiv2 \pmod{23}$, $7^{-1}\equiv10$, $x\equiv20$: soluções 20, 43, 66.

O enunciado pede "todas as soluções entre 0 e m": dar só uma, quando d > 1, deixa a resposta incompleta.

**Verificação:** cada resto, inverso e conjunto de soluções foi conferido em Python por força bruta em $0\le x<m$ e com pow(a, -1, m).
