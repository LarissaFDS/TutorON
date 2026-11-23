---
id: comp-geracao-de-codigo-para-comandos-repeat-until-for-to-step-laco-controlado-por-contador-numero-de-iteracoes
titulo: Geração de código para laços: repeat-until, for-to-step e laço controlado por contador com número de iterações pré-calculado
assunto: comp-03-semantica-e-codigo-intermediario
tipo: exercicio_resolvido
questao: questões 4 e 5 da prova de 2015.2 e questão 8 da reavaliação
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
status_resolucao: validada
revisao_humana: pendente
---
Compiladores (Ciência da Computação), questões 4 e 5 da prova de 2015.2 e questão 8 da reavaliação (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**repeat L until EL** (executa $L$, avalia $EL$; repete enquanto for falsa):
```
EL.true  = S.prox
L.prox   = geraRot()
EL.false = geraRot()
S.cod = rot(EL.false) + L.cod + rot(L.prox) + EL.cod
```
O rótulo `EL.false` fica **antes** do corpo, então a condição falsa volta ao início; verdadeira segue para `S.prox`. Uma resposta da cópia punha `rot(EL.false)` só no fim, o que não repete o corpo.

**for AT to EN1 step EN2 do L end** (pré-teste, como a resolução do professor na cópia):
```
L.prox = geraRot(); prim = geraRot()
S.cod = AT.cod + goto(prim)
      + rot(L.prox) + EN2.cod + (AT.nome = AT.nome + EN2.nome)
      + rot(prim) + EN1.cod + if AT.nome > EN1.nome goto S.prox
      + L.cod + goto(L.prox)
```
A primeira passagem pula o incremento.

**Laço controlado por contador** com expressões pré-avaliadas: de $i$ até $j$ com passo $k > 0$, o número de iterações é
$$n = \max\left(0, \left\lfloor \frac{j - i + k}{k} \right\rfloor\right)$$
De 1 a 10 de 3 em 3: $\lfloor 12/3 \rfloor = 4$ (1, 4, 7, 10). Calcula-se $n$ uma vez e o laço decrementa um contador oculto, então mudar $j$ dentro do corpo não altera o número de voltas.

**Verificação:** `test_lacos` executa o código gerado e confere a fórmula do número de iterações.
