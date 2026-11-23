---
id: comp-traducao-dirigida-por-sintaxe-gramatica-de-atributos-herdados-e-sintetizados-rotulos-prox-true-false
titulo: Tradução dirigida por sintaxe: gramática de atributos, atributos herdados e sintetizados (prox, true, false, cod, nome) e if-then-else para análise descendente
assunto: comp-03-semantica-e-codigo-intermediario
tipo: exercicio_resolvido
questao: questões 3 e 6 da prova de 2015.2
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
Compiladores (Ciência da Computação), questões 3 e 6 da prova de 2015.2 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Atributos sintetizados** são calculados a partir dos filhos (sobem na árvore): `cod`, `nome`, `tipo`, `lexval`. **Herdados** vêm do pai ou dos irmãos (descem): o rótulo seguinte `prox` e os rótulos de desvio `true` e `false` de uma expressão lógica.

Na gramática de comandos da prova:
- **herdados:** `S.prox`, `L.prox`, `EL.true`, `EL.false` (e os de `TL`, `FL`);
- **sintetizados:** `S.cod`, `L.cod`, `EL.cod`, `AT.cod`, `AT.nome`, `EN.nome`, `EN.cod`, `TN.nome`, `FN.nome`, `id.lexval`, `num.lexval`.

**if-then e if-then-else:**
- `S = if EL then L end`: `EL.true = geraRot(); EL.false = L.prox = S.prox; S.cod = EL.cod + rot(EL.true) + L.cod`;
- `S = if EL then L1 else L2 end`: dois rótulos novos; `L1.prox = L2.prox = S.prox`; `S.cod = EL.cod + rot(EL.true) + L1.cod + goto(S.prox) + rot(EL.false) + L2.cod`.

**Para análise descendente** (questão 6) as duas regras começam iguais: fatore.
- `S = if EL then L Sr`; `Sr = end | else L end`.
- Ações no meio da produção, antes de usar o atributo herdado: `EL.true` e `EL.false` antes de `EL`; `L.prox = S.prox` antes de `L`; `Sr.prox = S.prox` e `Sr.false = EL.false` antes de `Sr`.
- `S.cod = EL.cod + rot(EL.true) + L.cod + goto(S.prox) + Sr.cod`.
- `Sr = else L end`: `Sr.cod = rot(Sr.false) + L.cod`; `Sr = end`: `Sr.cod = rot(Sr.false)`.

**Verificação:** `test_if_then_else` gera e executa o código das duas formas.
