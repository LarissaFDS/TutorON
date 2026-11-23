---
id: cg-recorte-de-retas-cohen-sutherland-codigos-de-regiao-4-bits-aceitacao-e-rejeicao-trivial-intersecao
titulo: Recorte (clipping) de segmentos de reta pelo algoritmo de Cohen-Sutherland: códigos de região de 4 bits, aceitação trivial (OR = 0), rejeição trivial (AND ≠ 0), cálculo da interseção com a janela
assunto: cg-02-transformacoes-projecao-e-recorte
tipo: prova
questao: prova bimestral I.2 (questões 2 a 4) e exercícios de recorte
resolucao: sim
fonte: Exercícios e provas de Computação Gráfica do Prof. Marcelo Costa Oliveira (IC-UFAL)
curso: Ciência da Computação (UFAL), COMP381 Computação Gráfica; aulas de 2012 a 2017 e provas de 2014 e 2021.2 (Prof. Marcelo Costa Oliveira)
fontes_catalogo: ufal-marcelo-aulas-cg,ufal-cg-provas-exercicios
autoria: Questões do Prof. Marcelo Costa Oliveira (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Computação Gráfica (IC-UFAL), prova bimestral I.2 (questões 2 a 4) e exercícios de recorte (parafraseado). Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Janela de recorte** $[x_{\min}, x_{\max}] \times [y_{\min}, y_{\max}]$. As retas das bordas dividem o plano em 9 regiões, cada uma com um **código de 4 bits** (da esquerda para a direita):
- bit 1: acima, $y > y_{\max}$;
- bit 2: abaixo, $y < y_{\min}$;
- bit 3: à direita, $x > x_{\max}$;
- bit 4: à esquerda, $x < x_{\min}$.

Regiões: 1001, 1000, 1010 em cima; 0001, **0000** (janela), 0010 no meio; 0101, 0100, 0110 embaixo.

**Testes com os códigos $c_1$ e $c_2$ das extremidades:**
- **aceitação trivial:** $c_1 \lor c_2 = 0000$ (os dois dentro);
- **rejeição trivial:** $c_1 \land c_2 \ne 0000$ (os dois do mesmo lado de fora);
- senão, corta o segmento numa borda indicada por um bit 1, troca a extremidade de fora pela interseção e repete.

**Interseção** com $m = \dfrac{y_2-y_1}{x_2-x_1}$: borda horizontal $y = y_b$: $x = x_1 + \dfrac{y_b - y_1}{m}$; borda vertical $x = x_b$: $y = y_1 + m(x_b - x_1)$.

**Exercício:** janela de $(0,0)$ a $(20,20)$, segmento de $A(30,50)$ a $B(10,10)$. Códigos: $A = 1010$, $B = 0000$; o OR não é zero e o AND é zero, então não há decisão trivial. $m = 40/20 = 2$. O bit 1 de $A$ manda cortar no topo $y = 20$: $x = 10 + (20-10)/2 = 15$, e $C = (15, 20)$, que está na borda (código 0000). Fica $B$–$C$; o trecho $C$–$A$ é descartado.

Erro comum: usar a fórmula da borda vertical para a horizontal (dá $y = 30$, fora da janela).

**Verificação:** `test_cohen_sutherland` implementa o algoritmo, confere os códigos 1010 e 0000 e o ponto $C = (15, 20)$.
