"""Acervo de Projeto de Software (Programação 2, Ciência da Computação) e conferência do código.

Os blocos parafraseiam as perguntas das notas de aula de Programação II da UFCG (Profs. Jacques Sauvé,
Raquel Lopes e Dalton Serey) usadas pela turma de CC. Todo o código citado está em
`tests_acervo/projsw_java`, escrito pela equipe, e é compilado e executado aqui com o JDK.
"""

import re
import shutil
import subprocess

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

PROJSW = disciplinas.obter("projsw")
PASTA = ROOT / "disciplinas/projsw"
JAVA = ROOT / "tests_acervo/projsw_java"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(PROJSW.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "projsw")
FRONTEIRA = ("prog1", "ed", "bd")


def buscar(pergunta, d=PROJSW):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def _jdk():
    if not (shutil.which("javac") and shutil.which("java")):
        pytest.skip("JDK não encontrado: instale javac e java para compilar tests_acervo/projsw_java")


def compilar(caso, destino):
    _jdk()
    fontes = sorted(str(p) for p in (JAVA / caso).glob("*.java"))
    return subprocess.run(["javac", "-encoding", "UTF-8", "-nowarn", "-d", str(destino), *fontes], capture_output=True, text=True)


def rodar(caso, classe, tmp_path, *args):
    r = compilar(caso, tmp_path)
    assert r.returncode == 0, r.stderr
    p = subprocess.run(["java", "-cp", str(tmp_path), classe, *args], capture_output=True, text=True, timeout=60)
    assert p.returncode == 0, p.stderr
    return p.stdout.splitlines(), p.stderr.splitlines()


# ---------------------------------------------------------------- cadastro e acervo


