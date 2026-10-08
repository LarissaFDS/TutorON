# f38bb8142136-q9-9

Fonte: materiais\Disponiveis\RAG PAA\PAA_L7.pdf | página(s): 10, 11

Versão derivada corrigida por agente; original SHA-256: 4b8b85c6ebdf35871542cfcf74ec8b7c1ffb41ef24094f6c1a76a0a18df6449c. Não é aprovação do professor.

ISOMORFISMO DE SUBGRAFO: dados o padrão G e o grafo alvo H, existe um mapeamento injetivo f:V(G)->V(H) que preserva todas as arestas do padrão?
O certificado é esse mapeamento. Verificar injetividade e que cada aresta {u,v} de G mapeia para uma aresta {f(u),f(v)} de H leva tempo polinomial. Para subgrafo não induzido, não é necessário preservar não arestas.
Redução de CLIQUE: para instância (H,k), construa o padrão G=K_k e mantenha H como alvo. Há uma clique de tamanho k em H se e somente se K_k é isomorfo a um subgrafo de H. Se k>|V(H)|, a resposta é imediatamente NÃO e pode ser enviada a uma instância NÃO fixa; a construção restante é polinomial.
Logo ISOMORFISMO DE SUBGRAFO é NP-completo. A resolução trocava padrão e alvo e concluía incorretamente NP-completude de ISOMORFISMO DE GRAFOS, que é outro problema; essa conclusão não foi preservada.
