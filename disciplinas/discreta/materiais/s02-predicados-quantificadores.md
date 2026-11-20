---
id: discreta-predicados-quantificadores
titulo: Predicados e quantificadores — "para todo", "existe" e como negar
assunto: discreta-01-nocoes-logica
tipo: material_estudo
fonte: Notas de aula do Prof. Pablo Sampaio (UFRPE), Lógica de Predicados de 1ª ordem, partes 1 e 2, e lista 6; slides do Prof. Leandro Balby Marinho (UFCG), Lógica de Predicados
fontes_catalogo: ufrpe-discreta-pablo,ufcg-discreta-leandro
autoria: Prof. Pablo Sampaio (UFRPE) e Prof. Leandro Balby Marinho (UFCG), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material dos professores)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Um **predicado** P(x) vira proposição quando x recebe um valor do **universo de discurso**. Quantificadores: $\forall x\, P(x)$ ("para todo x, P(x)") e $\exists x\, P(x)$ ("existe x tal que P(x)"). O universo precisa estar dito: "existe x com $x^2 = 2$" é falso em $\mathbb{Z}$ e verdadeiro em $\mathbb{R}$.

Negação (De Morgan para quantificadores):
- $\neg \forall x\, P(x) \equiv \exists x\, \neg P(x)$: para negar "todo inteiro é par", basta exibir um ímpar.
- $\neg \exists x\, P(x) \equiv \forall x\, \neg P(x)$.

A ordem dos quantificadores importa: em $\mathbb{Z}$, $\forall x\, \exists y\, (y > x)$ é verdadeira (tome y = x + 1), mas $\exists y\, \forall x\, (y > x)$ é falsa (não há inteiro maior que todos).

Tradução: "todo aluno de Computação gosta de lógica" fica $\forall x\, (C(x) \to G(x))$, com condicional. "Algum aluno de Computação gosta de lógica" fica $\exists x\, (C(x) \land G(x))$, com conjunção. Trocar os dois conectivos é o erro mais comum: $\exists x\, (C(x) \to G(x))$ já é verdadeira se existir alguém que não é de Computação.

Regras de generalização usadas nas provas: para provar $\forall x\, P(x)$, tome um x **arbitrário** e prove P(x) (prova universal); para provar $\exists x\, P(x)$, basta exibir um exemplo (prova existencial). Para refutar um "para todo", basta um **contraexemplo**.

**Verificação:** a negação dos quantificadores e o efeito da ordem foram conferidos por código num universo finito pequeno.
