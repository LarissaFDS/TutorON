---
id: prob-anot-uniforme-discreta-bernoulli
titulo: Distribuições uniforme discreta e de Bernoulli: função de probabilidade, média e variância
assunto: prob-05-distribuicoes-discretas
tipo: material_estudo
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Principais Distribuições Discretas_251011_130200.pdf" (2025.2), pág. 1
autoria: Otávio Joshua Costa Brandão Menezes (aluno, equipe TutorON), anotações de estudo; paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações pessoais do aluno); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia as anotações e não reproduz imagens
fontes_catalogo: ufal-prob-anotacoes-2025-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Anotações de aluno (2025.2), parafraseadas. Status da resolução: validada. Conferido com `scipy.stats.randint` e `bernoulli`.

**Uniforme discreta** nos inteiros $a, a+1, \dots, b$: todos os $n = b - a + 1$ valores têm a mesma probabilidade, $P(X = x) = 1/n$ (no gráfico, uma linha horizontal). Ex.: sortear um número de 1 a 10.
$$E(X) = \frac{a + b}{2}, \qquad \operatorname{Var}(X) = \frac{(b - a + 1)^2 - 1}{12}.$$
Para 1 a 10: $E(X) = 5{,}5$ e $\operatorname{Var}(X) = (100 - 1)/12 = 8{,}25$. (A variância da uniforme **contínua** é outra: $(b-a)^2/12$.)

**Bernoulli** com parâmetro p: um ensaio com dois resultados, sucesso (X = 1) com probabilidade p e fracasso (X = 0) com $q = 1 - p$.
$$P(X = x) = p^x\,q^{1-x},\ x \in \{0, 1\}; \qquad E(X) = 0\cdot q + 1\cdot p = p.$$
$E(X^2) = 0^2 q + 1^2 p = p$, então $\operatorname{Var}(X) = p - p^2 = p\,q$.

**Verificação:** `randint(1, 11).var()` dá 8,25; para p = 0,3, $\operatorname{Var} = 0{,}21$ e as probabilidades 0,7 + 0,3 somam 1.
