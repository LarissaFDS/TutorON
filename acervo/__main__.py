import argparse
import json

from .common import ROOT, init, read_json, write_json
from .extract import inventory, extract
from .curate import organize, triage
from .retrieval import build, search
from .evaluate import make_questions, evaluate, offline
from .app import serve, summarize


def report(root=ROOT):
    from collections import Counter
    docs = read_json(root / '03-triagem/inventario.json', [])
    items = read_json(root / '02-acervo/itens.json', [])
    index = read_json(root / '04-rag/indice.json', {})
    results = read_json(root / '06-avaliacao/resultados.json', [])
    pairs = read_json(root / '07-validacao-alunos/pares.json', [])
    extracts = [read_json(root / '01-extraido' / (d['id'] + '.json'), {}) for d in docs]
    pages = [p for d in extracts for p in d.get('paginas_extraidas', [])]
    candidates = [c for p in pages for c in p.get('visao_candidata', [])]
    verdicts = read_json(root / '03-triagem/pareceres.json', [])
    counts = Counter(i['assunto'] for i in items)
    lines = ['# TutorON — relatório para quinta-feira, 1º de outubro', '',
             'Este relatório separa execução técnica de validação pedagógica. Os resultados anteriores de 41%/70% pertencem à PoC fornecida, não a esta rodada.', '',
             '## 1. Digitalizar e revisar o acervo', '',
             f'- {len(docs)} documentos de entrada inventariados; {len(extracts)} saídas de extração.',
             f'- {len(pages)} páginas/blocos: ' + ', '.join(f'{k}: {v}' for k,v in Counter(p['qualidade'] for p in pages).items()) + '.',
             f'- {len(candidates)} tentativas de visão em recortes/fotos: {sum(c["status"] == "incerto_revisao_humana" for c in candidates)} candidatos incertos e {sum(c["status"] == "ilegivel" for c in candidates)} falhas. Nenhum candidato substitui automaticamente a fonte.',
             '- Cópias imutáveis por hash em 00-originais; imagens/páginas para conferência em 01-extraido/figuras.',
             '- Extração automática não certifica manuscritos, fórmulas, diagramas nem qualidade de soluções.', '',
             '## 2. Organizar por questão, fonte e confiabilidade', '',
             f'- {len(items)} blocos no índice; {sum(i["segmentacao"] == "pendente" for i in items)} sem segmentação segura.',
             f'- {sum(i["confiabilidade"] == "baixa" for i in items)} classificados como baixa confiança, incluindo ilegíveis.',
             f'- Pareceres locais: {sum(v["parecer_ia"]["status"] == "executado" for v in verdicts)} concluídos; {sum(v["parecer_ia"]["status"] == "falhou" for v in verdicts)} falhas; os demais não foram solicitados ou não tinham resolução identificada.',
             '- Contagens por assunto (blocos candidatos, não questões únicas certificadas):', '']
    lines += [f'  - {k}: {v}' for k,v in sorted(counts.items())]
    lines += ['', '## 3. Automatizar a busca do trecho certo', '',
              f'- {len(index.get("chunks", []))} blocos elegíveis; busca: {index.get("modo", "não executada")}.',
              '- Baixa confiança, ilegíveis e cortes incertos não entram na busca. Metadados acompanham cada citação.',
              '- Ollama local; Gemini opcional com fallback. As chamadas reais registram provedor, modelo e tempo.', '',
              '## 4. Validar com questões, alunos e professor', '',
              f'- {len(read_json(root / "06-avaliacao/questoes.json", []))} questões no conjunto; {sum(r["status"] == "ok" for r in results)} respostas reais concluídas na rodada atual.',
              f'- {len(pairs)} pares offline; {summarize(root)["total"]} registros de avaliação salvos (não equivalem, por si, a um estudo com alunos).',
              '- Comparação A/B sorteada no servidor; notas separadas para clareza, confiança e utilidade.',
              '- Professor: pendente. As expressões regulares medem cobertura lexical, não prova de correção.', '',
              '## Limitações e revisão manual necessária', '',
              '- Conferir páginas com imagens e OCR parcial; segmentação automática pode confundir enumerações e linhas de código.',
              '- Conferir origem/autoria e corrigir apenas em arquivos derivados aprovados; triagem não reescreve resoluções.',
              '- Revisar suspeitas em 03-triagem/relatorio.md e confirmar enunciados, fontes esperadas e checklists em 06-avaliacao/questoes.json.',
              '- Nenhum fine-tuning foi executado. Dataset só admite pares de alta confiança, com aprovação e fonte verificável.',
              '- Os dois modelos de texto erraram na comparação rápida; veja 05-modelo/comparacao.json. Respostas de IA exigem conferência, mesmo quando o checklist lexical passa.',
              '- Esta entrega é local. Não houve publicação, envio do acervo a Gemini, commit ou push automático.', '',
              'Execução: iniciar_validacao.bat abre o ambiente; atualizar_acervo.bat refaz o pipeline; avaliar_modelos.bat executa as três condições.']
    lines += ['', '## Resultados técnicos do checklist', '',
              '| Condição | Respostas concluídas | Critérios encontrados / aplicáveis |',
              '|---|---:|---:|']
    for scenario in ('generico', 'rag_manual', 'rag_automatica'):
        complete = [r for r in results if r['cenario'] == scenario and r['status'] == 'ok']
        hits = sum(r['avaliacao']['acertos'] for r in complete)
        total = sum(r['avaliacao']['total'] for r in complete)
        lines.append(f'| {scenario} | {len(complete)} | {hits} / {total} |')
    lines += ['', 'Esses números não são acurácia matemática. Fontes recuperadas e exclusões estão em 06-avaliacao/relatorio.md; respostas, tempos de geração e eventuais repetições estão em 06-avaliacao/resultados.json.']
    (root / 'RELATORIO_QUINTA.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def dataset(root=ROOT):
    items = read_json(root / '02-acervo/itens.json', [])
    approved = read_json(root / '05-modelo/pares-aprovados.json', [])
    by_id = {r['id']: r for r in items}
    records = []
    for pair in approved:
        item = by_id.get(pair.get('fonte_id'))
        if item and item['confiabilidade'] == 'alta' and pair.get('sha256') == item['sha256'] and pair.get('revisor') and pair.get('pergunta') and pair.get('resposta_ideal'):
            records.append(pair)
    (root / '05-modelo/dataset-finetuning.jsonl').write_text(''.join(json.dumps(p, ensure_ascii=False) + '\n' for p in records), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='TutorON — acervo local de PAA')
    parser.add_argument('acao', choices=['inventario', 'extrair', 'organizar', 'triar', 'indexar', 'avaliar', 'offline', 'servir', 'resumo', 'pipeline', 'relatorio', 'buscar'])
    parser.add_argument('--visao', action='store_true')
    parser.add_argument('--reprocessar', action='store_true')
    parser.add_argument('--ia', action='store_true')
    parser.add_argument('--embeddings', action='store_true')
    parser.add_argument('--gerar', action='store_true')
    parser.add_argument('--provedor', choices=['ollama', 'auto', 'gemini'], default='ollama')
    parser.add_argument('--questoes', help='IDs separados por vírgula')
    parser.add_argument('--limite-ia', type=int)
    parser.add_argument('--pasta')
    parser.add_argument('--pergunta')
    parser.add_argument('--porta', type=int, default=8765)
    args = parser.parse_args()
    init()
    if args.acao in ('inventario', 'pipeline'): inventory(extra=args.pasta)
    if args.acao in ('extrair', 'pipeline'): extract(vision=args.visao, retry=args.reprocessar)
    if args.acao in ('organizar', 'pipeline'): organize()
    if args.acao in ('triar', 'pipeline'): triage(use_ai=args.ia, limit=args.limite_ia)
    if args.acao in ('indexar', 'pipeline'): build(embed=args.embeddings)
    if args.acao in ('avaliar', 'pipeline'):
        make_questions()
        evaluate(provider=args.provedor, generate=args.gerar, selected=args.questoes.split(',') if args.questoes else None)
    if args.acao in ('offline', 'pipeline'): offline()
    if args.acao == 'servir': serve(port=args.porta)
    if args.acao == 'resumo': print(json.dumps(summarize(), ensure_ascii=False, indent=2))
    if args.acao == 'buscar': print(json.dumps(search(args.pergunta or ''), ensure_ascii=False, indent=2))
    dataset()
    report()


if __name__ == '__main__':
    main()
