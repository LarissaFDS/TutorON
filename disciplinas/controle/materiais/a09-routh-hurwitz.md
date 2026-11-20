---
id: controle-anot-routh
titulo: Critério de Routh-Hurwitz: montagem da tabela, mudanças de sinal na 1ª coluna, caso do zero (ε); exemplos s⁶+4s⁵+3s⁴+2s³+s²+4s+4 e s⁵+s⁴+5s³+5s²+12s+10
assunto: controle-04-estabilidade-routh
tipo: resolucao
resolucao: sim
fonte: Anotações "Estabilidade de SLIT contínuo" (9 set. 2026), p. 6–8
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Condição necessária:** todos os coeficientes de $A(s)$ não nulos e com o mesmo sinal. Para grau 2 ela também é suficiente; para grau 3 ou mais, não.

**Tabela:** linhas $s^n$: $a_n, a_{n-2}, a_{n-4}, \dots$ e $s^{n-1}$: $a_{n-1}, a_{n-3}, \dots$. Cada novo elemento: $b_1 = \frac{a_{n-1}a_{n-2} - a_na_{n-3}}{a_{n-1}}$ (o determinante das duas linhas de cima, com sinal trocado, dividido pelo primeiro elemento da linha anterior). **O número de mudanças de sinal na 1ª coluna é o número de raízes com parte real positiva**; estável se e só se não há mudança.

**Ex. 1:** $s^6 + 4s^5 + 3s^4 + 2s^3 + s^2 + 4s + 4$. 1ª coluna: $1,\ 4,\ \tfrac52,\ 2,\ 3,\ -\tfrac{76}{15},\ 4$. Duas mudanças: **2 raízes no semiplano direito**, instável (mesmo com todos os coeficientes positivos).

**Correção:** as anotações escrevem o polinômio com $2s^2$, mas a tabela usa $1$ nesse coeficiente; a coluna acima é a do coeficiente $1$. Com $2s^2$ a 1ª coluna seria $1,\ 4,\ \tfrac52,\ \tfrac25,\ 16,\ -\tfrac52,\ 4$, também com 2 mudanças.

**Ex. 2 (zero na 1ª coluna):** $s^5 + s^4 + 5s^3 + 5s^2 + 12s + 10$. A linha $s^3$ começa com $0$: troque por $\varepsilon > 0$ pequeno. Linha $s^2$: $c_1 = \frac{5\varepsilon - 2}{\varepsilon} \approx -\frac2\varepsilon$ (negativo grande); depois $d_1 \approx 2$ e $10$. Duas mudanças: **2 polos instáveis**.

**Verificação:** `numpy.roots` dá duas raízes com parte real positiva em cada exemplo, como a tabela indica.
