"""Corrida escalonada entre modelos, com provedores falsos (sem rede)."""
import asyncio
import dataclasses

import pytest

from backend.config import Settings
from backend.llm import LLM, AllUnavailable, Model, Unavailable


def settings(**kw):
    base = Settings(gemini_api_key="x", gemini_models=("g1", "g2", "g3"), stagger_s=0.05, local_wait_s=0.5,
                    gemini_first_chunk_s=1.0, gemini_idle_s=1.0, local_first_chunk_s=1.0)
    return dataclasses.replace(base, **kw)


class FakeLLM(LLM):
    """Cada modelo tem um roteiro: ("erro", status) | ("lento", segundos, texto) | ("ok", texto)."""

    def __init__(self, roteiro, **kw):
        super().__init__(settings(**kw))
        self.roteiro = roteiro
        self.iniciados = []
        self.fechados = []

    def _provider(self, model, system, prompt):
        self.iniciados.append(model.name)
        plano = self.roteiro.get(model.name, ("erro", 503))
        llm = self

        async def gen():
            try:
                if plano[0] == "erro":
                    await asyncio.sleep(0.01)
                    raise Unavailable(f"HTTP {plano[1]}", 20)
                if plano[0] == "lento":
                    await asyncio.sleep(plano[1])
                for parte in plano[-1].split(" "):
                    yield parte + " "
                if plano[0] == "cai":
                    raise Unavailable("caiu", 5)
            finally:
                llm.fechados.append(model.name)
        return gen()


def run(coro):
    return asyncio.run(coro)


def test_primeiro_modelo_responde():
    llm = FakeLLM({"g1": ("ok", "resposta um")})
    r = run(llm.complete("s", "p"))
    assert r.model == Model("gemini", "g1") and r.text == "resposta um"
    assert llm.iniciados == ["g1"]


def test_erro_passa_ao_proximo_imediatamente():
    llm = FakeLLM({"g1": ("erro", 503), "g2": ("erro", 429), "g3": ("ok", "do terceiro")})
    r = run(llm.complete("s", "p"))
    assert r.model.name == "g3"
    assert [a["resultado"] for a in r.attempts][:2] == ["HTTP 503", "HTTP 429"]
    # Disjuntor: na próxima pergunta, g1 e g2 nem são tentados.
    llm.iniciados.clear()
    r2 = run(llm.complete("s", "p"))
    assert llm.iniciados == ["g3"] and r2.model.name == "g3"


def test_lento_nao_bloqueia_e_quem_responde_primeiro_vence():
    llm = FakeLLM({"g1": ("lento", 0.6, "lenta"), "g2": ("ok", "rapida")})
    r = run(llm.complete("s", "p"))
    assert r.model.name == "g2" and r.text == "rapida"
    assert "g1" in llm.fechados  # o lento foi cancelado
    assert any(a["resultado"].startswith("cancelado") for a in r.attempts)


def test_local_quando_todos_os_gemini_falham():
    llm = FakeLLM({"tutoron-paa": ("ok", "local")})
    r = run(llm.complete("s", "p"))
    assert r.model == Model("ollama", "tutoron-paa") and r.text == "local"


def test_local_entra_depois_da_espera_maxima():
    lentos = {g: ("lento", 5, "x") for g in ("g1", "g2", "g3")}
    llm = FakeLLM({**lentos, "tutoron-paa": ("ok", "local")}, local_wait_s=0.3, gemini_first_chunk_s=10)
    r = run(llm.complete("s", "p"))
    assert r.model.provider == "ollama"
    assert r.seconds < 2


def test_queda_no_meio_reinicia_com_o_proximo():
    llm = FakeLLM({"g1": ("cai", "parcial"), "g2": ("ok", "completa")})

    async def eventos():
        return [e async for e in llm.stream("s", "p")]
    evs = run(eventos())
    tipos = [e["tipo"] for e in evs]
    assert "reiniciar" in tipos and evs[-1]["modelo"] == "g2"


def test_nenhum_disponivel():
    llm = FakeLLM({})
    with pytest.raises(AllUnavailable) as info:
        run(llm.complete("s", "p"))
    assert len(info.value.attempts) == 4


def test_modelos_fixos():
    llm = FakeLLM({"g2": ("ok", "fixo")})
    r = run(llm.complete(None, "p", models=[Model("gemini", "g2")]))
    assert r.model.name == "g2" and llm.iniciados == ["g2"]
