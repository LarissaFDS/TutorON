---
id: discreta-funcoes
titulo: Funções — domínio, contradomínio, imagem, injetiva, sobrejetiva, bijetiva, composta e inversa
assunto: discreta-05-funcoes
tipo: resolucao
resolucao: sim
questao: 1 a 4
fonte: Notas de aula do Prof. Pablo Sampaio (UFRPE), Funções, e respostas da 5ª lista (2011.1); slides do Prof. Leandro Balby Marinho (UFCG), Funções; exercício de revisão sobre funções (UFCG); Evaristo e Perdigão, seção 1.10
fontes_catalogo: ufrpe-discreta-pablo,ufcg-discreta-leandro,ufal-evaristo-algebra
autoria: Prof. Pablo Sampaio (UFRPE), Prof. Leandro Balby Marinho (UFCG) e Jaime Evaristo e Eduardo Perdigão (UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material dos professores; livro sem licença aberta)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Uma **função** $f : A \to B$ associa a **cada** elemento de A (domínio) **um único** elemento de B (contradomínio). Imagem: $\text{Im}(f) = \{f(a) \mid a \in A\} \subseteq B$. Sem domínio e contradomínio ditos, "f(x) = x²" não é uma função bem definida: a classificação muda com eles.

- **Injetiva**: $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$ (elementos diferentes têm imagens diferentes).
- **Sobrejetiva**: para todo $y \in B$ existe $x \in A$ com f(x) = y (Im(f) = B).
- **Bijetiva**: injetiva e sobrejetiva; só as bijetivas têm **inversa** $f^{-1} : B \to A$.

Como provar (respostas da 5ª lista do Prof. Pablo):
- $f : \mathbb{Z} \to \mathbb{Z}$, f(x) = x + 1. Injetiva: $x_1 + 1 = x_2 + 1 \Rightarrow x_1 = x_2$. Sobrejetiva: dado y, tome x = y − 1. Bijetiva.
- $g : \mathbb{Z} \to \mathbb{Z}$, g(x) = 2x: injetiva, mas não sobrejetiva (2x = 3 não tem solução inteira). Com $g : \mathbb{R} \to \mathbb{R}$ fica bijetiva (x = y/2).
- $h : \mathbb{Z} \to \mathbb{N}$, h(x) = x²: não injetiva (h(3) = h(−3) = 9) e não sobrejetiva (nenhum inteiro tem quadrado 3). Com $h : \mathbb{R} \to [0, \infty)$ fica sobrejetiva, mas continua não injetiva.

Contagem entre conjuntos finitos, |A| = m e |B| = n: há $n^m$ funções de A em B; injetivas só existem se m ≤ n, e são $n(n-1)\cdots(n-m+1)$. Com A = {1, 2, 3, 4} e B = {a, …, f}: 6 · 5 · 4 · 3 = **360** injetivas (= 6!/2!); nenhuma sobrejetiva de A em B (|B| > |A|) e nenhuma injetiva de B em A.

**Composta**: $(g \circ f)(x) = g(f(x))$, definida quando $f : A \to B$ e $g : B \to C$. Composta de injetivas é injetiva; de sobrejetivas, sobrejetiva. Se $g \circ f$ é injetiva, f é injetiva (UFCG, revisão de funções).

Grafo dirigido como função (UFCG, Q1): representa uma função se de cada vértice do domínio sai **exatamente uma** seta; é injetiva se nenhum vértice recebe duas setas; sobrejetiva se todo vértice do contradomínio recebe ao menos uma.

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** 360 injetivas de {1,2,3,4} em 6 letras e as classificações acima conferidas por força bruta em intervalos finitos.
