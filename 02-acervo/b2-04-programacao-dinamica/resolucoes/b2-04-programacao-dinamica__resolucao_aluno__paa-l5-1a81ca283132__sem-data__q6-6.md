# 1a81ca283132-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L5.pdf | página(s): 5, 6

Versão derivada corrigida por agente; original SHA-256: d74241311f84dffd701b94a4183fe97e2fe9c7e9a694998dd2ba70da6b09c36e. Não é aprovação do professor.

Custo mínimo de cortar uma string de comprimento n nas posições dadas.
Ordene os m cortes distintos e internos e acrescente p[0]=0 e p[m+1]=n. Para j=i+1, C[i][j]=0. Para intervalos com cortes internos, C[i][j]=(p[j]-p[i])+min(C[i][k]+C[k][j]) sobre i<k<j. Calcule por tamanho crescente do intervalo e retorne C[0][m+1].
Cada primeiro corte custa o comprimento do segmento atual e divide o problema em dois segmentos independentes. Tempo O(m^3), memória O(m^2). Para n=20 e cortes 3 e 10, cortar em 3 primeiro custa 37; cortar em 10 primeiro custa 30, que é o ótimo.
