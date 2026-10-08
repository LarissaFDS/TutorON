# a177bf5bc3c7-q2-2

Fonte: materiais\Disponiveis\RAG PAA\PAA_L4.pdf | página(s): 3

Versão derivada corrigida por agente; original SHA-256: 00def19c291a56826b74693e3ce89a2914d12883f2a56d66addd80b67b11d9de. Não é aprovação do professor.

Prove a unicidade da árvore geradora mínima quando os pesos das arestas são distintos.
Assuma duas AGMs diferentes T e U. Seja e a aresta de menor peso na diferença simétrica T xor U; troque seus nomes se necessário para que e esteja em T. Inserir e em U cria um ciclo. Esse ciclo contém uma aresta f de U que não está em T, pois T não contém ciclos. Como os pesos são distintos e e é a menor aresta na diferença simétrica, w(e)<w(f). Logo U+e-f é uma árvore geradora de custo menor que U, contradição. É a distinção entre pesos que interessa; arestas serem objetos distintos por si só não garante unicidade.
