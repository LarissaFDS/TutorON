---
id: discreta-estruturas-algebricas
titulo: Estruturas algébricas — semigrupo, monoide, grupo, anel e o anel Zn
assunto: discreta-10-estruturas-algebricas-booleanas
tipo: material_estudo
resolucao: sim
fonte: Slides e lista de Estruturas Algébricas do Prof. Leandro Balby Marinho (UFCG); Evaristo e Perdigão, Introdução à Álgebra Abstrata, capítulos 4 e 7
fontes_catalogo: ufcg-discreta-leandro,ufal-evaristo-algebra
autoria: Prof. Leandro Balby Marinho (UFCG) e Jaime Evaristo e Eduardo Perdigão (UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor; livro sem licença aberta)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Uma **estrutura algébrica** [S, ∘] é um conjunto S com uma operação binária ∘. Para classificar, confira **cada propriedade separadamente**, nesta ordem:
1. **Fechamento**: x ∘ y ∈ S para todos x, y ∈ S.
2. **Associatividade**: (x ∘ y) ∘ z = x ∘ (y ∘ z).
3. **Elemento neutro** e: e ∘ x = x ∘ e = x.
4. **Inverso**: para cada x existe x' com x ∘ x' = x' ∘ x = e.

Com 1 e 2: **semigrupo**. Com 1, 2 e 3: **monoide**. Com 1 a 4: **grupo**; se ainda for comutativo, **grupo abeliano**.

Exemplos (para justificar, basta um contraexemplo quando a propriedade falha):
- [ℕ, +] com ℕ = {0, 1, 2, …}: monoide (neutro 0), não é grupo (1 não tem oposto em ℕ).
- [ℤ, +]: grupo abeliano. [ℤ, ·]: monoide (neutro 1), não é grupo (2 não tem inverso em ℤ).
- [ℤ, −]: não é semigrupo, pois (5 − 3) − 1 = 1 e 5 − (3 − 1) = 3.
- Inteiros ímpares com +: não é fechado (1 + 1 = 2).

**Anel** [A, +, ·]: [A, +] é grupo abeliano, · é associativa e distributiva sobre +. **Corpo**: anel comutativo com 1 em que todo elemento não nulo tem inverso multiplicativo. ℤ é anel e não é corpo; ℚ e ℝ são corpos.

**O anel $\mathbb{Z}_n$**: classes [0], …, [n − 1] com [a] + [b] = [a + b] e [a] · [b] = [ab] (módulo n). Em $\mathbb{Z}_6$: [2] · [3] = [0] com [2], [3] ≠ [0] (divisores de zero), e só [1] e [5] têm inverso. $\mathbb{Z}_n$ é corpo **se e somente se n é primo**: em $\mathbb{Z}_7$, todo [a] ≠ [0] tem inverso.

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** as tabelas de + e · de $\mathbb{Z}_n$ para n de 2 a 12 foram geradas por código: os invertíveis de $\mathbb{Z}_6$ são {1, 5}, e $\mathbb{Z}_n$ não tem divisores de zero exatamente para n primo.
