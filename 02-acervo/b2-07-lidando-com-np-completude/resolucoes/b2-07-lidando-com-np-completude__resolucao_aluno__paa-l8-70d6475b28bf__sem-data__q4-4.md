# 70d6475b28bf-q4-4

Fonte: materiais\Disponiveis\RAG PAA\PAA_L8.pdf | página(s): 7, 8

Versão derivada corrigida por agente; original SHA-256: 80d42e8075ed67a85d9913516a9841c65fce482e205507da39386474abff2c50. Não é aprovação do professor.

Branch-and-bound para COBERTURA DE CONJUNTOS.
Entrada: universo U e coleção S_1,...,S_m; minimizar o número de conjuntos escolhidos cuja união é U. Uma solução gulosa viável fornece um limitante superior UB.
Estado: conjuntos escolhidos C, elementos descobertos R e conjuntos candidatos. Se R for vazio, atualize UB com |C|. Se algum elemento de R não tiver candidato que o cubra, descarte. Um limitante inferior válido é ceil(|R|/max_i |S_i intersection R|), quando o denominador é positivo; sobreposição só pode aumentar a necessidade real.
Se |C|+LB>=UB, pode podar ao buscar uma solução ótima (se quiser enumerar todas as ótimas, ajuste o empate). Escolha um elemento descoberto e ramifique escolhendo cada conjunto candidato que o contém. A busca exata é exponencial no pior caso. A formulação em grafo e os limitantes de cobertura de vértices presentes na resolução original não respondem diretamente a este enunciado.
