"""Treino do TutorON em uma única execução (chamado por 3-Treinar.bat).

Etapas:
  1. dados      exporta pares pergunta/solução do acervo curado (02-acervo), separados por família;
                questões reservadas do benchmark nunca entram no treino.
  2. treino     QLoRA (4 bits) sobre o mesmo modelo de base servido pelo Ollama (Qwen3-8B), na GPU.
  3. mescla     aplica o adapter LoRA nos pesos originais, arquivo por arquivo (cabe em 16 GB de RAM).
  4. ollama     importa os pesos mesclados como "tutoron-paa-ft", quantizados em Q4_K_M.
  5. avaliação  compara tutoron-paa (atual) e tutoron-paa-ft nas questões de validação, com a solução
                de referência ao lado e nota de um juiz (Gemini) quando disponível.

O modelo novo NÃO substitui o atual automaticamente. Depois de ler o relatório, para usar:
  TUTORON_MODELO_LOCAL=tutoron-paa-ft  no .env, e reinicie o 1-Iniciar-Servidor.bat.

Uso: python scripts/treinar.py [--passos 60] [--base Qwen/Qwen3-8B] [--so-dados] [--pular-avaliacao]
"""
from __future__ import annotations

import argparse
import asyncio
import gc
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from acervo.common import digest, read_json, write_json  # noqa: E402
from backend.prompts import SISTEMA_TUTOR, prompt_tutor  # noqa: E402

PASTA_DADOS = ROOT / '05-modelo/treino'
PASTA_TRABALHO = ROOT / '.tools/treino'
OLLAMA = ROOT / '.tools/ollama/ollama.exe'
OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://127.0.0.1:11434')
os.environ.setdefault('HF_HOME', str(ROOT / '.tools/hf'))
os.environ.setdefault('HF_HUB_DISABLE_SYMLINKS_WARNING', '1')

# Questões e conceitos usados no benchmark de 06-avaliacao: fora do treino para a avaliação continuar honesta.
RESERVADAS = {'c01', 'c02', 'c05', 'c06', 'c08', 'c09', 'a177bf5bc3c7-q1-1', 'a177bf5bc3c7-q2-2',
              '1a81ca283132-q4-4', '70d6475b28bf-q1-1', '97254bb4a1b8-q1-1', 'd455baef2cdf-q1-1',
              '97254bb4a1b8-q2-2', '97254bb4a1b8-q10-10'}

# Perguntas novas de conferência matemática (respostas conhecidas), além da validação.
SONDAS = [
    {'pergunta': 'Resolva T(n) = 3T(n/4) + n^2 pela árvore de recursão e confirme pelo Teorema Mestre.',
     'referencia': 'Nível i custa 3^i (n/4^i)^2 = (3/16)^i n^2; soma geométrica decrescente, T(n) = Θ(n^2). '
                   'Mestre: a=3, b=4, n^{log_4 3} ≈ n^0,79; f(n)=n^2 é polinomialmente maior e 3(n/4)^2 = (3/16)n^2 ≤ c n^2 '
                   'com c=3/16<1: caso 3, Θ(n^2).'},
    {'pergunta': 'Quantas vezes a linha "x = x + 1" executa em: for i = 1 to n: for j = i to n: x = x + 1? Dê a fórmula fechada.',
     'referencia': 'Para cada i, executa n - i + 1 vezes. Soma de i=1 a n de (n-i+1) = n(n+1)/2 = Θ(n^2).'},
    {'pergunta': 'O guloso por maior moeda falha para moedas {1, 3, 4} e troco 6? Mostre as duas soluções.',
     'referencia': 'Guloso: 4+1+1 = 3 moedas. Ótimo: 3+3 = 2 moedas. Logo o guloso falha.'},
]


def titulo(texto: str) -> None:
    print(f'\n== {texto}', flush=True)


