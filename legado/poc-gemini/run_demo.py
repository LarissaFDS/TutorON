#!/usr/bin/env python3
"""TutorON — PoC de RAG simulada: prompt genérico vs. prompt estruturado + contexto de PAA.

Uso rápido:
  export GEMINI_API_KEY=...            # chave do Google AI Studio
  python run_demo.py                   # roda as 4 questões e gera o relatório HTML
  python run_demo.py --controle --juiz # + cenário de controle e avaliação cega pelo Gemini

Sem chave de API:
  python run_demo.py --dry-run         # só gera os prompts em prompts_gerados/ para colar no AI Studio
  python run_demo.py --importar respostas_manuais   # gera o relatório a partir das respostas coladas
"""
import argparse
import datetime as dt
import html
import json
import os
import random
import re
import sys
import time
import unicodedata
from pathlib import Path

import prompts as P

RAIZ = Path(__file__).parent
CENARIOS = {
    "generico": ("Cenário 1 — Prompt genérico", P.prompt_generico),
    "estruturado": ("Cenário 2 — Prompt estruturado + contexto acadêmico", P.prompt_estruturado),
    "controle": ("Controle — Prompt estruturado SEM contexto", P.prompt_controle),
}
# Rótulos curtos para cabeçalhos de tabela: dizem o que muda, não o número do cenário.
CURTO = {"generico": "Genérico", "estruturado": "Estruturado + contexto", "controle": "Controle sem contexto"}
MODELO_PADRAO = os.environ.get("GEMINI_MODEL", "gemini-3.1-pro")
TEMPERATURA = 0.2


# ---------------------------------------------------------------- Gemini
class Gemini:
    def __init__(self, modelo: str):
        from google import genai
        from google.genai import types

        chave = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not chave:
            sys.exit("Defina GEMINI_API_KEY (ou use --dry-run / --importar).")
        self.types = types
        self.client = genai.Client(api_key=chave)
        self.modelo = self._resolver_modelo(modelo)

    def _resolver_modelo(self, pedido: str) -> str:
        """Usa o modelo pedido; se não existir mais, cai para o primeiro 'flash' disponível."""
        try:
            nomes = [m.name.split("/")[-1] for m in self.client.models.list()
                     if "generateContent" in (m.supported_actions or [])]
        except Exception:
            return pedido
        if pedido in nomes:
            return pedido
        flash = [n for n in nomes if "flash" in n and "lite" not in n and "image" not in n
                 and "tts" not in n and "live" not in n]
        escolhido = (flash or nomes or [pedido])[0]
        print(f"[aviso] modelo '{pedido}' indisponível; usando '{escolhido}'.")
        return escolhido

    def gerar(self, system: str | None, conteudo: str, json_mode=False) -> str:
        cfg = dict(temperature=TEMPERATURA)
        if system:
            cfg["system_instruction"] = system
        if json_mode:
            cfg["response_mime_type"] = "application/json"
        for tentativa in range(4):
            try:
                r = self.client.models.generate_content(
                    model=self.modelo, contents=conteudo,
                    config=self.types.GenerateContentConfig(**cfg))
                return r.text or ""
            except Exception as e:  # limite de taxa etc.
                if tentativa == 3:
                    raise
                espera = 10 * (tentativa + 1)
                print(f"   erro ({e.__class__.__name__}: {str(e)[:80]}); tentando de novo em {espera}s")
                time.sleep(espera)


# ---------------------------------------------------------------- checkpoints
def normalizar(t: str) -> tuple[str, str]:
    t = t.replace("\\subseteq", "⊆").replace("\\le", "≤").replace("\\ge", "≥")
    t = t.replace("\\cdot", "").replace("·", "").replace("−", "-").replace("–", "-")
    t = t.replace("\\left", "").replace("\\right", "").replace("\\lfloor", "").replace("\\rfloor", "")
    t = re.sub(r"[\\${}*`]", "", t)
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    palavras = re.sub(r"\s+", " ", t)
    return palavras, re.sub(r"\s+", "", t)


