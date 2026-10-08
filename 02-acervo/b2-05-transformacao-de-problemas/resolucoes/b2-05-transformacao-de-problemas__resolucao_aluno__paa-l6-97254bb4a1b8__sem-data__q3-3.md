# 97254bb4a1b8-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 2

Versão derivada corrigida por agente; original SHA-256: 7e856e23f90aa3ef6a14888b874b231ddbbf7bf88707b6e9baad3b4168e31207. Não é aprovação do professor.

Famílias em mesas via fluxo máximo.
Crie fonte s, vértices F_i para famílias e M_j para mesas, e sorvedouro t. Arestas s->F_i têm capacidade a_i; F_i->M_j têm capacidade 1 para todos os pares; M_j->t têm capacidade b_j. Capacidades inteiras permitem obter um fluxo máximo integral.
Existe disposição para todos se e somente se o fluxo máximo vale sum_i a_i. Uma unidade em F_i->M_j significa colocar um membro da família i na mesa j; capacidade 1 impede dois membros da mesma família na mesma mesa. As capacidades de origem e destino asseguram tamanhos das famílias e mesas. Se o fluxo for menor, a disposição completa é impossível. O desenho original trocava nomes de índices; esta reconstrução define todas as arestas.
