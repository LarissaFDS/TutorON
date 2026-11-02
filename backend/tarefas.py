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
import re
import secrets
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field

from acervo.disciplinas import obter

from . import animacao, foto, prompts, seguranca, tutoria
from .dados import Registro, agora, novo_id
from .llm import LLM, SEM_RACIOCINIO, PLANEJAMENTO_JSON, AllUnavailable, Model, Result, degradado
from .animacao.roteiro import extrair_json
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
    tipo: str  # "tutor" | "comparacao" | "foto" | "animacao"
    id: str = field(default_factory=lambda: secrets.token_urlsafe(16))
    status: str = "fila"  # fila | gerando | pronta | erro
    mensagem: str = "Procurando no material da disciplina…"
    texto: str = ""
    rotulo: str = ""
    fontes: list[dict] = field(default_factory=list)
    resultado: dict = field(default_factory=dict)
    criada: float = field(default_factory=time.monotonic)
    concluida: float | None = None
    disciplina: str | None = None

    def publico(self) -> dict:
        dados = {"id": self.id, "status": self.status, "mensagem": self.mensagem}
        if self.disciplina:
            dados['disciplina'] = self.disciplina
        if self.tipo == "tutor":
            dados.update(texto=self.texto, rotulo=self.rotulo, fontes=self.fontes, **self.resultado)
        elif self.tipo in ("foto", "animacao"):
            dados.update(self.resultado)
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
    def _criar(self, tipo: str, trabalho: Callable[[Tarefa], Awaitable[None]], *, disciplina=None) -> Tarefa:
        self._limpar()
        t = Tarefa(tipo, disciplina=disciplina)
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

    async def _orientar(self, sistema, prompt, pergunta, d, trechos, t, *, raciocinio=True):
        """Só publica texto completo e revisado. No máximo uma reformulação."""
        atomica = tutoria.ajuda_atomica(pergunta, d.id)
        if atomica:
            r = Result(text=atomica, model=Model("codigo", "orientacao-atomica"), seconds=0, attempts=[])
            return atomica, r, ["orientacao_atomica"], None, []
        r = await self._gerar(sistema, prompt, t, raciocinio=raciocinio)
        ajustes, pareceres, bloqueada = [], [], None
        validos = {x.rotulo for x in trechos}
        for rodada in range(2):
            texto, mais = seguranca.revisar(r.text, sistema, validos, d.nome)
            ajustes += mais
            if texto == seguranca.recusa(d.nome):
                return texto, r, ajustes, bloqueada, pareceres
            t.mensagem = "Revisando a ajuda antes de mostrar…"
            parecer = await tutoria.avaliar_ajuda(self.llm, pergunta, prompt, texto)
            pareceres.append(parecer)
            if parecer["aprovada"]:
                texto, faltou = seguranca.garantir_sua_vez(texto)
                if faltou:
                    ajustes.append("sua_vez_acrescentada")
                return texto, r, ajustes, bloqueada, pareceres
            bloqueada = bloqueada or texto
            ajustes.append("entregou_resposta" if rodada == 0 else "entregou_resposta_de_novo")
            if rodada == 0:
                refazer = (prompt + "\n\nRESPOSTA ANTERIOR (proibida, reprovada na revisão):\n<<<\n"
                           + texto[:4000] + "\n>>>\n" + prompts.SISTEMA_REFORCO)
                try:
                    r2 = await self._gerar(sistema, refazer, t, raciocinio=raciocinio)
                    r = Result(text=r2.text, model=r2.model, seconds=round(r.seconds + r2.seconds, 2),
                               attempts=r.attempts + r2.attempts)
                except AllUnavailable:
                    ajustes.append("reforco_indisponivel")
                    break
        ajustes.append("ajuda_de_reserva")
        return tutoria.ajuda_de_reserva(d.id), r, ajustes, bloqueada, pareceres

    # ------------------------------------------------------------------ modo Tutor
    def perguntar(self, pergunta: str, contexto_aluno: str | None, disciplina: str | None = None,
                  ajuda: str = "auto", leitura_foto: str | None = None, historico: list[dict] | None = None,
                  travou: str | None = None) -> Tarefa:
        d = obter(disciplina)  # antes da tarefa: disciplina desconhecida falha na hora, não em segundo plano
        ajuda = prompts.ajuda_valida(ajuda)
        historico = historico or []
        if historico and ajuda == "auto":
            # "Ainda não consegui" com o tutor escolhendo: troca a forma de explicar a cada rodada.
            ajuda = prompts.proxima_ajuda([prompts.ajuda_valida(h.get("ajuda")) for h in historico])

        async def trabalho(t: Tarefa) -> None:
            if seguranca.pedido_de_instrucoes(pergunta):
                # Não chega à IA: a recusa não depende de o modelo obedecer ao prompt.
                ident = novo_id()
                t.texto = seguranca.recusa(d.nome)
                self.registro.anexar("perguntas.jsonl", {"id": ident, "data": agora(), "disciplina": d.id,
                                                         "pergunta": pergunta, "contexto": contexto_aluno,
                                                         "resposta": t.texto, "bloqueio": "pedido_de_instrucoes"})
                t.resultado = {"id_resposta": ident, "segundos": 0, "degradado": False}
                t.status, t.mensagem = "pronta", ""
                return
            atomica = tutoria.ajuda_atomica(pergunta, d.id, len(historico))
            if atomica:
                ident = novo_id()
                t.texto = atomica
                self.registro.anexar("perguntas.jsonl", {"id": ident, "data": agora(), "disciplina": d.id,
                    "pergunta": pergunta, "contexto": contexto_aluno, "resposta": atomica,
                    "modo": "socratico", "versao_politica": "socratico-v2", "bloqueio": "questao_atomica"})
                t.resultado = {"id_resposta": ident, "segundos": 0, "degradado": False, "ajuda": ajuda}
                t.status, t.mensagem = "pronta", ""
                return
            trechos = await recuperar(pergunta, self.llm, self.settings, d)
            t.fontes = [x.publico() for x in trechos]
            t.status, t.mensagem = "gerando", "Preparando a resposta…"
            tamanho = len(pergunta) + len(contexto_aluno or "") + len(leitura_foto or "")
            prompt = prompts.prompt_socratico(pergunta, contexto(trechos, tamanho), contexto_aluno, ajuda, leitura_foto,
                                              historico, travou)

            ident = novo_id()
            sistema = prompts.sistema_socratico(d)
            try:
                texto, r, ajustes, bloqueada, pareceres = await self._orientar(
                    sistema, prompt, pergunta, d, trechos, t)
            except AllUnavailable as exc:
                self.registro.anexar("perguntas.jsonl", {"id": ident, "data": agora(), "disciplina": d.id,
                                                         "pergunta": pergunta, "erro": "nenhum_modelo",
                                                         "tentativas": exc.attempts})
                t.status, t.mensagem = "erro", MSG_ERRO
                return
            t.texto = texto
            # Respondeu o flash-lite porque os modelos melhores falharam ou estavam em pausa.
            # Só registro e payload por enquanto; a interface não muda.
            caiu = degradado(r.model, r.attempts, self.llm.cascade())
            if caiu:
                logger.warning("Resposta degradada para %s", r.model.key)
            self.registro.anexar("perguntas.jsonl", {
                "id": ident, "data": agora(), "disciplina": d.id, "pergunta": pergunta, "contexto": contexto_aluno,
                "modo": "socratico", "versao_politica": "socratico-v2", "revisoes_pedagogicas": pareceres,
                "ajuda": ajuda, **({"leitura_foto": leitura_foto} if leitura_foto else {}),
                **({"rodada": len(historico) + 1, "travou": travou} if historico else {}),
                **({"resposta_bloqueada": bloqueada} if bloqueada else {}),
                "resposta": texto, **({"resposta_original": r.text, "ajustes": ajustes} if ajustes else {}),
                "provedor": r.model.provider, "modelo": r.model.name, "segundos": r.seconds, "degradado": caiu,
                "tentativas": r.attempts, "fontes": t.fontes})
            t.resultado = {"id_resposta": ident, "segundos": r.seconds, "degradado": caiu, "ajuda": ajuda}
            t.status, t.mensagem = "pronta", ""

        return self._criar("tutor", trabalho, disciplina=d.id)

    # ------------------------------------------------------------------ modo Validação
    def comparar(self, pergunta: str, contexto_aluno: str | None, disciplina: str | None = None) -> Tarefa:
        d = obter(disciplina)

        async def trabalho(t: Tarefa) -> None:
            trechos = await recuperar(pergunta, self.llm, self.settings, d)
            t.status, t.mensagem = "gerando", "Gerando as duas respostas…"
            prompt_tutor = prompts.prompt_socratico(pergunta, contexto(trechos, len(pergunta) + len(contexto_aluno or "")), contexto_aluno)
            prompt_gen = prompts.prompt_generico(pergunta, contexto_aluno)
            modelos_gen = self.llm.cascade(local_model=self.settings.local_generic_model)
            try:
                # No local, os dois lados rodam um depois do outro na GPU; sem raciocínio a espera cai
                # de ~3 min para ~1 min. Os dois lados usam a mesma configuração (comparação justa).
                pensar = self.settings.local_thinking_validacao
                sistema = prompts.sistema_socratico(d)
                orientacao, generico = await asyncio.gather(
                    self._orientar(sistema, prompt_tutor, pergunta, d, trechos, t, raciocinio=pensar),
                    self._gerar(None, prompt_gen, t, models=modelos_gen, raciocinio=pensar))
                texto_tutor, tutor, ajustes, bloqueada, pareceres = orientacao
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
            # O lado TutorON passa pela mesma revisão do modo Tutor (o genérico é o controle, sem revisão).
            ordem = ["tutoron", "generico"]
            secrets.SystemRandom().shuffle(ordem)
            par = {
                "tutoron": {"texto": texto_tutor, "provedor": tutor.model.provider, "modelo": tutor.model.name,
                            "segundos": tutor.seconds, "tentativas": tutor.attempts,
                            "fontes": [x.publico() for x in trechos], "sistema": "TutorON socrático (RAG + prompt)",
                            "versao_politica": "socratico-v2", "ajustes": ajustes,
                            "revisoes_pedagogicas": pareceres, "resposta_bloqueada": bloqueada},
                "generico": {"texto": generico.text, "provedor": generico.model.provider,
                             "modelo": generico.model.name, "segundos": generico.seconds,
                             "tentativas": generico.attempts,
                             "sistema": "Genérico (mesmo modelo, sem material nem instruções)"},
            }
            sessao = novo_id()
            self.registro.nova_comparacao({"sessao": sessao, "data": agora(), "disciplina": d.id, "pergunta": pergunta,
                                           "contexto": contexto_aluno, "lados": {"A": ordem[0], "B": ordem[1]},
                                           "respostas": par})
            t.resultado = {"sessao": sessao, "pergunta": pergunta, "A": par[ordem[0]]["texto"], "B": par[ordem[1]]["texto"]}
            t.status, t.mensagem = "pronta", ""

        return self._criar("comparacao", trabalho, disciplina=d.id)

    # ------------------------------------------------------------------ foto do papel
    def ler_foto(self, imagem: bytes, disciplina: str | None = None, observacao: str | None = None) -> Tarefa:
        """Transcreve a foto para o aluno conferir. Não responde nada: só lê."""
        d = obter(disciplina)
        preparada = foto.preparar(imagem)  # antes da tarefa: imagem inválida falha na hora (400)

        async def trabalho(t: Tarefa) -> None:
            t.status, t.mensagem = "gerando", "Lendo a foto inteira e os recortes ampliados…"
            imagens = [preparada["inteira"], *preparada["recortes"]]
            texto = prompts.prompt_foto(d, len(preparada["recortes"]), observacao)
            ident = novo_id()
            try:
                r = await self.llm.ver_imagens(prompts.SISTEMA_FOTO, texto, imagens)
                leitura = foto.normalizar(extrair_json(r.text))
            except AllUnavailable as exc:
                self.registro.anexar("fotos.jsonl", {"id": ident, "data": agora(), "disciplina": d.id,
                                                     "erro": "nenhum_modelo", "tentativas": exc.attempts})
                t.status = "erro"
                t.mensagem = "Não consegui ler a foto agora. Tente de novo em instantes ou digite o enunciado."
                return
            except ValueError:
                t.status, t.mensagem = "erro", "A leitura da foto veio incompleta. Tente de novo ou digite o enunciado."
                return
            # A foto não é guardada; só a leitura, sem identificação (para medir a qualidade da leitura).
            self.registro.anexar("fotos.jsonl", {"id": ident, "data": agora(), "disciplina": d.id,
                                                 "preparo": preparada["info"], "leitura": leitura,
                                                 "modelo": r.model.key, "segundos": r.seconds})
            t.resultado = {"id_leitura": ident, "leitura": leitura, "modelo": r.model.label, "segundos": r.seconds}
            t.status, t.mensagem = "pronta", ""

        return self._criar("foto", trabalho, disciplina=disciplina)

    # ------------------------------------------------------------------ animação (Manim, protótipo)
    def animar_exemplo(self, ident: str) -> Tarefa:
        from .animacao import galeria
        exemplo = galeria.obter(ident)

        async def trabalho(t: Tarefa) -> None:
            t.status, t.mensagem = 'gerando', 'Preparando o desenho. Na primeira vez pode levar até 90 segundos…'
            try:
                video = await galeria.preparar(exemplo, self.settings.data_dir / 'animacoes')
            except (animacao.FalhaAnimacao, OSError) as exc:
                logger.warning('Exemplo visual falhou: %s', exc)
                t.status, t.mensagem = 'erro', 'Não foi possível desenhar este exemplo. Tente novamente.'
                return
            self.registro.anexar('animacoes.jsonl', {'id': novo_id(), 'data': agora(),
                'disciplina': exemplo['disciplina'], 'exemplo': ident, 'video': video,
                'origem': 'roteiro_didatico_controlado', 'roteiro': exemplo['roteiro']})
            t.resultado = {'video': f'/api/animacoes/{video}.mp4', 'titulo': exemplo['titulo'],
                           'poster': f'/api/animacoes/{video}.jpg',
                           'pergunta_final': exemplo['roteiro']['pergunta_final'],
                           'modelo_cena': exemplo['roteiro']['modelo'], 'exemplo': ident}
            t.status, t.mensagem = 'pronta', ''

        return self._criar('animacao', trabalho, disciplina=exemplo['disciplina'])

    def animar(self, pergunta: str, resposta_tutor: str | None, disciplina: str | None = None,
               *, contexto_aluno: str | None = None, leitura_foto: str | None = None) -> Tarefa:
        d = obter(disciplina)

        async def trabalho(t: Tarefa) -> None:
            t.status, t.mensagem = "gerando", "Planejando a animação…"
            prompt = prompts.prompt_animacao(pergunta, resposta_tutor, d, contexto_aluno, leitura_foto)
            roteiro, erro, r = None, "", None
            tentativas_roteiro = []
            dados_numericos = bool(re.search(r'\d', pergunta + (contexto_aluno or '') + (leitura_foto or '')))
            for rodada in range(2):  # a segunda tentativa simplifica a forma, preservando a dúvida
                formato = PLANEJAMENTO_JSON.set(True)
                try:
                    sistema = prompts.SISTEMA_ANIMACAO if rodada == 0 and dados_numericos else prompts.SISTEMA_ESQUEMA
                    # Uma ajuda textual incorreta não pode ancorar as duas propostas.
                    # A revisão continua recebendo o contexto completo para checar a combinação.
                    planejamento = prompts.prompt_animacao(pergunta, None, d, contexto_aluno, leitura_foto) \
                        if rodada and resposta_tutor else prompt
                    r = await self._gerar(sistema, planejamento + erro, t, raciocinio=False)
                except AllUnavailable:
                    t.status, t.mensagem = "erro", MSG_ERRO
                    return
                finally:
                    PLANEJAMENTO_JSON.reset(formato)
                tentativa = {'texto': r.text, 'modelo': r.model.key}
                tentativas_roteiro.append(tentativa)
                try:
                    roteiro = animacao.roteiro_valido(r.text)
                    if (rodada or not dados_numericos) and roteiro['modelo'] != 'esquema':
                        raise animacao.FalhaAnimacao('esta pista deve usar esquema, sem inventar dados ou mudar de enunciado')
                except animacao.FalhaAnimacao as exc:
                    tentativa['erro_validacao'] = str(exc)
                    erro = f"\n\nO roteiro anterior era inválido ({exc}). Refaça um esquema de blocos para a mesma dúvida."
                    continue
                if not roteiro.get("pergunta_final", "").strip():
                    roteiro = None
                    erro = "\n\nInclua pergunta_final com uma tarefa curta e sem a resposta embutida."
                    continue
                parecer = await tutoria.avaliar_roteiro(self.llm, pergunta, prompt, roteiro)
                tentativa['revisao'] = parecer
                if parecer["aprovada"]:
                    break
                roteiro = None
                erro = "\n\nO roteiro anterior entregava a solução ou não pôde ser revisado. Faça só uma pista visual parcial."
            ident = novo_id()
            if roteiro is None:
                self.registro.anexar("animacoes.jsonl", {"id": ident, "data": agora(), "disciplina": d.id,
                                                         "pergunta": pergunta, "erro": erro.strip()[:300],
                                                         'tentativas_roteiro': tentativas_roteiro})
                t.status, t.mensagem = "erro", "Não consegui preparar um desenho correto para esta dúvida. " \
                    "Diga qual relação ou passo você quer enxergar e tente novamente."
                return
            t.mensagem = "Desenhando a animação (leva uns 10 segundos)…"
            try:
                video = await animacao.renderizar(roteiro, self.settings.data_dir / "animacoes")
            except animacao.FalhaAnimacao as exc:
                logger.warning("Animação falhou: %s", exc)
                self.registro.anexar("animacoes.jsonl", {"id": ident, "data": agora(), "disciplina": d.id,
                                                         "pergunta": pergunta, "roteiro": roteiro, "erro": str(exc)})
                t.status, t.mensagem = "erro", "A animação falhou ao ser desenhada. Tente de novo."
                return
            self.registro.anexar("animacoes.jsonl", {"id": ident, "data": agora(), "disciplina": d.id,
                                                     "pergunta": pergunta, "roteiro": roteiro, "video": video,
                                                     "modelo": r.model.key, 'tentativas_roteiro': tentativas_roteiro})
            t.resultado = {"video": f"/api/animacoes/{video}.mp4", "modelo_cena": roteiro["modelo"],
                           "titulo": roteiro.get("titulo", ""), "pergunta_final": roteiro.get("pergunta_final", "")}
            t.status, t.mensagem = "pronta", ""

        return self._criar("animacao", trabalho, disciplina=d.id)
