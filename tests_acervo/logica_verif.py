"""Verificador pequeno de lógica para conferir os blocos de Lógica Aplicada à Computação.

Lê as fórmulas em LaTeX como estão escritas nos blocos (\\neg, \\land, \\lor, \\to, \\leftrightarrow, \\bot, \\top)
e confere:
- consequência, equivalência e satisfatibilidade proposicional por tabela-verdade completa;
- refutações por resolução proposicional, passo a passo (cada resolvente vem das duas cláusulas citadas);
- provas em dedução natural, linha a linha: cada linha é consequência das linhas citadas, as regras de caixa
  (→i, ¬i, ∨e, PBC) usam a hipótese que abre a caixa, e nenhuma linha de uma caixa fechada é citada fora dela;
- unificação (algoritmo de Robinson com teste de ocorrência) e passos de resolução de primeira ordem;
- consequência em primeira ordem por busca de contramodelo em universos finitos pequenos.

Não depende de pacote externo; ``sympy.logic`` é usado só como segunda opinião em testes.
"""

from __future__ import annotations

import re
from itertools import product

# ---------------------------------------------------------------- fórmulas proposicionais

_TOK = re.compile(
    r"\s*(\\top|\\bot|\\leftrightarrow|\\Leftrightarrow|\\iff|\\equiv|\\to|\\rightarrow|\\Rightarrow|\\land|\\wedge|\\lor|\\vee"
    r"|\\neg|\\lnot|↔|→|∧|∨|¬|⊥|⊤|[()]|[A-Za-z][A-Za-z0-9_]*)"
)
_SINONIMO = {
    "\\Leftrightarrow": "↔", "\\iff": "↔", "\\equiv": "↔", "\\leftrightarrow": "↔",
    "\\rightarrow": "→", "\\Rightarrow": "→", "\\to": "→",
    "\\wedge": "∧", "\\land": "∧", "\\vee": "∨", "\\lor": "∨",
    "\\lnot": "¬", "\\neg": "¬", "\\bot": "⊥", "\\top": "⊤",
}  # fmt: skip


def _tokens(s: str) -> list[str]:
    s = s.replace("\\,", " ").replace("\\;", " ").replace("{", "").replace("}", "")
    out, pos = [], 0
    while pos < len(s):
        if s[pos].isspace():
            pos += 1
            continue
        m = _TOK.match(s, pos)
        if not m:
            raise ValueError(f"símbolo inesperado em {s!r}: {s[pos:]!r}")
        out.append(_SINONIMO.get(m.group(1), m.group(1)))
        pos = m.end()
    return out


def parse(s: str):
    """Precedência usual (Huth e Ryan, slides da UFCG): ¬ > ∧ > ∨ > → > ↔; → e ↔ associam à direita."""
    toks = _tokens(s)
    pos = 0

    def ver():
        return toks[pos] if pos < len(toks) else None

    def come(t=None):
        nonlocal pos
        tok = ver()
        if t is not None and tok != t:
            raise ValueError(f"esperava {t!r} em {s!r}, achei {tok!r}")
        pos += 1
        return tok

    def binario(op, prox, direita=False):
        def f():
            e = prox()
            if direita:
                if ver() == op:
                    come()
                    return (op, e, f())
                return e
            while ver() == op:
                come()
                e = (op, e, prox())
            return e

        return f

    def atomo():
        tok = come()
        if tok == "¬":
            return ("¬", atomo())
        if tok == "(":
            e = bic()
            come(")")
            return e
        if tok in ("⊥", "⊤"):
            return (tok,)
        if tok is None or not re.match(r"[A-Za-z]", tok):
            raise ValueError(f"fórmula malformada: {s!r}")
        return ("at", tok)

    conj = binario("∧", atomo)
    disj = binario("∨", conj)
    imp = binario("→", disj, direita=True)
    bic = binario("↔", imp, direita=True)
    e = bic()
    if pos != len(toks):
        raise ValueError(f"sobrou {toks[pos:]} em {s!r}")
    return e


def atomos(f) -> set[str]:
    if f[0] == "at":
        return {f[1]}
    return set().union(*(atomos(x) for x in f[1:])) if len(f) > 1 else set()