def avaliar_checkpoints(q: dict, resposta: str, cenario: str) -> list[dict]:
    palavras, compacto = normalizar(resposta)
    out = []
    for c in q["checkpoints"]:
        if c.get("so_estruturado") and cenario != "estruturado":
            out.append({**c, "ok": None})
            continue
        achou = bool(re.search(c["regex"], palavras) or re.search(c["regex"], compacto))
        if achou and c["tipo"] == "nao_deve" and c.get("exceto_se_proximo"):
            # citar o erro para corrigi-lo não conta como repetir o erro
            achou = any(not re.search(c["exceto_se_proximo"], palavras[max(0, m.start() - 200): m.end() + 200])
                        for m in re.finditer(c["regex"], palavras))
        ok = achou if c["tipo"] in ("deve", "info") else not achou
        out.append({**c, "ok": ok})
    return out


def cobertura(cks: list[dict]) -> tuple[int, int]:
    validos = [c for c in cks if c["tipo"] != "info" and c["ok"] is not None]
    return sum(c["ok"] for c in validos), len(validos)


# ---------------------------------------------------------------- juiz
CRITERIOS = ["precisao", "clareza", "aderencia_disciplina", "aderencia_enunciado",
             "uso_do_material", "especificidade", "ausencia_alucinacao"]
ROTULOS = {"precisao": "Precisão", "clareza": "Clareza", "aderencia_disciplina": "Aderência à disciplina",
           "aderencia_enunciado": "Aderência ao enunciado", "uso_do_material": "Uso do material",
           "especificidade": "Especificidade (não genérica)", "ausencia_alucinacao": "Sem alucinação"}

PROMPT_JUIZ = """Você é um professor avaliador de Projeto e Análise de Algoritmos.
Abaixo estão o MATERIAL DA DISCIPLINA (provas, listas e resoluções — atenção: resoluções de alunos
podem conter erros), a PERGUNTA de um aluno e duas respostas anônimas (A e B).

Avalie CADA resposta de 1 a 5 nos critérios:
- precisao: está tecnicamente correta?
- clareza: é compreensível para um aluno de graduação?
- aderencia_disciplina: segue a estrutura, notação e vocabulário usados no material da disciplina?
- aderencia_enunciado: responde exatamente ao que foi perguntado (incluindo o que a prova exige)?
- uso_do_material: aproveita informações específicas do material? (1 se ignora o material)
- especificidade: 5 = focada e específica; 1 = ampla/genérica demais
- ausencia_alucinacao: 5 = nada inventado nem contraditório ao material/à teoria; 1 = alucinações graves

Liste também afirmações problemáticas (erradas, inventadas, ou que repetem erro do material).
Responda APENAS com JSON no formato:
{{"A": {{"precisao": n, ..., "problemas": ["..."], "comentario": "..."}},
  "B": {{...}}, "melhor": "A" | "B" | "empate", "justificativa": "..."}}

=== MATERIAL DA DISCIPLINA ===
{contexto}

=== PERGUNTA ===
{pergunta}

=== RESPOSTA A ===
{a}

=== RESPOSTA B ===
{b}
"""


def julgar(llm: Gemini, q: dict, r_gen: str, r_est: str, rng: random.Random) -> dict:
    inverte = rng.random() < 0.5  # ordem cega e aleatória
    a, b = (r_est, r_gen) if inverte else (r_gen, r_est)
    txt = llm.gerar(None, PROMPT_JUIZ.format(contexto=P.bloco_contexto(q["contexto"]),
                                             pergunta=q["pergunta"], a=a, b=b), json_mode=True)
    try:
        j = json.loads(re.search(r"\{.*\}", txt, re.S).group(0))
    except Exception:
        return {"erro": txt[:500]}
    mapa = {"A": "estruturado" if inverte else "generico", "B": "generico" if inverte else "estruturado"}
    res = {mapa["A"]: j.get("A", {}), mapa["B"]: j.get("B", {})}
    melhor = j.get("melhor", "empate")
    res["melhor"] = mapa.get(melhor, "empate")
    res["justificativa"] = j.get("justificativa", "")
    res["ordem_apresentada"] = f"A={mapa['A']}, B={mapa['B']}"
    return res


