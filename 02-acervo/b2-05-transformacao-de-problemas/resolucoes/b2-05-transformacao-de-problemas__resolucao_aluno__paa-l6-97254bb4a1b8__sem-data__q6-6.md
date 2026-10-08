# 97254bb4a1b8-q6-6

Fonte: materiais\Disponiveis\RAG PAA\PAA_L6.pdf | página(s): 4, 5

Versão derivada corrigida por agente; original SHA-256: c718d2863d7d0daa7f4a07a25dc9b6c38f77feecc660724a14d9c79be7bc40b7. Não é aprovação do professor.

Troco mínimo como programa linear inteiro.
Para valores de moedas c_1,...,c_n positivos e alvo v>=0, use x_i inteiro não negativo, quantidade de moedas do tipo i. Minimize sum_i x_i sujeito a sum_i c_i*x_i=v.
Permitir x_i=0 é necessário: nem todos os tipos precisam aparecer. Para a versão de decisão com no máximo k moedas, acrescente sum_i x_i<=k e verifique viabilidade, sem necessidade de objetivo. Estoque ilimitado não requer limites superiores para x_i. Se não houver solução inteira, o troco exato é impossível. A relaxação para reais pode dar frações de moedas e não resolve o problema inteiro.
