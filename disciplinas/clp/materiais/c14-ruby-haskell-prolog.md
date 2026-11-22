---
id: clp-iterador-ruby-yield-haskell-avaliacao-preguicosa-prolog-mundo-fechado
titulo: Saída do iterador Ruby com yield (soma dos termos de Fibonacci até 5), avaliação passo a passo de r [6,2,5] em Haskell com ++ preguiçoso, suposição do mundo fechado do Prolog
assunto: clp-06-subprogramas
tipo: prova
questao: AB2 2011.2 Q11; final 2012.2 Q3-Q4
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
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB2 2011.2 Q11; final 2012.2 Q3-Q4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Ruby (AB2 Q11).** O método
```ruby
def f(u)
  p, s = 1, 1
  while p <= u
    yield p
    p, s = s, p + s
  end
end
r = 0
f(5) { |n| r += n }
puts "#{r}"
```
é um **iterador**: `yield p` chama o bloco passado na chamada com o valor de `p`. Rastreando `p, s`: (1, 1) → (1, 2) → (2, 3) → (3, 5) → (5, 8) → (8, 13), que para o laço. Os valores entregues ao bloco são 1, 1, 2, 3, 5, e a saída é **12**. O bloco altera `r`, que é do escopo de fora (o bloco é um fechamento).

**Haskell (final Q4).** Com `r [] = []` e `r (a:x) = r x ++ [a]` (é a função que inverte uma lista):
```text
r [6,2,5]
= r [2,5] ++ [6]
= (r [5] ++ [2]) ++ [6]
= ((r [] ++ [5]) ++ [2]) ++ [6]
= (([] ++ [5]) ++ [2]) ++ [6]
= ([5] ++ [2]) ++ [6]
= [5,2] ++ [6]
= [5,2,6]
```
Com `++` associativo à esquerda e avaliação preguiçosa, os elementos só são produzidos quando pedidos: o primeiro, `5`, sai depois de descer até `r []`. Resultado: **[5, 2, 6]**.

**Prolog, mundo fechado (final Q3):** tudo o que **não pode ser provado** a partir dos fatos e regras é considerado **falso**. Se a base tem só `pai(joao, ana).`, a consulta `pai(joao, pedro)` responde *false*, não "desconhecido". Por isso a negação do Prolog (`\+`) é **negação por falha**: `\+ pai(joao, pedro)` sucede porque a prova falhou, não porque se provou o contrário.

**Verificação:** `test_ruby_haskell_prolog` reproduz o iterador com um gerador Python (soma 12, termos 1, 1, 2, 3, 5), aplica a reescrita da função `r` passo a passo ([5, 2, 6]) e simula a negação por falha numa base de fatos.
