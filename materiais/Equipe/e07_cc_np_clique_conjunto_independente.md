---
id: e07
titulo: Verdadeiro ou falso sobre P, NP e NP-completo e a redução de clique para conjunto independente (prova 4 de PAA, Ciência da Computação)
assunto: b2-05-transformacao-de-problemas
autoria: Equipe TutorON (não é material do professor); enunciado parafraseado de uma prova 4 de PAA da turma de Ciência da Computação da UFAL, resolução da equipe com auxílio de IA
revisado: false
---
Curso: Ciência da Computação (UFAL), prova 4 de PAA. Status da resolução: validada pela equipe (redução conferida por força bruta em Python); revisão humana pendente.
Verdadeiro ou falso (P1 ∝ P2 quer dizer: P1 se transforma em P2 em tempo polinomial).
(a) Um algoritmo determinístico polinomial para um problema NP-completo implica P = NP. VERDADEIRO: todo problema de NP se reduz a ele, então todos ficariam polinomiais.
(b) Se P ≠ NP, um problema NP-completo pode ter algoritmo de tempo n log n. FALSO: n log n é polinomial, e isso daria P = NP. (Atenção: a prova falava em tempo médio; a afirmação sobre pior caso é a que se prova assim.)
(c) Se P1 ∝ P2 e P1 está em P, então P2 está em P. FALSO: a redução diz que P2 é pelo menos tão difícil quanto P1, não o contrário. Qualquer problema de P se reduz a SAT, e isso não põe SAT em P. O certo é: se P2 está em P, então P1 está em P.
(d) Se P1 está em NP, então SAT ∝ P1. FALSO: isso faria todo problema de NP ser NP-difícil. Ordenar, por exemplo, está em NP.
(e) Backtracking com poda resolve o caixeiro-viajante com eficiência para qualquer entrada. FALSO: a poda corta ramos, mas o pior caso continua exponencial (a árvore tem até (n−1)! caminhos). O motivo não é o uso de memória.
Redução clique ∝ conjunto independente. Entrada do clique: grafo G = (V, A) e inteiro k. Monte o complemento G' = (V, A'), em que u–v é aresta de G' se e só se não é aresta de G (u ≠ v). Pergunte se G' tem conjunto independente de tamanho k.
Por que funciona: S é clique em G ⇔ todo par de S é aresta de G ⇔ nenhum par de S é aresta de G' ⇔ S é independente em G'.
Custo: montar G' leva O(|V|^2), polinomial; a resposta não precisa de conversão. A ida volta igual (G'' = G), então os dois problemas se reduzem um ao outro.
Exemplo: em G com vértices a..f, se {a, b, d, f} é clique, em G' esses quatro vértices não têm aresta entre si.
**Verificação:** em Python, para grafos aleatórios de até 7 vértices, o maior clique de G tem o mesmo tamanho do maior conjunto independente do complemento.
