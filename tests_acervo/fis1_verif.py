"""Resoluções independentes das questões de Física 1 (turma do Prof. Rosso), usadas pelos testes do acervo.

Cada função refaz uma questão a partir dos dados do enunciado parafraseado no bloco, sem usar o livro
nem manuais de soluções. Os testes comparam estes números com os que aparecem no texto dos blocos.
"""

from math import atan2, cos, degrees, hypot, radians, sin, sqrt

G = 9.8


def fmt(x: float, casas: int) -> str:
    """Número no formato do acervo: vírgula decimal (12.0 → '12,0')."""
    return f"{x:.{casas}f}".replace(".", ",")


def raizes_quadratica(a: float, b: float, c: float) -> list[float]:
    d = b * b - 4 * a * c
    if d < 0:
        return []
    return sorted({(-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)})


# ---------------------------------------------------------------- AB1


def ab1_q1_velocidade():
    """v = (6t − 4t²) i + 8 j."""
    ax = lambda t: 6 - 8 * t  # noqa: E731
    t_a0 = 6 / 8
    # rapidez 10 → vx = ±6
    tempos = [t for s in (6, -6) for t in raizes_quadratica(4, -6, s) if t > 0]
    return {"a3": ax(3.0), "t_a0": t_a0, "v_nula": False, "t_rapidez10": tempos}


def ab1_q2_projetil(g=10.0, sen=sin(radians(60)), cos_=cos(radians(60))):
    v0, t = 42.0, 5.50
    vx, vy0 = v0 * cos_, v0 * sen
    h = vy0 * t - g * t * t / 2
    vy = vy0 - g * t
    return {"h": h, "vx": vx, "vy": vy, "v": hypot(vx, vy), "ang": degrees(atan2(vy, vx)), "H": vy0**2 / (2 * g),
            "t_topo": vy0 / g}  # fmt: skip


def atrito_bloco(F, P, m=2.5, mus=0.40, muk=0.25, g=G):
    """Bloco em repouso com F horizontal e P vertical para cima: (atrito, desliza?)."""
    N = m * g - P
    if F <= mus * N + 1e-12:
        return F, False
    return muk * N, True


def ab1_q4_mu(a=0.5, g=10.0):
    return (g - 5 * a) / (2 * g)


def ab1_q4_tracoes_por_massa(a=0.5, g=10.0):
    return g + a, 2 * (g - a)


# ---------------------------------------------------------------- reavaliação AB1


def projetil_parede(v0=25.0, th=40.0, d=22.0, g=G):
    c, s = cos(radians(th)), sin(radians(th))
    t = d / (v0 * c)
    return {"t": t, "y": v0 * s * t - g * t * t / 2, "vx": v0 * c, "vy": v0 * s - g * t, "t_topo": v0 * s / g,
            "alcance": v0**2 * sin(radians(2 * th)) / g}  # fmt: skip


def alcance(v0, th, g=G):
    return v0**2 * sin(radians(2 * th)) / g


def bloco_forca_inclinada(m=3.5, F=15.0, th=40.0, muk=0.25, g=G, para_baixo=True):
    s = 1 if para_baixo else -1
    N = m * g + s * F * sin(radians(th))
    fk = muk * N
    return {"N": N, "fk": fk, "a": (F * cos(radians(th)) - fk) / m}


def plano_inclinado_polia(mA=10.0, muk=0.20, th=30.0, g=G, A_desce=True):
    s = -1 if A_desce else 1
    return mA * (sin(radians(th)) + s * muk * cos(radians(th)))


# ---------------------------------------------------------------- AB2


def pacote_mola(m=2.0, v=4.0, k=10_000.0, f=15.0):
    d = max(raizes_quadratica(k / 2, f, -m * v * v / 2))
    return {"d": d, "K": m * v * v / 2, "U": k * d * d / 2, "termica": f * d, "d_sem_atrito": v * sqrt(m / k)}


