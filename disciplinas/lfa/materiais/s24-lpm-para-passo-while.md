---
id: lfa-lpm-para-passo-2-e-while-com-goto
titulo: LPM — comando PARA X = 5 ATÉ 10 PASSO 2 com LOOP e GOTO, e por que WHILE (repetição indefinida) precisa de GOTO; programas LOOP só computam funções recursivas primitivas
assunto: lfa-07-funcoes-recursivas-programas
tipo: prova
questao: lista 2014.1, questão 2; Prova 2 de 2017.1, questão 3
resolucao: sim
fonte: Lista (prova) de Teoria da Computação 2014.1, Profa. Eliana (UFAL), questão 2, com resolução manuscrita de aluno; segunda avaliação 2017.1, questão 3
fontes_catalogo: ufal-eliana-lista-2014-1,ufal-eliana-prova2-2017-1
autoria: Enunciados da Profa. Eliana (UFAL); resolução manuscrita de aluno conferida por código e resolução da equipe TutorON
licenca: Não declarada (lista); paráfrase, manuscrito não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
**Lista 2014.1, questão 2:** implementar em LPM "PARA X = 5 ATÉ 10, PASSO 2, FAÇA P". **Prova 2 de 2017.1, questão 3:** mostrar como implementar o WHILE $x > 0$ em LPM. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Resolução da turma para o PARA (conferida):**
```
X ← 5
L: J ← 10;  M ← X
   LOOP J: (decremento de M) END       M = X ∸ 10
   Lb ← [M = 0]                        1 se X ≤ 10
   LOOP Lb: P;  X ← X+1;  X ← X+1;  GOTO L  END
```
P executa para $X = 5, 7, 9$, e o programa termina com $X = 11$. Está certo, mas usa GOTO. Como o número de repetições é conhecido, dá para fazer **sem GOTO**: $N = \lfloor (10-5)/2 \rfloor + 1 = 3$; $X \leftarrow 5$; LOOP $N$: P; $X \leftarrow X+2$ END.

**WHILE $x > 0$ DO P** (repetição indefinida) com GOTO:
```
L: SE x = 0 GOTO FIM      (teste de zero com a macro [x = 0])
   P
   GOTO L
FIM:
```

**Por que precisa de GOTO:** LOOP $x$ fixa o número de voltas na entrada do laço. Por isso:
- todo programa só com LOOP **sempre para**;
- ele computa exatamente as funções **recursivas primitivas**.

O WHILE pode repetir um número de vezes que depende do que P faz, ou nunca parar. Com WHILE (ou GOTO), a linguagem computa todas as funções parciais computáveis, como a máquina de Turing. Uma função total computável e não recursiva primitiva (a de Ackermann) mostra que a diferença é real.

**Verificação:** o interpretador de `tests_acervo/lfa_verif.py` roda a resolução da turma: P executa 3 vezes e $X$ termina em 11; a versão sem GOTO dá o mesmo; o WHILE com GOTO, com $P = $ "$x \leftarrow x \dot- 1$", termina com $x = 0$ para entradas até 20.
