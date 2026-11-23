---
id: ia-busca-heuristica-subida-na-colina-primeiro-melhor-a-estrela-custo-uniforme-gulosa-heuristica-admissivel
titulo: Busca heurística (informada): subida na colina e máximos locais, primeiro melhor, feixe, A* com f = g + h, custo uniforme (Dijkstra), busca gulosa, heurística admissível e monotônica
assunto: ia-02-busca-e-jogos
tipo: material_estudo
questao: slide 05 (Métodos de Busca), parte 2
resolucao: sim
fonte: Slides de Inteligência Artificial do Prof. Jacson R. C. Silva (Departamento de Computação, CCA-UFES), usados na turma da UFAL
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufes-jeiks-slides
autoria: Slides do Prof. Jacson R. C. Silva (UFES), usados como material da turma da UFAL; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), slide 05 (Métodos de Busca), parte 2 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Heurística:** função $h(n)$ que estima a distância do nó $n$ ao objetivo. Métodos **informados** usam heurística; **cegos** não.

- **Subida na colina:** vai para o vizinho melhor que o atual; a versão de **maior aclive** compara todos os vizinhos. Problemas: **máximo local** (contraforte), **platô** e **crista**. Não retrocede.
- **Primeiro melhor:** ordena a **lista inteira** de nós abertos a cada passo e segue o melhor disponível.
- **Feixe (limite superior):** guarda só os $n$ melhores caminhos por nível; economiza memória.

**Caminho ótimo:**
- **A\*:** $f(n) = g(n) + h(n)$, com $g$ o custo do caminho até $n$ e $h$ a estimativa até o objetivo;
- **custo uniforme (Dijkstra):** $h(n)=0$, só $g$;
- **gulosa:** $g(n)=0$, só $h$; rápida, mas não é ótima.

**Heurística admissível:** nunca superestima o custo real, $h(n) \le h^*(n)$; com ela o A\* é **ótimo**. **Monotônica (consistente):** $h(n) \le c(n,n') + h(n')$; cada nó é alcançado primeiro pelo caminho mais curto.

**Exemplo:** grafo S→A (custo 1), S→B (4), A→B (2), A→G (12), B→G (3), com $h(S)=5$, $h(A)=4$, $h(B)=2$, $h(G)=0$ (admissível). O A\* expande S ($f=5$), A ($f=1+4=5$), B ($f=3+2=5$) e acha **S→A→B→G com custo 6**. A gulosa vai S→B→G, com custo 7, que não é o ótimo.

**Verificação:** `test_a_estrela_e_gulosa` roda o A\* e a busca gulosa no grafo do exemplo e confere os custos 6 e 7.
