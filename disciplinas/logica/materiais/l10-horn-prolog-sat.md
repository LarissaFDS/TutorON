---
id: logica-horn-prolog-sat
titulo: Fórmulas de Horn, algoritmo de marcação, Prolog e SAT solvers
assunto: logica-05-formas-normais-horn-sat
tipo: material_estudo
resolucao: sim
fonte: Slides Forma Normal: Transformações (Tiago Massoni, UFCG), partes Fórmulas Horn, Horn em Prolog e SAT Solvers
fontes_catalogo: ufcg-massoni-slides
autoria: Prof. Tiago Massoni (UFCG; Alloy com Prof. Rohit Gheyi), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Fórmula de Horn:** conjunção de cláusulas de Horn, cada uma da forma $p_1\land\dots\land p_k\to q$, em que os $p_i$ são átomos ou $\top$ e $q$ é átomo ou $\bot$ (nenhum átomo aparece negado). Satisfazibilidade de Horn se decide rápido (tempo polinomial).

**Algoritmo HORN (marcação):**
1. marque $\top$;
2. enquanto houver cláusula $p_1\land\dots\land p_k\to q$ com todos os $p_i$ marcados e $q$ não marcado, marque $q$;
3. se $\bot$ foi marcado, a fórmula é **insatisfazível**; senão é **satisfazível** (átomos marcados V, demais F).

**Exemplos dos slides:** $(p\to\bot)\land(r\to p)\land(\top\to p)$: marca $p$ (por $\top\to p$), depois $\bot$: insatisfazível. $(p\to r)\land(\top\to p)$: marca $p$, depois $r$: satisfazível com $p$=V, $r$=V.

**Prolog:** a regra `p1 :- p2, p3, p4.` é a cláusula de Horn $p_2\land p_3\land p_4\to p_1$; um fato `p2.` é $\top\to p_2$. A consulta tenta casar o objetivo com um fato ou com a cabeça de uma regra e prova recursivamente o corpo.

**SAT solvers:** decidem se existe valoração que torna uma fórmula proposicional verdadeira. Os slides usam isso para checar restrições de um modelo UML: (loja da internet $\to$ sem clientes) $\land$ (loja da internet é loja) $\land$ (ao menos 1 cliente) é insatisfazível quando a loja é da internet. O solver linear dos slides marca nós de um grafo (DAG) da fórmula e propaga; é rápido mas **incompleto**: há fórmulas satisfazíveis em que ele não decide sem testar casos.

**Verificação:** os dois exemplos de Horn foram conferidos por tabela-verdade em Python (o primeiro sem modelo; o segundo com o modelo indicado).
