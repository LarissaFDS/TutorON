"""Acervo de Introdução à Engenharia de Computação e conferência das resoluções.

Os blocos parafraseiam duas reavaliações de 2016.1 (fotos não versionadas) e os slides usados na disciplina.
Cada conversão, expressão booleana e circuito que aparece num bloco é recalculado aqui por força bruta.
"""

import ipaddress
import json
import re
import shutil
import struct
import subprocess
from itertools import product

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

IEC = disciplinas.obter("iec")
PASTA = ROOT / "disciplinas/iec"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
ITENS = {i["id"]: i for i in read_json(IEC.itens)}
FRONTEIRA = ("sd", "oac", "prog1", "discreta")
OUTRAS = ("paa", "sd", "oac", "calc3", "prob", "ed", "prog1", "discreta", "fis2", "ga")
SEM_MATERIAL = {"iec-01-historia-atribuicoes", "iec-03-linguagens-programacao", "iec-11-embarcados-automacao"}


def buscar(pergunta, d=IEC):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return ITENS[ident]["texto"]


def tabela(f, n):
    return [m for m, bits in enumerate(product((0, 1), repeat=n)) if f(*bits)]


def n(x):
    return 1 - x


def ieee(v):
    return struct.pack(">f", v).hex().upper()


# ---------------------------------------------------------------- cadastro e acervo


