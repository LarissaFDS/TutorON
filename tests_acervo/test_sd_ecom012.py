"""Resoluções dos blocos m14–m16 de SD (provas de Circuitos Digitais, ECOM012, 2015–2016), por enumeração."""

from itertools import product

GRAY = [0, 1, 3, 2]


def nand(p, q):
    return 1 - (p & q)


def nor(p, q):
    return 1 - (p | q)


def test_m14_circuito_1_simplifica_para_ab_c():
    for a, b, c in product((0, 1), repeat=3):
        f = ((a & (1 - b)) | ((1 - a) | c)) & (1 - ((1 - a) | c))
        assert f == (a & (1 - b) & (1 - c))


def test_m14_karnaugh_4_variaveis():
    tab = [[1, 1, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1]]  # linhas xy, colunas zw (Gray)
    for i, xy in enumerate(GRAY):
        for j, zw in enumerate(GRAY):
            y, z, w = xy & 1, zw >> 1, zw & 1
            assert tab[i][j] == ((1 - w) | ((1 - y) & (1 - z)))


def test_m14_karnaugh_3_variaveis_tem_duas_formas_minimas():
    tab = [[0, 1, 0, 1], [1, 1, 0, 1]]  # linha x, colunas yz (Gray)
    for x in (0, 1):
        for j, yz in enumerate(GRAY):
            y, z = yz >> 1, yz & 1
            base = ((1 - y) & z) | (y & (1 - z))
            assert tab[x][j] == base | (x & (1 - z)) == base | (x & (1 - y))


def test_m14_bases():
    n = int("1001101001", 2)
    assert (n, oct(n), hex(n)) == (617, "0o1151", "0x269")


def test_m14_portas_universais():
    for a, b in product((0, 1), repeat=2):
        assert nand(nand(a, b), nand(a, b)) == a & b
        assert nand(nand(a, a), nand(b, b)) == a | b
        assert nor(nor(a, b), nor(a, b)) == a | b
        assert nor(nor(a, a), nor(b, b)) == a & b


def test_m15_latch_sr_nand_repousa_com_entradas_em_1():
    def latch(s, r, q):
        for _ in range(4):
            q = nand(s, nand(r, q))
        return q

    assert latch(1, 1, 0) == 0 and latch(1, 1, 1) == 1  # repouso: guarda Q
    assert latch(0, 1, 0) == 1 and latch(1, 0, 1) == 0


def detector(clock, porta):
    """Gerador de pulso com NOT de 1 passo de atraso: porta(clk, NOT atrasado)."""
    inv = [1 - clock[0]] + [1 - c for c in clock[:-1]]
    return [porta(c, i) for c, i in zip(clock, inv, strict=True)]


def test_m15_and_pulsa_na_subida_e_nor_na_descida():
    clock = [0, 0, 1, 1, 1, 0, 0, 0, 1, 1]
    assert detector(clock, lambda c, i: c & i) == [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
    assert detector(clock, nor) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]


def test_m16_mux_de_paridade_par():
    d = [int(bin(i).count("1") % 2 == 0) for i in range(8)]
    assert [i for i, v in enumerate(d) if v] == [0, 3, 5, 6]


def test_m16_decodificador_e_demux_3_bits():
    for e, s in product((0, 1), range(8)):
        s2, s1, s0 = (s >> 2) & 1, (s >> 1) & 1, s & 1
        saidas = [
            e & ((s2 if i & 4 else 1 - s2) & (s1 if i & 2 else 1 - s1) & (s0 if i & 1 else 1 - s0)) for i in range(8)
        ]
        assert saidas == [int(e and i == s) for i in range(8)]


def test_m16_comparador_de_igualdade_8_bits():
    for a, b in [(0, 0), (0xA5, 0xA5), (0xA5, 0xA4), (0xFF, 0x7F)]:
        assert all(1 - (((a >> i) & 1) ^ ((b >> i) & 1)) for i in range(8)) == (a == b)


