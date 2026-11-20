---
id: discreta-rsa
titulo: Criptografia RSA — como funciona, com números pequenos (exemplo de Evaristo e Perdigão)
assunto: discreta-09-aritmetica-modular-rsa
tipo: material_estudo
resolucao: sim
fonte: Evaristo e Perdigão, Introdução à Álgebra Abstrata (EDUFAL), seção 7.10 (Uma aplicação: criptografia RSA); notas do Prof. Pablo Sampaio (UFRPE), Teoria dos Números — Aplicações Práticas na Computação
fontes_catalogo: ufal-evaristo-algebra,ufrpe-discreta-pablo
autoria: Jaime Evaristo e Eduardo Perdigão (IC e IM/UFAL) e Prof. Pablo Sampaio (UFRPE), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (livro sem licença aberta; notas do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio; os números do exemplo foram recalculados; o livro não está no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Em cifras de **chave privada** (como trocar cada letra pela que está 3 posições à frente, "DEZ HORAS" → "GHC KRUDV", no alfabeto de 26 letras), quem sabe codificar sabe decodificar. O **RSA** (Rivest, Shamir e Adleman, 1978) é de **chave pública**: a chave de codificação é divulgada, e só quem conhece dois primos secretos consegue decodificar.

**Montando as chaves** (notação do livro: chave pública (n, c); em outros livros, (n, e)):
1. Escolha primos p e q e calcule n = p · q e $\varphi(n) = (p-1)(q-1)$.
2. Escolha c com mdc(c, φ(n)) = 1. Chave pública: (n, c).
3. Calcule d, o **inverso de c módulo φ(n)** (Euclides estendido). Chave privada: (n, d). Guarde p e q em segredo.

**Codificar e decodificar** um bloco M (inteiro, 0 < M < n, primo com n): $C = M^c \bmod n$ e $M = C^d \bmod n$. Funciona porque cd = 1 + kφ(n), e pelo Teorema de Euler $M^{cd} = M \cdot (M^{\varphi(n)})^k \equiv M \pmod n$.

**Exemplo do livro**: p = 97 e q = 53; n = 5141; φ(n) = 96 · 52 = 4992; c = 7 (mdc(7, 4992) = 1). Como 4992 = 7 · 713 + 1, temos 1 = 4992 − 713 · 7, e o inverso é d = −713 + 4992 = **4279**. Confira: 7 · 4279 = 29953 = 6 · 4992 + 1.

Codificando um bloco: o livro converte cada caractere em código ASCII + 100, então "A" vira 165. $C = 165^7 \bmod 5141 = 4813$ e $4813^{4279} \bmod 5141 = 165$, recuperando a mensagem. Na prática, as potências são calculadas por exponenciação rápida (quadrados sucessivos), sempre reduzindo módulo n.

**Por que é seguro**: conhecer (n, c) não basta; para achar d é preciso φ(n), e para isso fatorar n. Com primos de centenas de dígitos, não se conhece algoritmo eficiente de fatoração. Com primos pequenos como no exemplo, o RSA é só didático.

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** n, φ(n), d e a ida e volta do bloco 165 conferidos com `pow` do Python; o segundo exemplo do livro (p = 127, q = 193, c = 5) dá d = 9677, também conferido.
