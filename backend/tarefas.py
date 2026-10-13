"""Respostas geradas em segundo plano, consultadas pelo site a cada segundo.

Por que não uma requisição longa: o túnel da Cloudflare encerra com erro 524
qualquer requisição que passe de 100 s sem resposta, e conexões longas caem à
toa no celular. Aqui o POST só cria a tarefa (responde na hora) e o navegador
pergunta o andamento com GETs curtos. Se a rede do aluno oscilar, a próxima
consulta continua de onde parou.

A IA sempre tenta responder: cada geração passa pela corrida Gemini -> local
e, se nenhum modelo responder, tenta de novo (até 4 vezes, por quase 1 minuto). A partir da
segunda tentativa o modelo local roda sem raciocínio, que é bem mais rápido.
"""
from __future__ import annotations

import asyncio
import logging
import secrets
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field

from . import prompts
from .dados import Registro, agora, novo_id
from .llm import LLM, SEM_RACIOCINIO, AllUnavailable, Model, Result, degradado
from .rag import contexto, recuperar

logger = logging.getLogger("tutoron.tarefas")

TENTATIVAS = 4
ESPERAS = (8, 20, 30)
VALIDADE_S = 3 * 3600  # tarefas concluídas ficam disponíveis por 3 horas

MSG_ERRO = ("Não conseguimos gerar a resposta agora. Tente de novo em alguns instantes; "
            "se continuar, avise a equipe do TutorON.")


def msg_fila(posicao: int) -> str:
    base = "Muita gente usando agora: a resposta está sendo preparada no servidor do TutorON"
    if posicao > 0:
        return f"{base} ({posicao} pedido(s) à sua frente). Pode levar alguns minutos; mantenha esta aba aberta."
    return f"{base}. Pode levar até 2 minutos; mantenha esta aba aberta."


@dataclass
class Tarefa:
    tipo: str  # "tutor" | "comparacao"
    id: str = field(default_factory=lambda: secrets.token_urlsafe(16))
    status: str = "fila"  # fila | gerando | pronta | erro
    mensagem: str = "Procurando no material da disciplina…"
    texto: str = ""
    rotulo: str = ""
    fontes: list[dict] = field(default_factory=list)
    resultado: dict = field(default_factory=dict)
    criada: float = field(default_factory=time.monotonic)
    concluida: float | None = None

    def publico(self) -> dict:
        dados = {"id": self.id, "status": self.status, "mensagem": self.mensagem}
        if self.tipo == "tutor":
            dados.update(texto=self.texto, rotulo=self.rotulo, fontes=self.fontes, **self.resultado)
        elif self.status == "pronta":
            dados.update(self.resultado)  # sessao, pergunta, A, B: sem identidade dos lados
        return dados


