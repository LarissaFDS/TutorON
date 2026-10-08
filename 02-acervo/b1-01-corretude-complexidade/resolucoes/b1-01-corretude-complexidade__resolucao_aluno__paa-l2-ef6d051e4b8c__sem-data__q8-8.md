# ef6d051e4b8c-q8-8

Fonte: materiais\Disponiveis\RAG PAA\PAA_L2.pdf | página(s): 8, 9

Versão derivada corrigida por agente; original SHA-256: a8ede23ef22773025eb81e796d368daf05aeda0605bd1f5f9e0160badd731234. Não é aprovação do professor.

Contagem da palavra OI em Prog1(n), n>=1.
T(1)=1; para n>1, T(n)=n+T(n-1). A solução exata é n(n+1)/2.
Indução do limite T(n)<=n^2: base T(1)=1. Suponha T(k)<=k^2 para k>=1. Então T(k+1)=k+1+T(k)<=k^2+k+1<=(k+1)^2, pois a diferença é k>=1. Isso prova P(k)->P(k+1); não se deve inverter a implicação. Portanto o limite vale para todo n>=1.
