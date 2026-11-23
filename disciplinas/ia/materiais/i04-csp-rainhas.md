---
id: ia-problema-de-satisfacao-de-restricoes-psr-oito-rainhas-retrocesso-fator-de-ramificacao
titulo: Problemas de satisfação de restrições (PSR): variáveis, domínios e restrições; problema das oito rainhas com retrocesso e redução do fator de ramificação
assunto: ia-02-busca-e-jogos
tipo: material_estudo
questao: slide 05 (Métodos de Busca), busca por satisfação de restrições
resolucao: sim
fonte: Slides de Inteligência Artificial do Prof. Jacson R. C. Silva (Departamento de Computação, CCA-UFES), usados na turma da UFAL
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufes-jeiks-slides
autoria: Slides do Prof. Jacson R. C. Silva (UFES), usados como material da turma da UFAL; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), slide 05 (Métodos de Busca), busca por satisfação de restrições (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**PSR:** conjunto de **variáveis**, cada uma com um **domínio**, e **restrições** entre elas. Uma solução dá um valor a cada variável sem violar nenhuma restrição.

**Oito rainhas:** pôr 8 rainhas num tabuleiro $8\times8$ sem duas na mesma linha, coluna ou diagonal.
- Busca ingênua: 8 níveis, fator de ramificação 64, 63, ..., 57 (qualquer casa livre).
- Com as restrições: uma rainha por coluna; a variável $Q_i$ é a linha da rainha da coluna $i$, com domínio $\{1,\dots,8\}$. Cada rainha posta corta as casas atacadas, e o fator de ramificação cai muito.
- Restrição entre $Q_i$ e $Q_j$: $Q_i \ne Q_j$ e $|Q_i - Q_j| \ne |i - j|$.

**Retrocesso (backtracking):** atribui uma variável por vez e volta assim que uma restrição é violada. Melhorias: **verificação adiante** (forward checking) tira valores inconsistentes dos domínios futuros; a heurística **MRV** escolhe a variável com menos valores restantes.

O problema das 8 rainhas tem **92 soluções** (12 distintas a menos de rotação e reflexão).

```python
def rainhas(n, parcial=()):
    if len(parcial) == n:
        yield parcial
    for lin in range(n):
        if all(lin != l and abs(lin - l) != len(parcial) - c for c, l in enumerate(parcial)):
            yield from rainhas(n, parcial + (lin,))
```

**Verificação:** `test_oito_rainhas` roda o retrocesso acima e confere as 92 soluções e que nenhuma tem duas rainhas em ataque.
