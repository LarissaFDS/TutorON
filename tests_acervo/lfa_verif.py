"""Simuladores usados para conferir as resoluções do acervo de Linguagens Formais, Autômatos e Computabilidade.

Tudo aqui é pequeno e direto, para ser lido junto com os blocos de `disciplinas/lfa/materiais`:
AFD, AFN com transições vazias (construção de subconjuntos com fecho-ε), minimização, equivalência por
busca de contraexemplo, gramáticas livres de contexto (reconhecimento de Earley), autômato com pilha,
máquina de Turing de uma fita, interpretador da linguagem de programas LOOP/GOTO (a "LPM" da turma) e
funções recursivas primitivas.
"""

from collections import deque
from itertools import product

VAZIO = ""  # transição vazia (λ ou ε)


# ---------------------------------------------------------------- palavras


def palavras(alfabeto, ate):
    """Todas as palavras de comprimento 0..ate, em ordem de tamanho."""
    for n in range(ate + 1):
        for t in product(alfabeto, repeat=n):
            yield "".join(t)


# ---------------------------------------------------------------- AFD


class AFD:
    def __init__(self, estados, alfabeto, delta, inicial, finais):
        self.Q, self.S, self.d, self.q0, self.F = list(estados), list(alfabeto), dict(delta), inicial, set(finais)

    def total(self):
        return all((q, a) in self.d for q in self.Q for a in self.S)

    def roda(self, w):
        q = self.q0
        for a in w:
            if (q, a) not in self.d:
                return None  # sem transição: rejeita
            q = self.d[q, a]
        return q

    def aceita(self, w):
        return self.roda(w) in self.F

    def acessiveis(self):
        vistos, fila = {self.q0}, deque([self.q0])
        while fila:
            q = fila.popleft()
            for a in self.S:
                p = self.d.get((q, a))
                if p is not None and p not in vistos:
                    vistos.add(p)
                    fila.append(p)
        return vistos

    def completo(self, morto="d"):
        """Torna δ total com um estado morto não final."""
        if self.total():
            return self
        d = dict(self.d)
        for q in [*self.Q, morto]:
            for a in self.S:
                d.setdefault((q, a), morto)
        return AFD([*self.Q, morto], self.S, d, self.q0, self.F)

    def classes(self):
        """Classes de estados equivalentes (refinamento de partições, o mesmo resultado da tabela de pares)."""
        m = self.completo()
        Q = sorted(m.acessiveis(), key=str)
        bloco = {q: (q in m.F) for q in Q}
        while True:
            novo = {q: (bloco[q], tuple(bloco[m.d[q, a]] for a in m.S)) for q in Q}
            if len(set(novo.values())) == len(set(bloco.values())):
                break
            bloco = novo
        grupos = {}
        for q in Q:
            grupos.setdefault(bloco[q], []).append(q)
        return sorted((sorted(g, key=str) for g in grupos.values()), key=lambda g: str(g[0]))

    def minimo(self):
        m = self.completo()
        cls = m.classes()
        nome = {q: "".join(map(str, g)) if len(g) > 1 else g[0] for g in cls for q in g}
        d = {(nome[q], a): nome[m.d[q, a]] for g in cls for q in g[:1] for a in m.S}
        return AFD(sorted(set(nome.values()), key=str), m.S, d, nome[m.q0], {nome[q] for q in m.F if q in nome})


def contraexemplo(m1, m2, alfabeto=None):
    """Menor palavra aceita por um e rejeitada pelo outro (busca em largura no produto), ou None."""
    S = alfabeto or m1.S
    a, b = m1.completo("_d1"), m2.completo("_d2")
    inicio = (a.q0, b.q0)
    vistos, fila = {inicio: ""}, deque([inicio])
    while fila:
        p, q = fila.popleft()
        w = vistos[p, q]
        if (p in a.F) != (q in b.F):
            return w
        for s in S:
            nxt = (a.d[p, s], b.d[q, s])
            if nxt not in vistos:
                vistos[nxt] = w + s
                fila.append(nxt)
    return None


# ---------------------------------------------------------------- AFN (com λ)