class Tarefas:
    def __init__(self, llm: LLM, settings, registro: Registro):
        self.llm = llm
        self.settings = settings
        self.registro = registro
        self.itens: dict[str, Tarefa] = {}
        self._tarefas_async: set[asyncio.Task] = set()

    # ------------------------------------------------------------------ ciclo de vida
    def _criar(self, tipo: str, trabalho: Callable[[Tarefa], Awaitable[None]]) -> Tarefa:
        self._limpar()
        t = Tarefa(tipo)
        self.itens[t.id] = t
        tarefa = asyncio.create_task(self._executar(t, trabalho))
        self._tarefas_async.add(tarefa)
        tarefa.add_done_callback(self._tarefas_async.discard)
        return t

    async def _executar(self, t: Tarefa, trabalho) -> None:
        try:
            await trabalho(t)
        except Exception:  # nunca deixar a tarefa pendurada: o aluno veria "gerando" para sempre
            logger.exception("Falha inesperada na tarefa %s", t.tipo)
            t.status, t.mensagem = "erro", MSG_ERRO
        finally:
            t.concluida = time.monotonic()

    def obter(self, ident: str) -> Tarefa | None:
        return self.itens.get(ident)

    def _limpar(self) -> None:
        agora_s = time.monotonic()
        for ident in [i for i, t in self.itens.items() if t.concluida and agora_s - t.concluida > VALIDADE_S]:
            del self.itens[ident]

    def ativas(self) -> int:
        return sum(1 for t in self.itens.values() if t.concluida is None)

    async def encerrar(self) -> None:
        for tarefa in list(self._tarefas_async):
            tarefa.cancel()

    # ------------------------------------------------------------------ geração com novas tentativas
    async def _gerar(self, sistema: str | None, prompt: str, t: Tarefa, *, models: list[Model] | None = None,
                     ao_texto: Callable[[str], None] | None = None, raciocinio: bool = True) -> Result:
        """Corrida de modelos com até 3 tentativas. Atualiza a mensagem da tarefa quando entra na fila local."""
        tentativas: list[dict] = []
        for n in range(TENTATIVAS):
            marca = SEM_RACIOCINIO.set(n > 0 or not raciocinio)
            partes: list[str] = []
            try:
                async for ev in self.llm.stream(sistema, prompt, models=models):
                    if ev["tipo"] == "aguarde":
                        t.mensagem = msg_fila(self.llm.local_waiting)
                    elif ev["tipo"] == "modelo":
                        t.mensagem = "Escrevendo a resposta…"
                        if ao_texto:
                            t.rotulo = Model(ev["provedor"], ev["modelo"]).label
                    elif ev["tipo"] == "texto":
                        partes.append(ev["texto"])
                        if ao_texto:
                            ao_texto("".join(partes))
                    elif ev["tipo"] == "reiniciar":
                        partes.clear()
                        if ao_texto:
                            ao_texto("")
                    elif ev["tipo"] == "fim":
                        texto = "".join(partes).strip()
                        if not texto:
                            raise AllUnavailable(ev["tentativas"])
                        return Result(text=texto, model=Model(ev["provedor"], ev["modelo"]), seconds=ev["segundos"],
                                      attempts=tentativas + ev["tentativas"])
                raise AllUnavailable([])
            except AllUnavailable as exc:
                tentativas += exc.attempts
                logger.warning("Nenhum modelo respondeu (tentativa %s/%s)", n + 1, TENTATIVAS)
                if n < TENTATIVAS - 1:
                    t.mensagem = "Os servidores estão ocupados; tentando de novo…"
                    for m in models or self.llm.cascade():
                        if m.provider == "ollama":
                            self.llm.breaker.reset(m)
                    # 8, 20 e 30 s: tempo para o vigia do 1-Iniciar-Servidor religar o Ollama se ele caiu.
                    await asyncio.sleep(ESPERAS[n])
            finally:
                SEM_RACIOCINIO.reset(marca)
        raise AllUnavailable(tentativas)

    # ------------------------------------------------------------------ modo Tutor
    def perguntar(self, pergunta: str, contexto_aluno: str | None) -> Tarefa:
        async def trabalho(t: Tarefa) -> None:
            trechos = await recuperar(pergunta, self.llm, self.settings)
            t.fontes = [x.publico() for x in trechos]
            t.status, t.mensagem = "gerando", "Preparando a resposta…"
            prompt = prompts.prompt_tutor(pergunta, contexto(trechos, len(pergunta) + len(contexto_aluno or "")), contexto_aluno)

            def ao_texto(texto: str) -> None:
                t.texto = texto

            ident = novo_id()
            try:
                r = await self._gerar(prompts.SISTEMA_TUTOR, prompt, t, ao_texto=ao_texto)
            except AllUnavailable as exc:
                self.registro.anexar("perguntas.jsonl", {"id": ident, "data": agora(), "pergunta": pergunta,
                                                         "erro": "nenhum_modelo", "tentativas": exc.attempts})
                t.status, t.mensagem = "erro", MSG_ERRO
                return
            t.texto = r.text
            # Respondeu o flash-lite porque os modelos melhores falharam ou estavam em pausa.
            # Só registro e payload por enquanto; a interface não muda.
            caiu = degradado(r.model, r.attempts, self.llm.cascade())
            if caiu:
                logger.warning("Resposta degradada para %s", r.model.key)
            self.registro.anexar("perguntas.jsonl", {
                "id": ident, "data": agora(), "pergunta": pergunta, "contexto": contexto_aluno, "resposta": r.text,
                "provedor": r.model.provider, "modelo": r.model.name, "segundos": r.seconds, "degradado": caiu,
                "tentativas": r.attempts, "fontes": t.fontes})
            t.resultado = {"id_resposta": ident, "segundos": r.seconds, "degradado": caiu}
            t.status, t.mensagem = "pronta", ""

        return self._criar("tutor", trabalho)

    # ------------------------------------------------------------------ modo Validação
    def comparar(self, pergunta: str, contexto_aluno: str | None) -> Tarefa:
        async def trabalho(t: Tarefa) -> None:
            trechos = await recuperar(pergunta, self.llm, self.settings)
            t.status, t.mensagem = "gerando", "Gerando as duas respostas…"
            prompt_tutor = prompts.prompt_tutor(pergunta, contexto(trechos, len(pergunta) + len(contexto_aluno or "")), contexto_aluno)
            prompt_gen = prompts.prompt_generico(pergunta, contexto_aluno)
            modelos_gen = self.llm.cascade(local_model=self.settings.local_generic_model)
            try:
                # No local, os dois lados rodam um depois do outro na GPU; sem raciocínio a espera cai
                # de ~3 min para ~1 min. Os dois lados usam a mesma configuração (comparação justa).
                pensar = self.settings.local_thinking_validacao
                tutor, generico = await asyncio.gather(
                    self._gerar(prompts.SISTEMA_TUTOR, prompt_tutor, t, raciocinio=pensar),
                    self._gerar(None, prompt_gen, t, models=modelos_gen, raciocinio=pensar))
            except AllUnavailable:
                t.status, t.mensagem = "erro", MSG_ERRO
                return
            # Comparação justa: o genérico usa o mesmo modelo de base do TutorON, só sem
            # material e sem instruções. Se a corrida caiu em outro modelo, tenta uma vez
            # no mesmo; se não der, fica o que já foi gerado (o modelo de cada lado é registrado).
            alvo = tutor.model if tutor.model.provider == "gemini" else Model("ollama", self.settings.local_generic_model)
            if generico.model != alvo:
                marca = SEM_RACIOCINIO.set(not pensar)
                try:
                    generico = await self.llm.complete(None, prompt_gen, models=[alvo])
                except AllUnavailable:
                    pass
                finally:
                    SEM_RACIOCINIO.reset(marca)
            ordem = ["tutoron", "generico"]
            secrets.SystemRandom().shuffle(ordem)
            par = {
                "tutoron": {"texto": tutor.text, "provedor": tutor.model.provider, "modelo": tutor.model.name,
                            "segundos": tutor.seconds, "tentativas": tutor.attempts,
                            "fontes": [x.publico() for x in trechos], "sistema": "TutorON (RAG + prompt)"},
                "generico": {"texto": generico.text, "provedor": generico.model.provider,
                             "modelo": generico.model.name, "segundos": generico.seconds,
                             "tentativas": generico.attempts,
                             "sistema": "Genérico (mesmo modelo, sem material nem instruções)"},
            }
            sessao = novo_id()
            self.registro.nova_comparacao({"sessao": sessao, "data": agora(), "pergunta": pergunta,
                                           "contexto": contexto_aluno, "lados": {"A": ordem[0], "B": ordem[1]},
                                           "respostas": par})
            t.resultado = {"sessao": sessao, "pergunta": pergunta, "A": par[ordem[0]]["texto"], "B": par[ordem[1]]["texto"]}
            t.status, t.mensagem = "pronta", ""

        return self._criar("comparacao", trabalho)
