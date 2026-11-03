"""Treino do TutorON em uma única execução (chamado por 3-Treinar.bat).

Etapas:
  1. dados      exporta exemplos socráticos autorais de PAA e SD, separados por família;
                questões reservadas do benchmark nunca entram no treino.
  2. treino     QLoRA (4 bits) sobre o mesmo modelo de base servido pelo Ollama (Qwen3-8B), na GPU.
  3. mescla     aplica o adapter LoRA nos pesos originais, arquivo por arquivo (cabe em 16 GB de RAM).
  4. ollama     converte para GGUF (llama.cpp), quantiza em Q4_K_M e importa como "tutoron-socratico-ft".
  5. avaliação  compara tutoron-paa (atual) e tutoron-socratico-ft em casos reservados de orientação, com respostas brutas, bloqueios e revisão humana pendente.

O modelo novo NÃO substitui o atual automaticamente. Depois de ler o relatório, para usar:
  TUTORON_MODELO_LOCAL=tutoron-socratico-ft  no .env, e reinicie o 1-Iniciar-Servidor.bat.

Uso: python scripts/treinar.py [--passos 60] [--base Qwen/Qwen3-8B] [--so-dados] [--verificar] [--so-avaliar]
"""
from __future__ import annotations

import argparse
import asyncio
import gc
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from acervo.common import write_json  # noqa: E402

PASTA_DADOS = ROOT / '05-modelo/socratico/preparado'
PASTA_TRABALHO = ROOT / '.tools/treino-socratico'
OLLAMA = ROOT / '.tools/ollama/ollama.exe'
OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://127.0.0.1:11434')
os.environ.setdefault('HF_HOME', str(ROOT / '.tools/hf'))
os.environ.setdefault('HF_HUB_DISABLE_SYMLINKS_WARNING', '1')

def titulo(texto: str) -> None:
    print(f'\n== {texto}', flush=True)


# ---------------------------------------------------------------------------- 1. dados
def preparar_dados() -> dict:
    titulo('1/5 Dados socráticos (PAA + Sistemas Digitais)')
    from scripts.dados_socraticos import preparar
    return preparar(PASTA_DADOS)


# ---------------------------------------------------------------------------- 2. treino
def liberar_gpu() -> None:
    """Descarrega os modelos do Ollama: o treino precisa de quase toda a VRAM."""
    import httpx
    try:
        estado = httpx.get(OLLAMA_URL + '/api/ps', timeout=5)
        estado.raise_for_status()
        for m in estado.json().get('models', []):
            r = httpx.post(OLLAMA_URL + '/api/generate', json={'model': m['name'], 'keep_alive': 0}, timeout=180)
            r.raise_for_status()
            print(f'   descarregado da GPU: {m["name"]}')
    except httpx.ConnectError:
        pass
    except httpx.HTTPError as exc:
        raise SystemExit('Não foi possível liberar a GPU do Ollama. Feche os pedidos locais e tente novamente.') from exc


def tokenizar(tokenizer, linhas: list[dict], seq: int) -> list[dict]:
    """Prompt mascarado (-100): a perda conta só a resposta do tutor.

    O Qwen3 insere um bloco de raciocínio vazio (<think></think>) antes da resposta. Ele fica
    fora da perda: se o modelo aprendesse a gerá-lo, pararia de raciocinar antes de responder,
    e o raciocínio é justamente o que evita os erros de conta.
    """
    exemplos = []
    for r in linhas:
        prompt = tokenizer.apply_chat_template(r['prompt'], tokenize=False, add_generation_prompt=True)
        completo = tokenizer.apply_chat_template(r['prompt'] + r['completion'], tokenize=False)
        if not completo.startswith(prompt):
            raise SystemExit('O template de chat não mantém o prompt como prefixo; confira a base escolhida.')
        vazio = '<think>\n\n</think>\n\n'
        if completo[len(prompt):].startswith(vazio):
            prompt += vazio
        ids_prompt = tokenizer(prompt, add_special_tokens=False)['input_ids']
        ids = tokenizer(completo, add_special_tokens=False)['input_ids']
        if len(ids) > seq:
            raise SystemExit(f"Exemplo {r.get('id', '?')} tem {len(ids)} tokens, acima de --seq {seq}. "
                             "Nenhuma resposta será cortada silenciosamente; aumente --seq.")
        rotulos = [-100] * min(len(ids_prompt), len(ids)) + ids[len(ids_prompt):]
        if any(x != -100 for x in rotulos):
            exemplos.append({'input_ids': ids, 'attention_mask': [1] * len(ids), 'labels': rotulos})
    if not exemplos:
        raise SystemExit('Nenhum exemplo tem tokens de resposta para treinar.')
    return exemplos


