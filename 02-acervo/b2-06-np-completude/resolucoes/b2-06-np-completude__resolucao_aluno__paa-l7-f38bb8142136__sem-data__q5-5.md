# f38bb8142136-q5-5

Fonte: materiais\Disponiveis\RAG PAA\PAA_L7.pdf | página(s): 6, 7, 8

Versão derivada corrigida por agente; original SHA-256: abf6ccee2657c2c8f99e420f52f2311f8d12504135c4c104bb5a65f7364de0d1. Não é aprovação do professor.

TRI-PARTIÇÃO em três grupos de mesma soma: interpretação do enunciado.
Os três grupos são I, J e o complemento de I union J, disjuntos. A expressão da transcrição envolvendo complemento de I intersection J é inconsistente com essa interpretação e precisa ser conferida na página original.
Sob a interpretação de três grupos iguais, o problema está em NP: o certificado atribui cada elemento a um dos três grupos e as somas são verificadas em tempo polinomial em bits.
Redução de PARTIÇÃO: seja S a soma dos inteiros positivos. Se S é ímpar, envie uma instância NÃO fixa como [1,1,2]. Se S é par, acrescente o inteiro S/2. A soma nova é 3S/2; cada grupo deve somar S/2. Por positividade, o novo elemento ocupa sozinho seu grupo. Os dois grupos restantes particionam a entrada original em somas iguais, e vice-versa.
A transformação usa somente a entrada, sem conhecer uma partição prévia. NP mais essa redução prova NP-completude; uma redução inversa não é necessária. Não confundir este problema com 3-PARTITION, que particiona 3m números em m trios e tem outra definição.
