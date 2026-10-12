from acervo import models
from acervo.common import write_json
from acervo.evaluate import evaluate


def test_model_update_invalidates_only_affected_generation_cache(tmp_path, monkeypatch):
    write_json(tmp_path / '02-acervo/itens.json', [])
    write_json(tmp_path / '04-rag/indice.json', {'chunks': [], 'vectors': []})
    write_json(tmp_path / '06-avaliacao/questoes.json', [
        {'id': 'Qtest', 'pergunta': 'Explique', 'contexto': [], 'fontes_esperadas': [], 'checkpoints': []}])
    versions = {}
    calls = []
    monkeypatch.setattr(models, 'model_digest', lambda name: versions.get(name, 'v1'))

    def generate(*args, model=None, **kwargs):
        calls.append(model)
        return {'texto': 'resposta ' + str(len(calls)), 'segundos': 1, 'modelo': model}

    monkeypatch.setattr(models, 'generate', generate)
    first = evaluate(tmp_path, provider='ollama', generate=True)
    assert len(calls) == 4 and all(r['status'] == 'ok' for r in first)
    evaluate(tmp_path, provider='ollama', generate=True)
    assert len(calls) == 4
    base = first[0]['resposta']['modelo']
    versions[base] = 'v2'
    changed = evaluate(tmp_path, provider='ollama', generate=True)
    assert len(calls) == 6
    assert changed[0]['modelo_digest'] == 'v2'
    assert changed[2]['resposta']['texto'] == first[2]['resposta']['texto']