# ---------------------------------------------------------------- relatório
def esc(s): return html.escape(s or "")


def gerar_relatorio(dados: dict, destino: Path):
    qs, cen = dados["questoes"], dados["cenarios"]
    resumo_linhas = []
    tot = {c: [0, 0] for c in cen}
    for q in qs:
        cels = []
        for c in cen:
            ok, n = cobertura(q["checkpoints_resultado"][c])
            tot[c][0] += ok; tot[c][1] += n
            cels.append(f"<td class='num'>{ok}/{n}</td>")
        juiz = q.get("juiz") or {}
        venc = juiz.get("melhor", "—")
        venc = {"estruturado": "Estruturado + contexto", "generico": "Genérico"}.get(venc, venc)
        resumo_linhas.append(f"<tr><td><a href='#{q['id']}'>{q['id']}</a> {esc(q['titulo'])}</td>{''.join(cels)}"
                             f"{'<td>' + esc(venc) + '</td>' if dados['juiz'] else ''}</tr>")
    tot_cels = "".join(f"<td class='num'>{a}/{b} ({(100*a/b if b else 0):.0f}%)</td>" for a, b in tot.values())

    blocos = []
    for q in qs:
        chunks = "".join(
            f"<div class='chunk'><div class='meta'><b>[{c['id']}]</b> {esc(c['fonte'])} "
            f"<span class='tag'>{esc(c['tipo'])}</span></div><pre>{esc(c['texto'])}</pre></div>"
            for c in q["chunks"])
        prompts_html = "".join(
            f"<details><summary>Prompt enviado — {esc(CENARIOS[c][0])}</summary>"
            f"{'<p class=meta><b>system_instruction:</b></p><pre>' + esc(q['prompts'][c]['system']) + '</pre>' if q['prompts'][c]['system'] else '<p class=meta>(sem system_instruction)</p>'}"
            f"<p class='meta'><b>conteúdo:</b></p><pre>{esc(q['prompts'][c]['conteudo'])}</pre></details>"
            for c in cen)
        colunas = "".join(
            f"<div class='col'><h4>{esc(CENARIOS[c][0])}</h4>"
            f"<div class='resp md'>{esc(q['respostas'][c])}</div></div>" for c in cen)
        ck_rows = ""
        for i, ck in enumerate(q["checkpoints"]):
            tds = ""
            for c in cen:
                v = q["checkpoints_resultado"][c][i]["ok"]
                tds += ("<td class='na'>n/a</td>" if v is None else
                        f"<td class='{'ok' if v else 'no'}'>{'✓' if v else '✗'}</td>")
            tipo = {"deve": "deve ter", "nao_deve": "não deve ter", "info": "informativo"}[ck["tipo"]]
            ck_rows += f"<tr><td>{esc(ck['rotulo'])} <span class='tag'>{tipo}</span></td>{tds}</tr>"
        juiz_html = ""
        j = q.get("juiz")
        if j and "erro" not in j:
            linhas = "".join(
                f"<tr><td>{ROTULOS[k]}</td><td class='num'>{j.get('generico', {}).get(k, '—')}</td>"
                f"<td class='num'>{j.get('estruturado', {}).get(k, '—')}</td></tr>" for k in CRITERIOS)
            probs = lambda c: "".join(f"<li>{esc(p)}</li>" for p in j.get(c, {}).get("problemas", [])) or "<li>nenhum apontado</li>"
            juiz_html = (f"<h4>Avaliação cega pelo Gemini (1–5)</h4><div class='table-scroll'><table class='table'><tr><th>Critério</th><th>Genérico</th>"
                         f"<th>Estruturado + contexto</th></tr>{linhas}</table></div>"
                         f"<p><b>Melhor:</b> {esc(j.get('melhor'))} — {esc(j.get('justificativa'))} "
                         f"<span class='meta'>({esc(j.get('ordem_apresentada'))})</span></p>"
                         f"<div class='grid2'><div><b>Problemas — genérico</b><ul>{probs('generico')}</ul></div>"
                         f"<div><b>Problemas — estruturado</b><ul>{probs('estruturado')}</ul></div></div>")
        elif j:
            juiz_html = f"<p class='meta'>Juiz não retornou JSON válido: {esc(j['erro'])}</p>"
        blocos.append(f"""
<section class="report-section" id="{q['id']}">
  <h2><span class="qid">{q['id']}</span> {esc(q['titulo'])}</h2>
  <p class="why"><b>Por que esta questão:</b> {esc(q['por_que_escolhida'])}</p>
  <h3>Pergunta do aluno</h3><pre class="pergunta">{esc(q['pergunta'])}</pre>
  <details><summary>Materiais usados como contexto (recuperação simulada): {', '.join(c['id'] for c in q['chunks'])}</summary>{chunks}</details>
  {prompts_html}
  <h3>Respostas</h3><div class="cols n{len(cen)}">{colunas}</div>
  <h3>Checklist baseado no material</h3>
  <div class="table-scroll"><table class="table"><tr><th>Critério</th>{''.join('<th>' + esc(CURTO[c]) + '</th>' for c in cen)}</tr>{ck_rows}</table></div>
  {juiz_html}
  <h3>Notas da equipe</h3><div class="notas" contenteditable="true" aria-label="Notas da equipe (não são salvas)">Clique para anotar. As notas não são salvas: copie antes de fechar.</div>
</section>""")

    cab = "".join(f"<th>{esc(CURTO[c])}</th>" for c in cen)
    from design import stylesheet  # design system do TutorON, embutido: o relatório é um arquivo avulso
    css = stylesheet("report.css")
    page = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TutorON · Relatório da PoC de RAG em PAA</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<style>
{css}
</style></head><body class="report">
<header class="masthead">
  <div class="page masthead__bar">
    <div class="wordmark" aria-label="TutorON">Tutor<span>ON</span></div>
    <p class="masthead__context">Relatório interno da equipe<br>Projeto e Análise de Algoritmos, UFAL</p>
  </div>
  <div class="page masthead__intro">
    <h1>Contexto da disciplina melhora a resposta do tutor?</h1>
    <p class="masthead__lede">Prova de conceito de RAG com recuperação simulada: cada questão recebe, à mão, os trechos da base que uma RAG deveria encontrar. O checklist procura no texto o que o material exige; a leitura humana decide.</p>
  </div>