def test_iec_cadastrada_com_acervo_proprio():
    assert IEC.nome == "Introdução à Engenharia de Computação" and IEC.itens.exists() and not IEC.livro_supabase
    ids = {c["id"] for c in read_json(IEC.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({IEC.itens, IEC.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert all(c["disciplina"] == "iec" for c in read_json(IEC.indice)["chunks"])
    # todo tópico com material da turma tem bloco na busca; os sem material estão registrados na curadoria
    assert {i["assunto"] for i in ITENS.values()} == set(IEC.assuntos) - SEM_MATERIAL
    assert ids == set(ITENS)


def test_situacao_da_disciplina():
    assert IEC.situacao in ("em validação", "MVP")
    if IEC.situacao == "MVP":
        assert not IEC.em_validacao and not IEC.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas iec --embeddings`."""
    gerados = disciplinas.registros(IEC)
    assert gerados == read_json(IEC.itens)
    assert {c["id"] for c in read_json(IEC.indice)["chunks"]} == {
        i["id"] for i in gerados if i["confiabilidade"] in ("media", "alta")
    }


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for i in ITENS.values():
        assert len(i["texto"]) <= 2200, i["id"]
        assert "**Verificação:**" in i["texto"].strip().splitlines()[-1], i["id"]


def test_nenhuma_nota_da_ia_e_nada_revisado_sem_registro():
    assert not [i for i, x in ITENS.items() if x["natureza"] == "nota_da_equipe_ia"]
    for p in IEC.materiais.glob("*.md"):
        cab = p.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, p.name


def test_resolucoes_tem_status_e_dizem_no_texto():
    assert {i["status_resolucao"] for i in ITENS.values()} == {"validada"}
    for i in ITENS.values():
        assert "Status da resolução: validada" in i["texto"] and "não é gabarito do professor" in i["texto"], i["id"]


# ---------------------------------------------------------------- busca e isolamento


@pytest.mark.parametrize(
    "pergunta, aceitos",
    [
        ("Como converter 156 para binário e hexadecimal?", {"iec-conversao-bases-ip"}),
        (
            "Como simplificar uma expressão com mapa de Karnaugh?",
            {"iec-karnaugh-3-variaveis", "iec-karnaugh-4-variaveis"},
        ),
        ("O que faz uma porta XOR?", {"iec-portas-logicas"}),
        ("O que são os níveis de máquina do Tanenbaum?", {"iec-niveis-de-maquina"}),
        (
            "Como representar -3 em complemento de 2 com 8 bits?",
            {"iec-complemento-de-2-e-float", "iec-sistemas-numeracao-negativos"},
        ),
        (
            "Como escrever um número no padrão IEEE 754?",
            {"iec-fracoes-binarias-ieee754", "iec-complemento-de-2-e-float"},
        ),
        ("Qual a máscara e o broadcast de uma rede classe C?", {"iec-ipv4-classe-c-mascara-broadcast"}),
        ("O que é linkedição?", {"iec-software-basico-so-compilacao"}),
        ("Em que camada fica o protocolo UDP?", {"iec-redes-tcpip-www-dns"}),
        ("Como funciona um somador completo?", {"iec-somadores"}),
        ("Como montar um comparador de 2 bits?", {"iec-comparador-2-bits"}),
    ],
)
def test_pergunta_de_iec_encontra_bloco_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize("pergunta", ["Qual a capital da França?", "Como calcular uma integral dupla?"])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize(
    "pergunta",
    [
        "Como simplificar uma expressão com mapa de Karnaugh?",
        "Como representar -3 em complemento de 2?",
        "Como funciona um somador completo?",
        "O que são os níveis de máquina?",
        "Como declarar um float em C?",
    ],
)
def test_vocabulario_comum_fica_na_disciplina_escolhida(pergunta):
    """Fronteira com Sistemas Digitais, OAC, Programação 1 e Discreta: cada uma busca só no próprio índice."""
    assert all(i.startswith("iec-") for i in buscar(pergunta))
    for d in FRONTEIRA:
        assert not any(i.startswith("iec-") for i in buscar(pergunta, disciplinas.obter(d)))


def test_rigor_tem_fronteiras_e_metodos():
    for termo in ("Sistemas Digitais", "Organização e Arquitetura", "divisões sucessivas", "código Gray",
                  "tabela-verdade", "excesso 127", "**Verificação:**", "Não entregue a resolução"):  # fmt: skip
        assert termo in IEC.rigor, termo


# ---------------------------------------------------------------- conferência das resoluções


def test_conversoes_e_ip():
    t = texto("iec-conversao-bases-ip")
    assert format(156, "b") == "10011100" and format(156, "X") == "9C" and format(156, "o") == "234"
    q, restos = 156, []
    while q:
        q, r = divmod(q, 2)
        restos.append(r)
    assert "".join(map(str, reversed(restos))) == "10011100"
    octetos = [200, 17, 114, 17]
    assert ".".join(format(o, "08b") for o in octetos) in t
    assert ".".join(format(o, "02X") for o in octetos) in t
    assert format(int(ipaddress.IPv4Address("200.17.114.17")), "08X") == "C8117211"
    t = texto("iec-sistemas-numeracao-negativos")
    assert int("2A", 16) == 42 and format(-6 & 0xFF, "08b") == "11111010" and format((~6) & 0xFF, "08b") == "11111001"
    assert format(128 - 6, "08b") == "01111010" and format(0x80 | 6, "08b") == "10000110"
    for s in ("11111010", "11111001", "01111010", "10000110"):
        assert s in t


def test_complemento_de_2_e_ieee754():
    t = texto("iec-complemento-de-2-e-float")
    x, y = 67, -3
    assert format(x, "08b") == "01000011" and format(y & 0xFF, "08b") == "11111101"
    soma = (x & 0xFF) + (y & 0xFF)
    assert soma >> 8 == 1 and format(soma & 0xFF, "08b") == "01000000" and ieee(64.0) == "42800000"
    assert "0x42800000" in t
    t = texto("iec-fracoes-binarias-ieee754")
    assert 37 + 7 / 32 == 37.21875 and 0.3125 == 5 / 16 and format(37, "b") == "100101"
    assert ieee(37.21875) == "4214E000" and ieee(0.3125) == "3EA00000"
    assert (
        format(struct.unpack(">I", struct.pack(">f", 37.21875))[0], "032b")
        == "0" + "10000100" + "00101001110000000000000"
    )
    assert (1 + 2**-3 + 2**-5 + 2**-8 + 2**-9 + 2**-10) * 2**5 == 37.21875
    assert "0x4214E000" in t and "0x3EA00000" in t


def test_fatoracoes_dos_slides():
    pares = [
        (
            lambda a, b, c: n(a) & n(b) & n(c) | n(a) & b & n(c) | a & n(b) & c,
            lambda a, b, c: n(a) & n(c) | a & n(b) & c,
        ),
        (lambda a, b, c: n(a) & n(b) | n(a) & b, lambda a, b, c: n(a)),
        (
            lambda a, b, c: n(a) & n(b) & n(c) | n(a) & b & c | n(a) & b & n(c) | a & n(b) & n(c) | a & b & n(c),
            lambda a, b, c: n(a) & b | n(c),
        ),
        (lambda a, b, c: (a | b | c) & (n(a) | n(b) | c), lambda a, b, c: a & n(b) | n(a) & b | c),
        (lambda a, b, c: a & b & c | a & n(c) | a & n(b), lambda a, b, c: a),
        (lambda a, b, c: n(a) & n(b) | n(a) & b | a & n(b), lambda a, b, c: n(a) | n(b)),  # NAND (formas canônicas)
    ]
    for original, simplificada in pares:
        assert tabela(original, 3) == tabela(simplificada, 3)


def test_karnaugh_3_e_4_variaveis():
    assert tabela(lambda a, b, c: n(a) & c | a & n(b) | a & n(c), 3) == [1, 3, 4, 5, 6]
    assert tabela(lambda a, b, c: n(a) & c | n(b) & c | a & n(c), 3) == [1, 3, 4, 5, 6]
    assert tabela(lambda a, b, c: c | n(a) & n(b), 3) == [0, 1, 3, 5, 7]
    assert tabela(lambda a, b, c: n(a) & n(c) | b & c, 3) == [0, 2, 3, 7]
    assert tabela(lambda a, b, c, d: n(a) & d | n(a) & b | b & c & d | a & n(b) & c & n(d), 4) == [
        1,
        3,
        4,
        5,
        6,
        7,
        10,
        15,
    ]
    assert tabela(lambda a, b, c, d: n(c) & d | n(b) & n(d) | a & b & d, 4) == [0, 1, 2, 5, 8, 9, 10, 13, 15]
    assert "\\sum m(1,3,4,5,6,7,10,15)" in texto("iec-karnaugh-4-variaveis")


def test_portas_somadores_e_comparador():
    for a, b in product((0, 1), repeat=2):
        assert (a ^ b) == (n(a) & b | a & n(b)) and n(a & b) == (n(a) | n(b)) and n(a | b) == (n(a) & n(b))
    for a, b, c in product((0, 1), repeat=3):
        s, co = a ^ b ^ c, a & b | (a ^ b) & c
        assert a + b + c == 2 * co + s
    for x, y in product(range(16), repeat=2):
        carry, soma = 0, 0
        for i in range(4):
            ai, bi = x >> i & 1, y >> i & 1
            soma |= (ai ^ bi ^ carry) << i
            carry = ai & bi | (ai ^ bi) & carry
        assert soma + 16 * carry == x + y
    assert 0b0110 + 0b0111 == 0b1101
    for a1, a0, b1, b0 in product((0, 1), repeat=4):
        assert (n(a0 ^ b0) & n(a1 ^ b1)) == int((a1, a0) == (b1, b0))


def test_circuito_da_reavaliacao_ab1_q4():
    def porta_a_porta(a, b, c):
        g1 = n(n(a) | n(b) | n(c))
        g3 = n(a ^ c) & n(a)
        g6 = (a & n(b) | b) & c
        return g1 | g3 | g6

    assert tabela(porta_a_porta, 3) == [0, 2, 3, 5, 7]
    assert tabela(lambda a, b, c: n(a) & n(c) | a & c | b & c, 3) == [0, 2, 3, 5, 7]
    assert tabela(lambda a, b, c: n(a ^ c) | b & c, 3) == [0, 2, 3, 5, 7]
    assert "\\sum m(0,2,3,5,7)" in texto("iec-circuito-para-tabela-verdade")


def test_ipv4_classe_c():
    rede = ipaddress.IPv4Network("192.168.10.0/24")
    host = ipaddress.IPv4Address("192.168.10.25")
    assert (
        format(192, "08b").startswith("110")
        and format(223, "08b").startswith("110")
        and format(224, "08b")[:3] != "110"
    )
    assert host in rede and str(rede.netmask) == "255.255.255.0" and str(rede.broadcast_address) == "192.168.10.255"
    assert rede.num_addresses - 2 == 254
    assert ipaddress.IPv4Address(int(host) & int(rede.netmask)) == rede.network_address


def test_questoes_objetivas_da_reavaliacao_ab2():
    t = texto("iec-redes-tcpip-www-dns")
    for trecho in ("alternativa **(D)**", "alternativa **(A)**", "**HTML**", "**URL**", "**HTTP**"):
        assert trecho in t
    alternativas_q6 = {"a": "FVV", "b": "FFF", "c": "VFV", "d": "FVF", "e": "VFF"}
    alternativas_q10 = {"a": "FVV", "b": "FFF", "c": "VFF", "d": "VVV", "e": "VFV"}
    assert [k for k, v in alternativas_q6.items() if v == "VFV"] == ["c"]
    assert [k for k, v in alternativas_q10.items() if v == "VVV"] == ["d"]
    t = texto("iec-software-basico-so-compilacao")
    assert "alternativa **(E)**" in t and "Alternativa **(c)**" in t and "Alternativa **(d)**" in t


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in ITENS.values():
        assert i["texto"].count("$") % 2 == 0, i["id"]


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in ITENS.values() for a, b in FORMULA.findall(i["texto"])]
    formulas += [a or b for a, b in FORMULA.findall(IEC.rigor)]
    assert len(formulas) >= 80
    katex = (ROOT / "backend/web/vendor/katex/katex.min.js").as_posix()
    script = (
        f"const k=require({json.dumps(katex)});const fs=require('fs');"
        "const erros=[];for(const f of JSON.parse(fs.readFileSync(0,'utf8'))){"
        "try{k.renderToString(f,{throwOnError:true})}catch(e){erros.push(f+' :: '+e.message)}}"
        "console.log(JSON.stringify(erros))"
    )
    r = subprocess.run(
        ["node", "-e", script], input=json.dumps(formulas), capture_output=True, text=True, encoding="utf-8", check=True
    )
    assert json.loads(r.stdout) == []


def test_catalogo_completo_e_coerente():
    obrigatorios = {"id", "nome", "autoria", "url", "idioma", "formato", "isa", "topicos", "licenca", "acesso",
                    "prioridade", "uso", "justificativa"}  # fmt: skip
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f["id"]
        assert f["prioridade"] in ("alta", "media", "referencia")
        assert f["uso"] in ("acervo", "citada", "referencia", "candidato", "indisponivel")
        assert set(f["topicos"]) <= set(IEC.assuntos), f["id"]
    assert {x for i in ITENS.values() for x in i["fontes_catalogo"]} <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f["uso"] == "acervo"} == {
        x for i in ITENS.values() for x in i["fontes_catalogo"]
    }
    assert (
        CATALOGO["tanenbaum-livro"]["uso"] == "referencia" and "Não incluído" in CATALOGO["tanenbaum-livro"]["acesso"]
    )


def test_originais_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    assert not [
        p
        for p in arquivos
        if p.suffix.lower() in (".pdf", ".png", ".jpg", ".jpeg", ".heic", ".webp", ".docx", ".doc", ".zip", ".pptx")
    ]
    proibidos = re.compile(
        r"(?i)[\w.]+@[\w-]+\.\w+|groups\.google|dropbox|sites\.google|whatsapp|fmrp\.usp|fem\.unicamp"
    )
    for p in [
        *IEC.materiais.glob("*.md"),
        IEC.itens,
        PASTA / "rigor.md",
        PASTA / "CURADORIA.md",
        PASTA / "fontes.json",
    ]:
        assert not proibidos.search(p.read_text(encoding="utf-8")), p.name
    for i in ITENS.values():
        assert "http" not in i["texto"], i["id"]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert [i for i in CATALOGO if f"`{i}`" not in curadoria] == []
    assert [i for i in ITENS if f"`{i}`" not in curadoria] == []
    assert "`iec`" in (ROOT / "docs/DISCIPLINAS.md").read_text(encoding="utf-8")