def test_m16_hexadecimal_contagem_e_identidade():
    validos = [w for w in "BED CAB DEAD DECADE ACCEDED BAG DAD".split() if all(c in "0123456789ABCDEF" for c in w)]
    assert validos == ["BED", "CAB", "DEAD", "DECADE", "ACCEDED", "DAD"]
    for r, k in [(2, 3), (8, 2), (10, 3), (16, 2)]:
        assert len(range(1, r**k)) == r**k - 1
    assert all(((x & y) | (x & (1 - y))) == x for x, y in product((0, 1), repeat=2))


# ---------------------------------------------------------------- listas das aulas 1 a 7 (m17–m19)


def test_m17_bases_e_complemento_de_2():
    for n, b, o, h in [
        (1984, "11111000000", "3700", "7c0"),
        (4000, "111110100000", "7640", "fa0"),
        (8192, "10000000000000", "20000", "2000"),
        (100, "1100100", "144", "64"),
    ]:
        assert (format(n, "b"), format(n, "o"), format(n, "x")) == (b, o, h)
    assert (0b00000000 - 0b11111111) & 0xFF == 0b00000001
    assert (0b11111111 + 0b11111111) & 0xFF == 0b11111110
    assert [2 ** (2**n) for n in (1, 2, 3, 4)] == [4, 16, 256, 65536]


def test_m17_or_com_3_nand_e_xor_com_4_nand():
    for a, b in product((0, 1), repeat=2):
        assert nand(nand(a, a), nand(b, b)) == a | b
        n = nand(a, b)
        assert nand(nand(a, n), nand(b, n)) == a ^ b


def test_m18_circuitos_da_aula_4():
    for a, b in product((0, 1), repeat=2):
        assert 1 - (1 - (a ^ b)) == a ^ b  # (A XNOR B)' = A XOR B
    for a, b, c in product((0, 1), repeat=3):
        x = int((a, b, c) in {(0, 0, 0), (1, 0, 0), (1, 1, 1)})
        assert x == (((1 - b) & (1 - c)) | (a & b & c))


def test_m18_karnaugh_da_aula_5():
    t1 = [[1, 0, 0, 1], [1, 0, 1, 1]]  # linha x, colunas yz
    for x in (0, 1):
        for j, yz in enumerate(GRAY):
            y, z = yz >> 1, yz & 1
            assert t1[x][j] == ((1 - z) | (x & y))
    t3 = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]  # linhas gh, colunas ij
    for i, gh in enumerate(GRAY):
        for k, ij in enumerate(GRAY):
            assert t3[i][k] == (gh & 1) ^ (ij & 1)
    for a, b, c in product((0, 1), repeat=3):
        s = int(4 * a + 2 * b + c in {0, 1, 3, 5, 7})
        assert s == (c | ((1 - a) & (1 - b)))


def test_m19_tanque_mux_e_paridade():
    nivel = 0
    for _ in range(5):  # botão em 1: enche até o sensor e para
        ve, vs = 1 & (1 - nivel), 0
        nivel = 1 if ve else nivel
    assert (nivel, 1 & (1 - nivel), vs) == (1, 0, 0)
    for s, i0, i1 in product((0, 1), repeat=3):
        assert (((1 - s) & i0) | (s & i1)) == (i1 if s else i0)
    for a, b, c in product((0, 1), repeat=3):
        assert 1 - (a ^ b ^ c) == int((a + b + c) % 2 == 0)
        assert (a ^ b ^ c) == int(((1 - a) + (1 - b) + (1 - c)) % 2 == 0)  # chave fechada = 0


def test_m19_codificador_gray_e_decodificador_ativo_em_baixo():
    for i in range(4):
        e = [int(k == i) for k in range(4)]
        assert ((e[2] | e[3]) << 1 | (e[1] | e[3])) == i
    for n in range(16):
        g = n ^ (n >> 1)
        bits = [(g >> k) & 1 for k in range(4)]
        b3 = bits[3]
        b2 = b3 ^ bits[2]
        b1 = b2 ^ bits[1]
        b0 = b1 ^ bits[0]
        assert b3 << 3 | b2 << 2 | b1 << 1 | b0 == n
    for s in range(4):
        s1, s0 = s >> 1, s & 1
        y = [nand(s1 if i & 2 else 1 - s1, s0 if i & 1 else 1 - s0) for i in range(4)]
        assert y == [0 if i == s else 1 for i in range(4)]