class AFN:
    def __init__(self, estados, alfabeto, delta, inicial, finais):
        # delta: {(q, a): {p, ...}}, com a == VAZIO para transição vazia
        self.Q, self.S, self.d, self.q0, self.F = list(estados), list(alfabeto), delta, inicial, set(finais)

    def fecho(self, conjunto):
        pilha, fecho = list(conjunto), set(conjunto)
        while pilha:
            q = pilha.pop()
            for p in self.d.get((q, VAZIO), ()):
                if p not in fecho:
                    fecho.add(p)
                    pilha.append(p)
        return frozenset(fecho)

    def mover(self, conjunto, a):
        return self.fecho({p for q in conjunto for p in self.d.get((q, a), ())})

    def aceita(self, w):
        atual = self.fecho({self.q0})
        for a in w:
            atual = self.mover(atual, a)
        return bool(atual & self.F)

    def subconjuntos(self):
        """Construção de subconjuntos só com os estados atingíveis; ∅ vira um estado (morto) quando aparece."""
        inicio = self.fecho({self.q0})
        d, fila, vistos = {}, deque([inicio]), [inicio]
        while fila:
            X = fila.popleft()
            for a in self.S:
                Y = self.mover(X, a)
                d[X, a] = Y
                if Y not in vistos:
                    vistos.append(Y)
                    fila.append(Y)
        return AFD(vistos, self.S, d, inicio, [X for X in vistos if X & self.F])


def nome(conjunto):
    """Nome de um estado do AFD de subconjuntos: <q0,q1> ou ∅."""
    return "<" + ",".join(sorted(conjunto, key=str)) + ">" if conjunto else "∅"


# ---------------------------------------------------------------- gramáticas livres de contexto


def gramatica(texto):
    """'S -> aSb | λ ; A -> a' vira {'S': [('a','S','b'), ()], ...}. Variáveis: letras maiúsculas com índices."""
    g = {}
    for regra in texto.split(";"):
        cab, corpo = regra.split("->")
        cab = cab.strip()
        for alt in corpo.split("|"):
            alt = alt.strip()
            simbolos = () if alt in ("λ", "") else tuple(_simbolos(alt))
            g.setdefault(cab, []).append(simbolos)
    return g


def _simbolos(alt):
    i, out = 0, []
    while i < len(alt):
        c = alt[i]
        if c == " ":
            i += 1
            continue
        j = i + 1
        if c.isupper():  # variável com índice (D1, C+) ou nome entre colchetes
            while j < len(alt) and (alt[j].isdigit() or alt[j] in "+*[]'" and c == "C"):
                j += 1
        out.append(alt[i:j])
        i = j
    return out


def gera(g, w, inicial="S"):
    """Reconhecimento de Earley: True se a gramática gera w (aceita produções vazias)."""
    n = len(w)
    S = [set() for _ in range(n + 1)]
    S[0] = {("γ", (inicial,), 0, 0)}
    for i in range(n + 1):
        fila = deque(S[i])
        anulaveis_vistos = set()
        while fila:
            cab, corpo, ponto, origem = fila.popleft()
            if ponto < len(corpo):
                X = corpo[ponto]
                if X in g:
                    for alt in g[X]:
                        novo = (X, alt, 0, i)
                        if novo not in S[i]:
                            S[i].add(novo)
                            fila.append(novo)
                    if X in anulaveis_vistos:
                        novo = (cab, corpo, ponto + 1, origem)
                        if novo not in S[i]:
                            S[i].add(novo)
                            fila.append(novo)
                elif i < n and w[i] == X:
                    S[i + 1].add((cab, corpo, ponto + 1, origem))
            else:
                if origem == i:
                    anulaveis_vistos.add(cab)
                for c2, b2, p2, o2 in list(S[origem]):
                    if p2 < len(b2) and b2[p2] == cab:
                        novo = (c2, b2, p2 + 1, o2)
                        if novo not in S[i]:
                            S[i].add(novo)
                            fila.append(novo)
    return ("γ", (inicial,), 1, 0) in S[n]


