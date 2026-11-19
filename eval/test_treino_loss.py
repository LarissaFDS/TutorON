"""Executar com o ambiente de treino; compara loss e gradientes com a implementação densa."""
import pytest

torch = pytest.importorskip('torch')
transformers = pytest.importorskip('transformers')

from scripts.treinar import perda_so_resposta  # noqa: E402


def test_projecao_parcial_preserva_loss_e_gradientes():
    torch.manual_seed(42)
    cfg = transformers.Qwen3Config(vocab_size=31, hidden_size=16, intermediate_size=32,
                                  num_hidden_layers=1, num_attention_heads=2, num_key_value_heads=2,
                                  head_dim=8, attention_dropout=0.0)
    modelo = transformers.Qwen3ForCausalLM(cfg).eval()
    entradas = {'input_ids': torch.tensor([[1, 2, 3, 4, 5, 0], [1, 2, 3, 4, 0, 0]]),
                'attention_mask': torch.tensor([[1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0]]),
                'labels': torch.tensor([[-100, -100, -100, 4, 5, -100], [-100, -100, 3, 4, -100, -100]])}
    densa = modelo(**entradas).loss
    densa.backward()
    gradientes = {n: p.grad.clone() for n, p in modelo.named_parameters() if p.grad is not None}
    modelo.zero_grad()
    parcial, saida = perda_so_resposta(modelo, entradas)
    parcial.backward()
    assert saida.logits.shape[1] < entradas['labels'].shape[1]
    torch.testing.assert_close(parcial, densa)
    for nome, p in modelo.named_parameters():
        if nome in gradientes:
            torch.testing.assert_close(p.grad, gradientes[nome], atol=1e-6, rtol=1e-5)
    normalizada, _ = perda_so_resposta(modelo, entradas, num_items_in_batch=8)
    torch.testing.assert_close(normalizada, densa / 2)