def colisao_elastica(m1=0.030, m2=0.075, h1=0.080, g=G):
    v1 = sqrt(2 * g * h1)
    v1f = (m1 - m2) / (m1 + m2) * v1
    v2f = 2 * m1 / (m1 + m2) * v1
    return {"v1i": v1, "v1f": v1f, "v2f": v2f, "h2": v2f**2 / (2 * g),
            "p_antes": m1 * v1, "p_depois": m1 * v1f + m2 * v2f,
            "K_antes": m1 * v1**2 / 2, "K_depois": m1 * v1f**2 / 2 + m2 * v2f**2 / 2}  # fmt: skip


def disco_bloco(M=2.5, m=1.2, R=0.20, g=G):
    a = 2 * m * g / (M + 2 * m)
    return {"a": a, "alpha": a / R, "T": M * a / 2, "T_bloco": m * (g - a)}


def rolamento_rampa(fator_I, M=6.0, h=1.2, th=30.0, g=G):
    """fator_I = I/(MR²): 2/5 esfera maciça, 1/2 disco ou cilindro."""
    v = sqrt(2 * g * h / (1 + fator_I))
    a = g * sin(radians(th)) / (1 + fator_I)
    f = M * g * sin(radians(th)) - M * a
    return {"v": v, "a": a, "f": f, "mu_min": f / (M * g * cos(radians(th)))}


# ---------------------------------------------------------------- reavaliação AB2


def pendulo_balistico(h, m=0.0095, M=5.4, g=G):
    V = sqrt(2 * g * h)
    return {"V": V, "v": (m + M) / m * V, "perda": 1 - m / (m + M)}


def atwood_disco(M, m1=0.400, m2=0.600, R=0.12, g=G):
    a = (m2 - m1) * g / (m1 + m2 + M / 2)
    T1, T2 = m1 * (g + a), m2 * (g - a)
    return {"a": a, "T1": T1, "T2": T2, "alpha": a / R, "torque": (T2 - T1) * R, "I_alpha": M * R * R / 2 * a / R}


def cilindro_telhado(L=6.0, th=30.0, R=0.20, H=5.0, g=G):
    v = sqrt(4 / 3 * g * L * sin(radians(th)))
    vx, vy = v * cos(radians(th)), v * sin(radians(th))
    t = max(raizes_quadratica(g / 2, vy, -H))
    return {"v": v, "omega": v / R, "vx": vx, "vy": vy, "t": t, "x": vx * t, "t_largado": sqrt(2 * H / g)}


def barata_disco(w0=1.5, M_sobre_m=6.0, r0=0.8):
    Ii = M_sobre_m / 2 + r0**2
    If = M_sobre_m / 2 + 1
    wf = Ii * w0 / If
    return {"Ii": Ii, "If": If, "wf": wf, "K_razao": (If * wf**2) / (Ii * w0**2)}


# ---------------------------------------------------------------- análise dimensional


def dimensoes():
    """Confere com SymPy as dimensões das expressões finais usadas nos blocos."""
    from sympy import sqrt as ssqrt
    from sympy.physics.units import Quantity, kilogram, meter, newton, second
    from sympy.physics.units.util import convert_to

    g = meter / second**2
    m = M = kilogram
    h = L = R = d = meter
    k = newton / meter
    expr = {
        "v = sqrt(2gh)": (ssqrt(2 * g * h), meter / second),
        "a = 2mg/(M+2m)": (2 * m * g / (M + 2 * m), meter / second**2),
        "T = Ma/2": (M * (2 * m * g / (M + 2 * m)) / 2, newton),
        "alpha = a/R": (g / R, 1 / second**2),
        "R = v0^2/g": ((meter / second) ** 2 / g, meter),
        "kd^2/2": (k * d**2 / 2, newton * meter),
        "v = (m+M)/m sqrt(2gh)": ((m + M) / m * ssqrt(2 * g * h), meter / second),
        "v = sqrt(4gL/3)": (ssqrt(4 * g * L / 3), meter / second),
    }
    return [nome for nome, (e, esperado) in expr.items()
            if convert_to(e / esperado, [kilogram, meter, second]).has(Quantity)]  # fmt: skip
