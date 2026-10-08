from acervo.common import TOPICS, digest, write_json
from acervo.retrieval import build, search
from acervo import models


def test_unreviewed_material_is_excluded_even_from_stale_index(tmp_path):
    def item(identifier, confidence):
        text = 'asterisco recorrência dois subproblemas ' + identifier
        return {'id': identifier, 'texto': text, 'sha256': digest(text),
                'confiabilidade': confidence, 'qualidade_ocr': 'boa',
                'assunto': TOPICS[0], 'segmentacao': 'ok'}
    rows = [item('reviewed','media'), item('approved','alta'),
            item('unreviewed','nao_verificada'), item('rejected','baixa')]
    write_json(tmp_path / '02-acervo/itens.json', rows)
    index = build(tmp_path)
    assert {r['id'] for r in index['chunks']} == {'reviewed','approved'}
    # Um índice antigo não deve continuar servindo texto após retirar a revisão.
    rows[0]['confiabilidade'] = 'nao_verificada'
    write_json(tmp_path / '02-acervo/itens.json', rows)
    assert {r['id'] for r in search('asterisco', tmp_path, semantic=False)} == {'approved'}


def test_valid_cached_embeddings_need_no_server_request(tmp_path, monkeypatch):
    item = {'id': 'a', 'texto': 'asterisco', 'sha256': digest('asterisco'),
            'confiabilidade': 'media', 'qualidade_ocr': 'boa', 'assunto': TOPICS[0], 'segmentacao': 'ok'}
    write_json(tmp_path / '02-acervo/itens.json', [item])
    monkeypatch.setenv('TUTORON_EMBED_MODEL', 'embedding:test')
    write_json(tmp_path / '04-rag/indice.json', {'embedding_model': 'embedding:test',
        'embedding_janelas_caracteres': 1000, 'chunks': [item], 'vectors': [[1.0, 0.0]]})

    def unavailable(*args, **kwargs):
        raise AssertionError('Cache válido não precisa chamar servidor')

    monkeypatch.setattr(models, 'embeddings', unavailable)
    monkeypatch.setattr(models, 'post', unavailable)
    index = build(tmp_path, embed=True)
    assert index['modo'] == 'hibrido' and index['vectors'] == [[1.0, 0.0]]


def test_unload_failure_does_not_destroy_completed_embeddings(tmp_path, monkeypatch):
    write_json(tmp_path / '02-acervo/itens.json', [{'id': 'a', 'texto': 'asterisco', 'sha256': digest('asterisco'),
        'confiabilidade': 'media', 'qualidade_ocr': 'boa', 'assunto': TOPICS[0], 'segmentacao': 'ok'}])
    monkeypatch.setattr(models, 'embeddings', lambda *args, **kwargs: [[1.0, 0.0]])
    monkeypatch.setattr(models, 'post', lambda *args, **kwargs: (_ for _ in ()).throw(TimeoutError()))
    index = build(tmp_path, embed=True)
    assert index['modo'] == 'hibrido' and len(index['vectors']) == 1 and index['erro_embeddings'] is None
