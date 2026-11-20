---
id: discreta-demonstracao-direta
titulo: Técnicas de demonstração — prova direta, contrapositiva e por casos (par, ímpar, divide)
assunto: discreta-02-demonstracoes
tipo: material_estudo
resolucao: sim
fonte: Notas de aula do Prof. Pablo Sampaio (UFRPE), Demonstrações Matemáticas partes 1 e 3, axiomas dos inteiros e listas 2, 4 e 5; slides do Prof. Leandro Balby Marinho (UFCG), Técnicas de Demonstração
fontes_catalogo: ufrpe-discreta-pablo,ufcg-discreta-leandro
autoria: Prof. Pablo Sampaio (UFRPE) e Prof. Leandro Balby Marinho (UFCG), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material dos professores)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Definições usadas (inteiros): n é **par** se n = 2k para algum inteiro k; **ímpar** se n = 2k + 1; **a divide b** ($a \mid b$) se b = a·k para algum inteiro k.

**Prova direta** de P → Q: suponha P (hipótese), use definições e axiomas e chegue a Q.
Exemplo: "se n é ímpar, então $n^2$ é ímpar". Hipótese: n = 2k + 1. Então $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$; como $2k^2 + 2k$ é inteiro, $n^2$ é ímpar. ∎

**Contrapositiva**: P → Q equivale a ¬Q → ¬P. Use quando a negação da conclusão dá uma forma mais concreta.
Exemplo: "se $n^2$ é par, então n é par". Contrapositiva: "se n é ímpar, então $n^2$ é ímpar", que é o exemplo acima. ∎

Exemplo com divisibilidade (lista 4 do Prof. Pablo): se $a \mid b$ e $a \mid c$, então $a \mid (mb + nc)$ para inteiros m, n. Hipóteses: b = a·j e c = a·k. Então mb + nc = a(mj + nk), e mj + nk é inteiro. ∎

**Bicondicional** (P ↔ Q): prove as duas implicações separadamente (prova por partes). **Por casos (exaustão)**: divida em casos que cubram todas as possibilidades, por exemplo n par ou n ímpar; "para 1 ≤ n ≤ 4, $n^2 + 1 \ge 2n$" (lista 5) se prova testando os 4 valores: 2 ≥ 2, 5 ≥ 4, 10 ≥ 6, 17 ≥ 8.

Erros comuns: provar a recíproca no lugar da afirmação; usar o mesmo k para dois números diferentes ("a = 2k e b = 2k" supõe a = b); concluir "para todo" a partir de exemplos. Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** por força bruta, para todo n de −1000 a 1000, n ímpar implica $n^2$ ímpar e $n^2$ par implica n par.
