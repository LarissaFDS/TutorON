---
id: logica-primeira-ordem-semantica
titulo: Semântica de primeira ordem: modelo, universo, interpretação de predicados e avaliação de quantificadores
assunto: logica-10-primeira-ordem-semantica
tipo: material_estudo
resolucao: sim
fonte: Slides Lógica de predicados: Semântica (Tiago Massoni, UFCG); slides Linguagens de Primeira Ordem (Baldoino Fonseca, UFAL), semântica
fontes_catalogo: ufcg-massoni-slides, ufal-baldoino-slides-primeira-ordem
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL) e Prof. Tiago Massoni (UFCG), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: corrigida (resolução da equipe TutorON, não é gabarito do professor; conferida com Python; o original tem erro apontado abaixo).

Na primeira ordem não há tabela-verdade: é preciso um **modelo** $M$ com um universo não vazio $A$ e a interpretação de cada símbolo (constantes viram elementos, funções viram funções em $A$, predicados viram relações em $A$). $\forall x\,\varphi$ é V em $M$ se $\varphi$ é V para **todo** elemento de $A$ no lugar de $x$; $\exists x\,\varphi$, se é V para **algum**.

**Exemplo dos slides (estados de um programa):** $A=\{a,b,c\}$; constante $i$ (estado inicial) com $i^M=a$; $R(x,y)$ "há transição de $x$ para $y$" com $R^M=\{(a,a),(a,b),(a,c),(b,c),(c,c)\}$; $F(x)$ "estado final" com $F^M=\{b,c\}$.
- $\exists y\,R(i,y)$: V (de $a$ há transições).
- $\neg F(i)$: V ($a$ não é final).
- $\forall x\exists y\,R(x,y)$: V (todo estado tem sucessor; $b\to c$, $c\to c$).
- $\forall x\forall y\forall z(R(x,y)\land R(x,z)\to y=z)$ (transições determinísticas): F ($a\to a$ e $a\to b$).

**Consequência e validade:** $\Gamma\models\psi$ quando todo modelo de $\Gamma$ é modelo de $\psi$; $\psi$ é válida se é V em todos os modelos; satisfazível se é V em algum. Ex.: $\forall x(P(x)\to Q(x))\models\forall x\,P(x)\to\forall x\,Q(x)$, mas a recíproca não vale (universo $\{1,2\}$, $P=\{1\}$, $Q=\varnothing$).

**Correção nos slides de Baldoino:** a cláusula da negação aparece como "$\neg P$ é V se $\neg P$ é F"; o certo é "$\neg P$ é V se $P$ é F".

**Verificação:** as quatro fórmulas foram avaliadas em Python no modelo acima; a consequência foi testada sem contramodelo em universos de até 3 elementos, e o contramodelo da recíproca foi avaliado.
