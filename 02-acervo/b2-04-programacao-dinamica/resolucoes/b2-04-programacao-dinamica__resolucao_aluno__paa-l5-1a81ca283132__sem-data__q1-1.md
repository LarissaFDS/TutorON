# 1a81ca283132-q1-1

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 1

Versão derivada corrigida por agente; original SHA-256: 7b35d6d539fa5ed313bfefa8703e8804606c52548d22fa6b14b1c1480345afd7. Não é aprovação do professor.

Menor soma de um caminho do ápice à base de um triângulo.
Seja tri[i][j] a entrada. Para triângulo não vazio, inicialize dp=[tri[0][0]]. Para cada linha i>0, crie new de tamanho i+1: new[0]=tri[i][0]+dp[0]; new[i]=tri[i][i]+dp[i-1]; para 0<j<i, new[j]=tri[i][j]+min(dp[j-1],dp[j]). Substitua dp por new. A resposta é min(dp).
A recorrência considera exatamente os pais adjacentes de cada célula. Para n linhas, o tempo é O(n^2) e a memória auxiliar O(n). Para [[2],[3,4],[6,5,7],[4,1,8,3]], a soma mínima é 11. O código desta nota é uma reconstrução editorial, e não certifica a transcrição de índices da imagem.
