"""Contas de aluno (Supabase Auth): login com Google ou com e-mail e senha.

O navegador faz o login com a biblioteca do Supabase (backend/web/conta.js) e manda o token de
sessão no cookie `tutoron_sessao` (ou no cabeçalho Authorization). Aqui o token é conferido no
próprio Supabase e guardado em cache por alguns minutos, para não consultar a cada pedido.

Cada conta vira o usuário "u:<id>" da cota (backend/cota.py): limite diário por conta, com
limite próprio opcional definido no painel /admin. Sem Supabase configurado, nada disso liga e o
site segue com o convidado anônimo de antes.
"""
from __future__ import annotations

import hashlib
import logging
import threading
import time

logger = logging.getLogger("tutoron.contas")
CACHE_S = 300


class Contas:
    def __init__(self, banco, chave_publica: str, admins: tuple[str, ...] = ()):
        self.banco = banco
        self.chave_publica = chave_publica
        self.admins = {a.lower() for a in admins}
        self._cache: dict[str, tuple[float, dict | None]] = {}
        self._perfis_vistos: set[str] = set()
        self._trava = threading.Lock()

    @property
    def ativas(self) -> bool:
        return bool(self.banco and self.chave_publica)

    def usuario(self, token: str | None) -> dict | None:
        """{'id', 'email', 'nome', 'admin'} da sessão, ou None (sem login, token inválido ou expirado)."""
        if not (self.ativas and token):
            return None
        chave = hashlib.sha256(token.encode()).hexdigest()
        agora = time.monotonic()
        with self._trava:
            item = self._cache.get(chave)
            if item and agora - item[0] < CACHE_S:
                return item[1]
        bruto = self.banco.usuario_do_token(token, self.chave_publica)
        conta = None
        if bruto and bruto.get("id"):
            meta = bruto.get("user_metadata") or {}
            email = (bruto.get("email") or "").lower()
            conta = {"id": bruto["id"], "email": email,
                     "nome": meta.get("full_name") or meta.get("name") or email.split("@")[0],
                     "foto": meta.get("avatar_url") or meta.get("picture"),
                     "admin": email in self.admins}
            self._garantir_perfil(conta)
        with self._trava:
            if len(self._cache) > 5000:
                self._cache.clear()
            self._cache[chave] = (agora, conta)
        return conta

    def esquecer(self, ident: str) -> None:
        """Tira do cache as sessões desta conta (ex.: depois de trocar o nome)."""
        with self._trava:
            for chave in [k for k, (_, c) in self._cache.items() if c and c["id"] == ident]:
                del self._cache[chave]

    def _garantir_perfil(self, conta: dict) -> None:
        """Cria a linha em `perfis` no primeiro acesso (sem mexer em limite já definido pelo admin)."""
        if conta["id"] in self._perfis_vistos:
            return
        self._perfis_vistos.add(conta["id"])
        self.banco.inserir("perfis", {"id": conta["id"], "email": conta["email"], "nome": conta["nome"]},
                           upsert="id")


def token_da_requisicao(request) -> str | None:
    auth = request.headers.get("authorization", "")
    if auth.lower().startswith("bearer "):
        return auth[7:].strip() or None
    return request.cookies.get("tutoron_sessao") or None
