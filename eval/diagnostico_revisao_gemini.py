"""Reprodução direta do contrato JSON, com dois orçamentos; sem alterar o servidor."""
import asyncio
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import httpx
from backend.config import load_settings
from backend.llm import GEMINI_URL
from backend.tutoria import SISTEMA_REVISOR


async def main():
    s=load_settings()
    p=ROOT/'eval/results/auditoria-20261102/servidor-normal/resultados.json'
    original=json.loads(p.read_text(encoding='utf-8'))['casos'][0]
    modelo=original['registro']['modelo']
    if original['registro'].get('provedor')!='gemini':
        raise SystemExit('A rodada normal não registrou Gemini para reproduzir.')
    pergunta=original['corpo']['pergunta']
    contexto=original['corpo'].get('contexto','')
    candidata=original['registro'].get('resposta_bloqueada') or original['publicada']
    prompt=json.dumps({'pergunta':pergunta,'contexto_e_historico':contexto,'ajuda_candidata':candidata},ensure_ascii=False)
    url=GEMINI_URL.format(model=modelo).replace(':streamGenerateContent?alt=sse',':generateContent')
    resultados=[]
    async with httpx.AsyncClient(timeout=90) as client:
        for orcamento in (512,2048):
            r=await client.post(url,headers={'x-goog-api-key':s.gemini_api_key},json={
                'contents':[{'role':'user','parts':[{'text':prompt}]}],
                'systemInstruction':{'parts':[{'text':SISTEMA_REVISOR}]},
                'generationConfig':{'temperature':0,'maxOutputTokens':orcamento,'responseMimeType':'application/json'}})
            dado={'modelo':modelo,'orcamento_saida':orcamento,'http':r.status_code,'json_valido':False}
            if r.status_code==200:
                payload=r.json();cand=payload.get('candidates',[{}])[0]
                texto=''.join(p.get('text','') for p in cand.get('content',{}).get('parts',[]) if not p.get('thought'))
                dado.update(finishReason=cand.get('finishReason'),uso=payload.get('usageMetadata'),texto=texto)
                try:
                    j=json.loads(texto)
                    dado['json_valido']=type(j.get('aprovada')) is bool and isinstance(j.get('motivo'),str) and bool(j['motivo'].strip())
                except (ValueError,AttributeError):
                    pass
            resultados.append(dado)
            print(json.dumps(dado,ensure_ascii=False),flush=True)
    saida=ROOT/'eval/results/auditoria-20261102/diagnostico-gemini.json'
    saida.write_text(json.dumps({'limite':'Reprodução controlada com contexto curto; não registra o modelo que falhou em cada revisão passada. Não altera a configuração do servidor.','resultados':resultados},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')


if __name__=='__main__':
    asyncio.run(main())
