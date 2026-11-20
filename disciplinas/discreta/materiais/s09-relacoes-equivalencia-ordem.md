---
id: discreta-relacoes-equivalencia
titulo: Relação de equivalência, classes, partição e ordem parcial (como saber se é de equivalência)
assunto: discreta-04-relacoes
tipo: resolucao
resolucao: sim
questao: 4, 6, 8
fonte: Slides do Prof. Leandro Balby Marinho (UFCG), Relações (equivalência e ordem); lista sobre Relações (UFCG), questões 4, 6 e 8; respostas da 7ª lista do Prof. Pablo Sampaio (2011.1), questões 3 e 5; Evaristo e Perdigão, seção 1.9
fontes_catalogo: ufcg-discreta-leandro,ufrpe-discreta-pablo,ufal-evaristo-algebra
autoria: Prof. Leandro Balby Marinho (UFCG), Prof. Pablo Sampaio (UFRPE) e Jaime Evaristo e Eduardo Perdigão (UFAL), parafraseados pela equipe TutorON com auxílio de IA; resoluções da equipe
licenca: Não declarada (material dos professores; livro sem licença aberta)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Uma relação R em S é **de equivalência** se é **reflexiva, simétrica e transitiva**. Para saber se uma relação é de equivalência, teste as três propriedades; para mostrar que não é, basta exibir um par que quebre uma delas.

Exemplo: em $\mathbb{Z}$, a R b se 3 | (a − b). Reflexiva: 3 | 0. Simétrica: se a − b = 3k, então b − a = 3(−k). Transitiva: se a − b = 3k e b − c = 3j, então a − c = 3(k + j). ∎ Contraexemplo: "a R b se |a − b| ≤ 1" é reflexiva e simétrica, mas não transitiva (0 R 1 e 1 R 2, mas não 0 R 2).

**Classe de equivalência** de a: $[a] = \{x \in S \mid x \, R \, a\}$. As classes formam uma **partição** de S: são não vazias, disjuntas duas a duas e cobrem S. Na congruência módulo 3, as classes são [0], [1] e [2]. Na lista da UFCG (Q6a), com a relação {(a,a), (b,b), (c,c), (a,c), (c,a)}, $[a] = \{a, c\} = [c]$: a mesma classe tem mais de um representante.

"Nascer no mesmo dia" (respostas do Prof. Pablo) é de equivalência; o número de classes depende do que se entende por "dia": 7 (dia da semana), 31 (dia do mês) ou infinitas (data completa).

**Ordem parcial**: reflexiva, **antissimétrica** e transitiva. Ex.: "x divide y" em {2, 3, 5, 7, 21, 42, 105, 210} (Q8 da UFCG). **Minimais**: 2, 3, 5, 7 (ninguém do conjunto os divide, além deles mesmos); **mínimo**: não existe (nenhum divide todos). **Máximo** (e único maximal): 210, pois todos o dividem. Cadeia com 4 elementos (totalmente ordenada): 3 | 21 | 42 | 210.

"x divide y" em {1, 2, 3, 6, 12, 18} (Q4) tem 19 pares: os 6 reflexivos mais (1,2), (1,3), (1,6), (1,12), (1,18), (2,6), (2,12), (2,18), (3,6), (3,12), (3,18), (6,12), (6,18).

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** propriedades, classes, minimais, máximo e os 19 pares conferidos por força bruta.