def verificar_tokenizacao(grupos, base, seq, *, destino=None):
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(base)
    resumo = {}
    for nome, linhas in grupos.items():
        tokens = tokenizar(tokenizer, linhas, seq)
        resumo[nome] = {'exemplos': len(tokens), 'max_tokens': max(len(r['input_ids']) for r in tokens),
                        'min_tokens_resposta': min(sum(x != -100 for x in r['labels']) for r in tokens)}
    write_json((destino or PASTA_DADOS) / 'preflight-tokens.json', {'base': base, 'seq': seq, 'splits': resumo})
    print('   Tokenização sem cortes: ' + json.dumps(resumo, ensure_ascii=False))
    return resumo


def perda_so_resposta(modelo, entradas, num_items_in_batch=None):
    """Projeta no vocabulário só as posições que predizem a ajuda, não o prompt.

    Mesmo objetivo causal mascarado, com muito menos memória: o vocabulário do
    Qwen tem 151 mil tokens. A posição k-1 prediz o rótulo na posição k.
    """
    import torch
    from torch.nn import functional as F
    labels = entradas['labels']
    supervisionadas = labels.ne(-100).any(dim=0).nonzero().flatten()
    if supervisionadas.numel() == 0 or supervisionadas[0].item() == 0:
        raise ValueError('É necessário um prompt e ao menos um token de resposta supervisionado.')
    primeira = supervisionadas[0].item()
    posicoes = torch.arange(primeira - 1, labels.shape[1] - 1, device=labels.device)
    saida = modelo(**{k: v for k, v in entradas.items() if k != 'labels'}, logits_to_keep=posicoes)
    logits = saida.logits.float().reshape(-1, saida.logits.shape[-1])
    alvos = labels[:, primeira:].reshape(-1).to(logits.device)
    perda = F.cross_entropy(logits, alvos, ignore_index=-100, reduction='sum')
    divisor = num_items_in_batch if num_items_in_batch is not None else alvos.ne(-100).sum()
    return perda / divisor, saida


