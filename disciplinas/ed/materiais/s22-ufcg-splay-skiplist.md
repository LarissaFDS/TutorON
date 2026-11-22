---
id: ed-ufcg-splay-skiplist
titulo: Árvore splay e skip list — ideia, operações e custo (UFCG; fora da ementa confirmada da UFAL)
assunto: ed-15-arvores-balanceadas
tipo: material_estudo
resolucao: nao
fonte: Slides de Estrutura de Dados da UFCG (DSC), Prof. Adalberto Cajueiro, 2013, aulas "Splay Tree" e "Skip List"
fontes_catalogo: ufcg-ed-cajueiro-slides
autoria: Conteúdo dos slides do Prof. Adalberto Cajueiro (UFCG), parafraseado pela equipe TutorON com auxílio de IA
licenca: Não declarada nos slides
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: nao_verificada
revisao_humana: pendente
---
Atenção: árvore splay e skip list vêm dos slides da UFCG. A ementa de Estrutura de Dados da UFAL a que a equipe teve acesso (PPC de 2014) não as cita; confirme com o professor se caem na disciplina.

Árvore splay (Sleator e Tarjan, 1985): ABB sem campo de balanceamento. Toda operação termina levando o nó acessado até a raiz (o splay), em passos de rotação:
- zig: o nó é filho da raiz; gira uma vez.
- zig-zig: nó e pai são filhos do mesmo lado; gire primeiro no avô, depois no pai.
- zig-zag: lados opostos; gire no pai e depois no avô.
Busca sem sucesso faz splay no último nó visitado; inserção faz splay no nó inserido; remoção faz splay no pai do nó removido. Um acesso isolado pode custar O(n), mas qualquer sequência de m operações custa O(m log n): custo amortizado O(log n) por operação. Chaves acessadas com frequência ficam perto da raiz.

Skip list (Pugh, 1990): sequência ordenada de chaves em vários níveis de "atalhos" (pulos). O nível 0 tem todas as chaves; cada nó novo sobe mais um nível com probabilidade p = 1/2 (cara ou coroa), então o nível i tem cerca de $n/2^i$ nós e a altura esperada é O(log n). Busca: comece no nível mais alto e avance enquanto a próxima chave for menor que a procurada; quando não der, desça um nível. Inserção: busque guardando o último nó visitado em cada nível, sorteie a altura do nó novo e ligue-o em cada nível até essa altura. Custo esperado O(log n) para busca, inserção e remoção; o pior caso é O(n), mas é improvável. Não precisa de rotações.
