---
id: discreta-cc-fermat-potencias-rsa
titulo: Potência grande mod p pelo Pequeno Teorema de Fermat (provas de CC)
assunto: discreta-09-aritmetica-modular-rsa
tipo: resolucao
resolucao: sim
questao: Prova 3 2020.1 e 2020.2; Reavaliação 2 e Final 2020.2
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

**Pequeno Teorema de Fermat:** se p é primo e $p\nmid a$, então $a^{p-1}\equiv1 \pmod p$. Para reduzir $a^n$: divida o expoente, $n=q(p-1)+r$, e $a^n\equiv a^r \pmod p$.

- $3^{2021} \bmod 7$: $3^6\equiv1$ e $2021=6\cdot336+5$, logo $3^{2021}\equiv3^5=243\equiv5$.
- $8^{1330} \bmod 13$: $8^{12}\equiv1$ e $1330=12\cdot110+10$, logo $8^{1330}\equiv8^{10}$; como $8^2=64\equiv-1$, $8^{10}=(8^2)^5\equiv-1\equiv12$.
- $4^{883} \bmod 5$: $4\equiv-1$, e expoente ímpar dá $-1\equiv4$.
- $2^{2021} \bmod 3$: $2\equiv-1$, expoente ímpar, resposta 2.

O atalho $a\equiv-1$ resolve muitos casos sem Fermat. Erros comuns: usar o expoente p em vez de p − 1, ou aplicar Fermat com módulo que não é primo.

A questão discursiva da mesma prova (importância dos primos e da aritmética modular) se responde ligando estas contas ao bloco de criptografia: lá o teorema de Euler, generalização de Fermat, garante que decifrar devolve a mensagem.

**Verificação:** as quatro potências foram conferidas com pow(a, n, p) em Python, e o teorema foi testado para todo a de 1 a p − 1 com p = 5, 7 e 13.
