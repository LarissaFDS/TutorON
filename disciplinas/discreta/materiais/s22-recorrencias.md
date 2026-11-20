---
id: discreta-recorrencias
titulo: Relações de recorrência — expandir, conjecturar e verificar; recorrências lineares homogêneas
assunto: discreta-13-recorrencias
tipo: material_estudo
resolucao: sim
fonte: Slides de Indução e Recursão do Prof. Leandro Balby Marinho (UFCG); 6ª lista e respostas do Prof. Pablo Sampaio (UFRPE); Albertson e Hutchinson, Discrete Mathematics with Algorithms, capítulo 7 (apenas parafraseado por seção; livro protegido)
fontes_catalogo: ufcg-discreta-leandro,ufrpe-discreta-pablo,albertson-hutchinson
autoria: Prof. Leandro Balby Marinho (UFCG), Prof. Pablo Sampaio (UFRPE) e Albertson e Hutchinson (livro), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material dos professores); livro protegido por direito autoral, nada transcrito
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Uma **relação de recorrência** define cada termo a partir dos anteriores, mais condições iniciais. Ex. (lista 6 do Prof. Pablo): $a_1 = 1$, $a_2 = 0$, $a_n = a_{n-1} + a_{n-2}$ dá 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, então $a_3 = 1$, $a_5 = 2$ e $a_{10} = 21$.

**Expandir, conjecturar e verificar** (slides da UFCG):
1. Expanda: S(1) = 2 e S(n) = 2S(n − 1) dão S(n) = 2S(n − 1) = $2^2 S(n-2)$ = … = $2^{n-1} S(1)$.
2. Conjecture: S(n) = $2^n$.
3. **Verifique por indução** (sem isso, é só palpite): S(1) = 2; se S(k) = $2^k$, S(k + 1) = 2 · $2^k$ = $2^{k+1}$. ∎

Outro exemplo: S(1) = 4 e S(n) = 2S(n − 1) + 3 dá $S(n) = 2^{n+1} + 3(2^{n-1} - 1)$, ou seja, $S(n) = 7 \cdot 2^{n-1} - 3$ (4, 11, 25, 53, …).

**Recorrência linear homogênea de 2ª ordem com coeficientes constantes**: $a_n = c_1 a_{n-1} + c_2 a_{n-2}$.
1. Escreva a **equação característica** $r^2 = c_1 r + c_2$.
2. Se tiver raízes distintas $r_1, r_2$: $a_n = \alpha r_1^n + \beta r_2^n$. Se tiver raiz dupla r: $a_n = (\alpha + \beta n) r^n$.
3. Ache α e β pelas condições iniciais.

Ex.: $a_n = 5a_{n-1} - 6a_{n-2}$, $a_0 = 1$, $a_1 = 4$. Equação $r^2 - 5r + 6 = 0$, raízes 2 e 3. Então α + β = 1 e 2α + 3β = 4, logo β = 2 e α = −1: $a_n = 2 \cdot 3^n - 2^n$. Confira: $a_2$ = 5 · 4 − 6 · 1 = 14 = 18 − 4.

Recorrências de custo de algoritmos (como T(n) = 2T(n/2) + n) são aprofundadas em PAA.

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** as fórmulas fechadas foram comparadas com a recorrência para n de 1 a 30 em Python, e o SymPy (`rsolve`) dá a mesma solução $2 \cdot 3^n - 2^n$.
