"""QLoRA em GPU NVIDIA; o modo dry-run não importa bibliotecas de treino."""
import argparse
import importlib.metadata
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from acervo.common import ROOT, digest, read_json, write_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--steps', type=int, default=30)
    args = parser.parse_args()
    folder = ROOT / '05-modelo/treino'
    manifest = read_json(folder / 'manifesto.json', {})
    if not manifest:
        raise SystemExit('Execute scripts/preparar_treino.py primeiro.')
    if args.steps < 1:
        raise SystemExit('--steps deve ser positivo.')
    data = {}
    for split in ('treino', 'validacao'):
        path = folder / f'{split}.jsonl'
        if digest(path.read_bytes()) != manifest['dados'][split]:
            raise SystemExit('Dataset alterado; refaça o manifesto antes de treinar.')
        data[split] = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
        if not data[split]: raise SystemExit('Split vazio.')
    families = [{r['family'] for r in data[s]} for s in ('treino', 'validacao')]
    if families[0] & families[1] or (families[0] | families[1]) & set(manifest['familias_reservadas_benchmark']):
        raise SystemExit('Vazamento de famílias entre conjuntos.')
    if args.dry_run:
        print('Dados íntegros e famílias separadas. Nenhum peso foi treinado.')
        print('Base:', manifest['modelo'], 'Treino:', len(data['treino']), 'Validação:', len(data['validacao']))
        return
    import torch
    from datasets import Dataset
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    from peft import LoraConfig, prepare_model_for_kbit_training
    from trl import SFTConfig, SFTTrainer
    if not torch.cuda.is_available():
        raise SystemExit('GPU NVIDIA/CUDA necessária neste perfil QLoRA. Use outra máquina Linux/Windows/WSL2; o notebook atual serve inferência.')
    bf16 = torch.cuda.is_bf16_supported()
    dtype = torch.bfloat16 if bf16 else torch.float16
    tokenizer = AutoTokenizer.from_pretrained(manifest['modelo'], revision=manifest['revision'])
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(manifest['modelo'], revision=manifest['revision'],
        quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4', bnb_4bit_use_double_quant=True,
                                              bnb_4bit_compute_dtype=dtype), device_map={'': 0})
    model = prepare_model_for_kbit_training(model)
    config = SFTConfig(output_dir=str(ROOT / '.tools/treino/adapter'), max_steps=args.steps,
        max_length=1024, per_device_train_batch_size=1, per_device_eval_batch_size=1,
        gradient_accumulation_steps=4, learning_rate=1e-4, gradient_checkpointing=True,
        completion_only_loss=True, bf16=bf16, fp16=not bf16, seed=manifest['seed'],
        eval_strategy='steps', eval_steps=10, save_steps=10, save_total_limit=2,
        logging_steps=1, report_to='none', push_to_hub=False, optim='adamw_torch')
    trainer = SFTTrainer(model=model, processing_class=tokenizer, args=config,
        train_dataset=Dataset.from_list([{'prompt': r['prompt'], 'completion': r['completion']} for r in data['treino']]),
        eval_dataset=Dataset.from_list([{'prompt': r['prompt'], 'completion': r['completion']} for r in data['validacao']]),
        peft_config=LoraConfig(r=8, lora_alpha=16, lora_dropout=0.05, target_modules=['q_proj','k_proj','v_proj','o_proj'],
                               bias='none', task_type='CAUSAL_LM'))
    trained = trainer.train()
    trainer.save_model()
    tokenizer.save_pretrained(config.output_dir)
    versions = {p: importlib.metadata.version(p) for p in ('torch','transformers','peft','trl','datasets','accelerate','bitsandbytes')}
    write_json(ROOT / '.tools/treino/resultado.json', {'manifesto': manifest, 'versoes': versions,
               'metrics': trained.metrics, 'avaliacao_loss': trainer.evaluate(), 'steps': args.steps,
               'aviso': 'Loss de treino não comprova superioridade sobre o modelo base. Rode o benchmark e avaliação cega.'})


if __name__ == '__main__':
    main()
