# f38bb8142136-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L7.pdf | página(s): 1, 2

Versão derivada corrigida por agente; original SHA-256: 6afd7e7323c4debf3c3d6b23b4de4bd4617c7af3bd29fb0345749716e5becb3b. Não é aprovação do professor.

Defina P, NP, NP-completo e redução polinomial.
P é a classe dos problemas de decisão resolvidos por algoritmo determinístico em tempo polinomial no comprimento da entrada.
NP é a classe dos problemas de decisão cujas instâncias SIM possuem certificados de tamanho polinomial verificáveis em tempo polinomial. Equivalentemente, são decididos em tempo polinomial por máquina não determinística. NP não é definida como problemas que ninguém conseguiu provar polinomiais ou intratáveis. P está contida em NP; não se sabe se P=NP.
Uma redução many-one A<=p B é uma função f computável em tempo polinomial tal que x pertence a A se e somente se f(x) pertence a B.
B é NP-completo se B pertence a NP e todo problema de NP se reduz polinomialmente a B. Para demonstrar NP-dificuldade, reduza um problema já NP-difícil para o problema novo. A direção contrária não basta.
Exemplos apropriados de decisão: SAT, CLIQUE (existe clique de tamanho pelo menos k?) e MOCHILA com limite de peso e alvo de valor. Distinguir essas versões das versões de otimização. Se algum NP-completo estiver em P, então P=NP. Esta redação corrige a resolução de alunos.