# ---------------------------------------------------------------------------- 1. dados
def preparar_dados() -> dict:
    titulo('1/5 Dados de treino (acervo curado)')
    amostras, reservadas = [], []
    for item in read_json(ROOT / '02-acervo/itens.json', []):
        if item.get('curadoria', {}).get('status') != 'corrigido_por_agente':
            continue
        if item['id'] in RESERVADAS or item['id'].startswith('f38bb8142136'):
            reservadas.append(item['id'])
            continue
        texto = item['texto'].strip()
        enunciado = texto.split('\n', 1)[0].strip()
        fonte = item['fonte_original'].replace('\\', '/').split('/')[-1]
        material = f'[P1] Material de PAA — {fonte}\n(trecho omitido: responda com seu próprio raciocínio)'
        amostras.append({
            'family': item['id'], 'fonte_id': item['id'], 'sha256': item['sha256'],
            'qualidade': 'silver: corrigido por agente; revisão humana pendente',
            'prompt': [{'role': 'system', 'content': SISTEMA_TUTOR},
                       {'role': 'user', 'content': prompt_tutor(f'Resolva passo a passo: {enunciado}', material)}],
            'completion': [{'role': 'assistant', 'content': texto}],
            'pergunta': enunciado, 'referencia': texto,
        })
    amostras.sort(key=lambda s: digest(s['family']))
    n_val = max(2, len(amostras) // 5)
    grupos = {'validacao': amostras[:n_val], 'treino': amostras[n_val:]}
    PASTA_DADOS.mkdir(parents=True, exist_ok=True)
    for nome, linhas in grupos.items():
        (PASTA_DADOS / f'{nome}.jsonl').write_text(''.join(json.dumps(s, ensure_ascii=False) + '\n' for s in linhas),
                                                    encoding='utf-8', newline='\n')
    manifesto = {'gerado_em': datetime.now().isoformat(timespec='seconds'), 'sistema': platform.platform(),
                 'treino': len(grupos['treino']), 'validacao': len(grupos['validacao']),
                 'familias_reservadas_benchmark': sorted(reservadas),
                 'dados': {n: digest((PASTA_DADOS / f'{n}.jsonl').read_bytes()) for n in grupos},
                 'limite': 'Dataset pequeno e corrigido por agente: serve para validar o processo de treino; '
                           'ganho real exige mais soluções revisadas por humanos.'}
    write_json(PASTA_DADOS / 'manifesto.json', manifesto)
    print(f'   {manifesto["treino"]} exemplos de treino, {manifesto["validacao"]} de validação, '
          f'{len(reservadas)} reservados para o benchmark.')
    return grupos


# ---------------------------------------------------------------------------- 2. treino
def liberar_gpu() -> None:
    """Descarrega os modelos do Ollama: o treino precisa de quase toda a VRAM."""
    import httpx
    try:
        for m in httpx.get(OLLAMA_URL + '/api/ps', timeout=5).json().get('models', []):
            httpx.post(OLLAMA_URL + '/api/generate', json={'model': m['name'], 'keep_alive': 0}, timeout=30)
            print(f'   descarregado da GPU: {m["name"]}')
    except httpx.HTTPError:
        pass


def treinar(grupos: dict, base: str, passos: int, rank: int, seq: int) -> Path:
    titulo(f'2/5 Treino QLoRA de {base} ({passos} passos)')
    import torch
    from datasets import Dataset
    from peft import LoraConfig, prepare_model_for_kbit_training
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    from trl import SFTConfig, SFTTrainer

    if not torch.cuda.is_available():
        raise SystemExit('GPU NVIDIA com CUDA não encontrada.')
    liberar_gpu()
    saida = PASTA_TRABALHO / 'adapter'
    tokenizer = AutoTokenizer.from_pretrained(base)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    modelo = AutoModelForCausalLM.from_pretrained(
        base, device_map={'': 0}, dtype=torch.bfloat16,
        quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4',
                                               bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16))
    modelo = prepare_model_for_kbit_training(modelo, use_gradient_checkpointing=True)
    print(f'   VRAM após carregar: {torch.cuda.memory_allocated() / 2**30:.1f} GB')

    def ds(linhas):
        return Dataset.from_list([{'prompt': r['prompt'], 'completion': r['completion']} for r in linhas])

    config = SFTConfig(
        output_dir=str(saida), max_steps=passos, max_length=seq, per_device_train_batch_size=1,
        per_device_eval_batch_size=1, gradient_accumulation_steps=4, learning_rate=1e-4, lr_scheduler_type='cosine',
        warmup_steps=max(1, passos // 10), gradient_checkpointing=True, completion_only_loss=True, bf16=True,
        optim='paged_adamw_8bit', eval_strategy='steps', eval_steps=max(5, passos // 4), save_strategy='no',
        logging_steps=5, report_to='none', seed=42, dataloader_pin_memory=False)
    treinador = SFTTrainer(
        model=modelo, processing_class=tokenizer, args=config, train_dataset=ds(grupos['treino']),
        eval_dataset=ds(grupos['validacao']),
        peft_config=LoraConfig(r=rank, lora_alpha=2 * rank, lora_dropout=0.05, bias='none', task_type='CAUSAL_LM',
                               target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj']))
    inicio = time.monotonic()
    resultado = treinador.train()
    avaliacao = treinador.evaluate()
    treinador.save_model(str(saida))
    write_json(PASTA_TRABALHO / 'resultado-treino.json', {
        'base': base, 'passos': passos, 'rank': rank, 'max_length': seq, 'minutos': round((time.monotonic() - inicio) / 60, 1),
        'metricas_treino': resultado.metrics, 'metricas_validacao': avaliacao,
        'pico_vram_gb': round(torch.cuda.max_memory_allocated() / 2**30, 2),
        'aviso': 'Loss menor não prova que o tutor melhorou: leia o relatório de avaliação.'})
    print(f'   loss de validação: {avaliacao.get("eval_loss"):.3f}; pico de VRAM '
          f'{torch.cuda.max_memory_allocated() / 2**30:.1f} GB; {(time.monotonic() - inicio) / 60:.1f} min')
    del treinador, modelo
    gc.collect()
    torch.cuda.empty_cache()
    return saida


# ---------------------------------------------------------------------------- 3. mescla
def mesclar(base: str, adapter: Path) -> Path:
    """W' = W + (alpha/r)·B·A, arquivo por arquivo, sem carregar o modelo inteiro na RAM."""
    titulo('3/5 Mesclando o adapter nos pesos originais')
    import torch
    from huggingface_hub import snapshot_download
    from safetensors import safe_open
    from safetensors.torch import save_file

    origem = Path(snapshot_download(base, allow_patterns=['*.json', '*.safetensors', '*.txt', 'tokenizer*']))
    destino = PASTA_TRABALHO / 'mesclado'
    if destino.exists():
        shutil.rmtree(destino)
    destino.mkdir(parents=True)
    cfg = json.loads((adapter / 'adapter_config.json').read_text(encoding='utf-8'))
    escala = cfg['lora_alpha'] / cfg['r']
    lora = {}
    with safe_open(str(adapter / 'adapter_model.safetensors'), 'pt') as f:
        for chave in f.keys():
            lora[chave] = f.get_tensor(chave)
    pares = {}
    for chave in lora:
        if '.lora_A.' in chave:
            alvo = chave.replace('base_model.model.', '', 1).replace('.lora_A.weight', '.weight')
            pares[alvo] = (lora[chave], lora[chave.replace('.lora_A.', '.lora_B.')])
    aplicados = 0
    dispositivo = 'cuda' if torch.cuda.is_available() else 'cpu'
    for arquivo in sorted(origem.glob('*.safetensors')):
        tensores = {}
        with safe_open(str(arquivo), 'pt') as f:
            metadados = f.metadata()
            for chave in f.keys():
                w = f.get_tensor(chave)
                if chave in pares:
                    a, b = pares[chave]
                    delta = (b.to(dispositivo, torch.float32) @ a.to(dispositivo, torch.float32)) * escala
                    w = (w.to(dispositivo, torch.float32) + delta).to(torch.bfloat16).cpu()
                    aplicados += 1
                tensores[chave] = w.contiguous()
        save_file(tensores, str(destino / arquivo.name), metadata=metadados or {'format': 'pt'})
        print(f'   {arquivo.name}')
        del tensores
        gc.collect()
    if aplicados != len(pares):
        raise SystemExit(f'Só {aplicados} de {len(pares)} camadas LoRA encontraram o peso original. Base errada?')
    for extra in origem.iterdir():
        if extra.suffix != '.safetensors' and extra.is_file():
            shutil.copy2(extra, destino / extra.name)
    print(f'   {aplicados} matrizes atualizadas.')
    return destino


# ---------------------------------------------------------------------------- 4. ollama
def importar_no_ollama(pasta: Path, nome: str) -> None:
    titulo(f'4/5 Importando no Ollama como {nome} (Q4_K_M)')
    atual = subprocess.run([str(OLLAMA), 'show', 'tutoron-paa', '--modelfile'], capture_output=True, text=True,
                           encoding='utf-8', check=True).stdout
    linhas = [ln for ln in atual.splitlines() if not ln.startswith('FROM ') and not ln.startswith('#')]
    modelfile = pasta / 'Modelfile'
    modelfile.write_text(f'FROM {pasta}\n' + '\n'.join(linhas) + '\n', encoding='utf-8')
    env = {**os.environ, 'OLLAMA_MODELS': str(ROOT / '.tools/models'), 'OLLAMA_HOST': '127.0.0.1:11434'}
    subprocess.run([str(OLLAMA), 'create', nome, '-f', str(modelfile), '--quantize', 'q4_K_M'], check=True, env=env)


# ---------------------------------------------------------------------------- 5. avaliação
JUIZ = """Você corrige respostas de alunos monitores de Projeto e Análise de Algoritmos.
Compare a RESPOSTA com a SOLUÇÃO DE REFERÊNCIA e responda só com JSON:
{"nota": 0, 1 ou 2, "erro_matematico": true/false, "motivo": "uma frase"}
2 = correta e completa; 1 = parcialmente correta; 0 = errada ou com erro matemático grave."""


async def avaliar(grupos: dict, nome: str) -> Path:
    titulo('5/5 Avaliação: tutoron-paa (atual) x ' + nome)
    from backend.config import load_settings
    from backend.llm import LLM, AllUnavailable, Model

    settings = load_settings()
    llm = LLM(settings)
    casos = [{'pergunta': s['pergunta'], 'referencia': s['referencia'], 'origem': 'validação do acervo'} for s in grupos['validacao']]
    casos += [{**s, 'origem': 'sonda matemática'} for s in SONDAS]
    linhas = [f'# Avaliação do treino — {datetime.now():%d/%m/%Y %H:%M}', '',
              f'Modelos: `tutoron-paa` (atual) e `{nome}` (treinado). Mesmo prompt, sem material (testa o modelo, não a RAG).',
              'Nota do juiz (Gemini, comparando com a referência): 2 correta, 1 parcial, 0 errada. Leia as respostas: o juiz também erra.', '']
    placar = {'tutoron-paa': [], nome: []}
    gemini = [m for m in llm.cascade() if m.provider == 'gemini']
    for i, caso in enumerate(casos, 1):
        print(f'   [{i}/{len(casos)}] {caso["pergunta"][:70]}')
        linhas += [f'## {i}. {caso["pergunta"]}', '', f'*Origem: {caso["origem"]}*', '', '**Referência:**', '',
                   caso['referencia'], '']
        for modelo in ('tutoron-paa', nome):
            prompt = prompt_tutor(caso['pergunta'], 'Nenhum trecho do material foi encontrado para esta pergunta.')
            try:
                r = await llm.complete(SISTEMA_TUTOR, prompt, models=[Model('ollama', modelo)])
                resposta, segundos = r.text, r.seconds
            except AllUnavailable:
                resposta, segundos = '(sem resposta)', 0
            julgamento = {}
            if gemini:
                try:
                    j = await llm.complete(JUIZ, f'PERGUNTA:\n{caso["pergunta"]}\n\nSOLUÇÃO DE REFERÊNCIA:\n{caso["referencia"]}'
                                                 f'\n\nRESPOSTA:\n{resposta}', models=gemini)
                    julgamento = json.loads(j.text[j.text.find('{'):j.text.rfind('}') + 1])
                except (AllUnavailable, ValueError):
                    julgamento = {}
            if 'nota' in julgamento:
                placar[modelo].append(int(julgamento['nota']))
            nota = f'nota {julgamento["nota"]}/2 — {julgamento.get("motivo", "")}' if 'nota' in julgamento else 'sem juiz disponível'
            linhas += [f'### {modelo} ({segundos:.0f} s) — {nota}', '', resposta, '']
    await llm.client.aclose()
    resumo = ['## Placar', '', '| Modelo | Nota média (0–2) | Casos julgados |', '|---|---:|---:|']
    for modelo, notas in placar.items():
        media = f'{sum(notas) / len(notas):.2f}' if notas else '—'
        resumo.append(f'| {modelo} | {media} | {len(notas)} |')
    linhas[5:5] = resumo + ['']
    relatorio = PASTA_DADOS / f'avaliacao-{datetime.now():%Y%m%d-%H%M}.md'
    relatorio.write_text('\n'.join(linhas) + '\n', encoding='utf-8', newline='\n')
    print('\n'.join(resumo))
    return relatorio


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--passos', type=int, default=60)
    parser.add_argument('--base', default=os.environ.get('TUTORON_TREINO_BASE', 'Qwen/Qwen3-8B'))
    parser.add_argument('--nome', default='tutoron-paa-ft')
    parser.add_argument('--rank', type=int, default=16)
    parser.add_argument('--seq', type=int, default=1536, help='tamanho máximo de cada exemplo, em tokens')
    parser.add_argument('--so-dados', action='store_true')
    parser.add_argument('--pular-avaliacao', action='store_true')
    args = parser.parse_args()

    grupos = preparar_dados()
    if args.so_dados:
        return
    PASTA_TRABALHO.mkdir(parents=True, exist_ok=True)
    adapter = treinar(grupos, args.base, args.passos, args.rank, args.seq)
    mesclado = mesclar(args.base, adapter)
    importar_no_ollama(mesclado, args.nome)
    shutil.rmtree(mesclado, ignore_errors=True)  # 16 GB: o Ollama já guardou a versão quantizada
    if not args.pular_avaliacao:
        relatorio = asyncio.run(avaliar(grupos, args.nome))
        print(f'\nRelatório: {relatorio}')
    print(f'\nPronto. O modelo atual não foi alterado. Para usar o novo, coloque no .env:\n'
          f'   TUTORON_MODELO_LOCAL={args.nome}\ne reinicie o 1-Iniciar-Servidor.bat.')


if __name__ == '__main__':
    main()