def derivacoes_mais_a_esquerda(g, w, inicial="S", limite=40):
    """Conta as derivações mais à esquerda de w (até `limite`); gramática sem ciclos A ⇒+ A."""
    terminais = len(w)

    def conta(forma, feito):
        # forma: tupla de símbolos; feito: prefixo de w já gerado
        i = 0
        while i < len(forma) and forma[i] not in g:
            i += 1
        prefixo = "".join(forma[:i])
        if feito + prefixo != w[: len(feito) + len(prefixo)]:
            return 0
        if i == len(forma):
            return 1 if feito + prefixo == w else 0
        if sum(1 for s in forma if s not in g) + len(feito) > terminais:
            return 0
        if len(forma) > 2 * terminais + 4:
            return 0
        total = 0
        for alt in g[forma[i]]:
            total += conta(alt + forma[i + 1 :], feito + prefixo)
            if total >= limite:
                break
        return total

    return conta((inicial,), "")


# ---------------------------------------------------------------- autômato com pilha


def ap_aceita(delta, inicial, base, finais, w, passos=2000):
    """AP não determinístico, aceitação por estado final no fim da palavra.

    delta: {(q, a, X): [(p, γ), ...]} com a == VAZIO e/ou X == VAZIO permitidos; γ é empilhado com o
    primeiro símbolo no topo (o mesmo que "da direita para a esquerda" na apostila).
    """
    inicio = (inicial, 0, (base,))
    fila, vistos = deque([inicio]), {inicio}
    while fila and passos:
        passos -= 1
        q, i, pilha = fila.popleft()
        if i == len(w) and q in finais:
            return True
        topo = pilha[:1]
        opcoes = []
        for a in {VAZIO, *(w[i : i + 1])}:
            for X in {VAZIO, *topo}:
                for p, g in delta.get((q, a, X), ()):
                    resto = pilha[1:] if X else pilha
                    opcoes.append((p, i + len(a), tuple(g) + resto))
        for c in opcoes:
            if c not in vistos and len(c[2]) <= len(w) + 3:
                vistos.add(c)
                fila.append(c)
    return False


# ---------------------------------------------------------------- máquina de Turing


BRANCO = "_"


def mt(delta, w, inicial="q0", aceita="qa", rejeita="qr", passos=100_000):
    """MT de uma fita, infinita à direita; a cabeça fica parada se tentar passar da esquerda.

    delta: {(q, s): (p, escreve, 'E'|'D')}. Transição ausente = rejeita.
    Devolve (estado final, conteúdo da fita sem brancos nas pontas).
    """
    fita, cab, q = list(w) or [BRANCO], 0, inicial
    while passos and q not in (aceita, rejeita):
        passos -= 1
        s = fita[cab]
        if (q, s) not in delta:
            q = rejeita
            break
        q, fita[cab], mov = delta[q, s]
        cab = cab + 1 if mov == "D" else max(cab - 1, 0)
        if cab == len(fita):
            fita.append(BRANCO)
    if not passos:
        raise RuntimeError("MT não parou dentro do limite de passos")
    return q, "".join(fita).strip(BRANCO)


# ---------------------------------------------------------------- programas LOOP/GOTO ("LPM")


def lpm(programa, **entrada):
    """Interpreta programas LOOP com rótulos e GOTO.

    Comandos (tuplas): ('zero', x) x←0; ('inc', x) x←x+1; ('copia', x, y) x←y;
    ('loop', x, [corpo]) repete o corpo o número de vezes que x valia ao entrar; ('rotulo', L); ('goto', L);
    ('se_zero_goto', x, L). Variáveis não iniciadas valem 0.
    """
    v = dict(entrada)
    _executa(programa, v, [0])
    return v


class _Goto(Exception):
    def __init__(self, rotulo):
        self.rotulo = rotulo


def _executa(prog, v, passos):
    i = 0
    while i < len(prog):
        cmd = prog[i]
        passos[0] += 1
        if passos[0] > 5_000_000:
            raise RuntimeError("programa LPM não terminou")
        op = cmd[0]
        try:
            if op == "zero":
                v[cmd[1]] = 0
            elif op == "inc":
                v[cmd[1]] = v.get(cmd[1], 0) + 1
            elif op == "copia":
                v[cmd[1]] = v.get(cmd[2], 0)
            elif op == "loop":
                for _ in range(v.get(cmd[1], 0)):
                    _executa(cmd[2], v, passos)
            elif op == "goto":
                raise _Goto(cmd[1])
            elif op == "se_zero_goto" and v.get(cmd[1], 0) == 0:
                raise _Goto(cmd[2])
        except _Goto as g:
            alvos = [k for k, c in enumerate(prog) if c[0] == "rotulo" and c[1] == g.rotulo]
            if not alvos:
                raise
            i = alvos[0]
        i += 1


