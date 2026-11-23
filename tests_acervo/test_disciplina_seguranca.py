"""Acervo de Segurança de Sistemas Computacionais (Ciência da Computação) e conferência dos exemplos.

Os blocos parafraseiam provas e listas do IC-UFAL. Os exemplos são defensivos e conferidos com a
biblioteca padrão (`hashlib`, `hmac`, `zlib`, `ipaddress`, `secrets`); nada aqui ataca sistemas reais.
"""

import hashlib
import hmac
import ipaddress
import math
import re
import secrets
import zlib
from functools import reduce

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

SEG = disciplinas.obter("seguranca")
PASTA = ROOT / "disciplinas/seguranca"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(SEG.itens)}
OUTRAS = tuple(
    d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "seguranca"
)
FRONTEIRA = ("redes",)


def buscar(pergunta, d=SEG):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo


def test_seguranca_cadastrada_com_acervo_proprio():
    assert SEG.nome == "Segurança de Sistemas Computacionais" and SEG.itens.exists()
    ids = {c["id"] for c in read_json(SEG.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({SEG.itens, SEG.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(SEG.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert SEG.situacao == "MVP" and not SEG.em_validacao and not SEG.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas seguranca --embeddings`."""
    assert disciplinas.registros(SEG) == read_json(SEG.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert len(t) <= 2200, i["id"]
        ultima = t.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in t and "Status da resolução:" in t, i["id"]
        for nome in re.findall(r"`(test_\w+)`", ultima):
            assert nome in globals(), (i["id"], nome)
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO, (arq.name, f)


def test_rigor_proibe_codigo_de_exploracao():
    rigor = (PASTA / "rigor.md").read_text(encoding="utf-8")
    assert "Não escreva código de exploração" in rigor and "autorização por escrito" in rigor
    textos = " ".join(i["texto"] for i in TODOS.values())
    # nenhum comando de varredura ou de ataque pronto para copiar
    assert not re.search(r"\b(nmap|hping3?|msfconsole|aircrack-ng)\s+-", textos, re.I)
    assert "```" not in textos


def test_sem_dados_pessoais_normas_nem_binarios():
    textos = " ".join(i["texto"] for i in TODOS.values()) + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"].startswith("Protegido"):
            assert f["uso"] == "referencia", f["id"]
    soltos = [
        p for p in PASTA.rglob("*") if p.suffix.lower() in (".pdf", ".docx", ".pptx", ".png", ".jpg", ".jpeg", ".pkt")
    ]
    assert not soltos
    assert not list(ROOT.rglob("norma1.pdf")) and not list(ROOT.rglob("norma2.pdf"))


PERGUNTAS = [
    (
        "Quais os requisitos básicos de segurança da informação? Defina cada um deles.",
        "seguranca-requisitos-basicos-confidencialidade-integridade-disponibilidade-autenticidade-nao-repudio",
    ),
    (
        "O que é não repúdio?",
        "seguranca-requisitos-basicos-confidencialidade-integridade-disponibilidade-autenticidade-nao-repudio",
    ),
    ("Defina o ataque Pharming e contramedidas", "seguranca-engenharia-social-phishing-pharming-dns-contramedidas"),
    ("Qual o conceito de engenharia social?", "seguranca-engenharia-social-phishing-pharming-dns-contramedidas"),
    ("O que é Packet Sniffing?", "seguranca-packet-sniffing-modo-promiscuo-wireshark-contramedidas-criptografia"),
    (
        "O que significa uma interface em modo promíscuo?",
        "seguranca-packet-sniffing-modo-promiscuo-wireshark-contramedidas-criptografia",
    ),
    ("Qual a definição de Cavalo de Tróia?", "seguranca-malware-virus-worm-cavalo-de-troia-tipos-de-virus-exemplos"),
    ("Descreva o ataque DDoS com Syn Flood", "seguranca-negacao-de-servico-ddos-syn-flood-smurf-ping-of-death-defesas"),
    ("Descreva o ataque Smurf", "seguranca-negacao-de-servico-ddos-syn-flood-smurf-ping-of-death-defesas"),
    (
        "Qual a diferença entre Pentest e varredura de vulnerabilidades?",
        "seguranca-ip-spoofing-sequestro-de-sessao-pentest-varredura-de-vulnerabilidades-etapas",
    ),
    (
        "Quais os tipos de controle em uma Política de Segurança da Informação?",
        "seguranca-politica-de-seguranca-da-informacao-classificacao-controles-fisicos-logicos",
    ),
    (
        "Como cifrar uma palavra com RSA escolhendo p e q?",
        "seguranca-criptografia-simetrica-assimetrica-rsa-chaves-p-q-cifrar-decifrar-exemplo",
    ),
    (
        "Descreva o código de autenticação de mensagens (MAC)",
        "seguranca-hash-codigo-de-autenticacao-de-mensagem-mac-hmac-assinatura-digital-certificado-x509-autoridade-certificadora",
    ),
    (
        "Qual a finalidade de um nonce em um protocolo de autenticação?",
        "seguranca-autenticacao-nonce-reproducao-ap-homem-do-meio-kdc-kerberos-centro-de-distribuicao-de-chaves",
    ),
    (
        "Descreva o protocolo SSL: camada, portas e operação",
        "seguranca-protocolo-ssl-tls-camada-porta-443-handshake-registro-numero-de-sequencia",
    ),
    (
        "Quais requisitos o IPSec com ESP atende?",
        "seguranca-ipsec-ah-esp-modo-transporte-tunel-associacao-de-seguranca-requisitos",
    ),
    (
        "Descreva o modo de operação do protocolo WEP",
        "seguranca-redes-sem-fio-wep-rc4-vetor-de-inicializacao-crc-fraquezas-wpa2",
    ),
    (
        "Firewall ao nível de aplicação e ao nível de pacotes",
        "seguranca-firewall-filtro-de-pacotes-gateway-de-aplicacao-proxy-estado-regras-dmz",
    ),
    (
        "Qual a diferença entre PAP e CHAP?",
        "seguranca-autenticacao-ppp-pap-chap-aaa-radius-tacacs-controle-de-acesso-dac-mac-rbac",
    ),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Descreva o modo de operação do protocolo WEP", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a impedância de um indutor?")


# ---------------------------------------------------------------- s01 requisitos


def test_paridade_raid5():
    discos = [bytes([1, 2, 3, 4]), bytes([9, 8, 7, 6]), bytes([5, 5, 5, 5])]
    paridade = bytes(reduce(lambda a, b: a ^ b, col) for col in zip(*discos, strict=True))
    perdido = 1
    restantes = [d for i, d in enumerate(discos) if i != perdido] + [paridade]
    reconstruido = bytes(reduce(lambda a, b: a ^ b, col) for col in zip(*restantes, strict=True))
    assert reconstruido == discos[perdido]


def test_hash_detecta_alteracao():
    a = hashlib.sha256(b"transferir 100 reais").hexdigest()
    b = hashlib.sha256(b"transferir 900 reais").hexdigest()
    assert a != b and len(a) == len(b) == 64
    assert a == hashlib.sha256(b"transferir 100 reais").hexdigest()


# ---------------------------------------------------------------- s02 Pharming


def _nome_confere(padrao, host):
    """Regra de nomes de certificado (RFC 6125, simplificada): curinga só no rótulo mais à esquerda."""
    p, h = padrao.lower().split("."), host.lower().split(".")
    if len(p) != len(h):
        return False
    return (p[0] == "*" or p[0] == h[0]) and p[1:] == h[1:]


def test_certificado_confere_nome():
    assert _nome_confere("banco.com.br", "banco.com.br")
    assert _nome_confere("*.banco.com.br", "www.banco.com.br")
    assert not _nome_confere("banco.com.br", "banco-seguro.net")
    assert not _nome_confere("*.banco.com.br", "banco.com.br.falso.net")


# ---------------------------------------------------------------- s03 sniffing


def test_texto_aberto_versus_cifrado():
    pedido = b"POST /login HTTP/1.1\r\nHost: exemplo.test\r\n\r\nusuario=ana&senha=segredo123"
    assert b"segredo123" in pedido
    chave = secrets.token_bytes(len(pedido))
    cifrado = bytes(x ^ k for x, k in zip(pedido, chave, strict=True))
    assert b"segredo123" not in cifrado
    assert bytes(x ^ k for x, k in zip(cifrado, chave, strict=True)) == pedido


# ---------------------------------------------------------------- s04 malware


def test_assinatura_de_arquivo():
    conhecido = b"\x4d\x5a programa malicioso de exemplo"
    assinaturas = {hashlib.sha256(conhecido).hexdigest()}
    assert hashlib.sha256(conhecido).hexdigest() in assinaturas
    variante = bytearray(conhecido)
    variante[-1] ^= 1
    assert hashlib.sha256(bytes(variante)).hexdigest() not in assinaturas


# ---------------------------------------------------------------- s05 DoS


class _Servidor:
    def __init__(self, fila, cookies=False):
        self.fila, self.cookies, self.semiabertas = fila, cookies, set()

    def syn(self, origem):
        if self.cookies:
            return True  # sem estado: o SYN-ACK leva a informação no número de sequência
        if len(self.semiabertas) >= self.fila:
            return False
        self.semiabertas.add(origem)
        return True


def test_fila_semiaberta_syn_flood():
    s = _Servidor(fila=8)
    for i in range(8):
        s.syn(f"10.0.0.{i}")  # nunca completam o handshake
    assert not s.syn("cliente-legitimo")
    c = _Servidor(fila=8, cookies=True)
    for i in range(1000):
        c.syn(f"10.0.0.{i}")
    assert c.syn("cliente-legitimo") and not c.semiabertas


def test_amplificacao_smurf():
    rede = ipaddress.ip_network("192.168.10.0/28")
    hosts = list(rede.hosts())
    respostas = [(h, "vitima") for h in hosts]  # cada host responde ao IP de origem falsificado
    assert len(respostas) == rede.num_addresses - 2 == 14
    assert rede.broadcast_address == ipaddress.ip_address("192.168.10.15")


# ---------------------------------------------------------------- s06 spoofing


def test_filtro_bcp38():
    interno = ipaddress.ip_network("200.17.0.0/16")

    def sai(origem):
        return ipaddress.ip_address(origem) in interno

    assert sai("200.17.4.20")
    assert not sai("8.8.8.8")


# ---------------------------------------------------------------- s07 política

NIVEIS = ["pública", "interna", "confidencial", "secreta"]


def _pode_ler(autorizacao, classificacao):
    return NIVEIS.index(classificacao) <= NIVEIS.index(autorizacao)


def test_controle_por_classificacao():
    assert _pode_ler("interna", "pública") and _pode_ler("interna", "interna")
    assert not _pode_ler("interna", "confidencial")
    assert _pode_ler("secreta", "confidencial")


# ---------------------------------------------------------------- s08 RSA


def test_rsa_exemplo():
    p, q, e = 5, 11, 3
    n, phi = p * q, (p - 1) * (q - 1)
    assert (n, phi) == (55, 40) and math.gcd(e, phi) == 1
    d = pow(e, -1, phi)
    assert d == 27 and e * d % phi == 1
    m = [ord(c) - ord("a") + 1 for c in "cafe"]
    assert m == [3, 1, 6, 5]
    c = [pow(x, e, n) for x in m]
    assert c == [27, 1, 51, 15]
    assert [pow(x, d, n) for x in c] == m
    # Lista 9: com p=3 e q=11, n=33 > 26, todas as letras cabem
    assert 3 * 11 > 26


# ---------------------------------------------------------------- s09 MAC


def test_hmac_detecta_alteracao():
    k = b"chave-compartilhada"
    m = b"pagar 100 a Bob"
    tag = hmac.new(k, m, hashlib.sha256).digest()
    assert hmac.compare_digest(tag, hmac.new(k, m, hashlib.sha256).digest())
    assert not hmac.compare_digest(tag, hmac.new(b"outra", m, hashlib.sha256).digest())
    assert not hmac.compare_digest(tag, hmac.new(k, b"pagar 900 a Bob", hashlib.sha256).digest())


# ---------------------------------------------------------------- s10 nonce e KDC


class _Verificador:
    def __init__(self, chave):
        self.chave, self.usados, self.atual = chave, set(), None

    def desafio(self):
        self.atual = secrets.token_bytes(16)
        return self.atual

    def confere(self, nonce, resposta):
        if nonce != self.atual or nonce in self.usados:
            return False
        self.usados.add(nonce)
        return hmac.compare_digest(resposta, hmac.new(self.chave, nonce, hashlib.sha256).digest())


def test_desafio_resposta_com_nonce():
    k = b"segredo-alice-bob"
    bob = _Verificador(k)
    r1 = bob.desafio()
    resp1 = hmac.new(k, r1, hashlib.sha256).digest()
    assert bob.confere(r1, resp1)
    assert not bob.confere(r1, resp1)  # mesma resposta de novo: reprodução
    bob.desafio()
    assert not bob.confere(r1, resp1)  # nonce antigo
    r3 = bob.desafio()
    assert not bob.confere(r3, hmac.new(b"chave-errada", r3, hashlib.sha256).digest())


def test_numero_de_chaves_kdc():
    for n in (10, 100, 1000):
        assert n * (n - 1) // 2 > n
    assert 100 * 99 // 2 == 4950


# ---------------------------------------------------------------- s11 SSL


def _registro(k, seq, dados):
    return dados, hmac.new(k, seq.to_bytes(8, "big") + dados, hashlib.sha256).digest()


def _recebe(k, registros):
    for seq, (dados, mac) in enumerate(registros):
        if not hmac.compare_digest(mac, hmac.new(k, seq.to_bytes(8, "big") + dados, hashlib.sha256).digest()):
            return False
    return True


def test_mac_com_numero_de_sequencia():
    k = b"chave-mac-sessao"
    regs = [_registro(k, i, d) for i, d in enumerate([b"um", b"dois", b"tres"])]
    assert all(len(r) == 2 for r in regs)  # o número de sequência não vai no registro
    assert _recebe(k, regs)
    assert not _recebe(k, [regs[1], regs[0], regs[2]])
    assert not _recebe(k, [regs[0], regs[0], regs[1]])


# ---------------------------------------------------------------- s12 IPsec


class _JanelaAntiReproducao:
    def __init__(self, w=64):
        self.w, self.maior, self.vistos = w, 0, set()

    def aceita(self, seq):
        if seq <= self.maior - self.w or seq in self.vistos:
            return False
        self.vistos.add(seq)
        self.maior = max(self.maior, seq)
        return True


def test_janela_anti_reproducao():
    j = _JanelaAntiReproducao(w=4)
    assert j.aceita(1) and j.aceita(3) and j.aceita(2)  # fora de ordem, dentro da janela
    assert not j.aceita(2)  # repetido
    assert j.aceita(10)
    assert not j.aceita(5)  # antigo demais (10 - 4 = 6)
    assert j.aceita(8)


# ---------------------------------------------------------------- s13 WEP


def test_crc32_e_linear():
    a, b = b"pagar 100 reais", b"pagar 900 reais"
    zero = bytes(len(a))
    xor = bytes(x ^ y for x, y in zip(a, b, strict=True))
    assert zlib.crc32(xor) == zlib.crc32(a) ^ zlib.crc32(b) ^ zlib.crc32(zero)


def test_repeticao_de_iv():
    N = 2**24

    def prob(k):
        return 1 - math.exp(-k * (k - 1) / (2 * N))

    k = math.ceil(math.sqrt(2 * N * math.log(2)))
    assert k == 4823
    assert prob(k - 1) < 0.5 <= prob(k + 1)


# ---------------------------------------------------------------- s14 firewall


def _decide(regras, origem, destino, porta):
    for acao, rede_o, rede_d, p in regras:
        if (
            ipaddress.ip_address(origem) in ipaddress.ip_network(rede_o)
            and ipaddress.ip_address(destino) in ipaddress.ip_network(rede_d)
            and p in (porta, "*")
        ):
            return acao
    return "negar"  # negação por padrão


def test_regras_primeira_que_casa():
    DMZ, INTERNA = "203.0.113.0/28", "10.0.0.0/8"
    regras = [
        ("permitir", "0.0.0.0/0", DMZ, 443),
        ("negar", "0.0.0.0/0", INTERNA, "*"),
        ("permitir", INTERNA, "0.0.0.0/0", "*"),
    ]
    assert _decide(regras, "198.51.100.7", "203.0.113.5", 443) == "permitir"
    assert _decide(regras, "198.51.100.7", "203.0.113.5", 22) == "negar"
    assert _decide(regras, "198.51.100.7", "10.1.1.1", 443) == "negar"
    trocadas = [("permitir", "0.0.0.0/0", "0.0.0.0/0", "*")] + regras
    assert _decide(trocadas, "198.51.100.7", "10.1.1.1", 22) == "permitir"


# ---------------------------------------------------------------- s15 PPP e RBAC


def test_chap_md5():
    ident, segredo = bytes([7]), b"segredo-do-enlace"
    desafio = secrets.token_bytes(16)
    resposta = hashlib.md5(ident + segredo + desafio).digest()
    assert resposta == hashlib.md5(ident + segredo + desafio).digest()
    assert resposta != hashlib.md5(ident + segredo + secrets.token_bytes(16)).digest()
    assert segredo not in resposta


def test_rbac_por_papel():
    papeis = {"professor": {"lancar_nota", "ver_nota"}, "aluno": {"ver_nota"}}
    usuarios = {"u1": "professor", "u2": "aluno"}

    def pode(u, acao):
        return acao in papeis[usuarios[u]]

    assert pode("u1", "lancar_nota") and pode("u2", "ver_nota") and not pode("u2", "lancar_nota")
