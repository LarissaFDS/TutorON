"""Registro local das perguntas e das avaliações A/B.

Tudo fica em ``dados/`` (fora do Git), em JSON Lines: uma linha por evento,
fácil de abrir no Python/pandas e de juntar em datasets de treino.

- ``dados/perguntas.jsonl``           modo Tutor: pergunta, resposta, modelo e fontes
- ``dados/feedback.jsonl``            modo Tutor: "ajudou?" / "tem erro" do aluno
- ``dados/validacao/comparacoes.jsonl`` modo Validação: o par A/B gerado, com a identidade de cada lado
- ``dados/validacao/avaliacoes.jsonl``  modo Validação: notas do aluno + par completo + qual lado era o TutorON

Nenhum IP, nome ou identificador pessoal é gravado.
"""
from __future__ import annotations

import json
import secrets
import threading
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path


def agora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def novo_id() -> str:
    return secrets.token_urlsafe(12)


class Registro:
    def __init__(self, pasta: Path):
        self.pasta = pasta
        self.lock = threading.Lock()
        (pasta / "validacao").mkdir(parents=True, exist_ok=True)
        # Comparações aguardando nota. Também ficam em disco: reiniciar o
        # servidor não invalida uma comparação que o aluno está lendo.
        self.comparacoes: dict[str, dict] = {}
        self._carregar_comparacoes()

    def _carregar_comparacoes(self) -> None:
        caminho = self.pasta / "validacao" / "comparacoes.jsonl"
        avaliadas = {r.get("sessao") for r in self.ler("validacao/avaliacoes.jsonl")}
        if caminho.exists():
            for linha in caminho.read_text(encoding="utf-8").splitlines():
                try:
                    item = json.loads(linha)
                except json.JSONDecodeError:
                    continue
                if item.get("sessao") not in avaliadas:
                    self.comparacoes[item["sessao"]] = item

    def anexar(self, nome: str, registro: dict) -> None:
        caminho = self.pasta / nome
        linha = json.dumps(registro, ensure_ascii=False) + "\n"
        with self.lock:
            caminho.parent.mkdir(parents=True, exist_ok=True)
            with caminho.open("a", encoding="utf-8", newline="\n") as arquivo:
                arquivo.write(linha)
                arquivo.flush()

    def ler(self, nome: str) -> list[dict]:
        caminho = self.pasta / nome
        if not caminho.exists():
            return []
        linhas = []
        for linha in caminho.read_text(encoding="utf-8").splitlines():
            try:
                linhas.append(json.loads(linha))
            except json.JSONDecodeError:
                continue
        return linhas

    def nova_comparacao(self, comparacao: dict) -> None:
        with self.lock:
            self.comparacoes[comparacao["sessao"]] = comparacao
        self.anexar("validacao/comparacoes.jsonl", comparacao)

    def concluir_comparacao(self, sessao: str) -> dict | None:
        with self.lock:
            return self.comparacoes.pop(sessao, None)


class Limitador:
    """Janela deslizante por cliente, para proteger a cota do Gemini e a GPU."""

    def __init__(self, limite: int, janela_s: float = 600):
        self.limite = limite
        self.janela_s = janela_s
        self.eventos: dict[str, deque] = {}
        self.lock = threading.Lock()

    def permitir(self, cliente: str) -> bool:
        if self.limite <= 0:
            return True
        agora_s = time.monotonic()
        with self.lock:
            fila = self.eventos.setdefault(cliente, deque())
            while fila and agora_s - fila[0] > self.janela_s:
                fila.popleft()
            if len(fila) >= self.limite:
                return False
            fila.append(agora_s)
            if len(self.eventos) > 5000:  # não crescer sem limite
                self.eventos = {k: v for k, v in self.eventos.items() if v}
            return True