def valor(f, v: dict[str, bool]) -> bool:
    op = f[0]
    if op == "at":
        return v[f[1]]
    if op == "⊤":
        return True
    if op == "⊥":
        return False
    if op == "¬":
        return not valor(f[1], v)
    a, b = valor(f[1], v), valor(f[2], v)
    return {"∧": a and b, "∨": a or b, "→": (not a) or b, "↔": a == b}[op]


def _f(x):
    return parse(x) if isinstance(x, str) else x


def valoracoes(fs):
    nomes = sorted(set().union(*(atomos(f) for f in fs))) if fs else []
    for bits in product((True, False), repeat=len(nomes)):
        yield dict(zip(nomes, bits, strict=True))


def contramodelos(premissas, conclusao) -> list[dict]:
    ps, c = [_f(p) for p in premissas], _f(conclusao)
    return [v for v in valoracoes([*ps, c]) if all(valor(p, v) for p in ps) and not valor(c, v)]


def consequencia(premissas, conclusao) -> bool:
    return not contramodelos(premissas, conclusao)


def equivalentes(a, b) -> bool:
    a, b = _f(a), _f(b)
    return all(valor(a, v) == valor(b, v) for v in valoracoes([a, b]))


def satisfazivel(*fs) -> bool:
    fs = [_f(f) for f in fs]
    return any(all(valor(f, v) for f in fs) for v in valoracoes(fs))


def tabela(f) -> list[tuple[dict, bool]]:
    f = _f(f)
    return [(v, valor(f, v)) for v in valoracoes([f])]


# ---------------------------------------------------------------- cláusulas e resolução proposicional


def literal(s: str) -> tuple[str, bool]:
    t = _tokens(s)
    if t == ["⊥"]:
        raise ValueError("use a cláusula vazia, não ⊥, num literal")
    if len(t) == 2 and t[0] == "¬":
        return (t[1], False)
    if len(t) == 1:
        return (t[0], True)
    raise ValueError(f"literal malformado: {s!r}")


def clausula(s: str) -> frozenset:
    """'{¬P, Q}', '\\{\\neg P, Q\\}', '¬P ∨ Q' ou '□' (cláusula vazia)."""
    s = s.strip().replace("\\{", "{").replace("\\}", "}").strip()
    if s in ("\\square", "□", "{}", "\\Box", "\\emptyset"):
        return frozenset()
    s = s.strip("{}")
    partes = re.split(r",|\\lor|∨|\\vee", s)
    return frozenset(literal(p) for p in partes if p.strip())


def clausula_como_formula(c: frozenset):
    if not c:
        return ("⊥",)
    lits = [("at", a) if pos else ("¬", ("at", a)) for a, pos in sorted(c)]
    f = lits[0]
    for x in lits[1:]:
        f = ("∨", f, x)
    return f


def resolventes(c1: frozenset, c2: frozenset) -> list[frozenset]:
    out = []
    for a, pos in c1:
        if (a, not pos) in c2:
            out.append((c1 - {(a, pos)}) | (c2 - {(a, not pos)}))
    return out


def confere_refutacao(entrada: list[frozenset], passos: list[tuple[frozenset, int, int]]) -> None:
    """``entrada`` numera 1..n; cada passo (cláusula, i, j) tem que ser resolvente de i e j; o último é □."""
    linhas = list(entrada)
    for c, i, j in passos:
        assert max(i, j) <= len(linhas), f"cita linha inexistente: {i}, {j}"
        assert c in resolventes(linhas[i - 1], linhas[j - 1]), f"{set(c)} não é resolvente de {i} e {j}"
        linhas.append(c)
    assert passos and passos[-1][0] == frozenset(), "a refutação não termina na cláusula vazia"


def insatisfazivel_clausulas(cls) -> bool:
    return not satisfazivel(*(clausula_como_formula(c) for c in cls))


# ---------------------------------------------------------------- dedução natural

_CAIXA = {"→i", "¬i", "PBC", "∨e"}


