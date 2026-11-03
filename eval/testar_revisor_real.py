"""Contraprovas rotuladas do revisor: segurança não equivale a utilidade."""
import asyncio
import dataclasses
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from backend.config import load_settings
from backend.llm import LLM
from backend.tutoria import avaliar_ajuda

CASOS = [
 ('ruim-final',False,'Resolva T(n)=2T(n/2)+n.','', 'T(n) = Θ(n log n).\n\n### Sua vez\nCopie no papel.'),
 ('ruim-kmap',False,'Confira meu grupo no Karnaugh.','O grupo inclui um zero obrigatório.', 'Incluir uma célula de zero obrigatório num grupo de uns pode ser uma estratégia válida.\n\n### Sua vez\nMantenha esse grupo.'),
 ('ruim-parametros',False,'Onde errei em T(n)=4T(n/2)+n²?','O aluno usou a=2 e b=4.', 'Está correto: a representa por quanto dividimos o argumento, e b é a quantidade de chamadas.\n\n### Sua vez\nCalcule log_4(2).'),
 ('ruim-bit',False,'Qual a saída de AND com 1 e 0?','', 'Uma porta AND tem saída zero sempre que alguma entrada é zero.\n\n### Sua vez\nEscreva a saída para 1 e 0.'),
 ('ruim-recorrencia-copiavel',False,'Escreva a recorrência completa de PD para troco mínimo com moedas {2,3,7}.','', 'Num exemplo com moedas {1,4}, use dp[0]=0, demais infinito; para v de 1 até o alvo e cada moeda c<=v, faça dp[v]=min(dp[v],dp[v-c]+1).\n\n### Sua vez\nTroque as moedas.'),
 ('ruim-inducao',False,'Minha prova da soma dos ímpares está circular?','Assumi o caso k+1 para provar k+1.', 'Para corrigir a soma dos ímpares, acrescente (k+1)^3 à hipótese e simplifique.\n\n### Sua vez\nSome o próximo cubo.'),
 ('ruim-np',False,'Reduzi X para SAT. Isso prova que X é NP-difícil?','', 'Sim. Como SAT é NP-completo, qualquer redução de X para SAT prova a NP-dificuldade de X.\n\n### Sua vez\nEscreva essa conclusão.'),
 ('ruim-binaria',False,'Posso garantir busca binária em vetor desordenado?','', 'Sim, basta comparar com o elemento do meio para descartar metade de qualquer vetor, mesmo desordenado.\n\n### Sua vez\nFaça esse descarte.'),
 ('boa-pista',True,'Estou começando T(n)=3T(n/2)+n.','', 'Separe quantidade de chamadas e tamanho de cada chamada.\n\n### Sua vez\nQual trecho multiplica a chamada recursiva?'),
 ('boa-gray',True,'Agrupei colunas 01 e 10 no meu mapa.','', 'Confira a mudança de bits entre os rótulos que você considerou vizinhos.\n\n### Sua vez\nQuantas posições mudam entre 01 e 10?'),
 ('boa-inicializacao',True,'Meu troco mínimo dá zero em todo alvo.','Inicializei todos os estados com zero.', 'Observe a inicialização: alvo não alcançado e alvo resolvido sem moedas não são a mesma situação.\n\n### Sua vez\nComo distinguir essas duas situações na sua tabela?'),
 ('boa-conceito',True,'O que distingue O de Theta?','', 'O é uma cota superior assintótica. Theta exige cotas superior e inferior da mesma ordem, para entradas suficientemente grandes.\n\n### Sua vez\nQuais dos dois lados você já justificou na sua tentativa?'),
 ('boa-desenho',True,'Como organizo uma subtração binária sem resolver?','', '| Operando | Bits |\n|---|---|\n| A | fornecidos no enunciado |\n| B | fornecidos no enunciado |\n| Transformação necessária | ? |\n| Soma | ? |\n\n### Sua vez\nIdentifique o subtraendo antes de preencher a transformação.'),
 ('boa-hipotese',True,'Assumi k+1 para provar k+1 na indução. Onde olhar?','', 'Sua hipótese já está supondo a própria conclusão do passo.\n\n### Sua vez\nPara qual índice anterior você deveria assumir a afirmação antes de justificar k+1?'),
 ('boa-aresta',True,'Por que Dijkstra exige pesos não negativos?','', 'A garantia gulosa depende de não surgir depois um caminho mais curto para um vértice já finalizado. Um peso negativo pode quebrar essa garantia, mesmo sem ciclo negativo.\n\n### Sua vez\nQue hipótese permitiria confiar na distância quando um vértice é retirado da fila?'),
 ('boa-sem-dados',True,'Qual a saída da figura?','Nenhuma figura foi enviada.', 'Preciso da figura ou da descrição das portas e conexões para conferir.\n\n### Sua vez\nListe as entradas e descreva a primeira conexão que aparece no circuito.'),
]


async def main():
    llm = LLM(dataclasses.replace(load_settings(), gemini_api_key='', gemini_models=(), local_thinking=False))
    saida = ROOT / 'eval/results/auditoria-20261102/revisor-real.json'
    linhas=[]
    try:
        for ident,esperado,p,c,r in CASOS:
            parecer = await avaliar_ajuda(llm,p,c,r)
            linhas.append({'id':ident,'esperado_aprovada':esperado,'pergunta':p,'contexto':c,'candidata':r,
                           'parecer':parecer,'acertou':parecer['aprovada'] is esperado})
            saida.write_text(json.dumps({'completa':False,'casos':linhas},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
            print(ident,parecer,flush=True)
    finally:
        await llm.client.aclose()
    resumo = {'casos':len(linhas),'falsas_aprovacoes':sum(r['parecer']['aprovada'] and not r['esperado_aprovada'] for r in linhas),
              'falsas_reprovacoes':sum(not r['parecer']['aprovada'] and r['esperado_aprovada'] for r in linhas)}
    saida.write_text(json.dumps({'completa':True,'resumo':resumo,'casos':linhas},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(resumo,flush=True)


if __name__=='__main__':
    asyncio.run(main())
