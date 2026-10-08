from fastapi.testclient import TestClient

from backend.main import create_app


def test_local_endpoint_uses_named_tutor_and_course_context(monkeypatch):
    from acervo import models, retrieval
    calls = []
    monkeypatch.setenv('TUTORON_AI_PROVIDER', 'ollama')
    monkeypatch.setattr(retrieval, 'search', lambda q: [{'id': 'curado'}])
    monkeypatch.setattr(retrieval, 'context', lambda chunks, **kw: '[curado] Contexto revisado.')
    def generated(question, context, **kwargs):
        calls.append((question, context, kwargs))
        return {'texto': 'Resposta [curado]', 'modelo': 'tutoron-paa', 'segundos': 0.1}
    monkeypatch.setattr(models, 'generate', generated)
    result = TestClient(create_app()).post('/api/v1/questions', json={'question': 'Explique DP', 'context': 'código do aluno'})
    assert result.status_code == 200
    assert result.json()['source'] == 'ollama-rag'
    assert result.json()['metadata']['model'] == 'tutoron-paa'
    assert calls[0][1] == '[curado] Contexto revisado.'
    assert 'código do aluno' in calls[0][0]
    assert calls[0][2] == {'provider': 'ollama'}