# ---------------------------------------------------------------- funções recursivas primitivas


def zero(*_):
    return 0


def suc(x):
    return x + 1


def proj(i):
    return lambda *xs: xs[i]


def comp(f, *gs):
    return lambda *xs: f(*(g(*xs) for g in gs))


def rec(base, passo):
    """f(0, ys) = base(ys); f(n+1, ys) = passo(n, f(n, ys), ys)."""

    def f(n, *ys):
        r = base(*ys)
        for k in range(n):
            r = passo(k, r, *ys)
        return r

    return f


SOMA = rec(proj(0), lambda k, r, y: suc(r))  # soma(n, y) = n + y
MULT = rec(zero, lambda k, r, y: SOMA(r, y))  # mult(n, y) = n · y
POT = rec(lambda y: 1, lambda k, r, y: MULT(r, y))  # pot(n, y) = y^n
PRED = rec(zero, lambda k, r: k)  # pred(n) = n ∸ 1
MONUS = rec(proj(0), lambda k, r, x: PRED(r))  # monus(n, x) = x ∸ n
SG = rec(zero, lambda k, r: 1)  # sg(n) = 1 se n > 0


# ---------------------------------------------------------------- expressões regulares (notação da disciplina)


def er_para_afn(er, alfabeto):
    """Construção de Thompson para ER com '+' (união), concatenação, '*', parênteses, 'λ' e '∅'."""
    contador = [0]
    delta = {}

    def novo():
        contador[0] += 1
        return f"t{contador[0]}"

    def liga(p, a, q):
        delta.setdefault((p, a), set()).add(q)

    pos = [0]

    def ver():
        return er[pos[0]] if pos[0] < len(er) else None

    def uniao():
        i, f = concat()
        while ver() == "+":
            pos[0] += 1
            i2, f2 = concat()
            ni, nf = novo(), novo()
            for x in (i, i2):
                liga(ni, VAZIO, x)
            for x in (f, f2):
                liga(x, VAZIO, nf)
            i, f = ni, nf
        return i, f

    def concat():
        i, f = estrela()
        while ver() is not None and ver() not in "+)":
            i2, f2 = estrela()
            liga(f, VAZIO, i2)
            f = f2
        return i, f

    def estrela():
        i, f = atomo()
        while ver() == "*":
            pos[0] += 1
            ni, nf = novo(), novo()
            liga(ni, VAZIO, i)
            liga(ni, VAZIO, nf)
            liga(f, VAZIO, i)
            liga(f, VAZIO, nf)
            i, f = ni, nf
        return i, f

    def atomo():
        c = ver()
        pos[0] += 1
        if c == "(":
            i, f = uniao()
            assert ver() == ")", er
            pos[0] += 1
            return i, f
        i, f = novo(), novo()
        if c == "λ":
            liga(i, VAZIO, f)
        elif c != "∅":
            assert c in alfabeto, (c, er)
            liga(i, c, f)
        return i, f

    i, f = uniao()
    assert pos[0] == len(er), er
    estados = [f"t{k}" for k in range(1, contador[0] + 1)]
    return AFN(estados, alfabeto, delta, i, {f})


def er_gera(er, w, alfabeto):
    """Decisor de A_ER: converte a ER em AFN e simula o AFN sobre w (sempre para)."""
    return er_para_afn(er, alfabeto).aceita(w)


def afd_aceita_tudo(m):
    """Decisor de {<A> | A é AFD e L(A) = Σ*}: nenhum estado atingível pode ser não final."""
    c = m.completo()
    return all(q in c.F for q in c.acessiveis())


def afd_equivale_er(m, er):
    """Decisor de {<A, R> | L(A) = L(R)}: ER → AFN → AFD e busca de contraexemplo no produto."""
    return contraexemplo(m, er_para_afn(er, m.S).subconjuntos()) is None
