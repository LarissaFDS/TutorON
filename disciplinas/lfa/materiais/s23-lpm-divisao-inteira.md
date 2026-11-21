---
id: lfa-lpm-divisao-inteira-loop-sem-goto
titulo: Programa em LPM (linguagem minimal, LOOP sem GOTO) para a divisão inteira Z ← X/Y com X/0 = 0 — erro da resolução da turma (calcula o teto) e programa corrigido
assunto: lfa-07-funcoes-recursivas-programas
tipo: lista
questao: 1
resolucao: sim
fonte: Lista de exercícios (prova) de Teoria da Computação 2014.1, Profa. Eliana (UFAL), questão 1, com resolução manuscrita de aluno
fontes_catalogo: ufal-eliana-lista-2014-1
autoria: Enunciado da Profa. Eliana (UFAL); resolução manuscrita de aluno conferida por código pela equipe TutorON
licenca: Não declarada (lista); paráfrase, manuscrito não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Lista de 2014.1 da Profa. Eliana, questão 1 (enunciado parafraseado): escrever em LPM, **sem GOTO**, um programa para a divisão inteira $Z \leftarrow X/Y$, com $X/0 = 0$. Comandos: $x \leftarrow 0$, $x \leftarrow x+1$, $x \leftarrow y$ e LOOP $x$ … END, que repete o corpo o número de vezes que $x$ valia na entrada. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

Macros feitas só com esses comandos:
- **decremento** $x \leftarrow x \dot- 1$: $A \leftarrow 0$; LOOP $x$: $B \leftarrow A$; $A \leftarrow A+1$ END; $x \leftarrow B$. Inicie $B \leftarrow 0$ antes, para $x = 0$ continuar 0.
- **teste de zero** $U \leftarrow [x = 0]$: $U \leftarrow 0$; $U \leftarrow U+1$; LOOP $x$: $U \leftarrow 0$ END.

**Correção:** a resolução manuscrita da turma percorre $T = X, X-1, \dots, 1$ e faz $Z \leftarrow T$ sempre que $X \dot- T\cdot Y = 0$, isto é, quando $T \cdot Y \ge X$. A última atribuição é o **menor** $T$ com $T\cdot Y \ge X$: o programa calcula $\lceil X/Y \rceil$ (teto), não a divisão inteira. Exemplo: $X = 7, Y = 2$ dá 4, e o certo é 3. Só acerta quando a divisão é exata, quando $X = 0$ ou quando $Y = 0$.

**Programa corrigido** (conta os $T$ de 1 a $X$ com $T\cdot Y \le X$):
```
Z ← 0;  T ← 0
LOOP X
   T ← T + 1
   S ← T·Y            (LOOP T: LOOP Y: S ← S+1 END END, com S ← 0 antes)
   D ← S ∸ X          (LOOP X: decremento de D, com D ← S antes)
   E ← [D = 0]
   LOOP E: Z ← Z + 1 END
END
H ← [Y = 0];  LOOP H: Z ← 0 END
```
Com $Y > 0$, os $T$ com $T\cdot Y \le X$ são $1, \dots, \lfloor X/Y \rfloor$, então $Z = \lfloor X/Y \rfloor$. A última linha garante $X/0 = 0$ (sem ela, $Y = 0$ daria $Z = X$).

**Verificação:** o interpretador de `tests_acervo/lfa_verif.py` roda a transcrição do programa do aluno e o corrigido para $0 \le X < 10$ e $0 \le Y < 6$. O do aluno erra 15 dos 40 casos com $X < 8$, $Y < 5$ (sempre dá o teto); o corrigido acerta todos.
