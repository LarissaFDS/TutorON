"""Acervo de Sistemas Distribuídos (Ciência da Computação) e conferência das resoluções.

Os blocos parafraseiam as provas do Prof. Leandro Melo de Sales (IC-UFAL). O que pode ser executado
(RPC, REST, publicar-assinar, filas, eleição, detector de falhas, prova de trabalho) roda aqui com a
biblioteca padrão do Python, em localhost; Docker e Kubernetes só são conferidos no texto.
"""

import hashlib
import http.server
import json
import math
import random
import re
import struct
import threading
import urllib.request
import xmlrpc.client
import xmlrpc.server
from queue import Empty, Queue

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

SD = disciplinas.obter("sd_dist")
PASTA = ROOT / "disciplinas/sd_dist"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(SD.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "sd_dist")
FRONTEIRA = ("redes", "so")


def buscar(pergunta, d=SD):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(id_):
    return TODOS[id_]["texto"]


# ---------------------------------------------------------------- cadastro e acervo


def test_sd_dist_cadastrada_com_acervo_proprio():
    assert SD.nome == "Sistemas Distribuídos" and SD.itens.exists()
    ids = {c["id"] for c in read_json(SD.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({SD.itens, SD.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(SD.assuntos)
    assert ids == set(TODOS)
    cursos = (ROOT / "disciplinas/cursos.json").read_text(encoding="utf-8")
    # só o 7º período de CC; ECOM044 (Engenharia, 8º período) não foi ligada (ver CURADORIA.md)
    assert cursos.count('"acervo": "sd_dist"') == 1
    # "sd" é Sistemas Digitais: esta disciplina não pode reusar o id
    assert SD.id != "sd"


def test_situacao_da_disciplina():
    assert SD.situacao == "em validação" and SD.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas sd_dist --embeddings`."""
    assert disciplinas.registros(SD) == read_json(SD.itens)


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
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"] == "Protegido" or f["id"] == "turma-resumos-trabalhos-sd":
            assert f["uso"] == "referencia", f["id"]
    soltos = [
        p
        for p in PASTA.rglob("*")
        if p.suffix.lower() in (".pdf", ".docx", ".ppt", ".pptx", ".xlsx", ".png", ".jpg", ".jpeg")
    ]
    assert not soltos


PERGUNTAS = [
    ("O que é um sistema distribuído e quais os desafios?", "sd_dist-definicao-exemplos-desafios-transparencia"),
    ("Dê exemplos de sistemas distribuídos", "sd_dist-definicao-exemplos-desafios-transparencia"),
    ("O que é middleware e por que é importante?", "sd_dist-middleware-servico-sistema-operacional-compartilhamento"),
    ("Um sistema operacional é middleware?", "sd_dist-middleware-servico-sistema-operacional-compartilhamento"),
    (
        "Que entidades usar para substituir em tempo de execução: componentes, objetos ou web services?",
        "sd_dist-modelos-arquiteturais-entidades-padroes-camadas-tiers-desempenho",
    ),
    (
        "Qual a vantagem do RPC sobre o protocolo requisição-resposta?",
        "sd_dist-invocacao-remota-rpc-rmi-requisicao-resposta",
    ),
    (
        "Qual a diferença entre publicar-assinar e fila de mensagens?",
        "sd_dist-comunicacao-indireta-publicar-assinar-filas-de-mensagens-desacoplamento",
    ),
    (
        "O que é desacoplamento espacial e temporal na comunicação indireta?",
        "sd_dist-comunicacao-indireta-publicar-assinar-filas-de-mensagens-desacoplamento",
    ),
    (
        "O roteamento no peer-to-peer não estruturado é determinístico?",
        "sd_dist-peer-to-peer-estruturado-nao-estruturado-roteamento-determinista",
    ),
    (
        "Qual a diferença entre detector de falhas confiável e não confiável?",
        "sd_dist-modelo-sincrono-assincrono-detectores-de-falhas-confiaveis",
    ),
    (
        "Para que servem os algoritmos de eleição de líder?",
        "sd_dist-eleicao-de-lider-algoritmo-valentao-anel-exclusao-mutua",
    ),
    (
        "Como a replicação melhora o desempenho e a tolerância a falhas?",
        "sd_dist-replicacao-desempenho-tolerancia-a-falhas-disponibilidade",
    ),
    ("O que é Docker Swarm e Docker Network?", "sd_dist-docker-containers-swarm-kubernetes-cloud-functions"),
    (
        "O que é Kubernetes? Dê um exemplo de uso",
        "sd_dist-kubernetes-orquestracao-pods-autoescala-cloud-functions-serverless",
    ),
    (
        "O que é cloud functions?",
        "sd_dist-kubernetes-orquestracao-pods-autoescala-cloud-functions-serverless",
    ),
    (
        "O que é prova de trabalho na blockchain?",
        "sd_dist-blockchain-prova-de-trabalho-gasto-duplo-ipfs-enderecamento-por-conteudo",
    ),
    ("Quais as características do IPFS?", "sd_dist-ipfs-enderecamento-por-conteudo-cid-dag-de-merkle-dht"),
    ("Para que serve o RabbitMQ?", "sd_dist-rabbitmq-amqp-exchanges-kafka-log-de-eventos"),
    ("Quando usar Kafka?", "sd_dist-kafka-log-distribuido-particoes-grupos-de-consumidores-quando-usar"),
    ("O que é RESTful e o GraphQL?", "sd_dist-web-services-rest-graphql-grpc-protocol-buffers-envoy"),
    ("Quais as vantagens do gRPC?", "sd_dist-grpc-protocol-buffers-vantagens-envoy-proxy-service-mesh"),
    ("Que problemas o Envoy Proxy resolve?", "sd_dist-grpc-protocol-buffers-vantagens-envoy-proxy-service-mesh"),
    (
        "Como cobrar por um serviço de ordenação em utility computing?",
        "sd_dist-utility-computing-cobranca-por-uso-servico-de-ordenacao",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Qual a diferença entre detector de falhas confiável e não confiável?", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a transformada de Laplace de um degrau?")
    assert "Sistemas Digitais" in (PASTA / "rigor.md").read_text(encoding="utf-8")


# ---------------------------------------------------------------- conferência das resoluções


def test_caracterizacao():
    t = texto("sd_dist-definicao-exemplos-desafios-transparencia")
    for termo in (
        "trocando mensagens",
        "relógio global",
        "falhas independentes",
        "busca na Web",
        "MMOG",
        "financeiros",
        "nuvem",
        "heterogeneidade",
        "abertura",
        "segurança",
        "escalabilidade",
        "falhas",
        "concorrência",
        "transparência",
    ):
        assert termo in t, termo


def _servidor_xmlrpc(funcoes):
    srv = xmlrpc.server.SimpleXMLRPCServer(("127.0.0.1", 0), logRequests=False, allow_none=True)
    for nome, f in funcoes.items():
        srv.register_function(f, nome)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}/"


def test_middleware_esconde_a_rede():
    srv, url = _servidor_xmlrpc({"soma": lambda a, b: a + b})
    try:
        with xmlrpc.client.ServerProxy(url) as proxy:
            assert proxy.soma(2, 3) == 5
    finally:
        srv.shutdown()
        srv.server_close()
    assert "Não" in texto("sd_dist-middleware-servico-sistema-operacional-compartilhamento")


def test_custo_de_intermediarios():
    salto = 1.0  # ms por mensagem

    def ida_e_volta(intermediarios):
        return 2 * salto * (intermediarios + 1)

    assert ida_e_volta(1) == 2 * ida_e_volta(0)
    t = texto("sd_dist-modelos-arquiteturais-entidades-padroes-camadas-tiers-desempenho")
    assert "**componentes**" in t and "comunicação em grupo" in t


def test_rpc_e_semanticas():
    estado = {"n": 0}

    def incrementa():
        estado["n"] += 1
        return estado["n"]

    srv, url = _servidor_xmlrpc({"incrementa": incrementa})
    try:
        with xmlrpc.client.ServerProxy(url) as proxy:
            assert proxy.incrementa() == 1
    finally:
        srv.shutdown()
        srv.server_close()

    # 2 respostas perdidas: o cliente reenvia até receber a terceira
    def chamar(semantica, perdas=2):
        contador, vistos, respostas = {"n": 0}, {}, []
        for _ in range(perdas + 1):
            if semantica == "no_maximo_uma" and "req-1" in vistos:
                respostas.append(vistos["req-1"])
                continue
            contador["n"] += 1
            vistos["req-1"] = contador["n"]
            respostas.append(contador["n"])
        return contador["n"]

    assert chamar("pelo_menos_uma") == 3
    assert chamar("no_maximo_uma") == 1


def test_pubsub_e_fila():
    eventos = [f"e{i}" for i in range(5)]
    # publicar-assinar: cada assinante recebe todos
    assinantes = [Queue() for _ in range(3)]
    for e in eventos:
        for q in assinantes:
            q.put(e)
    entregas_pubsub = sum(q.qsize() for q in assinantes)
    assert entregas_pubsub == 15 and all(list(q.queue) == eventos for q in assinantes)

    # fila de mensagens: consumidores competem, cada mensagem vai a um só
    fila, recebidas, trava = Queue(), [], threading.Lock()
    for e in eventos:
        fila.put(e)

    def consumidor():
        while True:
            try:
                m = fila.get(timeout=0.2)
            except Empty:
                return
            with trava:
                recebidas.append(m)

    ts = [threading.Thread(target=consumidor) for _ in range(3)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    assert sorted(recebidas) == eventos and len(recebidas) == 5


def test_p2p_estruturado_e_nao_estruturado():
    m = 16
    nos = sorted(random.Random(1).sample(range(2**m), 16))

    def sucessor(k):
        return next((n for n in nos if n >= k % 2**m), nos[0])

    def dist(a, b):
        return (b - a) % 2**m

    def buscar_chord(origem, chave):
        alvo, atual, saltos = sucessor(chave), origem, 0
        while atual != alvo:
            fingers = [sucessor(atual + 2**i) for i in range(m)]
            # maior finger que não ultrapassa a chave
            cand = [f for f in fingers if 0 < dist(atual, f) <= dist(atual, alvo)]
            atual = max(cand, key=lambda f: dist(atual, f))
            saltos += 1
        return alvo, saltos

    chave = int(hashlib.sha1(b"arquivo.txt").hexdigest(), 16) % 2**m
    resultados = {buscar_chord(o, chave) for o in nos}
    assert {r[0] for r in resultados} == {sucessor(chave)}
    assert max(r[1] for r in resultados) <= int(math.log2(len(nos)))

    vizinhos = {i: random.Random(2).sample([j for j in range(30) if j != i], 3) for i in range(30)}

    def caminhada(semente, passos=6):
        r, atual, caminho = random.Random(semente), 0, [0]
        for _ in range(passos):
            atual = r.choice(vizinhos[atual])
            caminho.append(atual)
        return tuple(caminho)

    assert len({caminhada(s) for s in range(5)}) > 1


def test_detector_de_falhas():
    T = 1.0

    def suspeitas(atrasos, prazo):
        # heartbeat enviado a cada T; suspeita se o intervalo entre chegadas passa de T + prazo
        chegadas = [i * T + a for i, a in enumerate(atrasos)]
        return sum(1 for a, b in zip(chegadas, chegadas[1:], strict=False) if b - a > T + prazo)

    D = 0.3
    sincrono = [random.Random(3).uniform(0, D) for _ in range(200)]
    assert suspeitas(sincrono, D) == 0
    r = random.Random(4)
    assincrono = [r.expovariate(4) for _ in range(200)]  # sem limite superior
    assert suspeitas(assincrono, D) > 0
    assert suspeitas(assincrono, 2.0) < suspeitas(assincrono, D)


def test_eleicao_anel_e_valentao():
    ids, morto = [3, 7, 2, 9, 5], 9
    vivos = [i for i in ids if i != morto]

    def anel(iniciador):
        anel_vivo = [i for i in ids if i != morto]
        pos, candidato, msgs = anel_vivo.index(iniciador), iniciador, 0
        while True:
            pos = (pos + 1) % len(anel_vivo)
            msgs += 1
            atual = anel_vivo[pos]
            if atual == candidato:
                return candidato, msgs
            candidato = max(candidato, atual)

    def valentao(iniciador):
        maiores = [i for i in vivos if i > iniciador]
        if not maiores:
            return iniciador
        return valentao(min(maiores))

    eleito, msgs = anel(3)
    assert eleito == 7 == valentao(2) == valentao(3) == max(vivos)
    # de 3: dá a volta (4 mensagens) e segue até o 7 (1 salto)
    assert msgs == len(vivos) + 1


def test_disponibilidade_com_replicas():
    p, r = 0.05, random.Random(5)
    for n, esperado in ((1, 0.95), (2, 0.9975), (3, 0.999875)):
        assert math.isclose(1 - p**n, esperado)
        sim = sum(any(r.random() >= p for _ in range(n)) for _ in range(200_000)) / 200_000
        assert abs(sim - esperado) < 0.003


def test_tecnologias_tem_conceito_e_exemplo():
    t = texto("sd_dist-docker-containers-swarm-kubernetes-cloud-functions")
    for termo in ("Container", "máquina virtual", "Docker Network", "Docker Swarm", "orquestrador"):
        assert termo in t, termo
    k = texto("sd_dist-kubernetes-orquestracao-pods-autoescala-cloud-functions-serverless")
    for termo in ("pods", "estado desejado", "Exemplo", "Cloud functions", "por execução"):
        assert termo in k, termo


def _minerar(dados, zeros=4):
    nonce = 0
    while True:
        h = hashlib.sha256(f"{dados}|{nonce}".encode()).hexdigest()
        if h.startswith("0" * zeros):
            return nonce, h
        nonce += 1


def test_prova_de_trabalho():
    b1 = "anterior=0|tx=A paga 5 a B"
    n1, h1 = _minerar(b1)
    assert hashlib.sha256(f"{b1}|{n1}".encode()).hexdigest() == h1  # conferir: um hash
    b2 = f"anterior={h1}|tx=B paga 2 a C"
    n2, h2 = _minerar(b2)
    adulterado = "anterior=0|tx=A paga 50 a B"
    h1x = hashlib.sha256(f"{adulterado}|{n1}".encode()).hexdigest()
    assert not h1x.startswith("0000")  # o nonce antigo não vale mais
    assert f"anterior={h1x}" not in b2 and h2.startswith("0000")  # o bloco seguinte aponta para o hash antigo


def test_enderecamento_por_conteudo():
    def cid(b):
        return hashlib.sha256(b).hexdigest()

    a = b"aula de sistemas distribuidos"
    assert cid(a) == cid(bytes(a)) and cid(a) != cid(a[:-1] + b"S")

    def merkle(blocos):
        nivel = [cid(b) for b in blocos]
        while len(nivel) > 1:
            nivel = [cid((nivel[i] + nivel[min(i + 1, len(nivel) - 1)]).encode()) for i in range(0, len(nivel), 2)]
        return nivel[0]

    blocos = [b"b0", b"b1", b"b2", b"b3"]
    raiz = merkle(blocos)
    alterado = blocos[:2] + [b"bX"] + blocos[3:]
    assert merkle(alterado) != raiz and merkle(list(blocos)) == raiz


def _casa_topico(padrao, chave):
    p, c = padrao.split("."), chave.split(".")

    def casa(i, j):
        if i == len(p):
            return j == len(c)
        if p[i] == "#":
            return any(casa(i + 1, k) for k in range(j, len(c) + 1))
        return j < len(c) and p[i] in ("*", c[j]) and casa(i + 1, j + 1)

    return casa(0, 0)


def test_exchanges():
    ligacoes = {"erros": "erro", "avisos": "aviso"}
    assert [f for f, k in ligacoes.items() if k == "erro"] == ["erros"]  # direct
    filas = ["estoque", "cobranca", "entrega"]
    assert len(filas) == 3  # fanout: cópia para todas as filas ligadas
    assert _casa_topico("pedido.*.br", "pedido.novo.br")
    assert not _casa_topico("pedido.*.br", "pedido.novo.extra.br")
    assert _casa_topico("log.#", "log") and _casa_topico("log.#", "log.app.erro")
    assert not _casa_topico("log.#", "pedido.novo")


def test_log_com_offsets():
    log = [f"m{i}" for i in range(6)]
    offsets = {"analise": 0, "auditoria": 0}

    def ler(grupo):
        lidas = log[offsets[grupo] :]
        offsets[grupo] = len(log)
        return lidas

    assert ler("analise") == log and ler("auditoria") == log  # cada grupo lê tudo
    assert ler("analise") == []
    offsets["analise"] = 2  # volta o offset e relê
    assert ler("analise") == log[2:]
    # dentro de um grupo, partições divididas entre consumidores: cada mensagem a um só
    particoes = {p: [m for i, m in enumerate(log) if i % 2 == p] for p in (0, 1)}
    c1, c2 = particoes[0], particoes[1]
    assert sorted(c1 + c2) == sorted(log) and not set(c1) & set(c2)


def test_rest_idempotencia():
    recursos, contador = {}, {"n": 0}

    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _corpo(self):
            return json.loads(self.rfile.read(int(self.headers["Content-Length"])))

        def do_PUT(self):
            recursos[self.path] = self._corpo()
            self.send_response(200)
            self.end_headers()

        def do_POST(self):
            contador["n"] += 1
            recursos[f"{self.path}/{contador['n']}"] = self._corpo()
            self.send_response(201)
            self.end_headers()

    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}"

    def enviar(metodo, caminho, dados):
        req = urllib.request.Request(base + caminho, data=json.dumps(dados).encode(), method=metodo)
        req.add_header("Content-Type", "application/json")
        return urllib.request.urlopen(req, timeout=5).status

    try:
        for _ in range(2):
            assert enviar("PUT", "/alunos/42", {"nome": "A"}) == 200
        assert len(recursos) == 1
        for _ in range(2):
            assert enviar("POST", "/alunos", {"nome": "B"}) == 201
        assert len(recursos) == 3
    finally:
        srv.shutdown()
        srv.server_close()


def test_serializacao_binaria():
    msg = {"id": 42, "nota": 9.5, "aprovado": True}
    em_json = json.dumps(msg).encode()
    # campos numerados 1, 2, 3 (como no .proto): tag de 1 byte + valor
    binario = struct.pack("!BiBdB?", 1, 42, 2, 9.5, 3, True)
    assert len(binario) < len(em_json)
    _, i, _, nota, _, ok = struct.unpack("!BiBdB?", binario)
    assert {"id": i, "nota": nota, "aprovado": ok} == msg


def test_tarifa_por_uso():
    FIXA, PRECO_TRABALHO, PRECO_MB = 0.01, 1e-6, 1e-3

    def trabalho(n):
        return n * math.log2(max(n, 2))

    def tarifa(n, bytes_por_item=8):
        return FIXA + PRECO_TRABALHO * trabalho(n) + PRECO_MB * n * bytes_por_item / 2**20

    assert trabalho(1024) == 10_240 and trabalho(2048) == 22_528
    assert tarifa(2048) > tarifa(1024) > tarifa(10)

    def merge_sort(v, cont):
        if len(v) <= 1:
            return v
        a, b = merge_sort(v[: len(v) // 2], cont), merge_sort(v[len(v) // 2 :], cont)
        out = []
        while a and b:
            cont[0] += 1
            out.append(a.pop(0) if a[0] <= b[0] else b.pop(0))
        return out + a + b

    r = random.Random(6)
    for n in (16, 256, 1024):
        v, cont = [r.random() for _ in range(n)], [0]
        assert merge_sort(v, cont) == sorted(v)
        assert cont[0] <= trabalho(n)
