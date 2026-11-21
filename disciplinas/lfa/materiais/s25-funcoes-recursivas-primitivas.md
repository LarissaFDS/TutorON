---
id: lfa-funcoes-recursivas-primitivas-composicao
titulo: Funções recursivas primitivas — zero, sucessor, projeção, composição e recursão primitiva; soma, multiplicação, potência, monus; f(x,y,z) = (x+y, y+2z, z^z) e função de um programa LPM
assunto: lfa-07-funcoes-recursivas-programas
tipo: lista
questao: 3 e 4
resolucao: sim
fonte: Lista (prova) de Teoria da Computação 2014.1, Profa. Eliana (UFAL), questões 3 e 4, com resolução manuscrita de aluno
fontes_catalogo: ufal-eliana-lista-2014-1
autoria: Enunciados da Profa. Eliana (UFAL); resolução da equipe TutorON (a do aluno usa a notação de composição da disciplina e foi lida, não transcrita)
licenca: Não declarada (lista); paráfrase, manuscrito não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista 2014.1, questões 3 e 4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Funções básicas:** zero $Z(x) = 0$, sucessor $S(x) = x+1$ e projeções $\pi_i(x_1, \dots, x_n) = x_i$. Elas são fechadas por **composição** e por **recursão primitiva**:
$$f(0, \vec y) = g(\vec y) \qquad f(n+1, \vec y) = h(n, f(n, \vec y), \vec y)$$

**Funções construídas:**
- $\text{soma}(0, y) = y$; $\text{soma}(n+1, y) = S(\text{soma}(n, y))$.
- $\text{mult}(0, y) = 0$; $\text{mult}(n+1, y) = \text{soma}(\text{mult}(n, y), y)$.
- $\text{pot}(0, y) = 1$; $\text{pot}(n+1, y) = \text{mult}(\text{pot}(n,y), y)$, que dá $y^n$.
- $\text{pred}(0) = 0$; $\text{pred}(n+1) = n$.
- $x \dot- n$ (monus, "x menos n, sem passar de zero") aplica pred $n$ vezes.
- $\text{sg}(x) = 1$ se $x > 0$; senão, 0.

**Questão 3:** $f(x,y,z) = (x+y,\; y+2z,\; z^z)$. Cada componente é composição de primitivas recursivas:
- $f_1 = \text{soma}(\pi_1, \pi_2)$;
- $f_2 = \text{soma}(\pi_2, \text{mult}(2, \pi_3))$, em que a constante 2 é $S(S(Z))$;
- $f_3 = \text{pot}(\pi_3, \pi_3)$.

Uma função com várias saídas é recursiva primitiva quando cada componente é. A resposta da turma usa a notação de produto e composição de funções da disciplina e chega às mesmas três componentes. Ela não foi conferida símbolo a símbolo, porque é manuscrita.

**Questão 4:** o programa faz $v \leftarrow x \dot- y$; $k \leftarrow (z > v)$; $t \leftarrow (v > 0) \wedge k$. Então:
$$t(x,y,z) = \text{sg}(x \dot- y) \cdot \text{sg}(z \dot- (x \dot- y))$$
Isso vale 1 exatamente quando $0 < x - y < z$ (com $x > y$); senão, vale 0. Comparações viram $\text{sg}$ de um monus, e o "e" vira produto.

**Verificação:** `tests_acervo/lfa_verif.py` monta soma, mult, pot, pred e monus só com zero, sucessor, projeção e recursão; compara $f$ e $t$ com as fórmulas diretas para $x, y, z$ de 0 a 5.
