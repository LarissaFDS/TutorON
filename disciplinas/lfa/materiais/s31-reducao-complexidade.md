---
id: lfa-reducao-por-mapeamento-e-complexidade
titulo: Redutibilidade — redução por mapeamento A ≤m B, E_TM e EQ_TM indecidíveis, teorema de Rice, correspondência de Post; noções de complexidade: tempo, classes P e NP
assunto: lfa-09-reducao-complexidade
tipo: material_estudo
resolucao: nao
fonte: Aulas 9 a 14 das notas de Sipser (MIT, Holden Lee), redutibilidade, PCP e complexidade de tempo; ementa de ECOM014
fontes_catalogo: lee-sipser-notas-2012,mit-ocw-18-404j,ufal-ppc-ecomp-2014
autoria: Aulas de Michael Sipser (MIT) nas notas de Holden Lee; paráfrase da equipe TutorON
licenca: Notas sem licença declarada; paráfrase. Curso aberto MIT OCW 18.404J sob CC BY-NC-SA 4.0
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
revisao_humana: pendente
---
**Redução por mapeamento:** $A \le_m B$ se existe uma função **computável** $f$ com $w \in A \iff f(w) \in B$ para toda $w$.
- Se $B$ é decidível, $A$ também é: calcule $f(w)$ e use o decisor de $B$.
- Pela contrapositiva: se $A$ é indecidível e $A \le_m B$, então $B$ é indecidível.
- O mesmo vale para "reconhecível". $A \le_m B$ também dá $\overline{A} \le_m \overline{B}$.

**Exemplo — $E_{TM} = \{\langle M\rangle \mid L(M) = \emptyset\}$ é indecidível.** Dado $\langle M, w\rangle$, construa $M_w$, que com entrada $x$ ignora $x$, simula $M$ sobre $w$ e aceita se $M$ aceitar. Então $L(M_w) = \Sigma^*$ se $M$ aceita $w$, e $L(M_w) = \emptyset$ se não aceita. Logo, $\langle M, w\rangle \mapsto \langle M_w\rangle$ reduz $A_{TM}$ a $\overline{E_{TM}}$, e um decisor de $E_{TM}$ decidiria $A_{TM}$.

Em seguida, $EQ_{TM}$ ("duas MT reconhecem a mesma linguagem?") não é decidível, por redução de $E_{TM}$: compare com uma MT que rejeita tudo.

**Teorema de Rice:** toda propriedade **não trivial** da **linguagem** reconhecida por uma MT não é decidível. Exemplos: "$L(M)$ é regular?" e "$L(M)$ contém 0101?". Propriedades da **máquina** (como "tem 5 estados?") podem ser decidíveis.

**Correspondência de Post (PCP)** e ambiguidade de GLC também não são decidíveis, por redução com histórias de computação.

**Noções de complexidade** (a ementa termina em "complexidade computacional"; o aprofundamento é de PAA):
- $\text{TIME}(t(n))$: linguagens decididas por MT de uma fita em $O(t(n))$ passos.
- **P**: decidíveis em tempo polinomial por MT determinística.
- **NP**: verificáveis em tempo polinomial a partir de um certificado, ou decididas por MT não determinística em tempo polinomial.
- **P = NP?** está em aberto.
- Mudar de modelo (várias fitas para uma fita) custa no máximo um fator polinomial, então P não depende do modelo.

**Verificação:** a direção de cada redução foi conferida passo a passo pela equipe contra as notas de aula; não há conta a executar.
