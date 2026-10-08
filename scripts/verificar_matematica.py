"""Casos objetivos para as correções; não executa nenhum código do OCR/LLM."""
import itertools
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from acervo.common import ROOT, write_json


def verify():
    checks = []
    # Contagem por recursão, independente da fórmula fechada.
    def stars(n):
        return 0 if not n else stars(n-1)+n+stars(n-1)
    for n in range(13):
        assert stars(n) == 2**(n+1)-n-2
    checks.append({'familia': 'asterisco', 'casos': 13, 'ok': True})
    # Todas as permutações até sete elementos: ordenação e limite de inversões.
    count = 0
    for n in range(1,8):
        for values in itertools.permutations(range(n)):
            a, flips = list(values), 0
            for m in range(n,1,-1):
                p = a.index(max(a[:m]))
                if p == m-1: continue
                if p:
                    a[:p+1] = reversed(a[:p+1]); flips += 1
                a[:m] = reversed(a[:m]); flips += 1
            assert a == sorted(values) and flips <= 2*(n-1)
            count += 1
    checks.append({'familia': 'panquecas', 'casos': count, 'ok': True})
    # Soma máxima: recorrência confrontada com enumeração de TODOS os intervalos.
    count = 0
    for n in range(8):
        for a in itertools.product((-2,0,3), repeat=n):
            end = best = 0
            for x in a:
                end = max(0,end+x); best = max(best,end)
            brute = max([0]+[sum(a[i:j]) for i in range(n) for j in range(i+1,n+1)])
            assert best == brute
            count += 1
    checks.append({'familia': 'soma_maxima_vazia', 'casos': count, 'ok': True})
    # Todas as tabelas normais 3x3: conta rotações/reflexões como soluções distintas.
    magic = []
    for a in itertools.permutations(range(1,10)):
        if a[4] != 5 or sum(a[:3]) != 15 or sum(a[3:6]) != 15: continue
        if all(sum(a[i::3]) == 15 for i in range(3)) and sum(a[6:]) == 15 and a[0]+a[4]+a[8] == 15 and a[2]+a[4]+a[6] == 15:
            magic.append(a)
    assert len(magic) == 8
    checks.append({'familia': 'quadrado_magico', 'casos': 362880, 'solucoes': len(magic), 'ok': True})
    rng = random.Random(42)
    for _ in range(250):
        n = rng.randrange(1,8)
        tri = [[rng.randrange(1,20) for _ in range(i+1)] for i in range(n)]
        dp = [tri[0][0]]
        for i in range(1,n):
            dp = [tri[i][0]+dp[0]] + [tri[i][j]+min(dp[j-1],dp[j]) for j in range(1,i)] + [tri[i][i]+dp[-1]]
        costs = []
        for moves in itertools.product((0,1), repeat=n-1):
            j = 0; cost = tri[0][0]
            for i,step in enumerate(moves,1):
                j += step; cost += tri[i][j]
            costs.append(cost)
        assert min(dp) == min(costs)
    checks.append({'familia': 'triangulo', 'casos': 250, 'ok': True})
    for _ in range(250):
        a = [rng.randrange(1,15) for _ in range(rng.randrange(1,10))]
        target = rng.randrange(30)
        possible = [True]+[False]*target
        for x in a:
            for s in range(target,x-1,-1): possible[s] |= possible[s-x]
        brute = any(sum(x for x,b in zip(a,bits) if b) == target for bits in itertools.product((0,1), repeat=len(a)))
        assert possible[target] == brute
    checks.append({'familia': 'subset_sum', 'casos': 250, 'ok': True})
    total = 0
    for n in range(1,201):
        for missing in range(1,n+1):
            numbers = [x for x in range(1,n+1) if x != missing]
            assert n*(n+1)//2-sum(numbers) == missing
            xor = 0
            for x in range(1,n+1): xor ^= x
            for x in numbers: xor ^= x
            assert xor == missing
            total += 1
    checks.append({'familia': 'numero_faltante', 'casos': total, 'ok': True})
    # Na fonte: três arestas de custo 0 versus uma aresta de custo 1.
    assert 0+0+0 < 1 and 1+1+1 > 2
    checks.append({'familia': 'contraexemplo_caminho', 'casos': 1, 'ok': True})
    # Todos os torneios até cinco vértices, confrontando o invariante de inserção.
    count = 0
    for n in range(1,6):
        pairs = list(itertools.combinations(range(n),2))
        for bits in itertools.product((0,1),repeat=len(pairs)):
            wins = {(a,b) if bit else (b,a) for (a,b),bit in zip(pairs,bits)}
            order = []
            for x in range(n):
                p = next((i for i,y in enumerate(order) if (x,y) in wins),len(order))
                order.insert(p,x)
            assert all((a,b) in wins for a,b in zip(order,order[1:]))
            count += 1
    checks.append({'familia': 'torneio', 'casos': count, 'ok': True})
    for _ in range(250):
        a = sorted(rng.randrange(-20,20) for _ in range(rng.randrange(12)))
        b = sorted(rng.randrange(-20,20) for _ in range(rng.randrange(1,12)))
        k = rng.randrange(1,len(a)+len(b)+1)
        if len(a)>len(b): a,b=b,a
        lo,hi=max(0,k-len(b)),min(k,len(a))
        while lo<=hi:
            i=(lo+hi)//2; j=k-i
            al=a[i-1] if i else float('-inf')
            ar=a[i] if i<len(a) else float('inf')
            bl=b[j-1] if j else float('-inf')
            br=b[j] if j<len(b) else float('inf')
            if al<=br and bl<=ar:
                answer=max(al,bl); break
            if al>br: hi=i-1
            else: lo=i+1
        else: raise AssertionError('Partição ausente')
        assert answer==sorted(a+b)[k-1]
    checks.append({'familia': 'selecao_duas_listas', 'casos': 250, 'ok': True})
    for n in range(11):
        pegs=[list(range(n,0,-1)),[],[],[]]
        moves=[0]
        def move(src,dst):
            x=pegs[src].pop()
            assert not pegs[dst] or x<pegs[dst][-1]
            pegs[dst].append(x); moves[0]+=1
        def hanoi(n,src,dst,a,b):
            if not n: return
            if n==1: move(src,dst); return
            hanoi(n-2,src,a,b,dst)
            move(src,b); move(src,dst); move(b,dst)
            hanoi(n-2,a,dst,src,b)
        hanoi(n,0,1,2,3)
        expected=(3 if n%2==0 else 4)*2**(n//2)-3
        assert moves[0]==expected and pegs[1]==list(range(n,0,-1))
    checks.append({'familia': 'hanoi_quatro_pinos_estrategia', 'casos': 11, 'ok': True})
    queens=sum(all(abs(a[i]-a[j])!=j-i for i in range(8) for j in range(i+1,8))
               for a in itertools.permutations(range(1,9)))
    assert queens==92
    checks.append({'familia': 'oito_damas', 'casos': 40320, 'solucoes': queens, 'ok': True})
    count=0
    for n in range(1,6):
        pairs=list(itertools.combinations(range(n),2))
        for bits in itertools.product((0,1),repeat=len(pairs)):
            edges={p for p,bit in zip(pairs,bits) if bit}
            for x in itertools.product((0,1),repeat=n):
                pair_model=all(x[i]+x[j]<=1 for i,j in pairs if (i,j) not in edges)
                aggregated=True
                for j in range(n):
                    nonneighbors=[i for i in range(n) if i!=j and tuple(sorted((i,j))) not in edges]
                    h=len(nonneighbors)
                    if h*x[j]+sum(x[i] for i in nonneighbors)>h: aggregated=False
                assert pair_model==aggregated
                count+=1
    checks.append({'familia': 'clique_modelo_inteiro', 'casos': count, 'ok': True})
    vertices=[(0,0),(0,120000),(60000,90000),(110000,15000),(110000,0)]
    for v,s in vertices:
        assert 0<=v<=110000 and s>=0 and v+2*s<=240000 and 3*v+2*s<=360000
    assert [16*v+14*s for v,s in vertices]==[0,1680000,2220000,1970000,1760000]
    checks.append({'familia': 'racoes_vertices_lucro', 'casos': 5, 'ok': True})
    result = {'verificacoes': checks, 'total_casos': sum(c['casos'] for c in checks),
              'limite': 'Casos finitos verificam propriedades das versões derivadas; não certificam todas as provas nem respostas de IA.'}
    write_json(ROOT / '03-triagem/verificacoes-curadoria.json', result)
    print(result)


if __name__ == '__main__':
    verify()
