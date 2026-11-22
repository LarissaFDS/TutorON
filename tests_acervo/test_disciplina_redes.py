"""Acervo de Redes de Computadores (Ciência da Computação) e conferência das resoluções.

Os blocos parafraseiam as provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (IC-UFAL).
As contas, os protocolos e as simulações citadas nos blocos são conferidos aqui com a biblioteca
padrão do Python (socket, http.server, ipaddress, struct), sempre em localhost.
"""

import heapq
import http.client
import http.server
import ipaddress
import re
import socket
import struct
import threading
import time
from email.utils import formatdate

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

REDES = disciplinas.obter("redes")
PASTA = ROOT / "disciplinas/redes"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(REDES.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "redes")
FRONTEIRA = ("so", "grafos", "projsw")


def buscar(pergunta, d=REDES):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo


def test_redes_cadastrada_com_acervo_proprio():
    assert REDES.nome == "Redes de Computadores" and REDES.itens.exists()
    ids = {c["id"] for c in read_json(REDES.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({REDES.itens, REDES.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(REDES.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert REDES.situacao == "em validação" and REDES.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas redes --embeddings`."""
    assert disciplinas.registros(REDES) == read_json(REDES.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert len(t) <= 2200, i["id"]
        ultima = t.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in t and "Status da resolução:" in t, i["id"]
        assert re.search(r"`(test_\w+)`", ultima).group(1) in globals(), i["id"]
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO, (arq.name, f)


def test_sem_dados_pessoais_livros_nem_binarios():
    textos = " ".join(i["texto"] for i in TODOS.values()) + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    # só os dois endereços fictícios do enunciado de e-mail
    assert set(re.findall(r"[\w.]+@[\w.]+\.\w+", textos)) <= {"aluno@ic.ufal.br", "gates@microsoft.com"}
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"] == "Protegido" or f["id"] == "turma-resolucoes-ple-2020-1":
            assert f["uso"] == "referencia", f["id"]
    soltos = [p for p in PASTA.rglob("*") if p.suffix.lower() in (".pdf", ".docx", ".png", ".jpg", ".jpeg")]
    assert not soltos


PERGUNTAS = [
    ("Quais são as 5 camadas da pilha TCP/IP?", "redes-camadas-tcpip-encapsulamento-pdu"),
    ("O que é encapsulamento e para que serve o cabeçalho?", "redes-camadas-tcpip-encapsulamento-pdu"),
    ("Como funciona o GET condicional do HTTP?", "redes-http-get-condicional-proxy-stateless"),
    ("O HTTP é stateless ou stateful?", "redes-http-get-condicional-proxy-stateless"),
    ("Como o DNS resolve www.ic.ufal.br?", "redes-dns-resolucao-iterativa-registro-mx"),
    ("Como o servidor de e-mail descobre o servidor MX do destinatário?", "redes-dns-resolucao-iterativa-registro-mx"),
    (
        "O que é um socket e o que acontece no bind, listen e accept?",
        "redes-sockets-bind-listen-accept-cliente-servidor-p2p",
    ),
    (
        "Qual a diferença entre multiplexação e demultiplexação?",
        "redes-multiplexacao-demultiplexacao-portas-campo-protocolo",
    ),
    (
        "Para que servem os números de sequência e de reconhecimento do TCP?",
        "redes-tcp-numero-sequencia-reconhecimento-cumulativo-byte-stream",
    ),
    ("O que aconteceu na conexão do log do tcpdump?", "redes-log-tcpdump-handshake-dados-encerramento"),
    (
        "Qual a diferença entre Go-Back-N e retransmissão seletiva?",
        "redes-tcp-entrega-confiavel-go-back-n-retransmissao-seletiva",
    ),
    (
        "Qual a diferença entre controle de fluxo e controle de congestionamento?",
        "redes-controle-de-fluxo-versus-congestionamento-tcp-udp",
    ),
    (
        "Como funciona a partida lenta da janela de congestionamento?",
        "redes-janela-congestionamento-partida-lenta-tahoe-reno",
    ),
    ("Com máscara /30, 192.168.0.9 e 192.168.0.13 conversam?", "redes-subredes-mascara-30-26-endereco-9-ttl"),
    ("Para que serve o campo TTL do IP?", "redes-subredes-mascara-30-26-endereco-9-ttl"),
    ("Qual a diferença entre Link State e Vetor de Distância?", "redes-roteamento-link-state-vetor-de-distancia"),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Qual a diferença entre controle de fluxo e controle de congestionamento?", d)).isdisjoint(
            TODOS
        )
    assert not buscar("Como funciona um flip-flop JK?")
    assert not set(buscar("Como calcular a transformada de Laplace de um degrau?"))


# ---------------------------------------------------------------- conferência das resoluções


def test_encapsulamento():
    msg = b"oi"
    udp = struct.pack("!HHHH", 53000, 5000, 8 + len(msg), 0) + msg
    ip = (
        struct.pack(
            "!BBHHHBBH4s4s",
            0x45,
            0,
            20 + len(udp),
            1,
            0,
            64,
            17,
            0,
            socket.inet_aton("10.0.0.1"),
            socket.inet_aton("10.0.0.2"),
        )
        + udp
    )
    quadro = b"\xaa" * 6 + b"\xbb" * 6 + struct.pack("!H", 0x0800) + ip + b"\x00" * 4
    (tipo,) = struct.unpack("!H", quadro[12:14])
    assert tipo == 0x0800
    datagrama = quadro[14:-4]
    assert datagrama[0] >> 4 == 4 and datagrama[9] == 17 and datagrama[8] == 64
    seg = datagrama[(datagrama[0] & 0xF) * 4 :]
    _, porta, tam, _ = struct.unpack("!HHHH", seg[:8])
    assert porta == 5000 and seg[8:tam] == msg


@pytest.fixture
def servidor_http(tmp_path):
    arq = tmp_path / "pagina.html"
    arq.write_text("versao 1", encoding="utf-8")

    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(tmp_path), **k)

        def log_message(self, *a):
            pass

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield srv.server_address[1], arq
    srv.shutdown()
    srv.server_close()


def _get(porta, cab=None):
    c = http.client.HTTPConnection("127.0.0.1", porta, timeout=10)
    c.request("GET", "/pagina.html", headers=cab or {})
    r = c.getresponse()
    corpo = r.read()
    c.close()
    return r.status, r.getheader("Last-Modified"), corpo


def test_get_condicional(servidor_http):
    porta, arq = servidor_http
    st, lm, corpo = _get(porta)
    assert st == 200 and lm and corpo == b"versao 1"
    st, _, corpo = _get(porta, {"If-Modified-Since": lm})
    assert st == 304 and corpo == b""
    arq.write_text("versao 2", encoding="utf-8")
    futuro = time.time() + 120
    import os

    os.utime(arq, (futuro, futuro))
    st, _, corpo = _get(porta, {"If-Modified-Since": lm})
    assert st == 200 and corpo == b"versao 2"
    assert formatdate(futuro, usegmt=True) != lm


def test_dns_iterativo():
    raiz = {"br.": ("NS", "ns-br")}
    servidores = {
        "raiz": raiz,
        "ns-br": {"ufal.br.": ("NS", "ns-ufal")},
        "ns-ufal": {"www.ic.ufal.br.": ("A", "200.17.112.1"), "microsoft.com.": None},
    }
    mx = [(10, "mx1.exemplo.com"), (5, "mx0.exemplo.com"), (20, "mx2.exemplo.com")]
    cache, consultados = {}, []

    def resolver(nome):
        if nome in cache:
            return cache[nome]
        atual = "raiz"
        while True:
            consultados.append(atual)
            zona = servidores[atual]
            chave = next(k for k in zona if nome.endswith(k) and zona[k])
            tipo, valor = zona[chave]
            if tipo == "A":
                cache[nome] = valor
                return valor
            atual = valor

    assert resolver("www.ic.ufal.br.") == "200.17.112.1"
    assert consultados == ["raiz", "ns-br", "ns-ufal"]
    resolver("www.ic.ufal.br.")
    assert len(consultados) == 3
    assert min(mx)[1] == "mx0.exemplo.com"


def test_sockets():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen()
    porta = s.getsockname()[1]

    def atender(conn):
        with conn:
            conn.sendall(conn.recv(100).upper())

    def laco():
        for _ in range(2):
            conn, _ = s.accept()
            threading.Thread(target=atender, args=(conn,), daemon=True).start()

    threading.Thread(target=laco, daemon=True).start()
    a = socket.create_connection(("127.0.0.1", porta), timeout=10)
    b = socket.create_connection(("127.0.0.1", porta), timeout=10)
    b.sendall(b"bia")
    a.sendall(b"ana")
    assert a.recv(100) == b"ANA" and b.recv(100) == b"BIA"
    a.close()
    b.close()
    outro = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with pytest.raises(OSError):
        outro.bind(("127.0.0.1", porta))
    outro.close()
    s.close()
    livre = socket.socket()
    livre.bind(("127.0.0.1", 0))
    p2 = livre.getsockname()[1]
    livre.close()
    with pytest.raises(OSError):
        socket.create_connection(("127.0.0.1", p2), timeout=5)


def test_multiplexacao():
    u1, u2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM), socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for u in (u1, u2):
        u.bind(("127.0.0.1", 0))
        u.settimeout(5)
    env = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    env.sendto(b"para1", u1.getsockname())
    env.sendto(b"para2", u2.getsockname())
    assert u1.recv(100) == b"para1" and u2.recv(100) == b"para2"
    for u in (u1, u2, env):
        u.close()
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    s.listen()
    c1 = socket.create_connection(s.getsockname(), timeout=5)
    c2 = socket.create_connection(s.getsockname(), timeout=5)
    k1, _ = s.accept()
    k2, _ = s.accept()
    tuplas = {(k.getpeername(), k.getsockname()) for k in (k1, k2)}
    assert len(tuplas) == 2 and k1.getsockname() == k2.getsockname()
    for k in (c1, c2, k1, k2, s):
        k.close()
    assert socket.IPPROTO_TCP == 6 and socket.IPPROTO_UDP == 17


def receptor_cumulativo(segmentos, inicio):
    """Devolve o ACK enviado após cada segmento (seq, tamanho)."""
    esperado, guardados, acks = inicio, {}, []
    for seq, tam in segmentos:
        guardados[seq] = tam
        while esperado in guardados:
            esperado += guardados.pop(esperado)
        acks.append(esperado)
    return acks


def test_sequencia_e_ack():
    assert receptor_cumulativo([(88, 8)], 88) == [96]
    assert receptor_cumulativo([(88, 8), (104, 8), (96, 8)], 88) == [96, 96, 112]
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    s.listen()
    c = socket.create_connection(s.getsockname(), timeout=5)
    k, _ = s.accept()
    c.sendall(b"0123456789")
    pedacos = []
    while sum(map(len, pedacos)) < 10:
        pedacos.append(k.recv(4))
    assert b"".join(pedacos) == b"0123456789" and len(pedacos) >= 3
    for x in (c, k, s):
        x.close()


LOG = """\
192.168.1.9.53123 > 194.57.88.66.80: Flags [S], seq 3455997603, win 29200, options [mss 1460,sackOK,TS val 1 ecr 0,nop,wscale 7], length 0
194.57.88.66.80 > 192.168.1.9.53123: Flags [S.], seq 1188911440, ack 3455997604, win 28960, options [mss 1452,sackOK,TS val 2 ecr 1,nop,wscale 7], length 0
192.168.1.9.53123 > 194.57.88.66.80: Flags [.], ack 1, win 229, length 0
192.168.1.9.53123 > 194.57.88.66.80: Flags [P.], seq 1:606, ack 1, win 229, length 605
194.57.88.66.80 > 192.168.1.9.53123: Flags [.], ack 606, win 236, length 0
194.57.88.66.80 > 192.168.1.9.53123: Flags [.], seq 1:1441, ack 606, win 236, length 1440
194.57.88.66.80 > 192.168.1.9.53123: Flags [.], seq 1441:2881, ack 606, win 236, length 1440
192.168.1.9.53123 > 194.57.88.66.80: Flags [.], ack 2881, win 274, length 0
194.57.88.66.80 > 192.168.1.9.53123: Flags [P.], seq 2881:4036, ack 606, win 236, length 1155
192.168.1.9.53123 > 194.57.88.66.80: Flags [.], ack 4036, win 296, length 0
192.168.1.9.53123 > 194.57.88.66.80: Flags [P.], seq 606:1152, ack 4036, win 296, length 546
194.57.88.66.80 > 192.168.1.9.53123: Flags [P.], seq 4036:4931, ack 1152, win 245, length 895
192.168.1.9.53123 > 194.57.88.66.80: Flags [.], ack 4931, win 318, length 0
194.57.88.66.80 > 192.168.1.9.53123: Flags [F.], seq 4931, ack 1152, win 245, length 0
192.168.1.9.53123 > 194.57.88.66.80: Flags [F.], seq 1152, ack 4932, win 318, length 0
194.57.88.66.80 > 192.168.1.9.53123: Flags [.], ack 1153, win 245, length 0
192.168.1.9.53124 > 194.57.88.66.80: Flags [S], seq 1717140021, win 29200, length 0
"""


def test_log_tcpdump():
    linhas = []
    for l in LOG.splitlines():
        m = re.match(r"(\S+) > (\S+): Flags \[(\S+)\](?:, seq (\d+)(?::(\d+))?)?(?:, ack (\d+))?.*length (\d+)", l)
        org, dst, fl, s0, s1, ack, tam = m.groups()
        linhas.append((org, fl, int(s0) if s0 else None, int(s1) if s1 else None, int(ack) if ack else None, int(tam)))
    assert [l[1] for l in linhas[:3]] == ["S", "S.", "."]
    assert linhas[1][4] == linhas[0][2] + 1
    for org, fl, s0, s1, _, tam in linhas:
        if s1 is not None:
            assert s1 - s0 == tam
    assert [l[5] for l in linhas if l[5]] == [605, 1440, 1440, 1155, 546, 895]
    fins = [l for l in linhas if "F" in l[1]]
    assert len(fins) == 2 and linhas[15][4] == fins[1][2] + 1 and fins[1][4] == fins[0][2] + 1
    assert all(l[0].endswith(".53123") or l[0].endswith(".80") for l in linhas[:-1]) and linhas[-1][0].endswith(
        ".53124"
    )
    assert "mss 1460" in LOG and "mss 1452" in LOG


def go_back_n(n, janela, perdido):
    enviados, perdas, base, prox, entregue = [], {perdido}, 0, 0, []
    while base < n:
        while prox < min(base + janela, n):
            enviados.append(prox)
            if prox in perdas:
                perdas.discard(prox)
            elif prox == len(entregue):
                entregue.append(prox)
            prox += 1
        if len(entregue) > base:
            base = len(entregue)
        else:
            prox = base  # timeout: volta N
    return len(enviados) - n, entregue


def seletiva(n, janela, perdido):
    enviados, recebidos = list(range(n)), set(range(n)) - {perdido}
    enviados.append(perdido)
    recebidos.add(perdido)
    return len(enviados) - n, sorted(recebidos)


def test_go_back_n_e_seletiva():
    r, ent = go_back_n(6, 4, 2)
    assert r == 4 and ent == list(range(6))
    r, ent = seletiva(6, 4, 2)
    assert r == 1 and ent == list(range(6))


def test_fluxo_e_congestionamento():
    assert min(64, 10) == 10 and min(4, 100) == 4
    enlace, udp, cwnd, total, rodadas = 100, 95, 1.0, 0.0, 200
    for _ in range(rodadas):
        if cwnd + udp > enlace:
            total += max(0, enlace - udp)
            cwnd = max(1.0, cwnd / 2)
        else:
            total += cwnd
            cwnd += 1
    assert total / rodadas < 0.1 * enlace


def congestionamento(variante, rodadas=15, limiar=8, perda=8):
    cwnd, th, serie = 1, limiar, []
    for r in range(1, rodadas + 1):
        serie.append(cwnd)
        if r == perda:
            th = cwnd // 2
            cwnd = 1 if variante == "tahoe" else th
        elif cwnd < th:
            cwnd = min(cwnd * 2, th)
        else:
            cwnd += 1
    return serie


def test_tahoe_e_reno():
    tahoe = congestionamento("tahoe")
    reno = congestionamento("reno")
    assert tahoe[:8] == [1, 2, 4, 8, 9, 10, 11, 12] == reno[:8]
    assert tahoe[8:] == [1, 2, 4, 6, 7, 8, 9]
    assert reno[8:] == [6, 7, 8, 9, 10, 11, 12]


def test_subredes():
    a, b = ipaddress.ip_interface("192.168.0.9/30"), ipaddress.ip_interface("192.168.0.13/30")
    assert str(a.network) == "192.168.0.8/30" and str(b.network) == "192.168.0.12/30" and a.network != b.network
    subs = list(ipaddress.ip_network("192.168.1.0/24").subnets(new_prefix=26))
    assert [(str(s.network_address), str(s.broadcast_address)) for s in subs] == [
        ("192.168.1.0", "192.168.1.63"),
        ("192.168.1.64", "192.168.1.127"),
        ("192.168.1.128", "192.168.1.191"),
        ("192.168.1.192", "192.168.1.255"),
    ]
    assert str(ipaddress.ip_network("192.168.1.0/255.255.255.192").netmask) == "255.255.255.192"
    n9 = ipaddress.ip_network("10.0.0.0/9")
    assert n9.num_addresses - 2 == 8388606 and str(n9.broadcast_address) == "10.127.255.255"


GRAFO = {
    "u": {"v": 2, "w": 5, "x": 1},
    "v": {"u": 2, "w": 3, "x": 2},
    "w": {"u": 5, "v": 3, "x": 3, "y": 1, "z": 5},
    "x": {"u": 1, "v": 2, "w": 3, "y": 1},
    "y": {"w": 1, "x": 1, "z": 2},
    "z": {"w": 5, "y": 2},
}


def dijkstra(g, s):
    dist, fila = {s: 0}, [(0, s)]
    while fila:
        d, u = heapq.heappop(fila)
        if d > dist[u]:
            continue
        for v, c in g[u].items():
            if d + c < dist.get(v, float("inf")):
                dist[v] = d + c
                heapq.heappush(fila, (d + c, v))
    return dist


def vetor_distancia(g, rodadas=50):
    inf = float("inf")
    D = {x: {y: (0 if x == y else g[x].get(y, inf)) for y in g} for x in g}
    for _ in range(rodadas):
        novo = {x: {y: 0 if x == y else min(g[x][v] + D[v][y] for v in g[x]) for y in g} for x in g}
        if novo == D:
            break
        D = novo
    return D


def test_link_state_e_vetor_de_distancia():
    D = vetor_distancia(GRAFO)
    for s in GRAFO:
        assert dijkstra(GRAFO, s) == D[s]
    assert D["u"]["z"] == 4
    # contagem ao infinito: x - y - z; o enlace y-z cai e x e y passam a se enganar
    dy_z, dx_z, historico = 1, 2, []
    for _ in range(5):
        dy_z = 1 + dx_z  # y acredita na rota de x (que passava por y)
        dx_z = 1 + dy_z
        historico.append(dy_z)
    assert historico == [3, 5, 7, 9, 11]
