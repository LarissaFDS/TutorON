---
id: discreta-mdc-primos
titulo: Como calcular o mdc (máximo divisor comum) pelo algoritmo de Euclides, identidade de Bézout, primos e Teorema Fundamental da Aritmética
assunto: discreta-08-mdc-primos
tipo: material_estudo
resolucao: sim
fonte: Notas de aula do Prof. Pablo Sampaio (UFRPE), Divisores e Primos e Algoritmo da Divisão (exemplo mdc(414, 662)); Evaristo e Perdigão, Introdução à Álgebra Abstrata, capítulos 3 e 6
fontes_catalogo: ufrpe-discreta-pablo,ufal-evaristo-algebra
autoria: Prof. Pablo Sampaio (UFRPE) e Jaime Evaristo e Eduardo Perdigão (UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (notas do professor; livro sem licença aberta)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
**Divisores**: os divisores positivos de 12 são 1, 2, 3, 4, 6, 12 (lista 4 do Prof. Pablo). Um inteiro p > 1 é **primo** se seus únicos divisores positivos são 1 e p. O **mdc(a, b)** é o maior inteiro que divide a e b; a e b são **primos entre si** quando mdc(a, b) = 1.

**Algoritmo de Euclides**: se b ≠ 0, então mdc(a, b) = mdc(b, a mod b), e mdc(a, 0) = |a|. Cada passo troca o par por números menores. Exemplo da aula: mdc(414, 662) = mdc(662, 414) = mdc(414, 248) = mdc(248, 166) = mdc(166, 82) = mdc(82, 2) = mdc(2, 0) = **2**.

**Identidade de Bézout**: existem inteiros x, y com $ax + by = \text{mdc}(a, b)$. Eles saem de "voltar" as divisões do algoritmo de Euclides (Euclides estendido). Exemplo: mdc(26, 7).
- 26 = 3 · 7 + 5; 7 = 1 · 5 + 2; 5 = 2 · 2 + 1; 2 = 2 · 1 + 0. Logo mdc = 1.
- Voltando: 1 = 5 − 2 · 2 = 5 − 2(7 − 5) = 3 · 5 − 2 · 7 = 3(26 − 3 · 7) − 2 · 7 = 3 · 26 − 11 · 7.
- Então x = 3, y = −11: 3 · 26 + (−11) · 7 = 78 − 77 = 1.

**Teorema Fundamental da Aritmética**: todo inteiro n ≥ 2 é primo ou se escreve como produto de primos, de forma única a menos da ordem. Ex.: 360 = $2^3 \cdot 3^2 \cdot 5$. Com as fatorações, mdc usa o menor expoente de cada primo e mmc o maior; e $\text{mdc}(a, b) \cdot \text{mmc}(a, b) = ab$ para a, b positivos.

**Teste de primalidade simples**: basta testar divisores até $\sqrt{n}$; se n é composto, tem um fator primo $\le \sqrt{n}$. **Crivo de Eratóstenes** (livro, cap. 6): liste 2, …, N e risque os múltiplos de cada primo até $\sqrt{N}$; o que sobra é primo. Lema de Euclides: se p é primo e p | ab, então p | a ou p | b (falha para não primos: 6 | 4 · 9 sem dividir 4 nem 9).

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** mdc(414, 662) = 2, os coeficientes de Bézout de (26, 7), a fatoração de 360 e o crivo até 100 (25 primos) foram conferidos com o Python e o SymPy.
