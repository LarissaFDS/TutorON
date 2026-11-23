---
id: compevol-algoritmo-genetico-completo-python-geracoes-criterio-de-parada
titulo: Passo a passo do algoritmo genético simples (inicialização, avaliação, seleção, cruzamento, mutação, atualização, finalização) e implementação em Python
assunto: compevol-02-operadores
tipo: exercicio_resolvido
questao: Apostila de Lucas, cap. 4; Lacerda e Carvalho, seção 3.1
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: lucas-apostila-ag,lacerda-carvalho-ag
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Apostila de Lucas, cap. 4; Lacerda e Carvalho, seção 3.1 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Passos:**
1. **inicialização:** população aleatória de $n$ indivíduos;
2. **avaliação:** aptidão de cada um;
3. **seleção** dos pais (roleta, torneio);
4. **cruzamento** com probabilidade $p_c$ e **mutação** com $p_m$;
5. **atualização:** a nova geração substitui a antiga (com **elitismo**, o melhor é mantido);
6. **finalização:** parar por número de gerações, por estagnação do melhor ou ao atingir uma meta.

```python
import math, random

def ag(f, a, b, bits=22, n=50, geracoes=100, pc=0.8, pm=0.01, semente=0):
    r = random.Random(semente)
    dec = lambda c: a + (b - a) * int("".join(map(str, c)), 2) / (2**bits - 1)
    pop = [[r.randint(0, 1) for _ in range(bits)] for _ in range(n)]
    for _ in range(geracoes):
        apt = [f(dec(c)) for c in pop]
        melhor = pop[max(range(n), key=apt.__getitem__)]
        def torneio():
            i, j = r.randrange(n), r.randrange(n)
            return pop[i] if apt[i] > apt[j] else pop[j]
        nova = [melhor[:]]                       # elitismo
        while len(nova) < n:
            p1, p2 = torneio()[:], torneio()[:]
            if r.random() < pc:
                k = r.randrange(1, bits)
                p1, p2 = p1[:k] + p2[k:], p2[:k] + p1[k:]
            for c in (p1, p2):
                nova.append([1 - g if r.random() < pm else g for g in c])
        pop = nova[:n]
    x = max(map(dec, pop), key=f)
    return x, f(x)

print(ag(lambda x: x * math.sin(10 * math.pi * x) + 1, -1, 2))
```
Com esses parâmetros, o AG chega perto de $x \approx 1{,}85$, $f \approx 2{,}85$ (máximo global do exemplo clássico). Rode com várias sementes: um AG é estocástico, e o resultado de uma execução só não basta para comparar configurações.

**Verificação:** `test_ag_completo` roda o código acima com 5 sementes e confere que todas passam de $f = 2{,}84$ e que o melhor de cada geração nunca piora (elitismo).
