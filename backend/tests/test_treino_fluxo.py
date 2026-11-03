"""Recuperar a avaliação não pode repetir ou perder um treino caro já concluído."""
import asyncio
import builtins
import sys

import httpx
import pytest

from scripts import treinar


def test_dependencia_de_avaliacao_ausente_para_antes_de_ocupar_gpu(monkeypatch, tmp_path):
    importar = builtins.__import__

    def sem_pydantic(nome, *args, **kwargs):
        if nome == 'eval.socratico':
            raise ModuleNotFoundError("No module named 'pydantic'", name='pydantic')
        return importar(nome, *args, **kwargs)

    def proibido(*args, **kwargs):
        pytest.fail('A falha de dependência precisa ser detectada antes do treino')

    monkeypatch.setattr(builtins, '__import__', sem_pydantic)
    monkeypatch.setattr(sys, 'argv', ['treinar.py'])
    monkeypatch.setattr(treinar, 'preparar_dados', lambda: {})
    monkeypatch.setattr(treinar, 'treinar', proibido)
    pasta = tmp_path / 'execucoes'
    monkeypatch.setattr(treinar, 'PASTA_TRABALHO', pasta)
    with pytest.raises(SystemExit, match="pydantic.*avaliação"):
        treinar.main()
    assert not pasta.exists()


def test_so_avaliar_reaproveita_instalado_sem_preparar_dados_ou_pesos(monkeypatch, tmp_path, capsys):
    nomes = []

    async def avaliar(nome):
        nomes.append(nome)
        return tmp_path / 'comparacao.md'

    def proibido(*args, **kwargs):
        pytest.fail('Recuperar avaliação não pode preparar dados, treinar, mesclar ou importar')

    monkeypatch.setattr(sys, 'argv', ['treinar.py', '--so-avaliar', '--nome', 'candidato'])
    monkeypatch.setattr(treinar, 'verificar_dependencias_avaliacao', lambda: None)
    monkeypatch.setattr(treinar, 'avaliar', avaliar)
    for funcao in ('preparar_dados', 'treinar', 'mesclar', 'importar_no_ollama'):
        monkeypatch.setattr(treinar, funcao, proibido)
    treinar.main()
    assert nomes == ['candidato']
    assert 'Avaliação concluída' in capsys.readouterr().out


@pytest.mark.parametrize('opcao', ['--so-dados', '--verificar', '--teste-gpu', '--pular-avaliacao'])
def test_modos_incompativeis_nao_iniciam_trabalho(monkeypatch, opcao):
    monkeypatch.setattr(sys, 'argv', ['treinar.py', '--so-avaliar', opcao])
    with pytest.raises(SystemExit) as exc:
        treinar.main()
    assert exc.value.code == 2


def test_candidato_ausente_nao_gasta_bateria_do_modelo_atual(monkeypatch, tmp_path):
    from eval import socratico

    async def proibido(*args, **kwargs):
        pytest.fail('Não deve começar a bateria sem o candidato instalado')

    def ausente(url, *, json, timeout):
        assert url.endswith('/api/show') and json == {'model': 'ausente'}
        return httpx.Response(404, request=httpx.Request('POST', url))

    monkeypatch.setattr(httpx, 'post', ausente)
    monkeypatch.setattr(socratico, 'executar', proibido)
    with pytest.raises(SystemExit, match='não está instalado'):
        asyncio.run(treinar.avaliar('ausente'))
