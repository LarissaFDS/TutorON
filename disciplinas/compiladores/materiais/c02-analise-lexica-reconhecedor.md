---
id: comp-analise-lexica-tokens-lexemas-expressoes-regulares-reconhecedor-de-numeros-cooperacao-lexico-sintatico
titulo: Análise léxica: tokens e lexemas, separadores, expressões regulares, gramática regular equivalente e reconhecedor de números com sinal, fração e expoente
assunto: comp-01-fundamentos-e-analise-lexica
tipo: exercicio_resolvido
questao: questões de análise léxica das provas de 2009, 2010 e 2017.1 (POSCOMP 2003)
resolucao: sim
fonte: Provas de Compiladores do Prof. Marcus Ramos (2009 e 2010), cópias da pasta da turma
curso: Ciência da Computação (UFAL), COMP263 Compiladores; provas de 2013 a 2017.1 e trabalhos de 2017.1 (o código ECOM045 aparece no cabeçalho da AB1 de 2017.1)
fontes_catalogo: ramos-provas-compiladores,ufal-compiladores-provas
autoria: Questões e respostas das provas do Prof. Marcus Ramos; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Compiladores (Ciência da Computação), questões de análise léxica das provas de 2009, 2010 e 2017.1 (POSCOMP 2003) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Papel do léxico:** agrupar caracteres em **tokens** (categoria + **lexema**, com linha e coluna) e descartar separadores (espaços, tabulações, quebras de linha, comentários). O **sintático** verifica se a sequência de tokens forma um programa válido. Em `soma = soma + 1` o léxico entrega `id`, `=`, `id`, `+`, `num`; o sintático confere a atribuição. Normalmente o sintático pede um token por vez.

**Tokens por expressões regulares** (AB2 de 2017.1): `Id = [a-zA-Z][a-zA-Z0-9_]*`, `CteI = [1-9][0-9]*`, `CteR = [1-9][0-9]*.[0-9]+`, `OpA = + | -`, `OpM = * | / | %`.

**POSCOMP 2003:** a gramática $S = W\,Z$, $W = X \mid Y$, $X = x \mid x X$, $Y = y \mid y Y$, $Z = z \mid z Z$ gera $(x x^* \mid y y^*)\, z z^*$: uma ou mais letras $x$ **ou** uma ou mais $y$, seguidas de uma ou mais $z$.

**Reconhecedor recursivo de números** (prova de 2009) para $(+\mid-\mid\varepsilon)\,(d^+(\varepsilon \mid . \mid .d^*) \mid .d^+)\,(e(+\mid-\mid\varepsilon)d^+ \mid \varepsilon)$:

```python
def numero(s):
    i = 0
    def tem(c):  # olha o símbolo atual
        return i < len(s) and (s[i].isdigit() if c == "d" else s[i] == c)
    if tem("+") or tem("-"): i += 1
    if tem("d"):
        while tem("d"): i += 1
        if tem("."):
            i += 1
            while tem("d"): i += 1
    elif tem("."):
        i += 1
        if not tem("d"): return False
        while tem("d"): i += 1
    else:
        return False
    if tem("e"):
        i += 1
        if tem("+") or tem("-"): i += 1
        if not tem("d"): return False
        while tem("d"): i += 1
    return i == len(s)
```

Aceita `123`, `-45.312`, `+.76`, `5.44e2`, `+0.88e-35`; rejeita `.`, `e5`, `1e`, `+-1`.

**Verificação:** `test_reconhecedor_de_numeros` roda o reconhecedor e compara com a expressão regular.
