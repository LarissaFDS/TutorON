---
id: discreta-cc-teorema-chines-resto
titulo: Sistema de congruências pelo Teorema Chinês do Resto, passo a passo (provas de CC)
assunto: discreta-09-aritmetica-modular-rsa
tipo: resolucao
resolucao: sim
questao: Prova 3 2020.1 e 2020.2 (sistemas); Reavaliação 2 2020.2 (Q4)
fonte: Provas do Prof. Bruno Pimentel (2020.1 e 2020.2) e revisão da monitoria da 3ª prova (2020.2)
curso: Ciência da Computação (UFAL), turmas de 2020.1 e 2020.2 (Prof. Bruno Pimentel)
fontes_catalogo: ufal-cc-discreta-provas-bruno,ufal-cc-discreta-monitoria
autoria: Prof. Bruno Pimentel (IC-UFAL) e revisão da monitoria, parafraseados (nomes dos monitores omitidos); resolução da equipe TutorON com auxílio de IA
licenca: Não declarada (provas do professor e material da monitoria)
publicacao_transcricao: não se aplica: o bloco parafraseia os enunciados e traz resolução própria; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Resolução da equipe TutorON, não é gabarito do professor. Status da resolução: validada.

Como resolver um sistema de congruências, como x ≡ 1 mod 5, x ≡ 2 mod 6, x ≡ 3 mod 7 (resposta: x = 206 mod 210)?

**Teorema Chinês do Resto:** se $m_1,\dots,m_k$ são primos entre si dois a dois, o sistema $x\equiv r_i \pmod{m_i}$ tem solução única módulo $M=m_1\cdots m_k$.

Passo a passo:
1. Confira que os módulos são primos entre si (senão o método não se aplica direto).
2. $M=\prod m_i$ e $M_i=M/m_i$.
3. Ache $s_i$ com $M_i s_i\equiv1 \pmod{m_i}$ (inverso).
4. $x_0=\sum r_i M_i s_i$ e **reduza módulo M**.

**Exemplo da revisão** ($x\equiv2 \bmod 3$, $x\equiv4 \bmod 5$, $x\equiv6 \bmod 7$): M = 105; $M_i$ = 35, 21, 15; $s_i$ = 2, 1, 1; $x_0=35\cdot2\cdot2+21\cdot1\cdot4+15\cdot1\cdot6=314$. A revisão para em 314; reduzindo, $x\equiv104 \pmod{105}$.

**Provas:**
- $x\equiv1 \pmod5$, $x\equiv2 \pmod6$, $x\equiv3 \pmod7$: $M=210$, $x\equiv206 \pmod{210}$;
- $x\equiv1 \pmod3$, $x\equiv2 \pmod7$, $x\equiv1 \pmod{11}$: $M=231$, $x\equiv100 \pmod{231}$;
- $x\equiv1 \pmod3$, $x\equiv2 \pmod7$, $x\equiv3 \pmod8$: $M=168$, $x\equiv163 \pmod{168}$.

Atalho para conferir o exemplo: $x\equiv-1$ módulo 3, 5 e 7, então $x\equiv-1\equiv104 \pmod{105}$. Sempre confira a resposta em cada congruência (206 = 41·5 + 1 = 34·6 + 2 = 29·7 + 3).

**Verificação:** os quatro sistemas foram resolvidos com sympy.ntheory.modular.crt e por força bruta de 0 a M − 1, que achou uma única solução em cada.
