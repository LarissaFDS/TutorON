---
id: logica-forma-clausal-skolem
titulo: Forma clausal na primeira ordem: forma prenex, skolemização, cláusulas e o procedimento de Herbrand
assunto: logica-12-forma-clausal-unificacao-resolucao
tipo: material_estudo
resolucao: sim
fonte: Slides de Resolução (Baldoino Fonseca, UFAL); Listas de Questões de lógica de primeira ordem (Baldoino Fonseca, UFAL), questões que pedem transformar em cláusulas
fontes_catalogo: ufal-baldoino-slides-primeira-ordem, ufal-baldoino-lista-primeira-ordem
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**O que é skolemização:** é o passo da forma clausal que elimina os quantificadores existenciais, trocando cada variável existencial por uma constante nova ou por uma função de Skolem. Para usar resolução, cada sentença vira um conjunto de cláusulas:
1. eliminar $\leftrightarrow$ e $\to$;
2. levar a negação até os átomos ($\neg\forall x\,\varphi\equiv\exists x\,\neg\varphi$, $\neg\exists x\,\varphi\equiv\forall x\,\neg\varphi$, De Morgan);
3. renomear variáveis para que cada quantificador tenha a sua e levar os quantificadores para a frente (**forma prenex**);
4. **skolemizar:** cada $\exists y$ vira uma constante nova (se não há $\forall$ antes) ou uma função nova dos $\forall$ que o precedem: em $\forall x\exists y\,\varphi$, troque $y$ por $f(x)$;
5. apagar os $\forall$ (variáveis livres são lidas como universais) e pôr a matriz em CNF; cada conjunção vira uma cláusula.
A skolemização preserva a satisfazibilidade (não a equivalência), que é o que a refutação precisa.

**Exemplo (cachorros):** $\exists x(C(x)\land\forall y(H(y)\to G(x,y)))$ dá as cláusulas $C(a)$ e $\neg H(y)\lor G(a,y)$ ($a$ é constante de Skolem). $\neg\exists x(C(x)\land\exists y(V(y)\land G(x,y)))$ dá $\neg C(x)\lor\neg V(y)\lor\neg G(x,y)$. A negação de "nenhum humano é vampiro" dá $H(b)$ e $V(b)$.

**Exemplo com função de Skolem (passageiros):** $\forall x(E(x)\land\neg V(x)\to\exists y(vd(x,y)\land P(y)))$ dá $\neg E(x)\lor V(x)\lor vd(x,f(x))$ e $\neg E(x)\lor V(x)\lor P(f(x))$.

**Herbrand:** um conjunto de cláusulas é insatisfazível se e somente se algum conjunto finito de **instâncias básicas** (sem variáveis) é insatisfazível em lógica proposicional. As listas pedem achar essas instâncias e refutar por resolução proposicional; a resolução de Robinson faz isso direto, com unificação.

**Verificação:** as cláusulas dos dois exemplos foram usadas nas refutações conferidas em Python passo a passo (unificação e resolvente recalculados).
