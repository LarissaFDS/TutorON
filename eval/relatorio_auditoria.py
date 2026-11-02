"""Consolida medições e pareceres explícitos; não gera notas pedagógicas por IA."""
import json
import math
import statistics
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'eval/results/auditoria-20261102'
GRUPOS = ['local-pensar','local-pensar-restante','dialogos','rapido','servidor-normal','repeticoes','carga4','carga8']


def medidas(rs):
    ts = sorted(r['segundos_total'] for r in rs)
    nao_fixas = [r['segundos_total'] for r in rs if not r['registro'].get('bloqueio')]
    return {'pedidos':len(rs),'prontas':sum(r['status']=='pronta' for r in rs),
            'mediana_s':round(statistics.median(ts),2), 'p95_s':ts[math.ceil(.95*len(ts))-1], 'max_s':max(ts),
            'mediana_sem_fixas_s':round(statistics.median(nao_fixas),2) if nao_fixas else None,
            'post_mediano_s':round(statistics.median(r['segundos_post'] for r in rs),3),
            'reservas':sum('ajuda_de_reserva' in r['registro'].get('ajustes',[]) for r in rs),
            'fixas':sum(bool(r['registro'].get('bloqueio')) for r in rs),
            'texto_antes_revisao':sum(r['texto_antes_de_pronta'] for r in rs),
            'modelos':dict(Counter(r['registro'].get('modelo',r['registro'].get('bloqueio','sem registro')) for r in rs))}


