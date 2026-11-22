---
id: clp-seletores-aninhados-else-pendente-dangling-else
titulo: Problema do aninhamento de seletores bidirecionais (else pendente, dangling else) e duas soluções: regra do if mais próximo, chaves ou terminadores (end if), indentação
assunto: clp-05-expressoes-e-controle
tipo: prova
questao: AB2 2011.2 Q8
resolucao: sim
fonte: Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (IC-UFAL)
curso: Ciência da Computação (UFAL), Conceitos de Linguagens de Programação (CCOM027); provas de 2011.2 a 2013.1
fontes_catalogo: ufal-alcino-provas-clp
autoria: Questões do Prof. Alcino Dall'Igna Jr. (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB2 2011.2 Q8 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**O problema:** em
```c
if (soma == 0)
    if (conta == 0)
        resultado = 0;
else
    resultado = 1;
```
a gramática permite ligar o `else` ao primeiro ou ao segundo `if`. A indentação sugere o primeiro, mas a linguagem pode decidir outra coisa. É uma ambiguidade da gramática.

**Soluções (basta descrever duas):**
1. **Regra semântica fixa (C, C++, Java):** o `else` liga-se ao **`if` mais próximo ainda sem `else`**. No exemplo, o `else` é do `if (conta == 0)`, apesar da indentação. Para ligar ao de fora, usa-se chaves: `if (soma == 0) { if (conta == 0) resultado = 0; } else resultado = 1;`.
2. **Sintaxe que fecha o seletor:** exigir **terminador** (`end if` em Ada, `fi` no shell, `end` em Ruby) ou **chaves obrigatórias** (Perl, Go, Rust). Cada seletor tem fim explícito e a ambiguidade some.
3. **Indentação como sintaxe (Python):** o `else` pertence ao `if` com a mesma indentação.
4. **Restrição sintática (ALGOL 60):** proibir um `if` diretamente dentro do `then`; quem quiser aninhar põe o interno num bloco.

**Verificação:** `test_else_pendente` compila com gcc o exemplo com `soma = 1` e `conta = 0`: como o `else` é do `if` interno, `resultado` não muda (fica com o valor inicial, -1), e com as chaves passa a valer 1.