def test_projsw_cadastrada_com_acervo_proprio():
    assert PROJSW.nome == "Projeto de Software" and PROJSW.itens.exists()
    ids = {c["id"] for c in read_json(PROJSW.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({PROJSW.itens, PROJSW.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(PROJSW.assuntos)
    assert ids == set(TODOS)
    cursos = (ROOT / "disciplinas/cursos.json").read_text(encoding="utf-8")
    # sem ligação em cursos.json: a Programação 2 de CC mudaria as preferidas do 4º período (ver CURADORIA.md)
    assert cursos.count('"acervo": "projsw"') == 0


def test_situacao_da_disciplina():
    assert PROJSW.situacao == "em validação" and PROJSW.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas projsw --embeddings`."""
    assert disciplinas.registros(PROJSW) == read_json(PROJSW.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert len(t) <= 2200, i["id"]
        ultima = t.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in t and "Status da resolução:" in t, i["id"]
        assert re.search(r"`(test_\w+)`", ultima).group(1) in globals(), i["id"]
        for caso in re.findall(r"tests_acervo/projsw_java/(\w+)", t):
            assert (JAVA / caso).is_dir(), (i["id"], caso)
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO, (arq.name, f)


def test_sem_dados_pessoais_livros_nem_binarios():
    textos = " ".join(i["texto"] for i in TODOS.values()) + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert "Alysson" not in textos
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"] == "Protegido":
            assert f["uso"] == "referencia", f["id"]
    soltos = [p for p in list(PASTA.rglob("*")) + list(JAVA.rglob("*")) if p.suffix.lower() in (".pdf", ".class", ".jar", ".png", ".jpg")]
    assert not soltos


PERGUNTAS = [
    ("Qual é o String retornado por umaConta.toString()?", "projsw-objetos-referencias-tostring-equals"),
    ("Qual a diferença entre == e equals para comparar duas pessoas?", "projsw-objetos-referencias-tostring-equals"),
    ("Usando um array como coleção, como implementar as 4 operações: adicionar, remover, pesquisar e iterar?", "projsw-colecao-array-quatro-operacoes"),
    ("O que ocorre se digitar mais do que 10 nomes no cadastro com array?", "projsw-colecao-array-quatro-operacoes"),
    ("Por que dá ConcurrentModificationException ao remover dentro do for-each?", "projsw-genericos-iterador-remocao"),
    ("Em que ordem são chamados os construtores com muitos níveis de herança?", "projsw-ordem-construtores-metodo-polimorfico"),
    ("O que acontece se chamar um método polimórfico dentro do construtor?", "projsw-ordem-construtores-metodo-polimorfico"),
    ("Quando usar composição em vez de herança?", "projsw-composicao-versus-heranca-acoplamento"),
    ("Como fazer um único cliente para coleções de alunos e de disciplinas com interfaces?", "projsw-polimorfismo-interfaces-selecionavel-por-nome"),
    ("O que é o padrão Strategy?", "projsw-padrao-strategy-comparator"),
    ("Como reduzir o acoplamento da lista ordenada de alunos com compareTo?", "projsw-acoplamento-comparable-lista-ordenada"),
    ("Como projetar as classes do robô que anda na sala?", "projsw-projeto-oo-robo-sala-substantivos-verbos"),
    ("O que é o refatoramento Move Method?", "projsw-refatoramento-extract-move-method"),
    ("Qual a saída do programa para os argumentos 2 4 oi?", "projsw-excecoes-try-catch-soma-argumentos"),
    ("Como ler um arquivo linha a linha com BufferedReader?", "projsw-arquivos-bufferedreader-try-with-resources"),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    assert esperado in buscar(pergunta)[:3], buscar(pergunta)


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Quando usar composição em vez de herança?", d)).isdisjoint(TODOS)
    assert not buscar("Como funciona um flip-flop JK?")
    assert not set(buscar("Como calcular a transformada de Laplace de um degrau?"))


# ---------------------------------------------------------------- código compilado e executado


def test_objetos_e_igualdade(tmp_path):
    out, _ = rodar("pessoa", "Pessoas", tmp_path)
    assert out == ["false true", "1", "false", "Pessoa Joao, CPF 113"]


def test_colecao_com_array(tmp_path):
    out, _ = rodar("cadastro", "Cadastro", tmp_path)
    assert out[:10] == [f"add p{i} true" for i in range(1, 11)] and out[10] == "add p11 false"
    assert out[11:] == ["2 -1", "true false", "p1,p2,p10,p4,p5,p6,p7,p8,p9", "sem teste: ArrayIndexOutOfBoundsException"]


def test_genericos_e_iteradores(tmp_path):
    out, _ = rodar("genericos", "Genericos", tmp_path)
    assert out == ["ClassCastException", "[Ana, Caio]", "ConcurrentModificationException"]
    r = compilar("genericos_erro", tmp_path / "erro")
    assert r.returncode != 0 and "cannot be converted to String" in r.stderr


def test_ordem_dos_construtores(tmp_path):
    out, _ = rodar("construtores", "MistoQuente", tmp_path)
    assert out == [
        "Refeicao()",
        "Almoco() antes do preparo",
        "Prepara MistoQuente (pao ainda null)",
        "Almoco() depois do preparo",
        "AlmocoPortatil() antes do preparo",
        "Prepara MistoQuente (pao ainda null)",
        "AlmocoPortatil() depois do preparo",
        "Pao()",
        "Queijo()",
        "Presunto()",
        "MistoQuente() antes do preparo",
        "Prepara MistoQuente",
        "MistoQuente() depois do preparo",
    ]


def test_composicao(tmp_path):
    out, _ = rodar("composicao", "Composicao", tmp_path)
    assert out == ["Joao 50.0", "Maria 50.0"]


def test_polimorfismo_e_interfaces(tmp_path):
    out, _ = rodar("interfaces", "Seletor", tmp_path)
    assert out == ["2 1 0", "Disciplina Grafos"]


def test_strategy(tmp_path):
    out, _ = rodar("strategy", "Estrategia", tmp_path)
    assert out == ["[Ana, Bia, Caio]", "[Ana, Caio, Bia]"]


def test_acoplamento_compareto(tmp_path):
    r = compilar("acoplamento_errado", tmp_path / "errado")
    assert r.returncode != 0 and "lossy conversion from long to int" in r.stderr
    out, _ = rodar("acoplamento", "Ordena", tmp_path)
    assert out == ["Bia Caio Ana", "true", "[a, b]"]


def test_projeto_robo(tmp_path):
    out, _ = rodar("robo", "Robos", tmp_path)
    assert out == ["false true true", "true false", "2 3 0", "true", "alarme", "responde a voz"]


def test_refatoramento(tmp_path):
    out, _ = rodar("refatoramento", "Refatora", tmp_path)
    assert out == ["62/62", "12.55", "17.5"]


def test_excecoes_soma(tmp_path):
    out, err = rodar("excecoes", "Soma", tmp_path, "1", "2", "4", "oi")
    assert out == [] and err == ["One of the command-line arguments is not an integer."]
    out, err = rodar("excecoes", "Soma", tmp_path, "2", "2", "4", "oi")
    assert out == ["Sum = 6"] and err == ["[oi] is not an integer and will not be included in the sum."]


def test_arquivos(tmp_path):
    arq = tmp_path / "tres.txt"
    arq.write_text("a\nb\nc\n", encoding="utf-8")
    out, _ = rodar("arquivos", "Linhas", tmp_path, str(arq))
    assert out == ["3", "FileNotFoundException"]