</header>
<main class="page">
<dl class="run-facts">
  <div><dt>Modelo</dt><dd>{esc(dados['modelo'])}</dd></div>
  <div><dt>Temperatura</dt><dd>{TEMPERATURA}</dd></div>
  <div><dt>Gerado em</dt><dd>{esc(dados['gerado_em'])}</dd></div>
  <div><dt>Modo</dt><dd>{esc(dados['modo'])}</dd></div>
</dl>
<section class="report-section" aria-labelledby="resumo">
<h2 id="resumo">Cobertura do checklist por cenário</h2>
<div class="table-scroll"><table class="table"><thead><tr><th>Questão</th>{cab}{'<th>Melhor (juiz cego)</th>' if dados['juiz'] else ''}</tr></thead>
<tbody>{''.join(resumo_linhas)}</tbody>
<tfoot><tr><td>Total</td>{tot_cels}{'<td></td>' if dados['juiz'] else ''}</tr></tfoot></table></div>
</section>
{''.join(blocos)}
</main>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<script>
try {{
  document.querySelectorAll('.md').forEach(el => {{
    if (!window.marked) return;
    const src = el.textContent;
    const math = []; // protege LaTeX antes do markdown
    const prot = src.replace(/\\$\\$[\\s\\S]+?\\$\\$|\\$[^$\\n]+?\\$/g, m => {{ math.push(m); return '@@M' + (math.length-1) + '@@'; }});
    el.innerHTML = marked.parse(prot).replace(/@@M(\\d+)@@/g, (_, i) => math[+i].replace(/</g,'&lt;'));
    el.classList.add('rendered');
    if (window.renderMathInElement) renderMathInElement(el, {{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}], throwOnError:false}});
  }});
}} catch (e) {{ console.warn(e); }}
</script></body></html>"""
    destino.write_text(page, encoding="utf-8")


# ---------------------------------------------------------------- principal
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default=MODELO_PADRAO, help=f"modelo Gemini (padrão: {MODELO_PADRAO})")
    ap.add_argument("--questoes", default="", help="ex.: Q1,Q4 (padrão: todas)")
    ap.add_argument("--controle", action="store_true", help="inclui cenário estruturado SEM contexto")
    ap.add_argument("--juiz", action="store_true", help="avaliação cega genérico × estruturado pelo Gemini")
    ap.add_argument("--dry-run", action="store_true", help="só escreve os prompts em prompts_gerados/")
    ap.add_argument("--importar", metavar="PASTA", help="usa respostas coladas manualmente (Q1_generico.md etc.)")
    ap.add_argument("--mock", action="store_true", help="respostas falsas, só para testar o pipeline")
    a = ap.parse_args()

    questoes = json.loads((RAIZ / "questoes.json").read_text(encoding="utf-8"))
    if a.questoes:
        sel = {s.strip().upper() for s in a.questoes.split(",")}
        questoes = [q for q in questoes if q["id"] in sel]
    cen = ["generico", "estruturado"] + (["controle"] if a.controle else [])

    if a.dry_run:
        out = RAIZ / "prompts_gerados"; out.mkdir(exist_ok=True)
        for q in questoes:
            for c in cen:
                system, conteudo = CENARIOS[c][1](q)
                txt = (f"### SYSTEM INSTRUCTION (cole em 'System instructions' no AI Studio)\n{system}\n\n"
                       if system else "### (sem system instruction)\n\n") + f"### PROMPT\n{conteudo}\n"
                (out / f"{q['id']}_{c}.txt").write_text(txt, encoding="utf-8")
        print(f"Prompts escritos em {out}/. Cole as respostas em respostas_manuais/<Q>_<cenario>.md "
              f"e rode: python run_demo.py --importar respostas_manuais")
        return

    llm = None
    if not (a.importar or a.mock):
        llm = Gemini(a.model)
    elif a.juiz and a.importar:
        llm = Gemini(a.model)  # juiz ainda precisa da API
    modelo = llm.modelo if llm else ("MOCK" if a.mock else "respostas importadas manualmente")
    modo = "mock (NÃO são respostas reais)" if a.mock else ("importado" if a.importar else "API Gemini")

    rng = random.Random(42)
    for q in questoes:
        print(f"• {q['id']} — {q['titulo']}")
        q["chunks"] = [P.carregar_chunk(c) for c in q["contexto"]]
        q["prompts"], q["respostas"], q["checkpoints_resultado"] = {}, {}, {}
        for c in cen:
            system, conteudo = CENARIOS[c][1](q)
            q["prompts"][c] = {"system": system, "conteudo": conteudo}
            if a.mock:
                resp = f"[MOCK {c}] Resposta de teste para {q['id']}. Indução forte, caso base inicio = fim."
            elif a.importar:
                arq = Path(a.importar) / f"{q['id']}_{c}.md"
                resp = arq.read_text(encoding="utf-8") if arq.exists() else f"(arquivo {arq} não encontrado)"
            else:
                print(f"   gerando {c}…")
                resp = llm.gerar(system, conteudo)
            q["respostas"][c] = resp
            q["checkpoints_resultado"][c] = avaliar_checkpoints(q, resp, c)
            ok, n = cobertura(q["checkpoints_resultado"][c])
            print(f"   {c:<12} checklist {ok}/{n}")
        if a.juiz and llm and not a.mock:
            print("   juiz cego…")
            q["juiz"] = julgar(llm, q, q["respostas"]["generico"], q["respostas"]["estruturado"], rng)

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    pasta = RAIZ / "resultados" / stamp
    pasta.mkdir(parents=True, exist_ok=True)
    dados = {"modelo": modelo, "modo": modo, "gerado_em": stamp, "cenarios": cen,
             "juiz": bool(a.juiz and llm and not a.mock), "questoes": questoes}
    (pasta / "respostas.json").write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
    gerar_relatorio(dados, pasta / "relatorio.html")
    print(f"\nRelatório: {pasta / 'relatorio.html'}")


if __name__ == "__main__":
    main()