def treinar(grupos: dict, base: str, passos: int, rank: int, seq: int, *, acumulacao: int = 4) -> Path:
    titulo(f'2/5 Treino QLoRA de {base} ({passos} passos)')
    import torch
    from datasets import Dataset
    from peft import LoraConfig, get_peft_model
    from transformers import (AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, DataCollatorForSeq2Seq,
                              Trainer, TrainingArguments)

    class TrainerSocratico(Trainer):
        def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
            loss, outputs = perda_so_resposta(model, inputs, num_items_in_batch)
            return (loss, outputs) if return_outputs else loss

    if not torch.cuda.is_available():
        raise SystemExit('GPU NVIDIA com CUDA não encontrada.')
    if shutil.disk_usage(ROOT).free < 35 * 2**30:
        raise SystemExit('São necessários pelo menos 35 GB livres para treino, mescla e conversão GGUF.')
    verificar_tokenizacao(grupos, base, seq, destino=PASTA_TRABALHO)
    liberar_gpu()
    saida = PASTA_TRABALHO / 'adapter'
    tokenizer = AutoTokenizer.from_pretrained(base)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    treino, validacao = tokenizar(tokenizer, grupos['treino'], seq), tokenizar(tokenizer, grupos['validacao'], seq)
    print(f'   tokens por exemplo: até {max(len(e["input_ids"]) for e in treino + validacao)} (limite {seq})')
    modelo = AutoModelForCausalLM.from_pretrained(
        base, device_map={'': 0}, dtype=torch.bfloat16,
        quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4',
                                               bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16))
    # Sem prepare_model_for_kbit_training: ele converte as embeddings (151 mil tokens) para float32
    # e estoura os 8 GB da GPU. Checkpointing + gradiente na entrada bastam para o LoRA.
    modelo.gradient_checkpointing_enable(gradient_checkpointing_kwargs={'use_reentrant': False})
    modelo.enable_input_require_grads()
    modelo.config.use_cache = False
    modelo = get_peft_model(modelo, LoraConfig(
        r=rank, lora_alpha=2 * rank, lora_dropout=0.05, bias='none', task_type='CAUSAL_LM',
        target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj']))
    print(f'   VRAM após carregar: {torch.cuda.memory_allocated() / 2**30:.1f} GB')

    argumentos = TrainingArguments(
        output_dir=str(saida), max_steps=passos, per_device_train_batch_size=1, per_device_eval_batch_size=1,
        gradient_accumulation_steps=acumulacao, learning_rate=5e-5, lr_scheduler_type='cosine',
        warmup_steps=0 if passos == 1 else max(1, passos // 10),
        bf16=True, optim='paged_adamw_8bit', eval_strategy='steps', eval_steps=max(5, passos // 4), save_strategy='no',
        logging_steps=min(5, passos), report_to='none', seed=42, dataloader_pin_memory=False, remove_unused_columns=False)
    treinador = TrainerSocratico(model=modelo, args=argumentos, train_dataset=Dataset.from_list(treino),
                        eval_dataset=Dataset.from_list(validacao),
                        data_collator=DataCollatorForSeq2Seq(tokenizer, label_pad_token_id=-100, pad_to_multiple_of=8))
    inicio = time.monotonic()
    resultado = treinador.train()
    avaliacao = treinador.evaluate()
    modelo.save_pretrained(str(saida))
    write_json(PASTA_TRABALHO / 'resultado-treino.json', {
        'base': base, 'passos': passos, 'rank': rank, 'max_length': seq, 'minutos': round((time.monotonic() - inicio) / 60, 1),
        'gradient_accumulation_steps': acumulacao,
        'metricas_treino': resultado.metrics, 'metricas_validacao': avaliacao,
        'historico': treinador.state.log_history,
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
    destino.mkdir(parents=True, exist_ok=False)
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
LLAMACPP_VERSAO = '0.6.0'
LLAMACPP_ZIP = f'https://github.com/ggml-org/llama.cpp/archive/refs/tags/v{LLAMACPP_VERSAO}.zip'


def conversor_gguf() -> Path:
    """Conversor oficial do llama.cpp (só os scripts Python), baixado uma vez para .tools/llamacpp."""
    pasta = ROOT / '.tools/llamacpp' / f'llama.cpp-{LLAMACPP_VERSAO}'
    if not (pasta / 'convert_hf_to_gguf.py').exists():
        import io
        import zipfile
        import httpx
        print('   baixando o conversor GGUF do llama.cpp (uma vez)...')
        dados = httpx.get(LLAMACPP_ZIP, follow_redirects=True, timeout=300).content
        with zipfile.ZipFile(io.BytesIO(dados)) as z:
            prefixo = f'llama.cpp-{LLAMACPP_VERSAO}/'
            nomes = [n for n in z.namelist() if n.startswith(prefixo) and (
                n.count('/') == 1 and n.endswith('.py') or n.startswith((prefixo + 'gguf-py/', prefixo + 'conversion/')))]
            z.extractall(pasta.parent, nomes)
    return pasta


def importar_no_ollama(pasta: Path, nome: str) -> None:
    """safetensors -> GGUF bf16 (llama.cpp) -> Q4_K_M (llama-quantize do Ollama) -> ollama create.

    O import direto de safetensors do Ollama usa o runtime MLX, que não existe no Windows.
    """
    titulo(f'4/5 Importando no Ollama como {nome} (Q4_K_M)')
    conversor = conversor_gguf()
    saida = PASTA_TRABALHO / 'gguf'
    saida.mkdir(parents=True, exist_ok=True)
    bf16, q4 = saida / f'{nome}-bf16.gguf', saida / f'{nome}-q4_k_m.gguf'
    env = {**os.environ, 'PYTHONPATH': str(conversor / 'gguf-py'), 'PYTHONUTF8': '1'}
    subprocess.run([sys.executable, str(conversor / 'convert_hf_to_gguf.py'), str(pasta), '--outtype', 'bf16',
                    '--outfile', str(bf16)], check=True, env=env)
    subprocess.run([str(OLLAMA.parent / 'lib/ollama/llama-quantize.exe'), str(bf16), str(q4), 'Q4_K_M'], check=True)
    bf16.unlink()
    atual = (ROOT / '05-modelo/Modelfile').read_text(encoding='utf-8')
    linhas = [ln for ln in atual.splitlines() if not ln.startswith('FROM ') and not ln.startswith('#')]
    modelfile = saida / 'Modelfile'
    modelfile.write_text(f'FROM {q4}\n' + '\n'.join(linhas) + '\n', encoding='utf-8')
    env = {**os.environ, 'OLLAMA_MODELS': str(ROOT / '.tools/models'), 'OLLAMA_HOST': '127.0.0.1:11434'}
    subprocess.run([str(OLLAMA), 'create', nome, '-f', str(modelfile)], check=True, env=env)
    q4.unlink()  # o Ollama guardou uma cópia em .tools/models


# ---------------------------------------------------------------------------- 5. avaliação
def verificar_dependencias_avaliacao() -> None:
    """Falha antes do treino caro se o ambiente não consegue importar o atendimento."""
    try:
        from eval.socratico import executar  # noqa: F401
    except ModuleNotFoundError as exc:
        raise SystemExit(
            f'Falta a dependência {exc.name!r} da avaliação. Execute novamente 3-Treinar.bat '
            'para instalar as dependências antes de treinar. Nenhum treino foi iniciado.'
        ) from exc


async def avaliar(nome: str) -> Path:
    titulo('5/5 Avaliação socrática pelo fluxo real do site')
    import httpx
    from eval.socratico import executar
    from backend.config import load_settings
    settings = load_settings()
    # Não gastar a bateria do modelo atual para só depois descobrir que falta o candidato.
    resposta = httpx.post(settings.ollama_url + '/api/show', json={'model': nome}, timeout=15)
    if resposta.status_code == 404:
        raise SystemExit(f'O modelo {nome!r} não está instalado no Ollama. Execute o treino completo primeiro.')
    resposta.raise_for_status()
    atual = settings.local_model
    destino = PASTA_DADOS / f'avaliacao-socratica-{datetime.now():%Y%m%d-%H%M%S}.json'
    await executar(list(dict.fromkeys([atual, nome])), destino)
    return destino.with_suffix('.md')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--passos', type=int, default=60, help='passos de otimização; revisar o relatório antes de ativar')
    parser.add_argument('--base', default=os.environ.get('TUTORON_TREINO_BASE', 'Qwen/Qwen3-8B'))
    parser.add_argument('--nome', default='tutoron-socratico-ft')
    parser.add_argument('--rank', type=int, default=8)
    parser.add_argument('--seq', type=int, default=2048, help='tamanho máximo de cada exemplo, em tokens')
    parser.add_argument('--so-dados', action='store_true')
    parser.add_argument('--verificar', action='store_true', help='dados e tokenização, sem carregar pesos ou treinar')
    parser.add_argument('--teste-gpu', action='store_true', help='um passo real e avaliação de loss; sem mesclar/importar')
    parser.add_argument('--pular-avaliacao', action='store_true')
    parser.add_argument('--so-avaliar', action='store_true',
                        help='avalia o candidato já instalado; não treina, mescla nem importa pesos')
    args = parser.parse_args()

    if min(args.passos, args.rank, args.seq) < 1:
        parser.error('--passos, --rank e --seq precisam ser positivos')
    if args.nome in ('tutoron-paa', 'qwen3:8b'):
        parser.error('use um nome novo para preservar o modelo base e permitir comparação')
    if args.so_avaliar:
        if args.so_dados or args.verificar or args.teste_gpu or args.pular_avaliacao:
            parser.error('--so-avaliar não combina com modos de preparação ou --pular-avaliacao')
        verificar_dependencias_avaliacao()
        print('Reaproveitando o modelo instalado. Nenhum passo de treino será repetido.', flush=True)
        relatorio = asyncio.run(avaliar(args.nome))
        print(f'\nAvaliação concluída. Relatório: {relatorio}\nO modelo em uso no servidor não foi alterado.')
        return
    grupos = preparar_dados()
    if args.so_dados:
        return
    if args.verificar:
        verificar_tokenizacao(grupos, args.base, args.seq)
        return
    if not args.teste_gpu and not args.pular_avaliacao:
        verificar_dependencias_avaliacao()
    global PASTA_TRABALHO
    PASTA_TRABALHO = PASTA_TRABALHO / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    PASTA_TRABALHO.mkdir(parents=True, exist_ok=True)
    for arquivo in ('manifesto.json', 'treino.jsonl', 'validacao.jsonl', 'teste.jsonl'):
        shutil.copy2(PASTA_DADOS / arquivo, PASTA_TRABALHO / arquivo)
    write_json(PASTA_TRABALHO / 'configuracao.json', vars(args))
    from backend.recursos import reservar_gpu
    with reservar_gpu():
        if args.teste_gpu:
            # Exercita o maior contexto de cada disciplina, sem importar o adapter de teste.
            maiores = {n: [max((r for r in grupos[n] if r['disciplina'] == d),
                              key=lambda r: sum(len(m['content']) for m in r['prompt'] + r['completion']))
                           for d in ('paa', 'sd')] for n in ('treino', 'validacao')}
            treinar(maiores, args.base, 1, args.rank, args.seq, acumulacao=2)
            print(f'Teste GPU concluído; adapter de teste em {PASTA_TRABALHO}. Nenhum modelo foi importado.')
            return
        adapter = treinar(grupos, args.base, args.passos, args.rank, args.seq)
        mesclado = mesclar(args.base, adapter)
        importar_no_ollama(mesclado, args.nome)
        alvo = mesclado.resolve()
        limite = ROOT.resolve() / '.tools' / 'treino-socratico'
        if alvo.name != 'mesclado' or not alvo.is_relative_to(limite):
            raise SystemExit('Pasta temporária fora do diretório de treino; limpeza cancelada.')
        shutil.rmtree(alvo)  # o Ollama já guardou a versão quantizada
    if not args.pular_avaliacao:
        print('Treino: 100% concluído. Modelo instalado; falta apenas a avaliação.', flush=True)
        try:
            relatorio = asyncio.run(avaliar(args.nome))
        except (Exception, SystemExit):
            print(f'\nO treino e o modelo instalado foram preservados em {PASTA_TRABALHO}.\n'
                  f'Para repetir só a avaliação: 3-Treinar.bat --so-avaliar --nome {args.nome}', flush=True)
            raise
        print(f'\nRelatório: {relatorio}')
    print(f'\nPronto. O modelo atual não foi alterado. Para usar o novo, coloque no .env:\n'
          f'   TUTORON_MODELO_LOCAL={args.nome}\ne reinicie o 1-Iniciar-Servidor.bat.')


if __name__ == '__main__':
    main()
