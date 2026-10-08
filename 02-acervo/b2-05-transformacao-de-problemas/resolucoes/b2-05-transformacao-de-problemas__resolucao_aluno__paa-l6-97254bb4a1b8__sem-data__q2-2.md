# 97254bb4a1b8-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 1, 2

Versão derivada corrigida por agente; original SHA-256: 5e1e706b225e890a835ea283142ec8b2506c963b85000bcda1410f99859d91eb. Não é aprovação do professor.

Mesa circular de cavaleiros: grafo de compatibilidade.
Cada cavaleiro é um vértice; existe aresta entre dois cavaleiros se eles podem sentar juntos. Uma disposição circular válida corresponde a um ciclo hamiltoniano nesse grafo, incluindo a compatibilidade entre último e primeiro. Um caminho hamiltoniano sozinho não garante a mesa circular.
Para a versão de decisão com número variável de cavaleiros, o certificado é a ordem circular, verificável em tempo polinomial. Para provar NP-dificuldade, reduza CICLO HAMILTONIANO à disposição: para qualquer grafo simples G com pelo menos três vértices, crie um cavaleiro por vértice e declare briguentos exatamente os pares sem aresta de G. Há disposição válida se e somente se G tem ciclo hamiltoniano. Isso fornece a direção de redução necessária; a decisão é NP-completa.
