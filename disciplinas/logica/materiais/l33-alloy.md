---
id: logica-alloy-especificacao
titulo: Alloy: assinaturas, relações, fatos, predicados, run e check com escopo (análise com SAT solver)
assunto: logica-13-model-checking-alloy
tipo: material_estudo
resolucao: sim
fonte: Slides Alloy (Rohit Gheyi e Tiago Massoni, UFCG)
fontes_catalogo: ufcg-massoni-slides
autoria: Prof. Tiago Massoni (UFCG; Alloy com Prof. Rohit Gheyi), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

Alloy é uma linguagem de especificação baseada em **lógica de primeira ordem** e **cálculo relacional**; a análise é **exaustiva até um escopo** e usa SAT solvers.

**Elementos:**
- `sig A { r: set B }`: assinatura = conjunto de objetos; campo = relação. Multiplicidades `set` (qualquer número), `one` (exatamente um), `lone` (zero ou um), `some` (um ou mais). `sig B extends A` cria subconjunto disjunto; `abstract sig` exige que todo objeto esteja num filho.
- `fact`: invariantes (conjunção de fórmulas). `pred` e `fun`: fórmulas e expressões com parâmetros. `assert`: propriedade a verificar.
- Fórmulas: `all x: A | ...` ($\forall$), `some x: A | ...` ($\exists$), `no`, `one`, `#A = 10`; `and`, `or`, `=>`, `<=>`, `!`; conjuntos `+` (união), `&` (interseção), `-` (diferença), `in` (subconjunto).
- Relações: junção `.` (composição: $(a,b)$ com $\{(b,c),(d,e),(b,f)\}$ dá $\{(a,c),(a,f)\}$), transposta `~`, fecho transitivo `^r` e reflexivo-transitivo `*r`.

**Análises:** `run pred for 2` procura uma **instância** que satisfaça fatos e predicado com no máximo 2 objetos por assinatura; `check assert for 2` procura **contraexemplo** no escopo. Não achar contraexemplo não prova a propriedade para escopos maiores.

**Exemplo dos slides (hierarquia de classes sem ciclo):** `sig Class { extend: lone Class }` e o fato `all c: Class | c !in c.^extend`: nenhuma classe estende a si mesma, nem direta nem indiretamente.

**Verificação:** a junção do exemplo e o fato do fecho transitivo foram conferidos em Python com relações pequenas (uma hierarquia com ciclo viola o fato; uma sem ciclo satisfaz).
