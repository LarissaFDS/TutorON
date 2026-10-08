# 70d6475b28bf-q7-7

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 11, 12

Versão derivada corrigida por agente; original SHA-256: d8f3db85a5b7451a0b3214927e9a440b4d136c2ad40564c2367e5c1f11995d03. Não é aprovação do professor.

Busca local 2-opt para TSP.
Em um ciclo de visita, escolha duas arestas não adjacentes (a,b) e (c,d). Substitua-as por (a,c) e (b,d), invertendo o segmento entre b e c. Em TSP simétrico, a variação de custo é d(a,c)+d(b,d)-d(a,b)-d(c,d). Aceite uma troca se ela reduzir o custo e repita até não haver melhora nessa vizinhança.
Há O(n^2) pares por varredura, com avaliação O(1) da diferença se as distâncias forem acessíveis; inverter o segmento pode custar O(n). Exemplo geométrico: desfazer duas arestas cruzadas pode encurtar o tour.
O término em ótimo local não garante ótimo global. Percorrer duas vezes uma AGM e atalhar vértices é outra heurística, com garantia de 2-aproximação em TSP métrico; isso não é a operação 2-opt. O exemplo numérico da figura original não foi usado para certificar esta busca local.
