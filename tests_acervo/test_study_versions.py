from acervo.app import Study, summarize
from acervo.common import write_json


def test_votes_remain_linked_to_the_answer_version_seen(tmp_path):
    folder = tmp_path / '07-validacao-alunos'
    pair = {'id': 'Q1', 'pergunta': 'Explique', 'origem': 'teste',
            'generico': {'texto': 'A'}, 'tutoron': {'texto': 'B'}}
    write_json(folder / 'pares.json', [pair])
    study = Study(tmp_path)
    first = study.start('Q1')
    pair['tutoron']['texto'] = 'Resposta corrigida'
    write_json(folder / 'pares.json', [pair])
    second = study.start('Q1')
    assert set(first) == {'sessao', 'pergunta', 'A', 'B'}
    hashes = [study.sessions[r['sessao']]['par_sha256'] for r in (first,second)]
    assert hashes[0] != hashes[1]
    for response in (first,second):
        study.vote({'sessao': response['sessao'], 'preferida': 'empate',
                    **{f'{c}_{s}': 3 for c in ('clareza','confianca','utilidade') for s in ('a','b')}})
    summary = summarize(tmp_path)
    assert summary['total'] == 2 and len(summary['por_questao']) == 2
    assert {r['par_sha256'] for r in summary['por_questao']} == set(hashes)
    assert all((folder / 'pares-sessoes' / (h + '.json')).exists() for h in hashes)