def confere_deducao(linhas: list[tuple[int, str, str, str]], premissas: list[str], conclusao: str) -> None:
    """Linhas (n, fórmula, regra, citações). Citação: '1, 3' ou '2-4' (caixa) ou '2, 3-4, 5-7' (∨e).

    Confere: numeração; premissas; hipóteses só abrem caixa; cada linha é consequência semântica do que cita
    (e, nas regras de caixa, da forma da regra); nenhuma linha de caixa fechada é citada depois; a última linha,
    fora de qualquer caixa, é a conclusão.
    """
    f = {}
    caixas: list[tuple[int, int]] = []
    abertas: list[int] = []
    for k, (n, formula, regra, cit) in enumerate(linhas, start=1):
        assert n == k, f"numeração: esperava {k}, achei {n}"
        f[n] = parse(formula)
        regra = regra.strip()
        simples, intervalos = [], []
        for parte in [p.strip() for p in cit.split(",") if p.strip()]:
            if re.fullmatch(r"\d+\s*[-–]\s*\d+", parte):
                a, b = (int(x) for x in re.split(r"[-–]", parte))
                intervalos.append((a, b))
            else:
                simples.append(int(parte))
        # fechar caixas: a última citada é a mais interna; no ∨e as duas caixas são vizinhas (3–4, 5–7)
        fim_esperado = n - 1
        for a, b in reversed(intervalos):
            assert regra in _CAIXA, f"linha {n}: {regra} não usa caixa"
            assert abertas and abertas[-1] == a, f"linha {n}: caixa {a}-{b} não é a mais interna aberta"
            assert b == fim_esperado, f"linha {n}: caixa {a}-{b} não termina logo antes"
            abertas.pop()
            caixas.append((a, b))
            fim_esperado = a - 1
        for j in simples:
            assert j < n, f"linha {n} cita linha futura {j}"
            for a, b in caixas:
                assert not (a <= j <= b and not (a <= n <= b)), f"linha {n} cita {j}, que está na caixa fechada {a}-{b}"
        if regra == "premissa":
            assert not abertas, f"linha {n}: premissa dentro de caixa"
            assert any(equivalentes(f[n], p) for p in premissas), f"linha {n}: não é premissa"
        elif regra in ("hipótese", "suposição"):
            abertas.append(n)
        elif regra in ("→i",):
            ((a, b),) = intervalos
            assert equivalentes(f[n], ("→", f[a], f[b])), f"linha {n}: →i não forma hipótese → fim da caixa"
        elif regra == "¬i":
            ((a, b),) = intervalos
            assert f[b] == ("⊥",) and equivalentes(f[n], ("¬", f[a])), f"linha {n}: ¬i exige ⊥ no fim da caixa"
        elif regra == "PBC":
            ((a, b),) = intervalos
            assert f[b] == ("⊥",) and equivalentes(("¬", f[n]), f[a]), f"linha {n}: PBC supõe a negação"
        elif regra == "∨e":
            (k0,) = simples
            (a1, b1), (a2, b2) = intervalos
            assert equivalentes(f[k0], ("∨", f[a1], f[a2])), f"linha {n}: casos do ∨e não batem com {k0}"
            assert equivalentes(f[b1], f[n]) and equivalentes(f[b2], f[n]), f"linha {n}: ∨e com conclusões diferentes"
        else:  # regra sem caixa: a linha segue das citadas (LEM e teoremas sem citação: fórmula válida)
            assert consequencia([f[j] for j in simples], f[n]), f"linha {n}: {regra} não segue de {simples}"
            if regra in ("→e", "MT"):
                assert len(simples) == 2, f"linha {n}: {regra} cita duas linhas"
            if regra == "∧i":
                assert f[n][0] == "∧", f"linha {n}: ∧i tem que formar conjunção"
    assert not abertas, f"caixas abertas no fim: {abertas}"
    ultima = linhas[-1][0]
    assert equivalentes(f[ultima], conclusao) and f[ultima] == parse(conclusao), "a última linha não é a conclusão"


_LINHA_DN = re.compile(r"^\s*(\d+)\.\s*\$(.+?)\$\s*[—–-]+\s*(.+?)\s*$", re.M)


