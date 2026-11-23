---
id: comp-analise-semantica-verificacao-de-tipos-coercao-de-expansao-convreal-acoes-semanticas-tabela-de-simbolos
titulo: Análise semântica: verificação de tipos com tabela de símbolos, coerção de expansão (convreal), erro de tipo e ações para código de três endereços
assunto: comp-03-semantica-e-codigo-intermediario
tipo: exercicio_resolvido
questao: questão 1 da prova de 2015.2 e da AB2 de 2017.1
resolucao: sim
fonte: Provas de Compiladores do IC-UFAL (2013 a 2017.1)
curso: Ciência da Computação (UFAL), COMP263 Compiladores; provas de 2013 a 2017.1 e trabalhos de 2017.1 (o código ECOM045 aparece no cabeçalho da AB1 de 2017.1)
fontes_catalogo: ufal-compiladores-provas
autoria: Questões das provas de Compiladores do IC-UFAL; resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Compiladores (Ciência da Computação), questão 1 da prova de 2015.2 e da AB2 de 2017.1 (parafraseado). Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Enunciado (resumo):** `S = id '=' E`, `E = E + T | T`, `T = T * F | F`, `F = ( E ) | id`. Tipos `Int`, `Real` e `Indef`; `looktype(nome)` consulta a tabela de símbolos; operadores `+int`, `+real`, `*int`, `*real`, `=int`, `=real` e `convreal`. Tipos diferentes resultam em `Real`; só **coerção de expansão** (int para real); atribuição tem o tipo da variável; erro gera `Erro_Tipo(lin, col)`.

**Ações:**
- `F = id`: `p = looktype(id.lex)`; se `Indef`, erro; senão `F.tipo = p; F.nome = id.lex`;
- `E = E1 + T`: se os dois são `Int`, `E.tipo = Int` e gera `+int`; senão converte o operando `Int` com `t = geraTemp(); convreal op, t`, gera `+real` e `E.tipo = Real`; `E.nome = geraTemp()` recebe o resultado;
- `T = T1 * F`: igual, com `*int` e `*real`;
- `S = id = E`: variável `Int` e `E` `Real` é estreitamento: **erro**; variável `Real` e `E` `Int`: `convreal` antes de `=real`.

**Correção da resolução da cópia** em `T = T1 * F`: no ramo em que `T1` é `Int` e `F` é `Real`, o temporário convertido deve ir para `T1.nome` (estava `E1.nome`); no ramo em que `T1` é `Real`, testa-se `F.tipo == Int` (estava `T1.tipo`). Faltava também atribuir `E.tipo` e `T.tipo`.

**Exemplo:** `r = i + r * i` com `i` inteiro e `r` real:
```
t1 = convreal i
t2 = r *real t1
t3 = convreal i
t4 = t3 +real t2
r =real t4
```
E `i = r` é erro de tipo (estreitamento).

**Verificação:** `test_verificacao_de_tipos` implementa as ações e confere o código e os erros.
