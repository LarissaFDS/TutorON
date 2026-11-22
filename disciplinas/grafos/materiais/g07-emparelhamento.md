---
id: grafos-emparelhamento-tabuleiro-cobertura
titulo: Emparelhamento (casamento, acoplamento) — tabuleiro 8×8 sem duas quinas opostas não pode ser coberto por dominós, conjunto independente e cobertura de vértices são complementares, teoremas de Hall e König
assunto: grafos-04-emparelhamento-estabilidade
tipo: lista
questao: 2.2, 3.9
resolucao: sim
fonte: Lista de exercícios de Teoria dos Grafos 2020.1, Prof. Rian Gabriel Pinheiro (IC-UFAL)
curso: Ciência da Computação (UFAL), Teoria dos Grafos (COMP369), 2020.1
fontes_catalogo: ufal-rian-lista-2020-1
autoria: Questões do Prof. Rian Gabriel Pinheiro (UFAL); resolução da equipe TutorON
licenca: Não declarada (lista, prova e slides); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista 2020.1, questões 2.2 e 3.9 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Emparelhamento** (casamento, acoplamento): conjunto de arestas sem pontas em comum. **Maximal** = não cabe mais nenhuma aresta; **máximo** = o maior possível; **perfeito** = cobre todos os vértices.

**Tabuleiro sem quinas opostas (2.2):** cada casa é um vértice, ligado às casas vizinhas; cobrir com dominós 1×2 é achar um emparelhamento perfeito. As quinas opostas têm a **mesma cor**: sobram 32 casas de uma cor e 30 da outra. Cada dominó cobre uma casa de cada cor, então cabem no máximo 30 dominós para 62 casas: não há cobertura.

**Independente e cobertura (3.9):** $S$ é independente (sem arestas internas) se e só se $V \setminus S$ é uma **cobertura de vértices** (toda aresta tem ponta fora de $S$): as duas frases dizem que nenhuma aresta tem as duas pontas em $S$. Logo $\alpha(G) + \beta(G) = |V|$ ($\alpha$ = maior independente, $\beta$ = menor cobertura).

**Hall:** num bipartido com lados $X$ e $Y$, há emparelhamento que cobre $X$ se e só se $|N(S)| \ge |S|$ para todo $S \subseteq X$. **König:** em bipartidos, o emparelhamento máximo tem o tamanho da cobertura mínima.

**Verificação:** `test_emparelhamento` calcula com NetworkX o emparelhamento máximo da grade 8×8 sem as quinas (30 arestas para 62 casas) e confere por força bruta, em grafos pequenos, que o complemento de um independente é cobertura.
