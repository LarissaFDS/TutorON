---
id: discreta-peano-recursao
titulo: Postulados de Peano, definições recursivas e indução na torre de Hanói
assunto: discreta-06-inducao-peano
tipo: material_estudo
resolucao: sim
fonte: Evaristo e Perdigão, Introdução à Álgebra Abstrata (EDUFAL), capítulo 2 (Os números naturais); notas do Prof. Pablo Sampaio (UFRPE), Definições Recursivas e Recursão e Indução na Torre de Hanói
fontes_catalogo: ufal-evaristo-algebra,ufrpe-discreta-pablo
autoria: Jaime Evaristo e Eduardo Perdigão (IC e IM/UFAL) e Prof. Pablo Sampaio (UFRPE), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (livro sem licença aberta; notas do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
**Construção axiomática dos naturais (Peano)**, como no livro de Evaristo e Perdigão (lá $\mathbb{N}$ começa em 1):
1. Existe uma função **sucessor** $s : \mathbb{N} \to \mathbb{N}$ injetiva.
2. Existe um elemento 1 tal que $s(\mathbb{N}) = \mathbb{N} - \{1\}$: 1 não é sucessor de ninguém, e todo outro natural é.
3. **Princípio da indução**: se um predicado p vale para 1 e, sempre que vale para n, vale para s(n), então p vale para todo natural.

A partir daí, soma e produto são definidos por recursão: n + 1 = s(n) e n + s(m) = s(n + m); n · 1 = n e n · s(m) = n · m + n. Propriedades como associatividade e comutatividade são provadas por indução a partir dessas definições. Atenção à notação: nos slides do Prof. Lucas, $\mathbb{N} = \{0, 1, 2, \dots\}$; no livro, $\mathbb{N}$ começa em 1. Diga sempre qual convenção está usando.

**Definição recursiva (indutiva)** de uma função: casos base mais uma regra que usa valores menores. Ex. (Prof. Pablo): f(1) = 2 e f(n) = 2 · f(n − 1) para n > 1. Conjectura: f(n) = $2^n$. Prova por indução: f(1) = 2 = $2^1$; se f(k) = $2^k$, então f(k + 1) = 2 · $2^k$ = $2^{k+1}$. ∎ Conjuntos também podem ser definidos assim: "1 ∈ S; se x ∈ S, então x + 2 ∈ S" gera os ímpares positivos.

**Torre de Hanói** (material extra do Prof. Pablo): mover n discos exige mover n − 1 para o pino auxiliar, o maior para o destino e os n − 1 de volta por cima. O número mínimo de movimentos satisfaz $H(1) = 1$ e $H(n) = 2H(n-1) + 1$, cuja forma fechada é $H(n) = 2^n - 1$ (prova por indução: $2(2^k - 1) + 1 = 2^{k+1} - 1$). Com 3 discos: 7 movimentos.

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** a recursão de Hanói foi simulada por código para n de 1 a 12 e dá exatamente $2^n - 1$ movimentos.