def deducao_do_texto(texto: str, inicio: int = 0) -> list[tuple[int, str, str, str]]:
    """Extrai, a partir de ``inicio``, linhas '3. $c$ — $\\land e_2$ 1' em sequência numerada 1, 2, 3…"""
    linhas = []
    for m in _LINHA_DN.finditer(texto, inicio):
        n, formula, resto = int(m.group(1)), m.group(2), m.group(3)
        if n == 1 and linhas:
            break
        if n != len(linhas) + 1:
            break
        regra_tex, cit = re.match(r"^(\$.+?\$|[^\d$]+?)\s*([\d,\s–-]*)$", resto).groups()
        regra = regra_tex.strip("$ ")
        regra = (
            regra.replace("\\to", "→").replace("\\neg", "¬").replace("\\land", "∧").replace("\\lor", "∨")
            .replace("\\bot", "⊥").replace(" ", "").replace("{", "").replace("}", "")
        )  # fmt: skip
        regra = re.sub(r"_?[12]$", "", regra)  # ∧e_1, ∨i_2 → ∧e, ∨i
        regra = {"¬¬e": "¬¬e", "¬¬i": "¬¬i", "premissa": "premissa", "hipótese": "hipótese"}.get(regra, regra)
        linhas.append((n, formula, regra, cit.strip()))
    return linhas


# ---------------------------------------------------------------- termos de primeira ordem e unificação

VAR = re.compile(r"^[u-z][0-9]*$")  # convenção dos slides: x, y, z, w, u, v (com índice) são variáveis


def termo(s: str):
    s = s.strip()
    toks = re.findall(r"[A-Za-zÀ-ú_][\wÀ-ú]*|[(),]", s)
    pos = 0

    def t():
        nonlocal pos
        nome = toks[pos]
        pos += 1
        if pos < len(toks) and toks[pos] == "(":
            pos += 1
            args = [t()]
            while toks[pos] == ",":
                pos += 1
                args.append(t())
            assert toks[pos] == ")", s
            pos += 1
            return (nome, *args)
        return nome

    r = t()
    assert pos == len(toks), f"sobrou em {s!r}"
    return r


def e_var(t) -> bool:
    return isinstance(t, str) and bool(VAR.match(t))


def subst(t, s: dict):
    if isinstance(t, str):
        return subst(s[t], s) if t in s else t
    return (t[0], *(subst(a, s) for a in t[1:]))


def ocorre(x: str, t) -> bool:
    return t == x if isinstance(t, str) else any(ocorre(x, a) for a in t[1:])


def unificar(exprs, s: dict | None = None) -> dict | None:
    """Unificador mais geral de uma lista de expressões (None se não unificam). Substituição triangular."""
    s = dict(s or {})
    for a, b in zip(exprs, exprs[1:], strict=False):
        pilha = [(a, b)]
        while pilha:
            p, q = (subst(x, s) for x in pilha.pop())
            if p == q:
                continue
            if e_var(p) or e_var(q):
                x, t = (p, q) if e_var(p) else (q, p)
                if ocorre(x, t):
                    return None
                s[x] = t
            elif isinstance(p, tuple) and isinstance(q, tuple) and p[0] == q[0] and len(p) == len(q):
                pilha.extend(zip(p[1:], q[1:], strict=True))
            else:
                return None
    return s


def resolver_mgu(s: dict) -> dict:
    return {x: subst(t, s) for x, t in s.items()}


def mesma_instancia(a, b) -> bool:
    """Duas expressões são iguais a menos de renomear variáveis."""
    m = {}

    def ok(p, q):
        if e_var(p) and e_var(q):
            return m.setdefault(p, q) == q
        if isinstance(p, tuple) and isinstance(q, tuple):
            return p[0] == q[0] and len(p) == len(q) and all(ok(x, y) for x, y in zip(p[1:], q[1:], strict=True))
        return p == q

    return ok(a, b)


# ---------------------------------------------------------------- cláusulas de primeira ordem


def lit1(s: str):
    s = s.strip()
    neg = s.startswith(("¬", "\\neg"))
    s = re.sub(r"^(¬|\\neg)\s*", "", s)
    return (not neg, termo(s))