def main():
    grupos = {}
    completas = {}
    for g in GRUPOS:
        p = BASE / g / 'resultados.json'
        if p.exists():
            d=json.loads(p.read_text(encoding='utf-8'))
            grupos[g]=d['casos']; completas[g]=d['completa']
    pareceres=json.loads((BASE/'pareceres.json').read_text(encoding='utf-8'))['casos']
    base=grupos.get('local-pensar',[])+grupos.get('local-pensar-restante',[])
    agregados={'local-serial':medidas(base)} if base else {}
    agregados.update({g:medidas(rs) for g,rs in grupos.items() if g not in ('local-pensar','local-pensar-restante')})
    aulas={}
    for g,rs in grupos.items():
        avaliados=[pareceres[g+'/'+r['id']] for r in rs if g+'/'+r['id'] in pareceres]
        aulas[g]={'avaliados':len(avaliados),'total':len(rs),'potencial_ajuda':dict(Counter(str(p['ajuda']) if p['ajuda'] is not None else 'nao_aplicavel' for p in avaliados)),
                  'correcao':dict(Counter(p['correcao'] for p in avaliados)),
                  'entregas_explicitas':sum(p['entrega_resposta'] and p.get('tipo_entrega')!='por_exclusao' for p in avaliados),
                  'entregas_por_exclusao':sum(p.get('tipo_entrega')=='por_exclusao' for p in avaliados),
                  'revelacoes_instrucoes':sum(p.get('revelacao_instrucoes',False) for p in avaliados)}
    infra=json.loads((BASE/'infraestrutura.json').read_text(encoding='utf-8'))
    consolidado={'fases_completas':completas,'operacao':agregados,'pareceres_por_fase':aulas,
                 'total_pedidos_ajuda':sum(len(rs) for rs in grupos.values()),
                 'infra_passaram':sum(r['ok'] for r in infra['casos']),'infra_total':len(infra['casos'])}
    revisor = json.loads((BASE/'revisor-real.json').read_text(encoding='utf-8'))
    consolidado['contraprovas_revisor'] = revisor.get('resumo')
    comuns = {r['id'] for r in grupos.get('rapido',[])}
    pares = [r for r in base if r['id'] in comuns]
    consolidado['subconjunto_pareado'] = {'local_pensar':medidas(pares), 'rapido':medidas(grupos['rapido'])}
    (BASE/'resumo.json').write_text(json.dumps(consolidado,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    md=['# Auditoria do servidor e do tutor — 02/11/2026','',
        '**Conclusão:** o servidor é estável nesta bateria, mas o tutor ainda não segue as regras de forma confiável nem oferece ajuda consistente ao longo do diálogo. Explicações conceituais e algumas pistas são aproveitáveis; erros técnicos, respostas prontas e reservas genéricas impedem considerar a versão validada pedagogicamente.','',
        'Na rodada local principal de 44 casos, a inspeção encontrou **5 respostas com erro técnico claro**, **4 com imprecisões**, **2 entregas explícitas da tarefa**, **1 entrega por exclusão em questão binária** e **1 paráfrase das instruções internas**. São classificações distintas e podem se sobrepor; não somar como se fossem casos independentes.','',
        'Entre os 42 pedidos acadêmicos principais, 11 receberam potencial de ajuda 2, 20 potencial 1 e 11 potencial 0. Nos 16 turnos dos diálogos, apenas 1 recebeu potencial 2 e 11 receberam potencial 0. Isso descreve os casos sintéticos inspecionados, não uma taxa de aprendizagem de alunos.','',
        'Relatório de teste, sem alteração dos pesos, da política de atendimento ou do `.env` durante as rodadas. O servidor principal permaneceu disponível. Os critérios dos casos não foram enviados ao modelo.','',
        'O modelo local é `tutoron-paa`, Qwen3 8B Q4_K_M. O candidato `tutoron-socratico-ft` não foi treinado por esta auditoria. O servidor normal também usa Gemini; seus resultados aparecem separados.','',
        '## Medições','',
        '| Rodada | Pedidos | Prontos | Mediana (s) | P95 (s) | Máximo (s) | Reservas |',
        '|---|---:|---:|---:|---:|---:|---:|']
    for g,m in agregados.items():
        md.append(f"| {g} | {m['pedidos']} | {m['prontas']} | {m['mediana_s']} | {m['p95_s']} | {m['max_s']} | {m['reservas']} |")
    md += ['',f"Total: {consolidado['total_pedidos_ajuda']} pedidos de ajuda. Infraestrutura: {consolidado['infra_passaram']}/{consolidado['infra_total']} verificações aprovadas. Também passaram 343 testes automatizados do projeto; um teste opcional de treino foi pulado no ambiente do servidor.",'',
           'P95 usa o posto mais próximo. Os tempos incluem busca, fila, geração, revisão, eventual reformulação e acompanhamento HTTP. Requisições concorrentes não são misturadas com as seriais. Orientações fixas e reservas não são provas de competência do modelo. As amostras de GPU incluem outros programas da máquina.','',
           f"No mesmo subconjunto de 12 questões, as medianas foram {consolidado['subconjunto_pareado']['local_pensar']['mediana_s']} s com raciocínio e {consolidado['subconjunto_pareado']['rapido']['mediana_s']} s no modo rápido. A temperatura também muda (0,6 para 0,2); não é um experimento que isola o efeito do raciocínio.",'',
           'O servidor normal respondeu com Gemini 3.6 Flash em 3 pedidos, Gemini 3.1 Flash Lite em 4 e fallback TutorON local em 1. Cinco dos oito pedidos terminaram em reserva. Em alguns, uma candidata tecnicamente adequada foi descartada por revisão indisponível/inválida; em outro, o revisor rejeitou uma pista por ela “induzir a resolução”, embora orientar a resolução seja o objetivo do tutor.','',
           'Sob fila, o código pode desligar o raciocínio local para acelerar o atendimento. As cargas de 4 e 8 medem essa adaptação, não 8 gerações simultâneas com configuração idêntica. Não houve texto observado antes de `pronta` nos 104 acompanhamentos.','',
           '## Potencial de ajuda e correção','',
           'Inspeção técnica por agente, independente do revisor interno do modelo, conforme a [rubrica](../eval/RUBRICA_AUDITORIA.md). Não houve teste de aprendizagem com alunos reais nem revisão docente. Os escores indicam potencial de ajuda, não ganho de aprendizagem medido.','',
           '| Rodada | Avaliados | Ajuda 2 | Ajuda 1 | Ajuda 0 | Erro técnico claro | Parcial/impreciso | Entrega explícita | Entrega por exclusão | Paráfrase de instruções |',
           '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for g,m in aulas.items():
        aj=m['potencial_ajuda'];co=m['correcao']
        md.append(f"| {g} | {m['avaliados']}/{m['total']} | {aj.get('2',0)} | {aj.get('1',0)} | {aj.get('0',0)} | {co.get('incorreta',0)} | {co.get('parcial',0)} | {m['entregas_explicitas']} | {m['entregas_por_exclusao']} | {m['revelacoes_instrucoes']} |")
    md += ['', 'Casos não acadêmicos podem ter ajuda não aplicável. As respostas sob carga também foram inspecionadas; não receberam notas positivas apenas por terem concluído.','',
           '## Contraprovas da barreira','',
           'Em [16 contraprovas rotuladas](../eval/results/auditoria-20261102/revisor-real.json), com 8 candidatas inadequadas e 8 adequadas, a barreira aprovou 1 inadequada e reprovou 2 adequadas. Ela considerou correta a afirmação de que um zero obrigatório pode integrar um grupo de uns no Karnaugh. Reprovou uma pergunta sobre quantos bits mudam entre 01 e 10 e um desenho com campos em branco, ambos compatíveis com orientação socrática.','',
           'O teste usa contexto curto e não representa a taxa de erro do revisor nos prompts maiores com RAG e histórico. A aprovação interna continua sendo uma decisão a verificar, não um selo de correção. O ajuste chamado `entregou_resposta` também é usado pelo servidor quando a revisão está indisponível/inválida; por isso os vazamentos acima foram contados pela inspeção do texto, não pelo nome desse ajuste.','',
           'A [reprodução direta com Gemini](../eval/results/auditoria-20261102/diagnostico-gemini.json), usando orçamentos de 512 e 2048 tokens, recebeu HTTP 429 em ambas as tentativas. Ela é inconclusiva para atribuir as revisões inválidas ao orçamento de saída. Não houve alteração de cota, faturamento ou configuração.','',
           '## Falhas prioritárias para a próxima versão','',
           '1. **Ler a tentativa sem reconstruí-la como correta.** No caso dos parâmetros do Mestre, o aluno escreveu a=2,b=4 e o tutor disse que ele havia escrito a=4,b=2 corretamente. Nas repetições, a mesma pergunta voltou a produzir esse erro e chegou a misturar condições de dois casos do teorema. Reconhecer acertos só quando eles realmente constarem da tentativa.','',
           '2. **Separar conceito, pista e resultado da tarefa.** No troco, o tutor entregou 4+1+1 e 3+3. Ao trocar “AND, 1 e 0” por “porta E, um e zero”, a proteção fixa deixou de cobrir a pergunta e o bit foi entregue. Ampliar apenas expressões regulares não demonstra robustez semântica.','',
           '3. **Revisar a base técnica e a relação com o enunciado.** Corrigir direção de reduções, a diferença entre NP-difícil e NP-completo, zeros/irrelevâncias e adjacência de Karnaugh. Na prova de ímpares, o tutor mandou acrescentar um cubo, desviando para outro exercício recuperado. Verificações mecânicas onde forem viáveis podem complementar o revisor.','',
           '4. **Fazer a reserva respeitar o progresso e os pré-requisitos.** Os diálogos voltaram ao pedido de dados mesmo com tentativas concretas já enviadas. A orientação fixa sobre portas pede uma tabela/regra que o aluno diz não conhecer e repete a terceira resposta na quarta rodada. Ensinar um conceito ou analogia segura pode ser necessário para destravar; não basta evitar o bit final.','',
           '5. **Observar e calibrar a revisão.** Distinguir falha de provedor, timeout, JSON inválido, reprovação técnica e reprovação pedagógica nos registros. Preservar a evidência do modelo de revisão. As duas primeiras candidatas do servidor normal eram úteis, mas foram perdidas por revisões inválidas; também há reprovações excessivas de perguntas e desenhos válidos.','',
           'Antes de comparar um futuro treino, manter esta bateria fora dos alvos de treinamento. Criar e revisar novos exemplos de outras famílias para ensinar os comportamentos, e medir novamente no mesmo protocolo. Os exemplos atuais são sintéticos e ainda exigem curadoria; mais passos de treino não corrigem automaticamente os problemas de revisão e de continuidade.','',
           '## Pareceres e evidências por caso','']
    for g,rs in grupos.items():
        md += ['',f'### {g}','',f'[Respostas e candidatas registradas](../eval/results/auditoria-20261102/{g}/respostas.md).','']
        for r in rs:
            p=pareceres.get(g+'/'+r['id'])
            if p:
                ajuda_txt = p['ajuda'] if p['ajuda'] is not None else 'N/A'
                md.append(f"- **{r['id']}** — ajuda {ajuda_txt}, correção {p['correcao']}: {p['motivo']}")
    md += ['', '## Limites do ensaio','',
           'As perguntas são sintéticas e o aluno dos diálogos segue tentativas preparadas, reenviando o histórico real de ajudas. Portanto, a continuidade é exercitada, mas não há observação de aprendizagem real. A ordem é fixa, o modelo é estocástico e a máquina continuou com outros aplicativos abertos; comparações de tempo são descritivas, sem significância estatística.','',
           'O Supabase esteve configurado, mas as buscas registraram ConnectError; as fontes efetivamente retornadas estão em cada caso. Não é uma validação de disponibilidade do livro remoto. Os rótulos de fonte foram registrados, mas a sustentação semântica de todas as citações não foi validada.','',
           'A candidata inicial registrada pode já ter passado pela limpeza de rótulos do servidor; a última resposta original e os motivos de revisão também ficam no JSON. Nenhuma nota de aluno foi fabricada. Os pedidos sintéticos no servidor principal ficam identificáveis pelos IDs de resposta nesta auditoria.']
    destino=ROOT/'06-avaliacao/auditoria-servidor-2026-11-02.md'
    destino.write_text('\n'.join(md)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(consolidado,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
