---
id: discreta-relacoes-propriedades
titulo: Relações binárias — reflexiva, simétrica, antissimétrica, transitiva e fechos
assunto: discreta-04-relacoes
tipo: resolucao
resolucao: sim
questao: 2, 3, 5
fonte: Notas de aula do Prof. Pablo Sampaio (UFRPE), Relações, e 9ª lista; slides do Prof. Leandro Balby Marinho (UFCG), Relações; lista sobre Relações (UFCG, Prof. Leandro), questões 2, 3 e 5; Evaristo e Perdigão, Introdução à Álgebra Abstrata, seção 1.9
fontes_catalogo: ufrpe-discreta-pablo,ufcg-discreta-leandro,ufal-evaristo-algebra
autoria: Prof. Pablo Sampaio (UFRPE), Prof. Leandro Balby Marinho (UFCG) e Jaime Evaristo e Eduardo Perdigão (UFAL), parafraseados pela equipe TutorON com auxílio de IA; resoluções da equipe
licenca: Não declarada (material dos professores; livro sem licença aberta)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Uma **relação binária** R de A em B é um subconjunto de $A \times B$; escrevemos a R b quando $(a, b) \in R$. Uma relação **em** S é um subconjunto de $S \times S$.

Propriedades de R em S (todas são "para todo"; uma falha basta como contraexemplo):
- **reflexiva**: $(a, a) \in R$ para todo $a \in S$;
- **simétrica**: se $(a, b) \in R$, então $(b, a) \in R$;
- **antissimétrica**: se $(a, b) \in R$ e $(b, a) \in R$, então a = b;
- **transitiva**: se $(a, b) \in R$ e $(b, c) \in R$, então $(a, c) \in R$.

Simétrica e antissimétrica **não** são opostas: a igualdade {(1,1), (2,2)} é as duas coisas, e {(1,2), (2,1), (2,3)} não é nenhuma. Antissimétrica com (a, b) e (b, a) na relação obriga a = b (questão 2d da lista da UFCG).

Exemplos em $\mathbb{Z}$: ≤ é reflexiva, antissimétrica e transitiva; < é transitiva, mas não reflexiva; "a | b" em $\mathbb{Z}^+$ é reflexiva, antissimétrica e transitiva; "a ≡ b (mod n)" é reflexiva, simétrica e transitiva.

**Fechos** (lista da UFCG, Q3): S = {1, 2, 3, 4} e R = {(1,1), (1,2), (1,3), (2,3), (2,4), (4,1), (3,4)}.
- Fecho reflexivo: acrescente (2,2), (3,3), (4,4).
- Fecho simétrico: acrescente os inversos (2,1), (3,1), (3,2), (4,2), (1,4), (4,3).
- Fecho transitivo: repita "se (a,b) e (b,c), acrescente (a,c)" até não mudar nada. Aqui há o ciclo 1 → 2 → 4 → 1 e 3 → 4 → 1, então todo elemento alcança todos: o fecho transitivo é $S \times S$ inteiro (16 pares).

Exemplos pedidos na Q5 (um entre vários possíveis), em S = {1, 2, 3}: reflexiva e antissimétrica, mas não transitiva: identidade mais (1,2) e (2,3); reflexiva e transitiva, mas não simétrica: ≤; transitiva, mas nem reflexiva nem simétrica: {(1,2)}; reflexiva, mas nem simétrica nem transitiva: identidade mais (1,2) e (2,3) (falta (1,3) e (2,1)).

Status da resolução: validada (conferida por código pela equipe TutorON; a lista não traz gabarito).

**Verificação:** fechos e propriedades checados por código, testando todos os pares.