def clausula1(s: str) -> frozenset:
    s = s.strip().replace("\\{", "{").replace("\\}", "}").strip()
    if s in ("\\square", "□", "{}"):
        return frozenset()
    partes = re.split(r"\\lor|∨", s.strip("{}"))
    return frozenset(lit1(p) for p in partes if p.strip())


def _renomear(c: frozenset, sufixo: str) -> frozenset:
    def r(t):
        if isinstance(t, str):
            return t + sufixo if e_var(t) else t
        return (t[0], *(r(a) for a in t[1:]))

    return frozenset((p, r(a)) for p, a in c)


def _aplica(c: frozenset, s: dict) -> frozenset:
    return frozenset((p, subst(a, s)) for p, a in c)


def fatores(c: frozenset) -> list[frozenset]:
    out = [c]
    lits = sorted(c, key=repr)
    for i, (p1, a1) in enumerate(lits):
        for p2, a2 in lits[i + 1 :]:
            if p1 == p2:
                s = unificar([a1, a2])
                if s is not None:
                    out.append(_aplica(c, s))
    return out


def resolventes1(c1: frozenset, c2: frozenset) -> list[frozenset]:
    """Resolventes binários de fatores de c1 e de c2 renomeada (Robinson, como nos slides)."""
    out = []
    c2 = _renomear(c2, "0")
    for f1 in fatores(c1):
        for f2 in fatores(c2):
            for p1, a1 in f1:
                for p2, a2 in f2:
                    if p1 != p2:
                        s = unificar([a1, a2])
                        if s is not None:
                            out.append(_aplica(f1 - {(p1, a1)}, s) | _aplica(f2 - {(p2, a2)}, s))
    return out


def mesma_clausula(a: frozenset, b: frozenset) -> bool:
    if len(a) != len(b):
        return False
    da = ("C", *sorted(((("+" if p else "-") + repr(x[0]), x) for p, x in a), key=repr))
    db = ("C", *sorted(((("+" if p else "-") + repr(x[0]), x) for p, x in b), key=repr))
    if mesma_instancia(da, db):
        return True
    # ordem dos literais pode não coincidir: tenta permutações pequenas
    from itertools import permutations

    la, lb = list(a), list(b)
    if len(la) > 5:
        return False
    for perm in permutations(lb):
        if all(p == q for (p, _), (q, _) in zip(la, perm, strict=True)) and mesma_instancia(
            ("C", *[x for _, x in la]), ("C", *[x for _, x in perm])
        ):
            return True
    return False


def confere_refutacao1(entrada: list[frozenset], passos: list[tuple[frozenset, int, int]]) -> None:
    linhas = list(entrada)
    for c, i, j in passos:
        cand = resolventes1(linhas[i - 1], linhas[j - 1])
        assert any(mesma_clausula(c, r) for r in cand), f"{c} não é resolvente de {i} e {j}"
        linhas.append(c)
    assert passos and passos[-1][0] == frozenset()


# ---------------------------------------------------------------- semântica de primeira ordem em universos finitos


def contramodelo_finito(premissas, conclusao, predicados: dict[str, int], constantes=(), max_universo=3):
    """Procura estrutura finita (universo 1..max) que satisfaz as premissas e falsifica a conclusão.

    Premissas e conclusão são funções Python ``f(U, I) -> bool`` (U = universo, I = interpretação dos símbolos).
    """
    for n in range(1, max_universo + 1):
        U = range(n)
        nomes = sorted(predicados)
        tuplas = {p: list(product(U, repeat=predicados[p])) for p in nomes}
        espacos = [product((False, True), repeat=len(tuplas[p])) for p in nomes]
        consts = list(product(U, repeat=len(constantes)))
        for valores in product(*[list(e) for e in espacos]):
            I = {p: {t for t, b in zip(tuplas[p], v, strict=True) if b} for p, v in zip(nomes, valores, strict=True)}
            for cv in consts:
                I.update(dict(zip(constantes, cv, strict=True)))
                if all(p(U, I) for p in premissas) and not conclusao(U, I):
                    return n, I
    return None
