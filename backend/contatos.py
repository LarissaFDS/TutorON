"""Controle da equipe: com quem já falamos para pedir feedback (caixinha no painel /admin).

Fica num JSON pequeno na pasta de dados do servidor, então todo administrador vê as mesmas marcações.
"""

from __future__ import annotations

import json
import threading
from datetime import datetime, timezone
from pathlib import Path


class Contatos:
    def __init__(self, arquivo: Path):
        self.arquivo = arquivo
        self._trava = threading.Lock()

    def _ler(self) -> dict:
        try:
            return json.loads(self.arquivo.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}

    def todos(self) -> dict[str, dict]:
        with self._trava:
            return self._ler()

    def marcar(self, quem: str, feito: bool, por: str | None) -> dict | None:
        with self._trava:
            dados = self._ler()
            if feito:
                dados[quem] = {"por": por, "em": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            else:
                dados.pop(quem, None)
            self.arquivo.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.arquivo.with_suffix(".tmp")
            tmp.write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
            tmp.replace(self.arquivo)
            return dados.get(quem)
