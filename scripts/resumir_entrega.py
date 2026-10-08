"""Resumo da rodada a partir de artefatos reais, com revisão vinculada por hash."""
import sys
from pathlib import Path
from statistics import mean

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from acervo.common import ROOT, digest, read_json


def main():
    audit = read_json(ROOT / '03-triagem/auditoria.json', {})['resumo']
    summary = read_json(ROOT / '06-avaliacao/comparacao-atual.json', {})
    reviews = read_json(ROOT / '06-avaliacao/revisao-tecnica.json', {})
    decisions = {(r['questao'],r['cenario']):r for r in reviews['revisoes']}
    results = read_json(ROOT / '06-avaliacao/resultados.json', [])
    assert len(results) == 48 and all(r['status'] == 'ok' for r in results)
    assert all(decisions[r['questao'],r['cenario']]['resposta_sha256'] == digest(r['resposta']['texto']) for r in results)
    follow = read_json(ROOT / '06-avaliacao/seguimento-7b.json', [])
    repeats = read_json(ROOT / '06-avaliacao/repeticoes.json', [])
    for r in follow + repeats:
        assert r['status'] == 'ok' and r['revisao_agente']['resposta_sha256'] == digest(r['resposta']['texto'])
    training = read_json(ROOT / '05-modelo/treino/manifesto.json', {})
    vision = read_json(ROOT / '06-avaliacao/visao-impressa.json', {})
    checks = read_json(ROOT / '03-triagem/verificacoes-curadoria.json', {})
    lines = ['# TutorON — relatório da validação antes do MVP', '',
        'Resultado: o fluxo local de OCR, curadoria, RAG e comparação funciona. **A superioridade do TutorON ainda não foi demonstrada.** '
        'Há ganhos em alguns critérios e respostas, mas também erros matemáticos graves. Não houve fine-tuning nem implantação pública.', '',
        '## Dados e OCR', '',
        f'- {audit["documentos"]} arquivos atuais: 16 PDFs, 30 WebP, dez transcrições Markdown e um TXT vazio. {audit["paginas"]} páginas/blocos extraídos; {audit["blocos"]} candidatos segmentados.',
        f'- {audit["blocos_corrigidos"]} versões corrigidas por agente, sem sobrescrever originais. {audit["blocos_rag"]} blocos no índice híbrido; confiança média por agente, nenhuma aprovação humana inventada.',
        '- Os outros 167 candidatos ficam fora da recuperação automática: 157 não verificados e dez com baixa confiança. Auditoria documental é estrutural; não certifica pedagogicamente todas as páginas.',
        '- Tesseract 5.3.4 português/inglês instalado de pacotes oficiais Ubuntu, localmente. PDFs digitalizados, PNG, JPEG, WebP, BMP, GIF e TIFF têm caminho de extração; seis formatos impressos e TIFF multipágina foram testados.',
        f'- Visão Qwen2.5VL 3B leu {vision.get("linhas_conferem",0)}/3 linhas de uma imagem impressa controlada em {vision["segundos"]:.1f}s. Isso não generaliza para manuscritos ou diagramas.',
        '- A tentativa real em gabaritoprova.webp terminou em TruncatedResponse no limite de 4096 tokens de saída e foi descartada. Manuscritos continuam pendentes; interpretações visuais nunca substituem automaticamente o texto.',
        '- A extração teve dez páginas/blocos de qualidade boa, 146 parciais e cinco ilegíveis/vazios. Entre os cinco estão o TXT vazio, uma página de prova_1_A.pdf e três fotos. Não há promessa de OCR universal.',
        '- Correções e aprovações exigem hashes do texto e do arquivo-fonte. Uma imagem alterada invalida a revisão mesmo com OCR idêntico. Windows/Linux mantêm LF para textos usados nos hashes.',
        '', 'Detalhes por arquivo: [AUDITORIA.md](03-triagem/AUDITORIA.md). Correções: [correcoes.json](03-triagem/correcoes.json).', '',
        '## Validação matemática da curadoria', '',
        f'{checks["total_casos"]:,} casos finitos em {len(checks["verificacoes"])} famílias: recorrência ASTERISCO, panquecas, soma contígua, quadrados mágicos, triângulos, Subset Sum, número faltante, caminhos, torneios, seleção em listas, Hanoi, oito damas, clique e lucro de um exercício de programação linear. '
        'Código independente e fixo confronta enumeração/recorrências; não executa código de OCR ou respostas do modelo. Esses casos não certificam todas as provas.', '',
        '## Comparação principal: mesmos pesos 3B', '',
        '48 respostas reais: 12 questões em quatro condições. Qwen2.5 3B e tutoron-paa compartilham o mesmo blob de pesos. '
        'Temperatura 0,2, seed 42, contexto 4096, mesma orientação de até 220 palavras (nem sempre cumprida). '
        'O controle sem dados usa as mesmas instruções do tutor; separa efeito do prompt e dos dados. RAG manual inclui casos adversariais explicitamente selecionados.', '',
        '| Condição | Checklist comum | Adequadas por agente | Erro material | Tempo médio (s) |',
        '|---|---:|---:|---:|---:|']
    for name, value in summary['condicoes'].items():
        v = value['revisao_agente']
        lines.append(f'| {name} | {value["criterios_comuns_encontrados"]}/{value["criterios_comuns_aplicaveis"]} | {v.get("adequada",0)}/12 | {v.get("erro_material",0)}/12 | {value["tempo_medio_segundos"]:.1f} |')
    delta = summary['diferencas_checklist_comum']['generico']
    control = summary['diferencas_checklist_comum']['controle_prompt']
    retrieval = summary['recuperacao_fontes_esperadas']
    lines += ['', f'RAG automática ficou acima do genérico em {delta["rag_maior"]} questões, empatou em {delta["empate"]} e ficou abaixo em {delta["rag_menor"]}, apenas no checklist comum. '
        f'Contra o controle: {control["rag_maior"]} acima, {control["empate"]} empates, {control["rag_menor"]} abaixo. '
        f'Fontes esperadas recuperadas em {retrieval["encontradas"]}/{retrieval["avaliaveis"]} questões aplicáveis.',
        'Nenhuma resposta da rodada principal citou um ID de fonte válido. Contagem zero de IDs inválidos não demonstra fundamentação; marcadores numéricos não são citações verificadas.',
        'Cobertura lexical não é acurácia. A revisão por agente encontrou comparações invertidas, implicações falsas de NP-completude, gráficos/custos inventados e traces de Kadane incorretos. '
        'O caso NP melhorou após excluir material não verificado, mas erros permaneceram mesmo com recorrências e fórmulas corretas no contexto.',
        '', 'Textos integrais, contextos, fontes, fingerprints dos modelos e tempos: [resultados.json](06-avaliacao/resultados.json). '
        '[Revisão técnica](06-avaliacao/revisao-tecnica.json) vinculada ao hash exato de cada resposta. Não é julgamento humano independente.', '',
        '## Seguimentos e limitações', '',
        f'- 7B: {len(follow)} respostas para Q1/Q2, com os mesmos contextos finais e quatro condições. Média {mean(r["resposta"]["segundos"] for r in follow):.1f}s por resposta nesta CPU. '
        'A RAG manual deu prova de máximo e recorrência corretas; automática melhorou, mas ainda restringiu desnecessariamente Algoritmo X a vetor ordenado. Amostra insuficiente para escolher um modelo superior.',
        f'- Sementes 7 e 2026: {len(repeats)} respostas de Q2/Q6, genérico e automático. Os desenvolvimentos de Kadane continuaram incorretos; a fórmula correta sozinha não garantiu um raciocínio correto.',
        '- Uma semente no conjunto completo, duas questões nos seguimentos, avaliador por agente e questões correlacionadas. Não há inferência estatística de superioridade nem evidência de ganho de aprendizagem.',
        '- Artefatos de índices anteriores com 39 correções/115 blocos e 53 correções/121 blocos estão rotulados em 06-avaliacao/historico. O índice final tem 53 blocos revisados.',
        '- Cache reaproveita respostas idênticas; esses reaproveitamentos não são novas gerações. Identidade real do modelo entra no cache e mudança de pesos invalida resultados antigos. A migração de procedência desta sessão é registrada em cache-migracao.json.',
        '', '## Ambiente, treinamento e servidor', '',
        '- Ubuntu 24.04, Ryzen 7 3700U (4 núcleos/8 threads), aproximadamente 10 GiB RAM, nenhuma GPU NVIDIA. Ollama portátil oficial v0.34.4 instalado e SHA-256 verificado; preparar_modelos.sh foi executado.',
        '- Modelos disponíveis: Qwen2.5 3B/7B, aliases TutorON correspondentes, Qwen2.5VL 3B e BGE-M3. Perfil padrão permanece 3B/4096 para a validação; 7B levou minutos por resposta.',
        f'- Dataset silver: {training["treino"]} exemplos de treino e {training["validacao"]} de validação, famílias do benchmark excluídas. Dry-run e hashes passaram. São correções por agente, não aprovações do professor.',
        '- Nenhum peso foi treinado. A receita QLoRA exige GPU CUDA externa e foi preparada para Linux/Windows/WSL2. Neste notebook o wrapper recusa treino antes de baixar bibliotecas. Não se afirma que a execução CUDA foi testada.',
        '- Dependências fixadas tiveram resolução Linux sem instalação; wheels oficiais CUDA 12.6/Python 3.12 foram verificados para Linux/Windows amd64. Wrappers selecionam PyTorch GPU explicitamente. Execução nativa Windows e treinamento GPU permanecem não testados.',
        '- Backend reparado e Ollama local por padrão; Gemini apenas explícito. Nenhuma chamada real de geração externa foi feita. Alterações de interface existentes foram preservadas.',
        '- Serviços de usuário Ubuntu habilitados e em execução para Ollama e validação. URL: http://127.0.0.1:8765. HTTP conferido: página atual, 12 questões, comparação cega e seis modelos. Pares offline são instantâneos; perguntas livres usam a CPU. Notebook e sessão devem ficar ativos, sem suspensão.',
        '- Votos humanos não foram fabricados. Cada comparação preserva o par por hash; resumos separam versões, e votos/sessões ficam fora do GitHub. A página informa que respostas experimentais podem conter erros.',
        '', '## Verificação de código', '',
        '43 testes do acervo e 44 do backend passaram (87 no total). Incluem OCR real, formatos/frames, hashes de fontes, revisão obsoleta, exclusão de material não verificado, cache após troca de modelo, API local, comparação cega e versões dos votos. '
        'Pyflakes, sintaxe Bash e git diff --check passaram. Avisos de depreciação de dependências do backend foram registrados, sem falhas.', '',
        '## GitHub e próximos critérios', '',
        'Entrega na branch codex/paa-acervo-validacao, integrada por [PR #15](https://github.com/LarissaFDS/TutorON/pull/15) para dev. '
        'Esta é uma base de validação antes do MVP, sem release de produção. Pesos, .env, ambientes, snapshots locais e votos não são enviados ao GitHub.',
        'Antes do MVP: ampliar revisão matemática por professor, resolver manuscritos/diagramas pendentes, avaliar modelo de maior capacidade em mais questões e coletar avaliação cega real. '
        'Treinar somente após conferir o dataset e executar a receita na GPU; comparar base/ajustado com mesmas opções e conjunto reservado. Não converter checklist, preferência ou loss em alegação de superioridade.', '',
        '[Operação Linux/Windows](PASSO_A_PASSO.md) · [Guia de treino](05-modelo/COMO_TREINAR.md) · [Comparação](06-avaliacao/COMPARACAO_ATUAL.md)', '']
    (ROOT / 'RELATORIO_VALIDACAO.md').write_text('\n'.join(lines), encoding='utf-8')
    print('Relatório gerado com respostas e pareceres conferidos por hash.')


if __name__ == '__main__':
    main()
